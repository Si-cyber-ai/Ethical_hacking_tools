from PIL import Image
import os

# Function to encrypt
def encrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    # Pixel Map
    pixels = image.load()  
    # Iterate through the pixels
    for i in range(image.width):
        for j in range(image.height):
            # Get the RGB(A) values
            pixel = pixels[i, j]
            
            # RGB
            if len(pixel) == 3:
                r, g, b = pixel
                # Apply a simple encryption by adding the key
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                # Set the pixel value
                pixels[i, j] = (r, g, b)

            # RGBA      
            elif len(pixel) == 4:  
                r, g, b, a = pixel
                # Apply a simple encryption by adding the key
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                # Preserve the Alpha Channel
                pixels[i, j] = (r, g, b, a) 

    # Save the encrypted image
    image.save(output_path)
    print("Encrypted image saved as ",output_path)

# Function to decrypt
def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    image = Image.open(image_path)
    # Pixel Map
    pixels = image.load() 
    # Iterate through the pixels
    for i in range(image.width):
        for j in range(image.height):
            pixel = pixels[i, j]

            # RGB
            if len(pixel) == 3:  
                r, g, b = pixel
                # Apply decryption by subtracting the key
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                pixels[i, j] = (r, g, b)  

            # RGBA
            elif len(pixel) == 4:  
                r, g, b, a = pixel
                # Apply decryption by subtracting the key
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                pixels[i, j] = (r, g, b, a)

    # Save the decrypted image
    image.save(output_path)
    print(f"Decrypted image saved as ",output_path)

# Main function 
action = input("Enter 'E' for encrypt or 'D' for decrypt: ").strip().upper()
image_path = input("Enter the path of the image file: ")
key = int(input("Enter a numerical key for encryption/decryption (0-255): "))

if action == 'E':
    output_path = "encrypted_image.png"
    encrypt_image(image_path, output_path, key)
elif action == 'D':
    output_path = "decrypted_image.png"
    decrypt_image(image_path, output_path, key)
else:
    print("Invalid action. Please enter 'E' for encrypt or 'D' for decrypt")
