# Deploy ExamSathi AI to Render (100% Free)

## Step 1: Prepare Your Model

### Train Your Model (Google Colab)

1. Open `scripts/train_model.py` in Google Colab
2. Add your educational questions/answers to `scripts/training_data.json`
3. Run the training script (uses free GPU)
4. Download the trained model folder

### Upload to Google Drive

1. **Compress your model**:
   - Zip the entire model folder
   - Name it: `examsathi-model.zip`

2. **Upload to your Google Drive folder**:
   - Go to: https://drive.google.com/drive/folders/1PIDn-fL0cQYc_TbOaTus4fhjMYsYoWlK
   - Click "New" → "File upload"
   - Upload `examsathi-model.zip`

3. **Make it public**:
   - Right-click the uploaded file
   - Click "Share"
   - Change to "Anyone with the link"
   - Click "Copy link"

4. **Get the File ID**:
   - Your link looks like: `https://drive.google.com/file/d/1ABC123XYZ456/view`
   - Copy the File ID: `1ABC123XYZ456`

## Step 2: Deploy to Render

### Create Render Account

1. Go to [render.com](https://render.com)
2. Sign up with GitHub (free)

### Deploy Your API

1. **Fork/Upload Code**:
   - Push the `api` folder to your GitHub repository
   - Or download and upload manually to Render

2. **Create New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Or select "Deploy from Git URL"

3. **Configure Service**:
   \`\`\`
   Name: examsathi-ai
   Environment: Docker
   Region: Choose closest to you
   Branch: main
   Root Directory: api
   Plan: Free
   \`\`\`

4. **Add Environment Variable**:
   - Click "Environment" tab
   - Add variable:
     - Key: `MODEL_FILE_ID`
     - Value: `1ABC123XYZ456` (your file ID from Step 1)

5. **Deploy**:
   - Click "Create Web Service"
   - Wait 5-10 minutes for first deployment
   - Render will build and start your API

### Get Your API URL

After deployment completes:
- Your API URL: `https://examsathi-ai.onrender.com`
- Copy this URL for your Flutter app

## Step 3: Test Your API

### Test in Browser

Visit: `https://examsathi-ai.onrender.com/health`

You should see:
\`\`\`json
{
  "status": "healthy",
  "model_loaded": true,
  "gpu_available": false
}
\`\`\`

### Test with curl

\`\`\`bash
curl -X POST https://examsathi-ai.onrender.com/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is photosynthesis?"}'
\`\`\`

### Test with the Web Interface

1. Update `app/page.tsx` with your API URL
2. Deploy the web interface to Vercel (free)
3. Test questions in the browser

## Step 4: Integrate with Flutter

Update your Flutter app:

\`\`\`dart
// lib/config/api_config.dart
class ApiConfig {
  static const String baseUrl = 'https://examsathi-ai.onrender.com';
}
\`\`\`

Use the service:
\`\`\`dart
import 'services/examsathi_ai_service.dart';

final aiService = ExamSathiAIService();
final answer = await aiService.askQuestion('What is gravity?');
print(answer);
\`\`\`

## Important Notes

### Free Tier Limits

- ✅ **750 hours/month** (enough for 24/7 usage)
- ✅ **512MB RAM** (good for small models like Phi-2, Llama 3.2 1B)
- ⚠️ **Sleeps after 15 min inactivity** (first request takes 30-60 seconds)
- ✅ **Automatic HTTPS**
- ✅ **Unlimited bandwidth**

### Keep Your API Awake

Render free tier sleeps after 15 minutes. To keep it active:

**Option 1: Use Cron Job (Recommended)**
1. Go to [cron-job.org](https://cron-job.org)
2. Create free account
3. Add new cron job:
   - URL: `https://examsathi-ai.onrender.com/health`
   - Interval: Every 10 minutes
4. This keeps your API awake 24/7

**Option 2: Flutter App Ping**
\`\`\`dart
// Ping API every 10 minutes when app is active
Timer.periodic(Duration(minutes: 10), (timer) {
  aiService.healthCheck();
});
\`\`\`

### Model Size Recommendations

For Render free tier (512MB RAM):

| Model | Size | Works? |
|-------|------|--------|
| Phi-2 | 2.7GB | ✅ Yes (with quantization) |
| Llama 3.2 1B | 2.5GB | ✅ Yes |
| Llama 3.2 3B | 6GB | ❌ Too large |
| Mistral 7B | 14GB | ❌ Too large |

**Tip**: Use 4-bit quantization to reduce model size by 75%

### Updating Your Model

To update your model:
1. Upload new model ZIP to Google Drive
2. Get new File ID
3. Update `MODEL_FILE_ID` in Render dashboard
4. Restart the service

No code changes needed!

## Troubleshooting

### Model Download Fails

**Error**: "Failed to download model from Google Drive"

**Solutions**:
- Verify file is public (Anyone with link can view)
- Check File ID is correct
- Try re-uploading the ZIP file
- Make sure ZIP is not corrupted

### Out of Memory

**Error**: "Killed" or "Out of memory"

**Solutions**:
- Use smaller model (Phi-2 or Llama 3.2 1B)
- Enable 4-bit quantization in training script
- Upgrade to Render paid tier ($7/month for 2GB RAM)

### Slow First Request

**Behavior**: First request takes 30-60 seconds

**Explanation**: 
- Render free tier sleeps after 15 min inactivity
- Model needs to download and load on wake-up
- Subsequent requests are fast (1-2 seconds)

**Solution**: Use cron job to keep API awake

### Model Not Loading

**Error**: "Model not loaded"

**Check**:
1. `MODEL_FILE_ID` is set in Render environment variables
2. File is accessible (test download link manually)
3. Check Render logs for errors

## Cost Summary

| Service | Cost | Usage |
|---------|------|-------|
| Google Colab | Free | Model training |
| Google Drive | Free | Model storage (15GB free) |
| Render | Free | API hosting (750 hrs/month) |
| Cron-job.org | Free | Keep API awake |
| **Total** | **$0/month** | **Unlimited requests** |

## Next Steps

1. ✅ Train your model in Google Colab
2. ✅ Upload to Google Drive
3. ✅ Deploy to Render
4. ✅ Test your API
5. ✅ Integrate with Flutter app
6. ✅ Set up cron job to keep awake

Your ExamSathi AI is now live and free forever!
