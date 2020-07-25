import tkinter as tk
import requests
from tkinter import font



#variables for screen
Height = 600
Width = 800


#Communicating with the NASA API
def comm_APOD(date):
	APOD_key = 'HfqfZabWQhGl6HQ2BctJdiOy10AtT5opHwZTDVsx'
	url = 'https://api.nasa.gov/planetary/apod?api_key=HfqfZabWQhGl6HQ2BctJdiOy10AtT5opHwZTDVsx'
	params = {'date': date}
	response = requests.get(url, params=params)
	APOD = response.json()
	textbox.delete(1.0, tk.END)
	textbox.insert(tk.INSERT, get_APOD(APOD))
	


def get_APOD(APOD):
	try:
		date = APOD['date']
		exp = APOD['explanation']
		url = APOD['url']

		string = 'The Date: %s \nExplanation of Picture: %s \nUrl of the photo/video: \n%s' % (date, exp, url)
	except:
		string = 'was not a valid date'
	return str(string)



	


#Whats on the screen
root = tk.Tk()

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

frame = tk.Frame(root, bg='#E0EEEE')
frame.place(relwidth=1, relheight=1)

frame2 = tk.Frame(root, bd=5, bg='#5F9F9F')
frame2.place(relx=.1, rely=.1, relheight=0.65, relwidth=.8)

textbox = tk.Text(frame2, font=('Arial', 12), text=None)
textbox.place(relx=0, rely=0, relheight=1, relwidth=1)

title = tk.Label(frame, bd=10, text="Astronomy Picture Of the Day",font=('Arial', 15), bg='#E0EEEE')
title.pack(side="top")

frame3 = tk.Frame(root, bg='#5F9F9F')
frame3.place(relx=.1, rely=.8, relheight=0.1, relwidth=.8)

tip = tk.Label(frame, text="*Type a Date.(YYYY-MM-DD)",font=('Arial', 9), bg='#E0EEEE')
tip.place(relx=.1, rely=.9, relheight=0.1, relwidth=.8)

entry = tk.Entry(frame3, font=("Arial", 14))
entry.place(relx=0.01, rely=.1, relheight=0.8, relwidth=0.8)

button = tk.Button(frame3, text='Get APOD', font=("Arial", 14), command=lambda: comm_APOD(entry.get()))
button.place(relx=0.82, rely=.1, relheight=0.8, relwidth=0.17)

root.mainloop()

