from configparser import ConfigParser
from tkinter import *
from tkinter import messagebox
import requests
from PIL import ImageTk, Image



# here API value comes
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


def get_weather(city):
    r = requests.get(url.format(city, api_key))
    res = r.json()
    city_name = res['name']
    country = res['sys']['country']
    temp_kelvin = res['main']['temp']
    temp_celsius = int(temp_kelvin -273.15)
    temp_far = int(temp_kelvin -459.67)
    icon = res['weather'][0]['icon']
    min_temp = int(res['main']['temp_min']-273.15)
    max_temp =  int(res['main']['temp_max']-273.15)
    description = res['weather'][0]['main']
    final = (city_name, country, temp_celsius, temp_far, icon, description, min_temp, max_temp,)

    return final


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = f'{weather[0]}, {weather[1]}'
        displ_temp['text'] = f'{weather[2]}°C'
        temp_rate['text'] = f'Min temp: {weather[6]}°C / Max temp: {weather[7]}°C'
        weather_desc['text'] = f'{weather[5]}'

    else:
        messagebox.showerror('Error', f'Cannot find {city}', )


app = Tk()
app.title('Weather App')
app.geometry('700x350')
# app.iconphoto(False, PhotoImage(file='/weather_icons/10d.png'))

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text, width = 20)
city_entry.pack()
search_btn = Button(app, text = 'search', width=16, command = search, bg = '#48484A', fg = 'White')
search_btn.pack()

location_lbl= Label(app, text= '', font = ('bold', 15))
location_lbl.pack()

displ_temp = Label(app, text = '', font = ('bold', 15))
displ_temp.pack()

temp_rate = Label(app, text= '')
temp_rate.pack()

weather_img = Label(app, image = "")
weather_img.pack ()

weather_desc = Label(app, text ='', font = ('bold', 15))
weather_desc.pack()

app.mainloop()
