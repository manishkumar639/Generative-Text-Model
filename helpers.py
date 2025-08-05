from PIL import Image
import torch
import numpy as np

def load_and_preprocess(path, transform_pipeline, device):
    image = Image.open(path).convert("RGB")
    tensor = transform_pipeline(image).unsqueeze(0).to(device)
    return tensor

def tensor_to_img(tensor):
    img = tensor.detach().cpu().squeeze().numpy()
    img = img.transpose(1, 2, 0)
    img = (img * 0.5) + 0.5  # De-normalize
    return np.clip(img, 0, 1)