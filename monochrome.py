from PIL import Image

def convert_to_monochrome(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to monochrome
    monochrome_img = img.convert("L")  # "L" mode stands for grayscale
    
    # Save the monochrome image
    monochrome_image_path = "monochrome_" + image_path
    monochrome_img.save(monochrome_image_path)
    
    print("Image converted to monochrome and saved as:", monochrome_image_path)

# Enter the path of the image
input_image_path = str(input("Enter Image: "))
convert_to_monochrome(input_image_path)
