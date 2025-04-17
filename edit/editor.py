from PIL import Image, ImageDraw

def crop_to_circle(image_path, output_path):
    # Open an image file
    photo_resized = Image.open(image_path)
    img1 = photo_resized.resize((1080, 1080),  Image.Resampling.LANCZOS)
    img1.save("paka.jpg")

    img=img1.convert("RGBA")
    # Create a new image (same size as the input image) with a transparent background
    mask = Image.new('L', img.size, 0)
    
    # Create a drawing context for the mask
    draw = ImageDraw.Draw(mask)
    
    print(img.size)

    # Draw a white-filled circle in the middle of the mask
    width, height = 416,416
    draw.ellipse((0, 0, width, height), fill=255)
    
    # Create a new image with an alpha channel (RGBA) to hold the output
    result = Image.new('RGBA', img.size)
    
    # Paste the original image into the result image using the mask
    result.paste(img, (0, 0), mask=mask)
    
    # Optionally, you can crop to the bounding box of the circle to remove extra space
    bbox = mask.getbbox()
    result = result.crop(bbox)
    
    # Save the resulting image
    result.save(output_path)

# Example usage
crop_to_circle('6I9A0704.JPG', 'round_image.png')
