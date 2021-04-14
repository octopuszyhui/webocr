import os,platform

upload_path = os.path.join(os.path.dirname(__file__), "img")
static_path = os.path.join(os.path.dirname(__file__), "static")

APP_ID     = '10041182'
API_KEY    = 'NldgdL1UgQWCLWQCv8Qjmshb'
SECRET_KEY = 'ecsCjvt5yv5brGRsIFuhSmm2Qy0ijQLR'

IP = '127.0.0.1'
if(platform.system() == 'Linux'):
    IP = '0.0.0.0'
PORT = 8080
