import torch
import torchvision.transforms as transforms
from PIL import Image
import os

def load_model(model_path):
    # Load your model here. This is just a placeholder.
    model = torch.load(model_path)
    model.eval()
    return model

def preprocess_image(image_path):
    # Example preprocessing
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    image = Image.open(image_path).convert('RGB')
    return transform(image).unsqueeze(0)

def predict(model, image_tensor):
    with torch.no_grad():
        output = model(image_tensor)
        # Assuming binary classification: 0 - real, 1 - deepfake
        _, predicted = torch.max(output, 1)
        return 'deepfake' if predicted.item() == 1 else 'real'

if __name__ == "__main__":
    import sys
    model = load_model('../models/image_deepfake_model.pth')
    image_tensor = preprocess_image(sys.argv[1])
    result = predict(model, image_tensor)
    print(f"The image is: {result}")
