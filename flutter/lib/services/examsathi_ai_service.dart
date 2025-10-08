import 'dart:convert';
import 'package:http/http.dart' as http;

/// ExamSathi AI Service
/// Handles all communication with your AI model API
class ExamSathiAIService {
  final String apiUrl;
  
  ExamSathiAIService({required this.apiUrl});

  /// Check if the API server is healthy
  Future<Map<String, dynamic>> checkHealth() async {
    try {
      final response = await http.get(
        Uri.parse('$apiUrl/health'),
      );

      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('Server returned ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Failed to connect to server: $e');
    }
  }

  /// Ask a single question
  Future<String> askQuestion({
    required String question,
    int maxLength = 512,
    double temperature = 0.7,
  }) async {
    try {
      final response = await http.post(
        Uri.parse('$apiUrl/ask'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'question': question,
          'max_length': maxLength,
          'temperature': temperature,
        }),
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        if (data['success']) {
          return data['answer'];
        } else {
          throw Exception(data['error'] ?? 'Unknown error');
        }
      } else {
        throw Exception('Server returned ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Failed to get answer: $e');
    }
  }

  /// Ask multiple questions at once
  Future<List<Map<String, dynamic>>> askBatch({
    required List<String> questions,
  }) async {
    try {
      final response = await http.post(
        Uri.parse('$apiUrl/batch-ask'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'questions': questions,
        }),
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        if (data['success']) {
          return List<Map<String, dynamic>>.from(data['results']);
        } else {
          throw Exception(data['error'] ?? 'Unknown error');
        }
      } else {
        throw Exception('Server returned ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Failed to get batch answers: $e');
    }
  }

  /// Get model information
  Future<Map<String, dynamic>> getModelInfo() async {
    try {
      final response = await http.get(
        Uri.parse('$apiUrl/model-info'),
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        if (data['success']) {
          return data;
        } else {
          throw Exception(data['error'] ?? 'Unknown error');
        }
      } else {
        throw Exception('Server returned ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Failed to get model info: $e');
    }
  }

  /// Trigger model loading (if not already loaded)
  Future<bool> loadModel() async {
    try {
      final response = await http.post(
        Uri.parse('$apiUrl/load-model'),
        headers: {'Content-Type': 'application/json'},
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        return data['success'] ?? false;
      } else {
        return false;
      }
    } catch (e) {
      return false;
    }
  }
}
