from PIL import Image

filename="6.jpg"
with Image.open(filename) as img:
    img.load()

new_img=img.resize((img.width // 3, img.height // 3))

new_img.save("resized_6.jpg")

converted_img= img.transpose(Image.FLIP_TOP_BOTTOM)
converted_img.save("Image_flip6.jpg")
converted_img= img.transpose(Image.FLIP_LEFT_RIGHT)
converted_img.save("Image_flip2_6.jpg")