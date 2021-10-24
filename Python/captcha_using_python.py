# install captcha using pip 
# pip install captcha 
# Import ImageCaptcha 
from captcha.image import ImageCaptcha

# Creating an obj Image for storing Captcha image
# Provide desirable height and width
image = ImageCaptcha(height = 100, width = 300)

# Now store the characters you want to show as a Captcha text. 
captcha_text = 'q6w8g4'

# Generate an Image Captcha of the given characters.
data = image.generate(captcha_text)

# Generate and write an image Captcha data to the output.
image.write(captcha_text, 'captcha.png')
