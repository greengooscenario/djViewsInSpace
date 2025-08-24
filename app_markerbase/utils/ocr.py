from PIL import Image, ImageFilter, ImageOps
import pytesseract

def read_text(imgfile):
    # Open the image file
    image = Image.open(imgfile)
    # Convert for easyer OCR:
    image = ImageOps.autocontrast(image)  # tweak contrast
    image = image.convert("L")  # to gray scale
    image = ImageOps.autocontrast(image)  # tweak contrast
    threshold = 200  # to black&white by threshold
    image = image.point(lambda x: 0 if x < threshold else 255, '1')

    
    # Perform OCR
    ##text0 = pytesseract.image_to_string(gray, lang='lat+deu', config='--psm 0')
    ##text1 = pytesseract.image_to_string(gray, lang='lat+deu', config='--psm 1')
    ##text3 = pytesseract.image_to_string(gray, lang='lat+deu', config='--psm 3')
    ##text4 = pytesseract.image_to_string(gray, lang='lat+deu', config='--psm 4')
    text6 = pytesseract.image_to_string(image, lang='lat+deu', config='--psm 6')
    ##text7 = pytesseract.image_to_string(gray, lang='lat+deu', config='--psm 7')
    ##text11 = pytesseract.image_to_string(gray, lang='lat+deu', config='--psm 11')
    ##text12 = pytesseract.image_to_string(gray, lang='lat+deu', config='--psm 12')
    ##print(f"========= OCR psm 0: {text0}")
    ##print(f"========= OCR psm 1: {text1}")
    ##print(f"========= OCR psm 3: {text3}")
    ##print(f"========= OCR psm 4: {text4}")
    print(f"========= OCR psm 6: {text6}")
    ##print(f"========= OCR psm 7: {text7}")
    ##print(f"========= OCR psm 11: {text11}")
    ##print(f"========= OCR psm 12: {text12}")
    ##data = pytesseract.image_to_data(gray, lang='lat+deu')
    ##print(f"========= OCR data: {data}")
    return text6

