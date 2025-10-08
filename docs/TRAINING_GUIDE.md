# ExamSathi AI Model Training Guide

## Step 1: Prepare Your Training Data

1. Edit `scripts/training_data.json` with your educational content
2. Add as many question-answer pairs as possible (minimum 100 recommended)
3. Format: `{"question": "...", "answer": "..."}`

### Example Topics to Include:
- Math problems and solutions
- Science concepts and explanations
- History facts and dates
- Grammar rules and examples
- Exam preparation tips

## Step 2: Run Training in Google Colab (FREE)

### Open Google Colab:
1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Create a new notebook
3. Enable GPU: Runtime → Change runtime type → GPU (T4)

### Install Dependencies:
\`\`\`python
!pip install transformers datasets torch accelerate bitsandbytes
\`\`\`

### Upload Your Files:
\`\`\`python
from google.colab import files
uploaded = files.upload()  # Upload training_data.json and train_model.py
\`\`\`

### Run Training:
\`\`\`python
!python train_model.py
\`\`\`

### Training Time:
- With 100 examples: ~10-15 minutes
- With 1000 examples: ~1-2 hours
- Free Colab GPU is sufficient!

## Step 3: Save Your Model

### Option A: Download to Your Computer
\`\`\`python
from google.colab import files
!zip -r examsathi-model.zip ./examsathi-model
files.download('examsathi-model.zip')
\`\`\`

### Option B: Upload to Google Drive
\`\`\`python
from google.colab import drive
drive.mount('/content/drive')
!cp -r ./examsathi-model /content/drive/MyDrive/
\`\`\`

### Option C: Upload to GitHub
\`\`\`bash
# Create a new repository on GitHub
# Then in Colab:
!git config --global user.email "your@email.com"
!git config --global user.name "Your Name"
!git clone https://github.com/yourusername/examsathi-model.git
!cp -r ./examsathi-model/* ./examsathi-model-repo/
!cd examsathi-model-repo && git add . && git commit -m "Add trained model" && git push
\`\`\`

## Step 4: Get Model Download Link

### For Google Drive:
1. Right-click on model folder → Share → Anyone with link
2. Copy the link (format: `https://drive.google.com/file/d/FILE_ID/view`)
3. Convert to direct download: `https://drive.google.com/uc?export=download&id=FILE_ID`

### For GitHub:
1. Use GitHub releases or raw file URLs
2. Example: `https://github.com/username/repo/releases/download/v1.0/model.zip`

## Model Size & Requirements

- **Phi-2 Model**: ~5GB
- **Llama 3.2 (1B)**: ~2GB (alternative, smaller)
- **Llama 3.2 (3B)**: ~6GB (alternative, more powerful)

## Tips for Better Results

1. **More Data = Better Model**: Aim for 500+ examples
2. **Diverse Topics**: Cover all subjects in your app
3. **Quality Over Quantity**: Accurate answers are crucial
4. **Regular Updates**: Retrain with new questions monthly
5. **Test Thoroughly**: Try edge cases before deployment

## Cost Breakdown

- Training: FREE (Google Colab)
- Storage: FREE (Google Drive 15GB or GitHub)
- Hosting: FREE (see API server setup)

Total Cost: $0
