"""
ExamSathi AI Model API Server
Downloads model from Google Drive and serves predictions
Optimized for Render.com free hosting
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import os
import gdown
import zipfile

app = Flask(__name__)
CORS(app)

# Configuration
MODEL_DIR = "./models"
CURRENT_MODEL = None
CURRENT_TOKENIZER = None
MODEL_LOADED = False

GDRIVE_FOLDER_URL = "https://drive.google.com/drive/folders/1PIDn-fL0cQYc_TbOaTus4fhjMYsYoWlK?usp=sharing"
MODEL_FILE_ID = os.getenv("MODEL_FILE_ID", "")  # Set this in Render
MODEL_NAME = "examsathi-model"

def download_model_from_gdrive():
    """Download model from your Google Drive folder"""
    print(f"Downloading model from Google Drive...")
    
    if not MODEL_FILE_ID:
        print("ERROR: MODEL_FILE_ID not set!")
        return False
    
    try:
        model_path = os.path.join(MODEL_DIR, MODEL_NAME)
        os.makedirs(MODEL_DIR, exist_ok=True)
        
        # Download using gdown
        download_url = f"https://drive.google.com/uc?id={MODEL_FILE_ID}"
        output_file = f"{model_path}.zip"
        
        print(f"Downloading from: {download_url}")
        gdown.download(download_url, output_file, quiet=False, fuzzy=True)
        
        # Extract zip file
        print("Extracting model files...")
        with zipfile.ZipFile(output_file, 'r') as zip_ref:
            zip_ref.extractall(model_path)
        
        # Clean up zip file
        os.remove(output_file)
        print("Model downloaded and extracted successfully!")
        return True
        
    except Exception as e:
        print(f"Error downloading model: {str(e)}")
        return False

def load_model():
    """Load the AI model"""
    global CURRENT_MODEL, CURRENT_TOKENIZER, MODEL_LOADED
    
    model_path = os.path.join(MODEL_DIR, MODEL_NAME)
    
    # Download if not exists
    if not os.path.exists(model_path):
        print("Model not found locally. Downloading from Google Drive...")
        if not download_model_from_gdrive():
            return False, "Failed to download model from Google Drive"
    
    # Load model and tokenizer
    try:
        print(f"Loading model from {model_path}...")
        
        CURRENT_TOKENIZER = AutoTokenizer.from_pretrained(
            model_path,
            trust_remote_code=True
        )
        
        CURRENT_MODEL = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto" if torch.cuda.is_available() else None,
            trust_remote_code=True,
            low_cpu_mem_usage=True
        )
        
        MODEL_LOADED = True
        print("Model loaded successfully!")
        return True, "Model loaded successfully"
        
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        return False, f"Error loading model: {str(e)}"

def generate_response(question, max_length=512, temperature=0.7):
    """Generate answer using the loaded model"""
    if not MODEL_LOADED:
        return None, "Model not loaded"
    
    try:
        # Format prompt for educational Q&A
        prompt = f"Question: {question}\nAnswer:"
        
        # Tokenize
        inputs = CURRENT_TOKENIZER(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=max_length
        )
        
        # Move to GPU if available
        if torch.cuda.is_available():
            inputs = {k: v.cuda() for k, v in inputs.items()}
        
        # Generate
        with torch.no_grad():
            outputs = CURRENT_MODEL.generate(
                **inputs,
                max_new_tokens=256,
                temperature=temperature,
                do_sample=True,
                top_p=0.9,
                pad_token_id=CURRENT_TOKENIZER.eos_token_id
            )
        
        # Decode
        response = CURRENT_TOKENIZER.decode(outputs[0], skip_special_tokens=True)
        answer = response.split("Answer:")[-1].strip()
        
        return answer, None
        
    except Exception as e:
        return None, f"Error: {str(e)}"

# API Routes

@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    return jsonify({
        "message": "ExamSathi AI API",
        "status": "running",
        "model_loaded": MODEL_LOADED,
        "endpoints": {
            "health": "/health",
            "ask": "/ask (POST)",
            "load": "/load-model (POST)"
        }
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check"""
    return jsonify({
        "status": "healthy",
        "model_loaded": MODEL_LOADED,
        "gpu_available": torch.cuda.is_available()
    })

@app.route('/load-model', methods=['POST'])
def load_model_endpoint():
    """Manually load model"""
    success, message = load_model()
    return jsonify({
        "success": success,
        "message": message,
        "model_loaded": MODEL_LOADED
    })

@app.route('/ask', methods=['POST'])
def ask_question():
    """Ask a question"""
    try:
        data = request.get_json()
        question = data.get('question', '')
        
        if not question:
            return jsonify({
                "success": False,
                "error": "Question is required"
            }), 400
        
        # Auto-load model if needed
        if not MODEL_LOADED:
            success, message = load_model()
            if not success:
                return jsonify({
                    "success": False,
                    "error": message
                }), 500
        
        # Generate answer
        answer, error = generate_response(
            question,
            max_length=data.get('max_length', 512),
            temperature=data.get('temperature', 0.7)
        )
        
        if error:
            return jsonify({
                "success": False,
                "error": error
            }), 500
        
        return jsonify({
            "success": True,
            "question": question,
            "answer": answer
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    print("🚀 Starting ExamSathi AI Server...")
    print(f"📁 Google Drive Folder: {GDRIVE_FOLDER_URL}")
    print(f"🔑 Model File ID: {MODEL_FILE_ID if MODEL_FILE_ID else 'NOT SET'}")
    
    # Auto-load model on startup
    if MODEL_FILE_ID:
        print("⏳ Loading model on startup...")
        load_model()
    else:
        print("⚠️  MODEL_FILE_ID not set. Model will load on first request.")
    
    # Start server
    port = int(os.getenv('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
