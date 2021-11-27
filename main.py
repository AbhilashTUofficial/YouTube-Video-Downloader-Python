import tkinter
from PIL import ImageTk,Image

window=tkinter.Tk();
window.title("YouTube Video Downloader");
window.geometry("600x800")

pyimage1=ImageTk.PhotoImage(Image.open('Img/thumb.png').resize((512,288)));
pyimage2=ImageTk.PhotoImage(Image.open('Img/raspberry.jpg').resize((512,288)));

imagesList=[pyimage1,pyimage2];
label=tkinter.Label(image=imagesList[1]);
label.grid(row=1,column=1,columnspan=3,padx=40,pady=40);

    

def onClick(n):
    global label;
    global fetchBtn;
    try:
        label.grid_forget();
        label=tkinter.Label(image=imagesList[n+1]);
        label.grid(row=1,column=1,columnspan=3,padx=40,pady=40);
        fetchBtn=tkinter.Button(window,text="Fetch",height=2,width=8,command=lambda : onClick(n+1));
        fetchBtn.grid(row=2,column=2,sticky='w');
    except:
        label.grid_forget();
        label=tkinter.Label(image=imagesList[0]);
        label.grid(row=1,column=1,columnspan=3,padx=40,pady=40);
        fetchBtn=tkinter.Button(window,text="Fetch",height=2,width=8,command=lambda : onClick(0));

        fetchBtn.grid(row=2,column=2,sticky='w');


urlField=tkinter.Entry(window,width=30,);
urlField.grid(row=2,column=1,sticky='e',ipady=10)


fetchBtn=tkinter.Button(window,text="Fetch",height=2,width=8,command=lambda : onClick(1));
fetchBtn.grid(row=2,column=2,sticky='w');

window.mainloop();