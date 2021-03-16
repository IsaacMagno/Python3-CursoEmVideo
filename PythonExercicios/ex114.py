import requests
try:
    response = requests.get('http://www.pudim.com.br/')
    on = response.status_code
    print('O site está acessivel.')
except:
    print('O site está inacessível.')
