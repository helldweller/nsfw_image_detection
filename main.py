# Falconsai/nsfw_image_detection
# Load model directly

import time
import torch
from PIL import Image
from transformers import AutoImageProcessor, AutoModelForImageClassification

model_dir = './saved_model' # path to https://huggingface.co/Falconsai/nsfw_image_detection
image_dir = './images'
processor = AutoImageProcessor.from_pretrained(f'{model_dir}/preprocessor_config.json', local_files_only=True)
model = AutoModelForImageClassification.from_pretrained(f'{model_dir}', local_files_only=True)

print(f'CUDA is {"ok" if torch.cuda.is_available() else "unavailable"}')

def predict(img_path):
    img = Image.open(f'{image_dir}/{img_path}')
    with torch.no_grad():
        inputs = processor(images=img, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits
    predicted_label = logits.argmax(-1).item()
    return model.config.id2label[predicted_label]
    # {0: 'normal', 1: 'nsfw'}


t0 = time.time()
imgs = ["usual1.jpg", "nsfw2.jpg", "nsfw1.jpg"]
for x in imgs:
  print(f'Image {x} is {predict(x)}')
t1 = time.time()

print(f'Time spent: {t1-t0}')
