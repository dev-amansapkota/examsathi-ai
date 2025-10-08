# ExamSathi AI - Quick Start Guide

Get your AI model running in 30 minutes!

## What You'll Build

- ✅ Your own AI model trained on educational content
- ✅ Free API hosted on Render
- ✅ Flutter app integration
- ✅ Zero monthly costs

## Prerequisites

- Google account (for Colab & Drive)
- GitHub account (for Render)
- Basic understanding of Python (optional)

## Step-by-Step Setup

### 1. Train Your Model (15 minutes)

**Open Google Colab**:
1. Upload `scripts/train_model.py` to Google Colab
2. Edit `scripts/training_data.json` with your questions/answers
3. Click Runtime → Run all
4. Wait for training to complete
5. Download the model folder

**Sample Training Data**:
\`\`\`json
{
  "data": [
    {
      "question": "What is photosynthesis?",
      "answer": "Photosynthesis is the process by which plants use sunlight, water and carbon dioxide to produce oxygen and energy in the form of sugar."
    },
    {
      "question": "What is the capital of France?",
      "answer": "The capital of France is Paris."
    }
  ]
}
\`\`\`

### 2. Upload to Google Drive (5 minutes)

1. **Zip your model**:
   - Compress the downloaded model folder
   - Name: `examsathi-model.zip`

2. **Upload**:
   - Go to: https://drive.google.com/drive/folders/1PIDn-fL0cQYc_TbOaTus4fhjMYsYoWlK
   - Upload the ZIP file

3. **Get File ID**:
   - Right-click → Share → Anyone with link
   - Copy link: `https://drive.google.com/file/d/FILE_ID_HERE/view`
   - Save the FILE_ID

### 3. Deploy to Render (10 minutes)

1. **Sign up**: [render.com](https://render.com)

2. **New Web Service**:
   - Click "New +" → "Web Service"
   - Connect this GitHub repo
   - Root Directory: `api`
   - Environment: Docker
   - Plan: Free

3. **Add Environment Variable**:
   - Key: `MODEL_FILE_ID`
   - Value: (paste your FILE_ID from step 2)

4. **Deploy**: Click "Create Web Service"

5. **Wait**: First deployment takes 5-10 minutes

6. **Get URL**: Copy your API URL (e.g., `https://examsathi-ai.onrender.com`)

### 4. Test Your API (2 minutes)

**Browser Test**:
Visit: `https://your-api-url.onrender.com/health`

**Command Line Test**:
\`\`\`bash
curl -X POST https://your-api-url.onrender.com/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is gravity?"}'
\`\`\`

**Expected Response**:
\`\`\`json
{
  "success": true,
  "question": "What is gravity?",
  "answer": "Gravity is a force that attracts objects toward each other..."
}
\`\`\`

### 5. Integrate with Flutter (5 minutes)

**Update API URL**:
\`\`\`dart
// lib/services/examsathi_ai_service.dart
class ExamSathiAIService {
  final String baseUrl = 'https://your-api-url.onrender.com';
  // ... rest of code
}
\`\`\`

**Use in Your App**:
\`\`\`dart
final aiService = ExamSathiAIService();
final answer = await aiService.askQuestion('What is photosynthesis?');
print(answer); // AI-generated answer
\`\`\`

## You're Done!

Your ExamSathi AI is now:
- ✅ Trained on your content
- ✅ Hosted for free
- ✅ Accessible via API
- ✅ Ready for Flutter integration

## Optional: Keep API Awake

Render free tier sleeps after 15 minutes. To keep it awake:

1. Go to [cron-job.org](https://cron-job.org)
2. Create account (free)
3. Add cron job:
   - URL: `https://your-api-url.onrender.com/health`
   - Interval: Every 10 minutes

This pings your API to keep it active 24/7.

## What's Next?

- Add more training data to improve answers
- Customize the model for specific subjects
- Build a beautiful UI in Flutter
- Add features like chat history, favorites, etc.

## Need Help?

Check these guides:
- `docs/RENDER_DEPLOYMENT.md` - Detailed deployment guide
- `docs/TRAINING_GUIDE.md` - Model training details
- `docs/FLUTTER_INTEGRATION_GUIDE.md` - Flutter integration

## Costs

Everything is 100% free:
- Google Colab: Free GPU
- Google Drive: 15GB free storage
- Render: 750 hours/month free
- Total: **$0/month**

Enjoy your free AI model!
\`\`\`

```typescriptreact file="api/railway.yaml" isDeleted="true"
...deleted...
