from PIL import Image
import cv2

def convert_png_to_jpg():
    img_png = Image.open('path_to_image_file.png')
    img_png.save('modified_path_to_image_file.jpg')

def convert_png_to_jpg_opencv():
    png_img = cv2.imread('path_to_image_file.png')
    cv2.imwrite('modified_path_to_image_file.jpg', png_img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

if __name__ == '__main__':
    print("converting png to jpg...")
    convert_png_to_jpg()

