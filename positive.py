from PIL import Image

def create_negative_image(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Get image dimensions
    width, height = img.size
    
    # Create a new image to store the color-inverted pixels
    color_inverted_img = Image.new("RGB", (width, height))
    
    # Iterate through each pixel
    for x in range(width):
        for y in range(height):
            # Get the pixel color at (x, y)
            pixel_color = img.getpixel((x, y))
            
            # Invert the color channels
            inverted_pixel_color = tuple(255 - val for val in pixel_color)
            
            # Set the inverted pixel color in the new image
            color_inverted_img.putpixel((x, y), inverted_pixel_color)
    
    # Save the color-inverted image
    color_inverted_image_path = "color_inverted_" + image_path
    color_inverted_img.save(color_inverted_image_path)
    
    print("Color-inverted image saved as:", color_inverted_image_path)

# Enter the path of the image
negative_image_path = str(input("Enter Image: "))
create_negative_image(negative_image_path)
