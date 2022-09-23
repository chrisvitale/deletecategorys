import requests
import json

#completa la apikey del cliente
api_key = "xxx"

#completa los id de categorías que deseas borrar.
category = [
'001014001013',
'001014001001',

]

for n in category:
    url = 'https://api.woowup.com/apiv3/categories'
    headers = {'content-type': 'application/json', "Authorization": "Basic "+str(api_key), 'accept': 'application/json'}
    payload = json.dumps({
      "code": str(n)})
    r = requests.delete(url, data=payload, headers=headers)
    print(payload)
    print(r.text)

