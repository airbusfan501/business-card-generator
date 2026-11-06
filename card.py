# DEVELOPED BY AIRBUSFAN501. WORK OF AIRBUSFAN501.
from PIL import Image, ImageDraw, ImageFont

# User Input/Variables
name = input("What is your name? eg. John Doe")
role = input("What is your role? eg. Manager")
email = input("What is your business email address?")
phone = input("What is your business phone number?")
website = input("What is your business website address?")

# Drawing/Frontend
img = Image.open("card.png")
draw = ImageDraw.Draw(img)
font_name = ImageFont.truetype("DMSans-VariableFont_opsz,wght.ttf", 64) 
font_role = ImageFont.truetype("DMSans-VariableFont_opsz,wght.ttf", 26) 
font_info = ImageFont.truetype("DMSans-VariableFont_opsz,wght.ttf", 22) 
text_color = (60, 75, 85)

# Printing
draw.text((130, 100), name, fill=text_color, font=font_name)
draw.text((140, 205), role, fill=text_color, font=font_role)
draw.text((215, 347), email, fill=text_color, font=font_info)
draw.text((215, 428), phone, fill=text_color, font=font_info)
draw.text((215, 498), website, fill=text_color, font=font_info)

# Final Product
img.save("finished_card.png")
print("\nYour card has been generated and saved as finished_card.png")