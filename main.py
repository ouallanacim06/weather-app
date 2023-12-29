import requests
from tkinter import *
root = Tk()
url = "http://api.weatherapi.com/v1/current.json"
param = {
    "key" : "f51883ed597245b1b2f55255232912",
    "q" : "Paris",
    "hour" : "12",
    "aqi" : "no",
    "tides" : "no",
    "lang" : "fr"
}
Data = {}
def call():
    global Data
    respose = requests.get(url,params=param)
    Data = respose.json()
    print('Data: ',Data)

def tempLabel():
    global Data
    call()
    location = location_Entery.get()
    try:
        tempe = Data["current"]["temp_c"]
        loc = Data["location"]["country"]
        temp.config(text=tempe)
        countory.config(text=loc)
        param["q"] = [location]
    except KeyError as e:
        print("error: ",e)

getTemp = Button(root,text="get temp",command=tempLabel)
countory = Label(root)
temp = Label(root)
location_Entery = Entry(root)
temp.pack()
countory.pack()
location_Entery.pack()
getTemp.pack()
root.mainloop()