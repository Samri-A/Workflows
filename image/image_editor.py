from PIL import Image, ImageTk , ImageEnhance , ImageFilter 

def Rotate(image , angle):
    img = Image.open(image)
    img = img.rotate(angle, expand=True)
    return img

def Flip( image , direction):
     img = Image.open(image)
     if direction == 'horizontal':
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
     elif direction == 'vertical':
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
     return img

def Resize(image , height , width):
    img = Image.open(image)
    img = img.resize((width, height), Image.ANTIALIAS)
    return img

def Modify_Color_Intensity(image , Color_pos):
      img = Image.open(image)
      Color_pos = float(Color_pos)
      enhancer = ImageEnhance.Color(img)
      img = enhancer.enhance(Color_pos)
      return img

def Crop(image, left, upper, right, lower):
     img = Image.open(image)
     img = img.crop((left, upper, right, lower))
     return img

def Blur(image):
     img = Image.open(image)
     img = img.filter(ImageFilter.BLUR)
     return img


def Emboss(image):
     img = Image.open(image)
     img = img.filter(ImageFilter.EMBOSS)
     return img

def EdgeEnhance(image):
     img = Image.open(image)
     img = img.filter(ImageFilter.EDGE_ENHANCE)
     return img
