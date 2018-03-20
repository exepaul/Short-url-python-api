import requests
import json

def shorten_url(url):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key={}'.format('api_key')
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(post_url, data=json.dumps(payload), headers=headers)
    return r.json()
    
    
    
    
    
    
    #image upload via python api:
    
import cloudinary
import cloudinary.uploader
import urllib
import cloudinary.api
import urllib
cloudinary.config(
  cloud_name = "cloud_",
  api_key = "key_",
  api_secret = "key_"
)

cloudinary.uploader.upload("sample.png")['url'])['id']
