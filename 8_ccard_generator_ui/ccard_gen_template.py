from PIL import Image, ImageDraw, ImageFont
from ccard_gen import card_number, c_expiry, c_cvv

def create_card_image(card_number, c_expiry, c_cvv):
    # Loads the card template in jpg format
    img = Image.open("CCard.jpg")

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("Orbitron-Bold.ttf", 8)

    draw.text((20, 130), f"CCARD: {card_number}", (0,0,0), font=font)
    draw.text((20, 160), "NAME:",(190,57,38), font=font)
    draw.text((20, 170), "JOHN DOE", (190,57,38), font=font)
    draw.text((100, 160), "EXPIRY DATE:",(190,57,38), font=font)
    draw.text((100, 170), f"{c_expiry}", (190,57,38), font=font)
    draw.text((200, 160), "CVV:", (190,57,38), font=font)
    draw.text((200, 170), f"{c_cvv}", (190,57,38), font=font)

    img.save("generated_card.jpg")

create_card_image(card_number, c_expiry, c_cvv)