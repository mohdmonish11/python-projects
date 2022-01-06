from tkinter import*
from pymysql import*
con=connect(host="localhost",user="root",password="",db="grocery_management")
cur=con.cursor()
def search_grocery():
    pass
def order_place_details():
    pass
def password_check():
    if uusername.get().lower()=="admin" and upassword.get().lower()=="admin":
        window=Tk()
        window.title("Home")
        window.minsize(650,650)
        window.config(bg="#CCFF66")
        mainMenu=Menu(window)
        grocery_mngmt=Menu(mainMenu,tearoff=0)
        grocery_mngmt.add_command(label="Insert",command=grocery_insert)
        grocery_mngmt.add_command(label="update",command=grocery_update)
        grocery_mngmt.add_command(label="delete",command=grocery_delete)
        supplier_mngmt=Menu(mainMenu,tearoff=0)
        supplier_mngmt.add_command(label="Insert",command=supplier_insert)
        supplier_mngmt.add_command(label="update",command=supplier_update)
        supplier_mngmt.add_command(label="delete",command=supplier_delete)
        mainMenu.add_cascade(label="Grocery Management",menu=grocery_mngmt)
        mainMenu.add_cascade(label="Supplier Management",menu=supplier_mngmt)
        window.config(menu=mainMenu)
    else:
        load_database_query="select username,password from user_login_id"
        result=cur.execute(load_database_query)
        for i in range(result):
            g=cur.fetchone()
            c=[]
            for j in g:
                c.append(j)
            if (uusername.get() in c) and (upassword.get() in c):
                window=Tk()
                window.title("DB login")
                window.minsize(650,650)
                window.config(bg="#CCFF66")
                mainMenu=Menu(window)
                search=Menu(mainMenu,tearoff=0)
                mainMenu.add_cascade(label="Search",menu=search)
                search.add_command(label="Search",command=search_grocery)
                order_place=Menu(mainMenu,tearoff=0)
                mainMenu.add_cascade(label="Order Place",menu=order_place)
                order_place.add_command(label="Order Place",command=order_place_details)
                window.config(menu=mainMenu)
def login_wd():
    global uusername,upassword
    window=Tk()
    window.title("Login Page")
    window.minsize(650,650)
    window.config(bg="#CCFF66")
    username=Label(window,text="Username: ",font=("Times New Roman",15),fg="#CC00FF",bg="#CCFF66")
    uusername=Entry(window,font=("Times New Roman",15),fg="#CC00FF",bg="#CCFF66")
    password=Label(window,text="Password: ",font=("Times New Roman",15),fg="#CC00FF",bg="#CCFF66")
    upassword=Entry(window,show="*",font=("Times New Roman",15),fg="#CC00FF",bg="#CCFF66")
    submit=Button(window,text="Submit",font=("Times New Roman",15),fg="#CC00FF",bg="#CCFF66",command=password_check)
    username.place(x=20,y=30)
    uusername.place(x=140,y=30)
    password.place(x=20,y=90)
    upassword.place(x=140,y=90)
    submit.place(x=250,y=240)
def get_rgstry_data():
    insert_query="insert into user_login_id(name,username,password)values('%s','%s','%s')"%(uname.get(),uusername.get(),upassword.get())
    cur.execute(insert_query)
    con.commit()
    uname.delete(0,END)
    uusername.delete(0,END)
    upassword.delete(0,END)
def get_regstr_bt():
    global uname,uusername,upassword
    window=Tk()
    window.title("Registration")
    window.minsize(650,650)
    window.config(bg="#CCFF66")
    name=Label(window,text="Name: ",font=("Times New Roman",15),fg="#CC00FF",bg="#CCFF66")
    uname=Entry(window,font=("Times New Roman",15),fg="#CC00FF",bg="#CCFF66")
    username=Label(window,text="Username: ",font=("Times New Roman",15),fg="#CC00FF",bg="#CCFF66")
    uusername=Entry(window,font=("Times New Roman",15),fg="#CC00FF",bg="#CCFF66")
    password=Label(window,text="Password: ",font=("Times New Roman",15),fg="#CC00FF",bg="#CCFF66")
    upassword=Entry(window,show="*",font=("Times New Roman",15),fg="#CC00FF",bg="#CCFF66")
    submit=Button(window,text="Submit",font=("Times New Roman",15),fg="#CC00FF",bg="#CCFF66",command=get_rgstry_data)
    name.place(x=20,y=30)
    uname.place(x=140,y=30)
    username.place(x=20,y=90)
    uusername.place(x=140,y=90)
    password.place(x=20,y=150)
    upassword.place(x=140,y=150)
    submit.place(x=250,y=240)
window=Tk()
window.title("Login")
window.minsize(650,650)
window.config(bg="#CCFF66")
#how to insert image
#how to autoadjust the text on maximizing the screen
grcy_mngmt=Label(window,text="WELCOM TO GROCERY MANAGEMENT\n SYSTEM",font=("Berlin Sans FB Demi",20),fg="#CC00FF",bg="#CCFF66")
login_bt=Button(window,text="Login",font=("Colonna MT",40),fg="#CC00FF",bg="#CCFF66",command=login_wd)
regstr_bt=Button(window,text="Register",font=("Colonna MT",40),fg="#CC00FF",bg="#CCFF66",command=get_regstr_bt)
grcy_mngmt.place(x=100,y=100)
login_bt.place(x=20,y=300)
regstr_bt.place(x=350,y=300)
