from PIL import Image

def swap_black_white(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Get image dimensions
    width, height = img.size
    
    # Create a new image to store the modified pixels
    new_img = Image.new("RGB", (width, height))
    
    # Iterate through each pixel
    for x in range(width):
        for y in range(height):
            # Get the pixel color at (x, y)
            pixel_color = img.getpixel((x, y))
            
            # Swap black and white pixels
            new_pixel_color = tuple(255 - val for val in pixel_color)
            
            # Set the new pixel color in the new image
            new_img.putpixel((x, y), new_pixel_color)
    
    # Save the new image
    new_image_path = "swapped_" + image_path
    new_img.save(new_image_path)
    
    print("Image processed and saved as:", new_image_path)

# Enter the path of the image
input_image_path = str(input("Enter Image: "))
swap_black_white(input_image_path)
