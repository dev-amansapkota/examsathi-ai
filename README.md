# ExamSathi AI - Your Own Educational AI Model

Build, train, and deploy your own AI model for educational purposes - completely free!

## What You Get

- **Model Training**: Fine-tune AI models on your educational content using Google Colab (FREE)
- **API Server**: Dynamic model loading from Google Drive/GitHub
- **Web Interface**: Test your model before Flutter integration
- **Flutter Integration**: Complete code for mobile app integration
- **Zero Cost**: Everything runs on free tiers

## Quick Start

### 1. Train Your Model (10-15 minutes)

1. Edit `scripts/training_data.json` with your questions and answers
2. Open [Google Colab](https://colab.research.google.com)
3. Upload `scripts/train_model.py` and `training_data.json`
4. Run the training script
5. Download your trained model

See: `docs/TRAINING_GUIDE.md`

### 2. Deploy API Server (5 minutes)

1. Upload model to Google Drive
2. Deploy to Railway/Render (free tier)
3. Set environment variables
4. Your API is live!

See: `docs/DEPLOYMENT_GUIDE.md`

### 3. Test Web Interface (2 minutes)

1. Run `npm install && npm run dev`
2. Enter your API URL
3. Test with sample questions

See: `docs/WEB_INTERFACE_GUIDE.md`

### 4. Integrate with Flutter (10 minutes)

1. Copy `lib/services/examsathi_ai_service.dart` to your project
2. Update API URL
3. Use the provided chat screen or create your own

See: `docs/FLUTTER_INTEGRATION_GUIDE.md`

## Project Structure

\`\`\`
examsathi-ai-model/
├── scripts/
│   ├── train_model.py          # Model training script
│   └── training_data.json      # Your educational data
├── api/
│   ├── server.py               # Flask API server
│   ├── requirements.txt        # Python dependencies
│   ├── Dockerfile             # Docker configuration
│   └── .env.example           # Environment variables
├── flutter/
│   ├── lib/
│   │   ├── services/
│   │   │   └── examsathi_ai_service.dart
│   │   ├── screens/
│   │   │   └── ai_chat_screen.dart
│   │   └── main.dart
│   └── pubspec.yaml
├── app/                        # Next.js web interface
│   ├── page.tsx               # Main testing interface
│   └── layout.tsx
└── docs/
    ├── TRAINING_GUIDE.md
    ├── DEPLOYMENT_GUIDE.md
    ├── WEB_INTERFACE_GUIDE.md
    └── FLUTTER_INTEGRATION_GUIDE.md
\`\`\`

## Features

### Model Training
- Fine-tune on your educational content
- Support for multiple model sizes (2GB - 14GB)
- Free GPU training via Google Colab
- Easy data format (JSON)

### API Server
- Dynamic model loading from cloud storage
- REST API endpoints
- Health monitoring
- Batch question support
- Docker support

### Web Interface
- Clean, modern UI
- API configuration
- Health checking
- Sample questions
- Error handling

### Flutter Integration
- Complete service class
- Chat interface example
- Error handling
- Loading states
- Caching support

## Supported Models

| Model | Size | Best For |
|-------|------|----------|
| Llama 3.2 (1B) | 2GB | Fast responses |
| Phi-2 | 5GB | Balanced (recommended) |
| Llama 3.2 (3B) | 6GB | Detailed answers |
| Gemma 2 | 4GB | Math & Science |
| Mistral 7B | 14GB | Complex topics |

## Free Hosting Options

### API Server
- Railway (500 hrs/month)
- Render (750 hrs/month)
- Hugging Face Spaces (unlimited)
- Oracle Cloud (forever free, 24GB RAM!)

### Web Interface
- Vercel (unlimited)
- Netlify (unlimited)
- GitHub Pages (unlimited)

### Model Storage
- Google Drive (15GB free)
- GitHub (unlimited for public repos)

## Cost Breakdown

| Component | Cost |
|-----------|------|
| Model Training | $0 (Google Colab) |
| Model Storage | $0 (Google Drive/GitHub) |
| API Hosting | $0 (Free tiers) |
| Web Interface | $0 (Vercel/Netlify) |
| **Total** | **$0** |

## Requirements

### For Training
- Google account (for Colab)
- 100+ question-answer pairs
- 10-15 minutes

### For API Server
- Python 3.10+
- 2-8GB RAM (depending on model)
- Internet connection

### For Flutter App
- Flutter 3.0+
- http package
- Your API URL

## Example Use Cases

1. **Exam Preparation App**: Students ask questions, get instant explanations
2. **Study Assistant**: Explain complex topics in simple terms
3. **Quiz Helper**: Provide hints and explanations
4. **Homework Help**: Answer subject-specific questions
5. **Language Learning**: Practice conversations and grammar

## API Endpoints

\`\`\`
GET  /health          - Check server status
POST /ask             - Ask a single question
POST /batch-ask       - Ask multiple questions
GET  /model-info      - Get model information
POST /load-model      - Trigger model loading
\`\`\`

## Environment Variables

\`\`\`env
MODEL_SOURCE=gdrive
MODEL_URL=https://drive.google.com/uc?id=YOUR_FILE_ID
MODEL_NAME=examsathi-model
PORT=5000
\`\`\`

## Performance

- **First Request**: 30-60 seconds (model loading)
- **Subsequent Requests**: 1-3 seconds
- **Batch Requests**: 2-5 seconds per question
- **Memory Usage**: 2-8GB (depending on model)

## Limitations

- Free tier hosting has usage limits
- First request is slow (model loading)
- Model size affects response time
- No streaming responses (yet)

## Roadmap

- [ ] Streaming responses
- [ ] Model quantization for smaller size
- [ ] Multi-language support
- [ ] Voice input/output
- [ ] Image understanding
- [ ] Conversation memory

## Contributing

This is a template project for educational purposes. Feel free to:
- Add more model options
- Improve the UI
- Add new features
- Share your improvements

## License

MIT License - Use freely for your educational projects!

## Support

For issues or questions:
1. Check the documentation in `docs/`
2. Test API with curl/Postman first
3. Verify server logs
4. Check network connectivity

## Credits

Built with:
- Transformers (Hugging Face)
- Flask (API server)
- Next.js (Web interface)
- Flutter (Mobile integration)

## Get Started Now!

1. Clone this repository
2. Follow `docs/TRAINING_GUIDE.md`
3. Deploy your API
4. Integrate with your app
5. Help students learn better!

Your own AI model, your own data, zero cost. Let's build something amazing!
"# examsathi-ai" 
