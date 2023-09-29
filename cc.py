import customtkinter
from tkinter import *
from forex_python.converter import CurrencyRates

app=customtkinter.CTk()
app.config(bg="#202630")
app.geometry ("400x450")
app.title("Currency Converter")
img=PhotoImage(file="")
photo_label=customtkinter.CTkLabel(app,fg="#202630",image=img)
photo_label.place(x=0,y=0)
app.iconphoto(False, img)




from_label=customtkinter.CTkLabel (app,text="From", text_font=('Arial',15, 'bold'), fg_color="#202630",text_color="#FFFFFF",width=1)
from_label.place(x=10,y=150)

to_label=customtkinter.CTkLabel (app,text="To", text_font=('Arial',15, 'bold'), fg_color="#202630",text_color="#FFFFFF",width=1)
to_label.place(x=248,y=150)


currency_list=["IND","USD","CNY","DKK","EUR","GBP"]

variable1=StringVar()
variable2=StringVar()


from_menu=customtkinter.CTkComboBox(app,variable=variable1,values=currency_list,text_font=('Arial',12,'bold'),dropdown_text_font=('Arial',12,'bold'),fg_color="#FFFFFF",text_color="#000000",button_color="#710193",button_hover_color="#710193",border_color="#FFFFFF",dropdown_color="#FFFFFF",dropdown_hover_color="#00FF00",dropdown_text_color="#000000")
from_menu.place(x=10,y=180)

to_menu=customtkinter.CTkComboBox(app,variable=variable2,values=currency_list,text_font=('Arial',12,'bold'),dropdown_text_font=('Arial',12,'bold'),fg_color="#FFFFFF",text_color="#000000",button_color="#710193",button_hover_color="#710193",border_color="#FFFFFF",dropdown_color="#FFFFFF",dropdown_hover_color="#00FF00",dropdown_text_color="#000000")
to_menu.place(x=250,y=180)


amount_entry=customtkinter.CTkEntry(app,text_font=('Arial',20,'bold'),text_color="#000000",justify=CENTER,width=370,fg_color="#FFFFFF",border_color="#FFFFFF")
amount_entry.place(x=18,y=240)


convert_button=customtkinter.CTkButton(app,text="Convert",text_font=('Arial',20,'bold'),texxt_color="#FFFFFF",fg_color="#710193",hover_color"#710193")
convert_button.place(x=50,y=300)

reset_button=customtkinter.CTkButton(app,text="Reset",text_font=('Arial',20,'bold'),texxt_color="#FFFFFF",fg_color="#bdSb15",hover_color"#bdSb15")
reset_button.place(x=200,y=300)





app.mainloop()