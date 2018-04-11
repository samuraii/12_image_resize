from PIL import Image
import sys


def resize_image(path_to_original):
    im = Image.open(path_to_original)
    im.thumbnail((100, 100))
    im.save('res.png', 'PNG')


if __name__ == '__main__':
    path = sys.argv[1]
    resize_image(path)
