import 'package:flutter/material.dart';
import 'screens/ai_chat_screen.dart';

void main() {
  runApp(const ExamSathiApp());
}

class ExamSathiApp extends StatelessWidget {
  const ExamSathiApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ExamSathi AI',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        useMaterial3: true,
      ),
      home: const AIChatScreen(
        // Replace with your deployed API URL
        apiUrl: 'https://your-api-url.com',
        // For local testing: 'http://10.0.2.2:5000' (Android emulator)
        // For local testing: 'http://localhost:5000' (iOS simulator)
      ),
    );
  }
}
