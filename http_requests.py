# From within the jupyter notebook, you can execute bash commands using ! char.
# so the following command gets you the requests package installed

!pip install requests --upgrade


# Basic http request
result = requests.get('http://swapi.dev/api/planets/3')
result.status_code # 200
pprint(result.headers) # {Will return a JSON object with lots of info}
result.text # raw text in a JSON object
json.loads(result.text) # return a python dictionary, like a javascript object.

# more examples
import requests
from pprint import pprint
import json

print(requests.__version__) # 2.22.0
result = requests.get('http://universities.hipolabs.com/search?country=United+States')
result.status_code # 200
type(result) # requests.model.response
type(result.headers) # requests.structures.CaseInsensitiveDict

# Another example
import requests
import webbrowser

url = 'https://www.wikipedia.org/'

result = requests.get(url)
print(result.url) # https://www.wikipedia.org/
webbrowser.open(result.url) # True and brings up a browser instance in default browser

search_term = input("Enter the term you need to search")
URL = 'https://www.youtube.com/search'
PARAMS = {'q': search_term}
result = requests.get(url = URL, params = PARAMS)
webbrowser.open(result.url) 

import requests
from pprint import pprint
result = requests.post('https://en.wikipedia.org/w/index.php', data = {'search': 'Skillsoft'})

with open('skillsoft.html', 'wb') as f:
  for chunk in result.iter_content(chunk_size=10000):
    f.write(chunk)
    
!open -a "Google Chrome" skillsoft.html

#Attach text file data to post request
!echo "This is a text file that will be attached to POST request" > test.txt
!cat test.txt # confirm the file contents 

url = 'http://httpbin.org/post'
files = {'files': open('test.txt', 'rb')}
values = {'upload_file' : 'test.txt', 'OUT': 'csv'}

result = requests.post(url, files=files, data=values)
result.status_code # 200

# Post request with multiple parameters

import requests
from pprint import pprint
import webbrowser

url = 'http://pastebin.com/api/api_post.php'
payload = "{'username': 'John', 'email': 'john@home.com'}"
API_KEY = '068HJHJJ84JJKH88H'
parameters = {'api_dev_key': API_KEY, 'api_option': 'paste', 'api_paste_code': payload, 'api_paste_format': 'python'}
result = requests.post(url, data=parameters)

if result.status_code == 200:
  print("Success, see, {}".format(result.text))
else:
  print("sorry, try again")

 # Head requests

import requests
from pprint import pprint
import json

result = requests.head('http://example.com')
result.headers # {HEADERS INFO AS JSON OBJECT}
result.headers['content-type'] # html

# Other HTTP codes

import requests
from pprint import pprint
import json

result = requests.put('http://httpbin.org/put', data = {'key':'value'}) # Overwrites data as oppose to creating like a post request

r_options = requests.options('https://httpbin.org/get')
r_options.headers # JSON object, such as 'Allow', 'Access-Control-Allow-Origin': '*'

result = requests.delete('http://httpbin.org')

# Request and Response Headers

import requests
from pprint import pprint

url = 'http://swapi.co/api/people/3'
headers = {'user-agent':'Googlechrome'}

resp = requests.get(url, headers=headers)
resp.headers # response headers
resp.json() # give me some json format

# Content encoding
import requests
from pprint import pprint

result = request.get('http://httpbin.org')
resp.encoding = 'utf-8' # or change to 'ISO-8859-1'

pprint(result.text) # encoding may affect text format

from PIL import Image
from io import BytesIO

resp = requests.get('SOME IMAGE online')
type(resp.content) # bytes

image = Image.open(BytesIO(resp.content))
type(image) # PIL.JpegImagePlugin.JpegImageFile
image.save('pic.png')


Image.open('pic.png')

# Handling responses in different formats

import requests

resp = requests.get("https://yahoo.com")
resp.ok # True
resp.raise_for_status()
resp.headers['content-type'] # 'text/html; charset-UTF-8'
resp.headers.get('content-type')


# if its json can invoke resp.json()

# Redirects and Timeout

import requests
from pprint import pprint

response = requests.get('http://gmail.com')
response.history # [<Response [301]>,<Response [302]>,<Response [302]>]
response.url # will show redirected url

response.is_redirect
response.is_permanent_redirect



# http exceptions

from requests import exceptions
try:
    result = requests.get('http://nonexistent.com/')
except exceptions.ConnectionError: # or ConnectTimeout ...
      print('oops')

    







           








  
  

                       
                       





