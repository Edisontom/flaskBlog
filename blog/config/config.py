import ConfigParser
import os


root = os.path.realpath(os.path.dirname(__file__))
config_path = os.path.join(root, 'config.ini')
config = ConfigParser.ConfigParser()
config.read(config_path)


DATABASE = config.get('PATH', 'DATABASE')
DEBUG = config.get('OTHER', 'DEBUG')
SECRET_KEY = config.get('SECRETS', 'SECRET_KEY')
USERNAME = config.get('SECRETS', 'USERNAME')
PASSWORD = config.get('SECRETS', 'PASSWORD')

APP_DIR = root.rsplit('/blog', 1)[0]
UPLOAD_IMAGE = os.path.join(APP_DIR, config.get('PATH', 'UPLOAD_IMAGE'))
IMAGE_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_MUSIC = os.path.join(APP_DIR, config.get('PATH', 'UPLOAD_MUSIC'))
MUSIC_EXTENSIONS = set(['mp3'])
IMG_WIDTH = int(config.get('OTHER', 'IMG_WIDTH'))









