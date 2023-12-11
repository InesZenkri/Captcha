from PIL import Image, ImageDraw, ImageFont
import random
import string

def generate_captcha(text_length=6, image_width=200, image_height=100):
    font_paths = [
        "./arial.ttf",  
        "./times.ttf",  
        "./calibri.ttf",
        "./consolaz.ttf"
    ]
    
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=text_length))

    image = Image.new('RGB', (image_width, image_height), color=(255, 255, 255))
    font_sizes = [40 for _ in range(text_length)]  

    d = ImageDraw.Draw(image)
    
    for i in range(text_length):
        font_path = random.choice(font_paths)
        font = ImageFont.truetype(font_path, font_sizes[i])
        text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        d.text((10 + i * 30, 10), captcha_text[i], fill=text_color, font=font)

    for _ in range(50):
        d.point((random.randint(0, image_width), random.randint(0, image_height)), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    image.save('captcha.png')
    image.show()

    return captcha_text

generated_text = generate_captcha()
print("Generated CAPTCHA text:", generated_text)
