"""
ExamSathi AI Model Training Script
This script fine-tunes a small language model for educational Q&A
Run this in Google Colab for free GPU access
"""

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from datasets import Dataset
import json

# Configuration
MODEL_NAME = "microsoft/phi-2"  # Small but powerful model (2.7B parameters)
OUTPUT_DIR = "./examsathi-model"
MAX_LENGTH = 512

def prepare_dataset(data_file="training_data.json"):
    """
    Load and prepare your educational dataset
    Expected format: [{"question": "...", "answer": "..."}, ...]
    """
    with open(data_file, 'r') as f:
        data = json.load(f)
    
    # Format data for training
    formatted_data = []
    for item in data:
        text = f"Question: {item['question']}\nAnswer: {item['answer']}"
        formatted_data.append({"text": text})
    
    return Dataset.from_list(formatted_data)

def tokenize_function(examples, tokenizer):
    """Tokenize the dataset"""
    return tokenizer(
        examples["text"],
        truncation=True,
        max_length=MAX_LENGTH,
        padding="max_length"
    )

def train_model():
    """Main training function"""
    print("Loading model and tokenizer...")
    
    # Load pre-trained model
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True
    )
    
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    
    print("Loading dataset...")
    dataset = prepare_dataset()
    
    # Tokenize dataset
    tokenized_dataset = dataset.map(
        lambda x: tokenize_function(x, tokenizer),
        batched=True,
        remove_columns=dataset.column_names
    )
    
    # Training arguments
    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        num_train_epochs=3,
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        learning_rate=2e-5,
        fp16=True,
        save_steps=100,
        logging_steps=10,
        save_total_limit=2,
        push_to_hub=False,
    )
    
    # Data collator
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )
    
    # Initialize trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        data_collator=data_collator,
    )
    
    print("Starting training...")
    trainer.train()
    
    print("Saving model...")
    model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    
    print(f"Model saved to {OUTPUT_DIR}")
    print("Upload this folder to Google Drive or GitHub!")

if __name__ == "__main__":
    train_model()
