import random
import urllib.request #module defines functions and classes which help in opening URLs

def download_image(url):
    name = random.randrange(1,1000)
    file_name = str(name)+".jpg"
    urllib.request.urlretrieve(url,file_name)


download_image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Grumpy_Cat_by_Gage_Skidmore.jpg/800px-Grumpy_Cat_by_Gage_Skidmore.jpg')
