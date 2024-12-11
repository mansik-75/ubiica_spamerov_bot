import re
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
model_name = 'NeuroSpaceX/ruSpamNS_v1'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=1).to(device).eval()
tokenizer = AutoTokenizer.from_pretrained(model_name)

async def clean_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^А-Яа-я0-9 ]+', ' ', text)
    text = text.lower().strip()
    return text
async def classify_message(message):
    message = await clean_text(message)
    encoding = tokenizer(message, padding='max_length', truncation=True, max_length=128, return_tensors='pt')
    input_ids = encoding['input_ids'].to(device)
    attention_mask = encoding['attention_mask'].to(device)
    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask).logits
        pred = torch.sigmoid(outputs).cpu().numpy()[0][0]
    is_spam = int(pred >= 0.8)
    return is_spam