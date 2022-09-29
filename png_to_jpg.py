from PIL import Image

def convert_png_to_jpg():
    print("converting png to jpg...")
    img_png = Image.open('path_to_image_file.png')
    img_png.save('modified_path_to_image_file.jpg')

if __name__ == '__main__':
    convert_png_to_jpg()

