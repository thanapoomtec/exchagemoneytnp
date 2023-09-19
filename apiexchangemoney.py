import requests
import json
import zlib

session = requests.Session()

apicurrency = 'https://www.apilayer.net/api/live?access_key=2ddcf98879872141c9cc2b4a2aec87b9'

def convertcurrencies(amount=''):
    headers = {
        'Host': 'www.apilayer.net',
        'Accept': '*/*',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; SM-N971N Build/PQ3B.190801.06281541)',
        'Accept-Language': 'th-TH;q=1',
        'te':'gzip, deflate; q=0.5',
        'Accept-Encoding': 'gzip'
    }

    payload = {}

    response = session.get(apicurrency, headers=headers, json=payload)
    
    if response.headers.get('content-encoding') == 'gzip':
        data = zlib.decompress(response.content, 16 + zlib.MAX_WBITS)
    else:
        data = response.content

    # แสดงข้อมูลที่ได้รับ
    
    try:
        json_data = json.loads(data)
        print(json_data)
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")



def listcheckcountry():
    access_key ='2ddcf98879872141c9cc2b4a2aec87b9'
    response = session.get(f'https://api.currencylayer.com/list?access_key={access_key}')
    data = response.json()['currencies'] 
    
    try:
        currencies_list = []
        
        json_data = json.loads(json.dumps(data))
        
        # ดึงข้อมูลสกุลเงิน 
        #gets_data = json_data.get('')
     
        for listcountry,get_data  in json_data.items():
            currency_info = f"{listcountry}:{get_data }"
            currencies_list.append(currency_info)
    
        for currency_info in currencies_list:
            listcc = currencies_list
        return listcc
            
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        


def currenciescheck():
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Basic bG9kZXN0YXI6Wk9tR1g4UkRpZ1V6MlJONHZnSTk3NlRVRlNYanF1emU=',
        'connection': 'keep-alive',
        'cookie': 'optimizelyEndUserId=oeu1691766449309r0.7264096484786993; _fbp=fb.1.1691766452923.606866309; IR_gbd=xe.com; ln_or=eyIxNDA3MDI4IjoiZCJ9; _y2=1%3AeyJjIjp7fX0%3D%3AMTc0OTg2MjMwNA%3D%3D%3A2; lastConversion={%22amount%22:1%2C%22fromCurrency%22:%22USD%22%2C%22toCurrency%22:%22EUR%22}; IR_12610=1691766576161%7C0%7C1691766576161%7C%7C; _uetsid=cc0f4540385811eeb5701959e71f953c; _uetvid=cc0f3f30385811ee8c5ca56a27d9fea7; _cc_id=558fed33cb6cbc8a6a2cb878f174ed0f; panoramaId_expiry=1691852982291; _au_1d=AU1D-0100-001691766583-NH1XV8R2-OE7S; _au_last_seen_pixels=eyJhcG4iOjE2OTE3NjY1ODMsInR0ZCI6MTY5MTc2NjU4MywicHViIjoxNjkxNzY2NTgzLCJydWIiOjE2OTE3NjY1ODMsInRhcGFkIjoxNjkxNzY2NTgzLCJhZHgiOjE2OTE3NjY1ODMsImdvbyI6MTY5MTc2NjU4MywiYWRvIjoxNjkxNzY2NTgzLCJ1bnJ1bHkiOjE2OTE3NjY1ODN9; _ga=GA1.2.832684383.1691766584; _gid=GA1.2.569857480.1691766584; cto_bundle=rSVw-F9nQkpEdk1WNGJmTGc4Y3pSOSUyQlBqUUZMU0hlWWk5RVZwZm0zRlA1OWpwTUxLSnV5JTJGWnpoJTJCWnZhSVNRd1pwbkJJU1NOSEdPdDRpTHNCSDh0cjlmVE1aamIwNmVDTW1OcjlpTkZrUkVZQWg3Q0x2R1BuUmdLckJuZXNMeGVEN1ZJNkZlc2dqd2ZKVDhJdXBZSVNWQ3J5bFElM0QlM0Q; amp_470887=oCITDcVIglVIYWLXberdvC...1h7ii6qut.1h7iibb3o.a.2.c; _yi=1%3AeyJsaSI6bnVsbCwic2UiOnsiYyI6MSwiZWMiOjQ5LCJsYSI6MTY5MTc2NjY0NDQyMiwicCI6Nywic2MiOjE5MH0sInUiOnsiaWQiOiI1MmI5MmRlYy0xNGRmLTQ5MmQtYTViMi03YmFkZmZkY2NhM2IiLCJmbCI6IjAifX0%3D%3ALTE4MDY5MDc0ODg%3D%3A2',  # แทนด้วยค่า cookie จริง
        'host': 'www.xe.com',
        'if-none-match': '"10f0-KLdVWcmg5WqNRjLbW1rA0j4Be+Y"',
        'referer': 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=EUR',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    access_key ='2ddcf98879872141c9cc2b4a2aec87b9'
    froms = ''
    to = ''
    amount = ''
    #response = session.get(f'https://api.currencylayer.com/live?access_key={access_key}&currencies')
    response = requests.get('https://www.xe.com/api/protected/midmarket-converter/', headers=headers)
    data = response.json()['rates']

    json_data = json.loads(json.dumps(data))
    
    for curenciesrates in json_data:
        
        print(json_data)
    



def currenciesselect():
    
    access_key ='2ddcf98879872141c9cc2b4a2aec87b9'
    response = session.get(f'https://api.currencylayer.com/list?access_key={access_key}convert?from={froms}&to={to}&amount={amount}')

    data = response.json()
    json_data = json.loads(json.dumps(data))
    get_datainputs = json_data.get(inputs)
    
    inputs = input("Enter Currencies: ").upper()
    if get_datainputs:
        
        print(f"Currencies:{inputs} Country List:{get_datainputs}",)
    
    else:
        
        print("Please enter Currencies!")

    return get_datainputs

