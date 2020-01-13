import requests
import shutil
from PIL import Image


def upload_test():

    url = 'http://127.0.0.1:5000/upload'
    files = {'media': open('image.jpg', 'rb')}
    x = requests.post(url, files = files)
    print(x)

def output_test():

    url = 'http://127.0.0.1:5000/output'
    x = requests.post(url)
    with open('output.jpg', 'wb') as out_file:
        out_file.write(x.content)
    print(x)


def report_test():

    url = 'http://127.0.0.1:5000/report'
    x = requests.post(url)
    with open('output.json', 'wb') as out_file:
        out_file.write(x.content)
    print(x)


report_test()
