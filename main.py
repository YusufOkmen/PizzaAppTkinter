import tkinter as tk

form = tk.Tk()
form.title("Pizza Order App")
form.geometry("500x500+500+150")


# Functions

def siparisVer():
    siparisBilgi = tk.Label(form, text="Sipariş Bilgileri", fg="white", bg="Green", font="20").place(x=180, y=180)

    usernameLabel = tk.Label(form, text="Username", fg="White", bg="black").place(x=40, y=250)

    adressLabel = tk.Label(form, text="Adress", fg="White", bg="black").place(x=40, y=280)

    theSizeLabel = tk.Label(form, text="Pizza Size", fg="White", bg="black").place(x=40, y=310)

    IngredientsLabel = tk.Label(form, text="Ingredients", fg="White", bg="black").place(x=40, y=340)

    detailNameLabel = tk.Label(form, text=entry1.get())
    detailNameLabel.place(x=130, y=250)

    detailAdressLabel = tk.Label(form, text=entry2.get())
    detailAdressLabel.place(x=130, y=280)   

    detailSizeLabel = tk.Label(form, text=pizzaBoy.get())
    detailSizeLabel.place(x=130, y=310)

    detailIngredientsLabel = tk.Label(form,
                                       text=variable1.get()+" "+variable2.get()+" "+variable3.get())
    detailIngredientsLabel.place(x=130, y=340)
            


    # detailNameLabel["text"] = usernameEntry.get()
    # detailAdressLabel["text"] = adressEntry.get()
    # if pizzaBoy == "Kucuk":
    #     detailSizeLabel["text"] = "Kucuk Boy"
    # if pizzaBoy == "Orta":
    #     detailSizeLabel["text"] = "Orta Boy"
    # if pizzaBoy == "Buyuk":
    #     detailSizeLabel["text"] = "Buyuk Boy"

def iptalEt():
    form.quit()

# User Information
usernameLabel = tk.Label(form, text="Username", fg="White", bg="black").place(x=10, y=30)

adressLabel = tk.Label(form, text="Adress", fg="White", bg="black").place(x=10, y=60)

entry1 = tk.StringVar()
entry2 = tk.StringVar()

usernameEntry = tk.Entry(textvariable=entry1)
usernameEntry.place(x=80, y=30)

adressEntry = tk.Entry(textvariable=entry2)
adressEntry.place(x=80, y=60)

# Pizza Size
variablex = tk.StringVar()
variabley = tk.StringVar()
variablez = tk.StringVar()

sizeLabel = tk.Label(form, text="Pizza Size", fg="white", bg="black").place(x=250, y=20)

pizzaBoy = tk.StringVar()

smallRadio = tk.Radiobutton(form, text="Small", fg="white", bg="gray", activebackground="white", value="Kucuk", variable=pizzaBoy)
smallRadio.place(x=250, y=60)

mediumRadio = tk.Radiobutton(form, text="Medium", fg="white", bg="gray", activebackground="white", value="Orta", variable=pizzaBoy)
mediumRadio.place(x=250, y=90)

largeRadio = tk.Radiobutton(form, text="Large", fg="white", bg="gray", activebackground="white", value="Buyuk", variable=pizzaBoy)
largeRadio.place(x=250, y=120)


# Pizza Includes
variable1 = tk.StringVar()
variable2 = tk.StringVar()
variable3 = tk.StringVar()

IcludesLabel = tk.Label(form, text="Pizza Includes", fg="white", bg="black").place(x=350, y=20)

cheeseButton = tk.Checkbutton(form, text="Cheese", fg="white", bg="gray", activebackground="white", variable=variable1, onvalue="Peynirli").place(x=350, y=60)

cornButton = tk.Checkbutton(form, text="Corn", fg="white", bg="gray", activebackground="white", variable=variable2, onvalue="Mısırlı").place(x=350, y=90)

sauceButton = tk.Checkbutton(form, text="Sauce", fg="white", bg="gray", activebackground="white", variable=variable3, onvalue="Soslu").place(x=350, y=120)


# Buttons

siparisiVer = tk.Button(form, text="Sipariş Ver", fg="white", bg="brown", activebackground="green", command=siparisVer).place(x=40, y=110)

iptal = tk.Button(form, text="Siparişi İptal Et", fg="white", bg="brown", activebackground="red", command=iptalEt).place(x=120, y=110)


# Order Details

form.mainloop()