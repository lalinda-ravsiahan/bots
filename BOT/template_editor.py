from PIL import Image, ImageDraw, ImageFont

def crop_to_circle(image):

    # Check if the image is 1080x1080
    if image.size != (435, 435):
        image=image.resize((435,435),Image.Resampling.LANCZOS)

    # Ensure the image is square
    width, height = 435,435
    
    # Create a circular mask
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    
    # Draw a white filled ellipse in the center
    draw.ellipse((0, 0, width, height), fill=255)
    
    # Apply the mask to create a circular image
    result = Image.new('RGBA', (width, height))
    result.paste(image, (0, 0), mask=mask)
    return result

def edit_text(card_template,text):
    draw = ImageDraw.Draw(card_template)

    image_width, image_height = card_template.size

    text_color = (255, 255, 255)  # White color
    font = ImageFont.truetype("arial.ttf", 40)  # You can use other fonts

    # Define the text and its properties

    #text_width, text_height = draw.textsize(text, font=font)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1] #if we need text height in our project

    # Calculate the position to center the text
    text_position = ((image_width - text_width) / 2 , 825)

    # Add text to the template
    draw.text(text_position, text, font=font, fill=text_color)


def place_image_on_card(card_path, photo_path, output_path, position):
    # Open the images
    card = Image.open(card_path).convert("RGBA")
    photo = Image.open(photo_path).convert("RGBA")
    
    # Crop the photo to a circle
    photo_cropped = crop_to_circle(photo)
    
    #type text into the card
    edit_text(card,"lalinda ravishan weerarathna")
    
    # Position to place the photo (top-left corner)
    x, y = position
    
    # Paste the circular photo onto the card
    card.paste(photo_cropped, (x, y), photo_cropped)
    
    # Save the result(saving the final output)
    card.save(output_path, format="PNG")


# Example usage
card_path = 'Gold Elegant Happy Birthday Instagram Post.png'  # Path to the birthday card image
photo_path = '422533692_1128616231636318_5321871712234321610_n.jpg'      # Path to the photo to insert
output_path = 'final_card.png'   # Path to save the final image
position = (310, 351)            # Position (top-left corner) to place the photo on the card



#page image on the card and get the final output of the edited image template
place_image_on_card(card_path, photo_path, output_path, position) 
