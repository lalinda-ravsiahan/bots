from PIL import Image

def rescale_image(input_path, output_path, scale_factor):
    # Open the original image
    img = Image.open(input_path)
    
    # Calculate the new dimensions
    original_width, original_height = img.size
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)
    
    # Rescale the image
    rescaled_img = img.resize((1080, 1080), Image.Resampling.LANCZOS)
    
    # Save the rescaled image
    rescaled_img.save(output_path)

# Example usage
input_path = 'original_image.jpg'  # Path to the original image
output_path = 'rescaled_image.jpg' # Path to save the rescaled image
scale_factor = 0.5                 # Scale factor (0.5 means half the size)

rescale_image('6I9A0704.JPG', 'lala.jpg', 0.5)
