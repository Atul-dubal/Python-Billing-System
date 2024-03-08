import customtkinter as ctk
import sqlite3
import threading
import tkinter as tk
from tkinter import ttk,messagebox
import cv2
from time import sleep
from playsound import playsound
from PIL import ImageTk,Image
import os
import pyqrcode 
window = ctk.CTk()

SHOP_NAME = "SMART SHOP BILLING SYSTEM"
window.title(SHOP_NAME)
window_width = window.winfo_screenwidth()
half_width = window_width//2
window_height = window.winfo_screenheight()
half_height = window_height//2 
#window.geometry("1280x720")
#window.attributes("-fullscreen",True)
window.geometry(f"{window_width}x{window_height}")
ctk.set_appearance_mode("light") 
window.maxsize(window_width,window_height)


# ALL VARIABLES
isAddProductView = False
isScannerOn = False
product_name = ctk.StringVar()
product_qantity = ctk.StringVar()
product_price = ctk.StringVar()
billing_data = ctk.StringVar()
total_price = tk.StringVar()
font = ('Franklin Gothic Medium', 30)
camera_id = 0
delay = 1
window_name = 'Scan The Product'
cart = {}
i = 1

def introduction():
    window.geometry("800x700")
    global usernameEntry,passwordEntry,common_frame
    common_frame = ctk.CTkFrame(window,fg_color="transparent")
    common_frame.pack(side=tk.TOP,pady=60)
    
    img = ImageTk.PhotoImage(Image.open("login1.png"))

    label = ctk.CTkLabel(common_frame,image=img,text="",width=100,height=100)
    label.photo=img
    label.pack(side=ctk.TOP,pady=20)

    
    # Convert the first frame to Tkinter-compatible format
    login_frame = ctk.CTkFrame(common_frame,fg_color="transparent")
    login_frame.pack(side=tk.LEFT,padx=100)
    
    # Login Form 
    login_title = ctk.CTkLabel(login_frame,text="Login",font=font)
    login_title.pack(side=tk.TOP)
    
    usernameEntry = ctk.CTkEntry(login_frame,placeholder_text="Username",width=200,height=30)
    usernameEntry.pack(side=tk.TOP,pady=5)
    passwordEntry = ctk.CTkEntry(login_frame,placeholder_text="Password",width=200,height=30)
    passwordEntry.pack(side=tk.TOP,pady=5)
    login_btn = ctk.CTkButton(login_frame,text="Login",command=login_function)
    login_btn.pack(side=tk.TOP,pady=5)
    
    # register_frame = ctk.CTkFrame(common_frame,fg_color="transparent")
    # register_frame.pack(side=tk.RIGHT,padx=100)
    
    # register_title = ctk.CTkLabel(register_frame,text="Register",font=font)
    # register_title.pack(side=tk.TOP)
    # # Registration Form 
    
    # nameEntry = ctk.CTkEntry(register_frame,placeholder_text="Name",width=200,height=20)
    # nameEntry.pack(side=tk.TOP,pady=5)
    
    # usernameEntry = ctk.CTkEntry(register_frame,placeholder_text="Username",width=200,height=20)
    # usernameEntry.pack(side=tk.TOP,pady=5)
    
    # phoneEntry = ctk.CTkEntry(register_frame,placeholder_text="Phone",width=200,height=20)
    # phoneEntry.pack(side=tk.TOP,pady=5)
    
    # passwordEntry = ctk.CTkEntry(register_frame,placeholder_text="Password",width=200,height=20)
    # passwordEntry.pack(side=tk.TOP,pady=5)
    
    # login_btn = ctk.CTkButton(register_frame,text="Login")
    # login_btn.pack(side=tk.TOP,pady=5)
    #islogin = login_check()
    
def login_function():
    global usernameEntry,passwordEntry,common_frame
    print(usernameEntry.get(),passwordEntry.get())
    
    if(usernameEntry.get() == "admin" and passwordEntry.get() == "admin123"):
        common_frame.pack_forget()
        common_layout()
    else:
        msg = messagebox.showerror("Authentication Error","Invalid Information")
def login_check():
    db = sqlite3.connect("allproducts.db")
    cursor = db.cursor()
    try:
        query = '''select * from users'''
        all_data = cursor.execute(query)
        if len(all_data)> 0:
            pass
        for i in all_data:
            print(i)
    except:
        setup_database()

def common_layout():
    global home_btn,add_product_btn,invoice_btn,billing_frame
    # TITLE FRAME 
    title_frame = ctk.CTkFrame(master=window,fg_color="transparent")
    title_frame.pack(side=ctk.TOP)

    title = ctk.CTkLabel(master=title_frame,text=SHOP_NAME,font=('Franklin Gothic Medium', 30))
    title.pack()

    # BUTTON OPTIONS FRAME 
    btn_option_frame = ctk.CTkFrame(master=window,fg_color="transparent")
    btn_option_frame.pack(side=ctk.TOP,pady=30)

    home_btn = ctk.CTkButton(master=btn_option_frame,text="DASHBOARD",command=dashboard_layout, font=('Franklin Gothic Medium', 10))
    home_btn.pack(side=ctk.LEFT,padx=20)

    add_product_btn = ctk.CTkButton(master=btn_option_frame,text="ADD PRODUCTS",command=add_product_layout, font=('Franklin Gothic Medium', 10))
    add_product_btn.pack(side=ctk.LEFT,padx=20)

    invoice_btn = ctk.CTkButton(master=btn_option_frame,text="INVOICE/BILLING", command=billing_layout, font=('Franklin Gothic Medium', 10))
    invoice_btn.pack(side=ctk.RIGHT,padx=20)
    # LINE
    line = ctk.CTkFrame(master=window,fg_color="black",height=2)
    line.configure(width=window_width)
    line.pack(side=ctk.TOP)
    
    
   
def dashboard_layout():
    
    if not(isScannerOn):
        try :
            
            global isAddProductView
            global add_product_frame
            add_product_frame.pack_forget()
            global add_product_btn
            add_product_btn.pack(side=ctk.LEFT,padx=20)
            global billing_frame
            billing_frame.pack_forget()
        except:
             global isAddProductView
             
             
             
            
        isAddProductView = False
def add_product_layout():
    
    global isScannerOn
    print(isScannerOn)
    if not(isScannerOn):
        try:
            global billing_frame
            billing_frame.pack_forget()
            global isAddProductView
            global add_product_btn
            #add_product_btn.pack_forget()
            global add_product_frame
        except:
            pass
        if not(isAddProductView):
            isAddProductView= True
            global add_product_name_entry,add_product_qantity_entry,add_product_price_entry
            
            add_product_frame = ctk.CTkFrame(master=window,fg_color="transparent")
            add_product_frame.pack(side=ctk.TOP,pady=20)

            add_product_title = ctk.CTkLabel(master=add_product_frame,text="ADD PRODUCT", font=('Franklin Gothic Medium', 20))
            add_product_title.pack(side=ctk.TOP,pady=20)

            add_product_name = ctk.CTkLabel(master=add_product_frame,text="PRODUCT NAME", font=('Franklin Gothic Medium', 15))
            add_product_name.pack(side=ctk.TOP,anchor=ctk.W,padx=200,pady=10)

            add_product_name_entry = ctk.CTkEntry(master=add_product_frame,width=half_width,textvariable=product_name ,font=('Franklin Gothic Medium', 15))
            add_product_name_entry.pack(side=ctk.TOP,anchor=ctk.W,padx=200,pady=10)

            add_product_qantity = ctk.CTkLabel(master=add_product_frame,text="PRODUCT QANTITY", font=('Franklin Gothic Medium', 15))
            add_product_qantity.pack(side=ctk.TOP,anchor=ctk.W,padx=200,pady=10)

            add_product_qantity_entry = ctk.CTkEntry(master=add_product_frame,width=half_width, textvariable=product_qantity,font=('Franklin Gothic Medium', 15))
            add_product_qantity_entry.pack(side=ctk.TOP,anchor=ctk.W,padx=200,pady=10)

            add_product_price = ctk.CTkLabel(master=add_product_frame,text="PRODUCT PRICE", font=('Franklin Gothic Medium', 15))
            add_product_price.pack(side=ctk.TOP,anchor=ctk.W,padx=200,pady=10)

            add_product_price_entry = ctk.CTkEntry(master=add_product_frame,width=half_width,textvariable=product_price, font=('Franklin Gothic Medium', 15))
            add_product_price_entry.pack(side=ctk.TOP,anchor=ctk.W,padx=200,pady=10)

            make_qr_btn = ctk.CTkButton(add_product_frame,text="MAKE BARCODE",command=make_barcode)
            make_qr_btn.pack(side=ctk.TOP,pady=20)


def billing_layout():
    
    
    global billing_frame, invoice_frame, billing_title, total_price_label, total_price
    
    total_price.set("Total : 0")
    
    if not(isScannerOn):
        global set
        try:
            global isAddProductView
            global add_product_btn
            add_product_btn.pack(side=ctk.LEFT,padx=20)
            global add_product_frame
            add_product_frame.pack_forget()
            isAddProductView = False
            
        except:
            pass
        
        billing_frame = tk.Frame(master=window,pady=30,padx=30)
        billing_frame.pack(side=tk.TOP)
        
        invoice_frame = tk.Frame(billing_frame)
        invoice_frame.pack(side=tk.TOP)
        
        billing_title = tk.Label(invoice_frame,text=SHOP_NAME+"\nInvoice",pady=5,font=('Arial',10))
        billing_title.pack(side=tk.TOP)
        style = ttk.Style(window)

        # Configure the style for the Treeview
        style.configure("Treeview",
                        background="#ffffff",
                        foreground="black",
                        rowheight=20,
                        font=("Arial",10),
                        fieldbackground="#ffffff")

        style.map("Treeview",
          background=[('selected', '#007ACC')])
        set = ttk.Treeview(invoice_frame,show="headings", style="Treeview",padding=20)
        set.pack(expand=True)

        set['columns']= ('Name', 'Qantity','Price')
        set.column("#0", width=0,anchor="center",  stretch=tk.NO)
        set.column("Name",anchor="center", width=150,stretch=tk.YES)
        set.column("Qantity",anchor="center", width=150)
        set.column("Price",anchor="center", width=150)

        set.heading("#0",text="")
        set.heading("Name",text="NAME",anchor=tk.CENTER)
        set.heading("Qantity",text="QANTITY")
        set.heading("Price",text="PRICE")
        window.columnconfigure(0, weight=1)
        
        total_price_label = tk.Label(invoice_frame,textvariable=total_price)
        total_price_label.pack(side=tk.TOP)
        
        print_btn = ctk.CTkButton(billing_frame,text="Print",command=print_invoice)
        print_btn.pack(side=tk.TOP,pady=20)
        # print_btn.pack(side=tk.TOP,pady=20)
        threading.Thread(target=start_scanner, daemon=True).start()
        

def update_total_price_label():
    global total_price_label, cart, total_price
    total_price_value = sum(int(item[2]) for item in cart.values())
    total_price.set("Total : "+str(total_price_value))
    total_price_label.config(textvariable=total_price)

def take_screenshot(widget):
    from PIL import ImageGrab
    
    # Hide the widget temporarily for screenshot
    widget.winfo_toplevel().withdraw()
    
    # Capture the content of the widget
    x, y, width, height = widget.winfo_rootx(), widget.winfo_rooty(), widget.winfo_width(), widget.winfo_height()
    img = ImageGrab.grab(bbox=(x, y, x+width, y+height))
    
    # Show the widget again
    widget.winfo_toplevel().deiconify()
    
    return img

def create_pdf(img):
    import tempfile
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    # Save the image to a temporary file
    temp_file = tempfile.mktemp(suffix=".png")
    img.save(temp_file)
    
    # Create a PDF file
    pdf_file = tempfile.mktemp(suffix=".pdf")
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.drawImage(temp_file, 0, 0, letter[0], letter[1])
    c.save()
    
    return pdf_file

def print_pdf(pdf_file):
    import subprocess
    # Open the PDF file with the default associated program
    subprocess.Popen(["start", "", pdf_file], shell=True)

def print_invoice():
    print_pdf(create_pdf(take_screenshot(billing_frame)))

    

def add_product_db(data):
        qrcode = pyqrcode.create(str(data))
        qrcode.png("PRODUCT_QR_CODES/"+str(data[0])+"Q"+str(data[1])+".png",scale=6)
        try:
            # Connect to DB and create a cursor
            db = sqlite3.connect('allproducts.db')
            cursor = db.cursor()
            print('DB Init')

            query = '''insert into ALLPRODUCTS  (NAME, QANTITY, PRICE) values (?,?,?)'''
            cursor.execute(query,(data[0],data[1],data[2]))
            
            db.commit()
            read_database()
            cursor.close()

        # Handle errors
        except sqlite3.Error as error:
            print('Error occurred - ', error)

        finally:
            if db:
                db.close()
                print('SQLite Connection closed')


def product_check(s):
    
    global i
    total_price = 0
    global cart
    global set
    curr_data = []
    s = s[:-1][1:].replace("'","").split(",")
    print(s[0])
    all_products_name = read_database(True)
    if s[0] in all_products_name:
        cart_data = [i[0] for i in cart.values()]
        print(cart_data)
        if s[0] in cart_data:
            print("same")
            curr_data = [cart[s[0]][0],int(cart[s[0]][1])+int(s[1]),int(cart[s[0]][2])+int(s[2])]
            cart[s[0]] = curr_data
        else:
            print("different")
            curr_data = [s[0],s[1],s[2]]
            cart[s[0]]=curr_data
            i=i+1
        playsound(os.path.join(os.getcwd(),"check-in.mp3"))
        sleep(1)
        print("Name : ",s[0],"Qauntity : ",s[1],"Price : ",s[2])
        print("CART : ",cart)
        try:
            set.insert(parent='',index='end',iid=s[0],text='',values=curr_data)
            total_price = total_price +int(curr_data[2])
        except:
            set.item(s[0], values=curr_data)
            total_price = total_price +int(curr_data[2])
        update_total_price_label()
        

def start_scanner():
    global isScannerOn
    global cart
    cart.clear()
    i=1
    qcd = cv2.QRCodeDetector()
    cap = cv2.VideoCapture(camera_id)
    isScannerOn = True
    while True:
        ret, frame = cap.read()

        if ret:
            ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
            if ret_qr:
                for s, p in zip(decoded_info, points):
                    if s :
                         color = (0, 255, 0)
                    else:
                        color = (0, 255, 0)
                    frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
                    #product_check(s)
                    cv2.imshow(window_name, frame)
                    product_check(s)
        cv2.imshow(window_name, frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            isScannerOn = False
            break

    cv2.destroyWindow(window_name)
    
def setup_database():
    db = sqlite3.connect('allproducts.db')
    cursor = db.cursor()
    print('DB Init')

    # Write a query and execute it with cursor
    try:
        query = '''DROP TABLE ALLPRODUCTS'''
        cursor.execute(query)
    except:
        pass  
    try:
        query = '''DROP TABLE USERS'''
        cursor.execute(query)
    except:
        pass  
    query = '''CREATE TABLE ALLPRODUCTS (NAME TEXT, QANTITY INT,PRICE INT)'''
    cursor.execute(query)
    query1 = '''CREATE TABLE USERS (NAME TEXT,USERNAME TEXT PASSWORD INT,PHONE INT)'''
    cursor.execute(query1)
    print("TABLE CREATED")
    
def read_database(isNames = False):
    names = []
    all_products_data = []
    #print("DATABASE READ")
    db = sqlite3.connect("allproducts.db")
    cursor = db.cursor()
    
    query = '''select * from ALLPRODUCTS'''
    all_data = cursor.execute(query)
    for i in all_data:
        #print(i)
        names.append(i[0])
        all_products_data.append(i)
    if isNames==True :
        return names
    else:
        return all_products_data
    

read_database(True)
def make_barcode():
    name=product_name.get()
    qantity = product_qantity.get()
    price = product_price.get()
    if(len(name) <= 0 or len(qantity) <= 0 or qantity == "0" or len(price) <=0):
        print("Please Fill All The Fields")
    else:
        data = [name,qantity,price]
        add_product_db(data)
        add_product_name_entry.delete(0,ctk.END)
        add_product_price_entry.delete(0,ctk.END)
        add_product_qantity_entry.delete(0,ctk.END)

introduction()
# common_layout()
# dashboard_layout()
# add_product_layout()
# billing_layout()


window.mainloop()
