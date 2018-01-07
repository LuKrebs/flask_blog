import os

SECRET_KEY = "1234"
DEBUG = True

DB_USERNAME = 'app_user'
DB_PASSWORD = 'app_password'
BLOG_DATABASE_NAME = 'blog'
DB_HOST = os.getenv('IP', '0.0.0.0.')

DB_URI = "mysql+pymysql://{}:{}@{}/{}".format(DB_USERNAME, DB_PASSWORD,DB_HOST,BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True