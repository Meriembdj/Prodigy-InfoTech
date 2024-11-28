from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def validate_image_path(image_path):
    if not os.path.isfile(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        return False
    return True

def display_image(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')  
    plt.show()

def encrypt_image(image_path, output_path, key):
    try:
        img = Image.open(image_path)
        pixel_array = np.array(img)  
        
        # I used np.clip to ensure pixel values remain in the valid range [0-255]
        encrypted_pixel_array = np.clip(pixel_array + key, 0, 255).astype(np.uint8) 
        encrypted_image = Image.fromarray(encrypted_pixel_array)
        encrypted_image.save(output_path)
        print(f"Encrypted image saved as: '{output_path}'.")
        display_image(encrypted_image, "Encrypted Image")
    
    except Exception as e:
        print(f"Error during image encryption: {e}")

def decrypt_image(image_path, output_path, key):
    try:
        img = Image.open(image_path)
        pixel_array = np.array(img) 
        decrypted_pixel_array = np.clip(pixel_array - key, 0, 255).astype(np.uint8) 
        decrypted_image = Image.fromarray(decrypted_pixel_array)
        decrypted_image.save(output_path)
        print(f"Decrypted image saved as: '{output_path}'.")
        display_image(decrypted_image, "Decrypted Image")
    
    except Exception as e:
        print(f"Error during image decryption: {e}")

if __name__ == "__main__":
    try:
        # Open file dialog to choose image
        Tk().withdraw()  # Hide the root window
        image_path = askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        
        if not image_path or not validate_image_path(image_path):
            raise FileNotFoundError("No valid image file selected.")
        
        key = int(input("Enter the encryption key (integer): "))
        encrypted_image_path = "encrypted_image.png"
        decrypted_image_path = "decrypted_image.png"
        encrypt_image(image_path, encrypted_image_path, key)
        decrypt_image(encrypted_image_path, decrypted_image_path, key)
        print("Thank you for using the image encryption/decryption program!")
    
    except ValueError:
        print("Oops! Please enter a valid integer for the key.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
