import os
import textwrap
from PIL import Image
import google.generativeai as genai

# Configure Google API key
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(image):
    model = genai.GenerativeModel('gemini-pro-vision')
   
    response = model.generate_content(image)
    return response.text

def main():
    print("Gemini Application")
    
    
    image_path = input("Enter the file path of the image: ")
    
    # Check if the file exists
    if not os.path.isfile(image_path):
        print("Error: File not found")
        return
    
    # Load the image
    try:
        image = Image.open(image_path)
        
    except Exception as e:
        print("Error opening image:", e)
        return
    
    # Get response
    response = get_gemini_response(image)
    

    

