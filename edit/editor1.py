from PIL import Image, ImageDraw, ImageOps

def crop_to_circle(image):
    # Create a circular mask
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 435, 435), fill=255)
    
    # Apply the mask to create a circular image
    circular_image = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    circular_image.putalpha(mask)
    return circular_image

def place_image_on_card(card_path, photo_path, output_path, position, circle_diameter):
    # Open the images
    card = Image.open(card_path).convert("RGBA")
    photo = Image.open(photo_path).convert("RGBA")
    
    # Crop the photo to a circle
    photo_cropped = crop_to_circle(photo)
    
    # Resize the circular photo to fit the circle on the card
    #photo_resized = photo_cropped.resize((circle_diameter, circle_diameter),  Image.Resampling.LANCZOS)
    
    # Position to place the photo (top-left corner)
    x, y = position
    
    # Paste the circular photo onto the card
    card.paste(photo_cropped, (x, y), photo_cropped)
    
    # Save the result
    card.save(output_path, format="PNG")

# Example usage
card_path = 'Gold Elegant Happy Birthday Instagram Post.png'  # Path to the birthday card image
photo_path = '6I9A0704.JPG'      # Path to the photo to insert
output_path = 'final_card.png'   # Path to save the final image
position = (310, 351)            # Position (top-left corner) to place the photo on the card
circle_diameter = 420            # Diameter of the circle where the photo should be placed

place_image_on_card(card_path, photo_path, output_path, position, circle_diameter)
