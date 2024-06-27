from tkinter import *
import pyshorteners

#function to copy the URL to clpiboard
def copy(link):
    window.clipboard_clear()
    window.clipboard_append(link)

#function to shorten the URL
def shorten_url():
    long_url = url_entry.get()          #takes the input and functions on it
    if long_url:
        try:
            object = pyshorteners.Shortener()
            short_url = object.tinyurl.short(long_url)
            result_label.config(text=f"Shortened URL: {short_url}")  #shortening of the URL and displaying it by overwriting result_label
            output = Button(window, text="Copy URL", command=lambda: copy(short_url))  #button to run execute copy function
            output.pack()
            
        except Exception as e:
            result_label.config(text=f"Error! An error occurred: {e}",font=("arial black", 12), foreground='red')  #handling the error
    else:
        result_label.config(text="Input Error! Please enter an URL",font=("arial black", 12), foreground='red')   # msg to display for blank input
            
#configuring/creating the main window
window = Tk(screenName= "Shortify",className="Shortify",)
window.geometry("800x400")
window.resizable(False, False)
window.configure(background='aqua')

#displaying message 
text = Label(window, text="Shortify", font=('cooper black',30,'bold italic'), background='aqua', )
text.pack(pady = 20)
text = Label(window, text = " Welcome to the fast and less complicated url shortner where you can shorten your link in few seconds ! ",font=("times new roman",14), background='aqua')
text.pack()
text = Label(window, text="It's easy, fast and Ad free ",font=("times new roman",14), background='aqua')
text.pack()

#displaying input message and box to take input
url_label = Label(window, text="Enter the URL to shorten:",font=('arial black', 12, 'bold'), background='aqua')
url_label.pack(pady=10)
url_entry = Entry(window, width=50)
url_entry.pack(pady=5)

#button to execute shorten_url function and define a place to display output
shorten_button = Button(window, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=10)
result_label = Label(window, text="", font=("Helvetica", 12), background='aqua')
result_label.pack(pady=10)

#Run the application
window.mainloop() 