from PIL import Image
import io
import os
import requests

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


def text_to_image(text):
    image_bytes = query({
        "inputs": text,
    })

    image = Image.open(io.BytesIO(image_bytes))

    filename = input(
        "Enter the filename to save the image as (include extension, e.g., image.png): ")

    current_directory = os.path.dirname(__file__) if __file__ else "."
    image_path = os.path.join(current_directory, filename)
    image.save(image_path)

    print(f"Image saved at: {image_path}")
