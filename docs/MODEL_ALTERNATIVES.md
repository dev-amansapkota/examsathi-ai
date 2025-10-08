# Alternative Models for ExamSathi

## Recommended Models by Size

### 1. Phi-2 (2.7B) - RECOMMENDED
- **Size**: 5GB
- **Best for**: General education, reasoning
- **Speed**: Fast
- **Quality**: Excellent for size
\`\`\`python
MODEL_NAME = "microsoft/phi-2"
\`\`\`

### 2. Llama 3.2 (1B) - SMALLEST
- **Size**: 2GB
- **Best for**: Quick responses, mobile-friendly
- **Speed**: Very fast
- **Quality**: Good for basic Q&A
\`\`\`python
MODEL_NAME = "meta-llama/Llama-3.2-1B"
\`\`\`

### 3. Llama 3.2 (3B) - BALANCED
- **Size**: 6GB
- **Best for**: Detailed explanations
- **Speed**: Fast
- **Quality**: Very good
\`\`\`python
MODEL_NAME = "meta-llama/Llama-3.2-3B"
\`\`\`

### 4. Gemma 2 (2B) - GOOGLE
- **Size**: 4GB
- **Best for**: Math and science
- **Speed**: Fast
- **Quality**: Excellent reasoning
\`\`\`python
MODEL_NAME = "google/gemma-2-2b"
\`\`\`

### 5. Mistral 7B - POWERFUL
- **Size**: 14GB
- **Best for**: Complex topics, detailed answers
- **Speed**: Moderate
- **Quality**: Excellent
\`\`\`python
MODEL_NAME = "mistralai/Mistral-7B-v0.1"
\`\`\`

## How to Choose

| Your Priority | Recommended Model |
|--------------|-------------------|
| Fastest responses | Llama 3.2 (1B) |
| Best quality | Mistral 7B |
| Balanced | Phi-2 |
| Math/Science focus | Gemma 2 |
| Smallest size | Llama 3.2 (1B) |

## Switching Models

Simply change the `MODEL_NAME` in `train_model.py`:

\`\`\`python
# Change this line:
MODEL_NAME = "microsoft/phi-2"

# To your preferred model:
MODEL_NAME = "meta-llama/Llama-3.2-1B"
\`\`\`

All models work with the same training script!
