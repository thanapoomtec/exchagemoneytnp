import requests
import apiexchangemoney
import time

def exchange():
    
    listconuntry = apiexchangemoney.listcheckcountry()
        
    for country in listconuntry:
        print(country)
    print("Can You See List Conuntry currencies on top ^^^^^^^ .")
    print("|--------------------------|") 
    print("About Program Convert Currency Money :>)")
    print("Please click Q or q for exit program please read!!!!")
    time.sleep(2)
    while True:
        print("Please Select the currency to be converted:")
        currency1 = input("Please Enter Currency To Convert:").upper()
        if currency1 == "q" or currency1 == "Q":
            print("Exit program thanks for use.")
            break 
        currency2 = input("Please enter the currency to be converted:").upper()
        response = requests.get(f"https://wise.com/rates/live?source={currency1}&target={currency2}&length=30&resolution=hourly&unit=day")
    
        data1 = response.json().get('source')
        data2 = response.json().get('target')
        data3 = response.json().get('value')

        print(f"Convert {data1} To {data2}.")
        
        time.sleep(0.5)
        amount = float(input("Please Enter Amount Money:"))
        
        cal = amount * data3 
    
        print("Total Money to convert:"+"%.2f"%(cal))
        time.sleep(2)
        print('\n')
        
exchange()