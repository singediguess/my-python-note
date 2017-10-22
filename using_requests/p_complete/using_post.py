import requests

me = {'name':'Iverson', 'email':'yolo@py.com'}
r = requests.post('https://www.w3schools.com/php/welcome.php', data=me)
print ('Status code:', r.status_code)

with open('respone.html', 'w+') as file:
    file.write(r.text)