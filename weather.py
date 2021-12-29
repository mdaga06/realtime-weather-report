import tkinter as tk
import requests
from PIL import Image, ImageTk
def format_response(weather):
    try:
        name=weather['name']
        desc=weather['weather'][0]['description']
        temp=weather['main']['temp']
        wind=weather['wind']['speed']
       
        final_str='City: %s \n Conditions: %s \n Temperature(°F): %s \n Wind-speed: %s' %(name,desc,temp,wind)
    except:
        final_str="No record Found"
    return final_str 
def weather(city):
    wkey='d1cb0a5e5b419f426726fb4b82ad9a8f'
    link='http://api.openweathermap.org/data/2.5/weather'
    parameters={'APPID': wkey, 'q': city, 'units': 'Imperial'}
    response=requests.get(link,params=parameters)
    weather=response.json()
    
    label['text']=format_response(weather)
    
    
root= tk.Tk()
root.geometry("600x600")
root.title("Mridula's weather forcasting App")

img='r.png'
bgs=ImageTk.PhotoImage(file=img,master=root)
bgs_label=tk.Label(root,image=bgs)
bgs_label.place(width=600,height=800)
frame=tk.Frame(root, bg='powder blue',bd=5,relief='ridge')
frame.place(relx=0.70,rely=0.15,relwidth=0.40,relheight=0.1,anchor='center')

frame1=tk.Frame(root, bg='powder blue',bd=5,relief='ridge')
frame1.place(relx=0.30,rely=0.1,relwidth=0.40,relheight=0.1,anchor='n')

entry=tk.Entry(frame1, font=('times new roman',20))
entry.place(relheight=1,relwidth=1)

lf=tk.Frame(root, bg='powder blue',bd=5,relief='ridge')
lf.place(relx=0.5,rely=0.20,relwidth=0.80,relheight=0.55,anchor='n')

button=tk.Button(frame, text="search weather report",font=20,bg='powder blue', command=lambda: weather(entry.get()))
button.place(relx=0.06,relheight=1,relwidth=0.90)

frame2=tk.Frame(root,bg='powder blue',bd=5,relief='ridge')
frame2.place(relx=0.5,rely=0.20,relwidth=0.75,relheight=0.55,anchor='n')

label=tk.Label(frame2,font=('arial',20))
label.place(relwidth=1,relheight=1)

root.mainloop()
    
        
