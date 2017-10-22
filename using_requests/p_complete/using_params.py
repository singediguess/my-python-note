import requests
params = {'q' : 'coffee'} 
res = requests.get('https://www.bing.com/search?', params=params)
print (res.url)
