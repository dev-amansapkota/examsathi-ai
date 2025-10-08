# ExamSathi AI Web Interface Guide

## Overview

The web interface provides a simple way to test your ExamSathi AI model before integrating it into your Flutter app.

## Features

- **API Configuration**: Connect to your deployed API server
- **Health Check**: Verify server status and model loading
- **Question Input**: Ask questions and get instant answers
- **Sample Questions**: Quick-start with pre-loaded examples
- **Error Handling**: Clear error messages for troubleshooting
- **Responsive Design**: Works on desktop and mobile

## Running Locally

### Prerequisites
- Node.js 18+ installed
- Your API server running (see DEPLOYMENT_GUIDE.md)

### Steps

1. **Install Dependencies**:
\`\`\`bash
npm install
\`\`\`

2. **Run Development Server**:
\`\`\`bash
npm run dev
\`\`\`

3. **Open Browser**:
Navigate to `http://localhost:3000`

4. **Configure API URL**:
- Enter your API URL (e.g., `http://localhost:5000` or your deployed URL)
- Click "Check Status" to verify connection

5. **Start Testing**:
- Type a question or click a sample question
- Press Enter or click "Get Answer"
- View the AI-generated response

## Deploying the Web Interface

### Option 1: Vercel (Recommended)

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Import your repository
4. Deploy (automatic)
5. Get your URL: `https://your-app.vercel.app`

### Option 2: Netlify

1. Push code to GitHub
2. Go to [netlify.com](https://netlify.com)
3. New site from Git
4. Deploy

### Option 3: GitHub Pages

\`\`\`bash
npm run build
npm run export
# Push the 'out' folder to gh-pages branch
\`\`\`

## Configuration

### Environment Variables

Create `.env.local`:

\`\`\`env
NEXT_PUBLIC_API_URL=https://your-api-url.com
\`\`\`

Then update the code to use it:

\`\`\`tsx
const [apiUrl, setApiUrl] = useState(
  process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000'
)
\`\`\`

## Customization

### Change Colors

Edit `app/globals.css`:

\`\`\`css
--color-primary: #2563eb; /* Change to your brand color */
\`\`\`

### Add More Sample Questions

Edit `app/page.tsx`:

\`\`\`tsx
const sampleQuestions = [
  'Your custom question 1',
  'Your custom question 2',
  // Add more...
]
\`\`\`

### Modify Layout

The interface uses:
- Tailwind CSS for styling
- shadcn/ui components
- Lucide icons

All components are in `components/ui/`

## Troubleshooting

### CORS Errors

If you see CORS errors, make sure your API server has CORS enabled:

\`\`\`python
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # This line is important!
\`\`\`

### Connection Refused

- Check API URL is correct
- Verify API server is running
- Check firewall settings

### Slow Responses

- First request takes 30-60 seconds (model loading)
- Subsequent requests are faster
- Consider keeping server warm with cron job

## Next Steps

Once you've tested the web interface:
1. Verify all features work correctly
2. Test with various questions
3. Check error handling
4. Proceed to Flutter integration (see FLUTTER_INTEGRATION_GUIDE.md)
