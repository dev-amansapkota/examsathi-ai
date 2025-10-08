# ExamSathi AI - Flutter Integration Guide

## Complete Integration Guide for Your Flutter App

This guide shows you how to integrate your ExamSathi AI model into your Flutter application.

## Prerequisites

- Flutter SDK installed (3.0.0 or higher)
- Your API server deployed and running
- API URL from deployment (e.g., `https://your-api.railway.app`)

## Step 1: Add Dependencies

Add to your `pubspec.yaml`:

\`\`\`yaml
dependencies:
  http: ^1.1.0
  provider: ^6.1.1  # Optional: for state management
  shared_preferences: ^2.2.2  # Optional: for caching
\`\`\`

Run:
\`\`\`bash
flutter pub get
\`\`\`

## Step 2: Add the AI Service

Copy `lib/services/examsathi_ai_service.dart` to your project.

This service handles all API communication:
- Health checks
- Single questions
- Batch questions
- Model information

## Step 3: Basic Usage

### Simple Question-Answer

\`\`\`dart
import 'package:your_app/services/examsathi_ai_service.dart';

// Initialize service
final aiService = ExamSathiAIService(
  apiUrl: 'https://your-api-url.com'
);

// Ask a question
try {
  final answer = await aiService.askQuestion(
    question: 'What is photosynthesis?'
  );
  print('Answer: $answer');
} catch (e) {
  print('Error: $e');
}
\`\`\`

### Check Server Health

\`\`\`dart
try {
  final health = await aiService.checkHealth();
  if (health['status'] == 'healthy') {
    print('Server is ready!');
  }
} catch (e) {
  print('Server not available');
}
\`\`\`

### Batch Questions

\`\`\`dart
final questions = [
  'What is photosynthesis?',
  'Explain gravity',
  'What is DNA?',
];

final results = await aiService.askBatch(questions: questions);

for (var result in results) {
  print('Q: ${result['question']}');
  print('A: ${result['answer']}');
}
\`\`\`

## Step 4: Integration Patterns

### Pattern 1: Chat Interface

Use the provided `AIChatScreen` widget:

\`\`\`dart
Navigator.push(
  context,
  MaterialPageRoute(
    builder: (context) => AIChatScreen(
      apiUrl: 'https://your-api-url.com',
    ),
  ),
);
\`\`\`

### Pattern 2: Quiz Helper

\`\`\`dart
class QuizHelper {
  final ExamSathiAIService _ai;
  
  QuizHelper(String apiUrl) 
    : _ai = ExamSathiAIService(apiUrl: apiUrl);
  
  Future<String> getHint(String question) async {
    return await _ai.askQuestion(
      question: 'Give a hint for: $question',
      temperature: 0.5,  // Lower = more focused
    );
  }
  
  Future<String> explainAnswer(String question, String answer) async {
    return await _ai.askQuestion(
      question: 'Explain why the answer to "$question" is "$answer"',
    );
  }
}
\`\`\`

### Pattern 3: Study Assistant

\`\`\`dart
class StudyAssistant extends StatefulWidget {
  @override
  _StudyAssistantState createState() => _StudyAssistantState();
}

class _StudyAssistantState extends State<StudyAssistant> {
  final _ai = ExamSathiAIService(apiUrl: 'YOUR_API_URL');
  String _explanation = '';
  bool _loading = false;
  
  Future<void> explainTopic(String topic) async {
    setState(() => _loading = true);
    
    try {
      final explanation = await _ai.askQuestion(
        question: 'Explain $topic in simple terms for students',
      );
      setState(() => _explanation = explanation);
    } catch (e) {
      // Handle error
    } finally {
      setState(() => _loading = false);
    }
  }
  
  @override
  Widget build(BuildContext context) {
    // Your UI here
  }
}
\`\`\`

## Step 5: Configuration

### For Development (Local Testing)

\`\`\`dart
// Android Emulator
const apiUrl = 'http://10.0.2.2:5000';

// iOS Simulator
const apiUrl = 'http://localhost:5000';

// Physical Device (same network)
const apiUrl = 'http://192.168.1.X:5000';  // Your computer's IP
\`\`\`

### For Production

\`\`\`dart
const apiUrl = 'https://your-api.railway.app';
\`\`\`

### Using Environment Variables

Create `lib/config/app_config.dart`:

\`\`\`dart
class AppConfig {
  static const String apiUrl = String.fromEnvironment(
    'API_URL',
    defaultValue: 'http://localhost:5000',
  );
}
\`\`\`

Run with:
\`\`\`bash
flutter run --dart-define=API_URL=https://your-api.com
\`\`\`

## Step 6: Error Handling

\`\`\`dart
Future<void> askQuestionSafely(String question) async {
  try {
    final answer = await aiService.askQuestion(question: question);
    // Success - show answer
  } on Exception catch (e) {
    if (e.toString().contains('Failed to connect')) {
      // Network error - show retry button
    } else if (e.toString().contains('Server returned')) {
      // Server error - show error message
    } else {
      // Unknown error
    }
  }
}
\`\`\`

## Step 7: Caching (Optional)

Save API responses to reduce costs:

\`\`\`dart
import 'package:shared_preferences/shared_preferences.dart';

class CachedAIService {
  final ExamSathiAIService _ai;
  final SharedPreferences _prefs;
  
  CachedAIService(this._ai, this._prefs);
  
  Future<String> askQuestion(String question) async {
    // Check cache first
    final cached = _prefs.getString('q_$question');
    if (cached != null) return cached;
    
    // Ask AI
    final answer = await _ai.askQuestion(question: question);
    
    // Save to cache
    await _prefs.setString('q_$question', answer);
    
    return answer;
  }
}
\`\`\`

## Step 8: Loading States

\`\`\`dart
class AIWidget extends StatefulWidget {
  @override
  _AIWidgetState createState() => _AIWidgetState();
}

class _AIWidgetState extends State<AIWidget> {
  bool _isLoading = false;
  String? _answer;
  String? _error;
  
  Future<void> _ask(String question) async {
    setState(() {
      _isLoading = true;
      _error = null;
    });
    
    try {
      final answer = await aiService.askQuestion(question: question);
      setState(() => _answer = answer);
    } catch (e) {
      setState(() => _error = e.toString());
    } finally {
      setState(() => _isLoading = false);
    }
  }
  
  @override
  Widget build(BuildContext context) {
    if (_isLoading) {
      return CircularProgressIndicator();
    }
    
    if (_error != null) {
      return Text('Error: $_error');
    }
    
    if (_answer != null) {
      return Text(_answer!);
    }
    
    return ElevatedButton(
      onPressed: () => _ask('Your question'),
      child: Text('Ask AI'),
    );
  }
}
\`\`\`

## Advanced Features

### 1. Streaming Responses (Future Enhancement)

For real-time responses, you can modify the API to support streaming.

### 2. Voice Input

\`\`\`dart
import 'package:speech_to_text/speech_to_text.dart';

// Convert speech to text, then ask AI
final speech = SpeechToText();
await speech.listen(
  onResult: (result) async {
    final answer = await aiService.askQuestion(
      question: result.recognizedWords,
    );
    // Show answer
  },
);
\`\`\`

### 3. Offline Mode

Cache common questions and answers for offline access.

## Testing

### Unit Tests

\`\`\`dart
import 'package:flutter_test/flutter_test.dart';

void main() {
  test('AI Service returns answer', () async {
    final service = ExamSathiAIService(
      apiUrl: 'https://your-api.com'
    );
    
    final answer = await service.askQuestion(
      question: 'Test question'
    );
    
    expect(answer, isNotEmpty);
  });
}
\`\`\`

## Performance Tips

1. **Preload Model**: Call `/load-model` when app starts
2. **Cache Responses**: Save common Q&A pairs
3. **Batch Requests**: Use batch API for multiple questions
4. **Timeout Handling**: Set reasonable timeouts (30-60 seconds)
5. **Connection Pooling**: Reuse HTTP client

## Security

1. **HTTPS Only**: Always use HTTPS in production
2. **API Keys**: Add authentication if needed
3. **Rate Limiting**: Implement client-side rate limiting
4. **Input Validation**: Sanitize user input

## Troubleshooting

### "Failed to connect to server"
- Check API URL is correct
- Verify server is running
- Check network connectivity
- For emulator, use correct IP (10.0.2.2 for Android)

### "Server returned 500"
- Model might not be loaded yet (wait 30-60 seconds)
- Check server logs
- Verify model files are accessible

### Slow responses
- First request takes longer (model loading)
- Consider showing "Model loading..." message
- Implement request timeout

## Complete Example App

See the provided files:
- `lib/main.dart` - App entry point
- `lib/services/examsathi_ai_service.dart` - API service
- `lib/screens/ai_chat_screen.dart` - Chat interface

## Next Steps

1. Copy the service file to your project
2. Update API URL in your code
3. Test with your deployed API
4. Integrate into your existing screens
5. Add error handling and loading states
6. Deploy your Flutter app

## Support

If you encounter issues:
1. Check API server is running (`/health` endpoint)
2. Verify network connectivity
3. Check Flutter console for errors
4. Test API directly with curl/Postman first

## Cost Optimization

- Cache frequently asked questions
- Implement request debouncing
- Use batch API for multiple questions
- Consider offline mode for common queries

Your ExamSathi AI is now ready to integrate into your Flutter app!
