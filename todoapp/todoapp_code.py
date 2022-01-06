#To do app
#Error in selecting multiple list box in window ony one of them will select
#how to make my code to install and run on any system or any OS
from tkinter import *
from pymysql import *
from tkinter import messagebox
con=connect(host="localhost",user="root",password="",db="todoapp")
cur=con.cursor()
def get_message_appr():
    global upasssword
    p=messagebox.askokcancel("Secure","Would you like to secure your file")
    if p==True:
        upassword.config(state=NORMAL)
def db_add_note():
    insert_qry="insert into add_note(title,description,color,password)values('%s','%s','%s','%s')"%(utitle.get(),udescription.get(),ucolor.get(ucolor.curselection()[0]),upassword.get())
    cur.execute(insert_qry)
    con.commit()
    utitle.delete(0,END)
    udescription.delete(0,END)
    upassword.delete(0,END)
def get_addnote_wd():
    global utitle,udescription,ucolor,upassword
    window=Tk()
    window.title("Add Note")
    window.minsize(650,650)
    window.config(bg="#99CC66")
    add_nt=Label(window,text="Add Notes",font=("Berlin Sans FB Demi",35),fg="#330000",bg="#99CC66")
    title=Label(window,text="Title: ",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    utitle=Entry(window,font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    description=Label(window,text="Description: ",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    udescription=Entry(window,font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    color=Label(window,text="color: ",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    ucolor=Listbox(window,height=2,selectmode="single",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    ucolor.insert(0,"WhiteSmoke")#F5F5F5
    ucolor.insert(1,"SaddleBrown")#8B4513
    ucolor.insert(2,"Salmon")#FA8072
    ucolor.insert(3,"MediumSeaGreen")#3CB371
    ucolor.insert(4,"MintCream")#F5FFFA
    ucolor.insert(5,"MediumPurple")#9370DB
    ucolor.insert(6,"LightCoral")#F08080
    secure=Label(window,text="Secure: ",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    secure_bt=Button(window,text="click to \n secure",font=("Colonna MT",13),fg="#330000",bg="#99CC66",command=get_message_appr)
    password=Label(window,text="Password:",font=("Times New Roman",15),fg="#330000",bg="#99CC66")
    upassword=Entry(window,show="*",state=DISABLED,font=("Times New Roman",15),fg="#330000",bg="#99CC66")
    fnl_add_nt_btn=Button(window,text="Submit",font=("Colonna MT",20),fg="#330000",bg="#99CC66",command=db_add_note)
    add_nt.place(x=220,y=20)
    title.place(x=20,y=90)
    utitle.place(x=250,y=90)
    description.place(x=20,y=160)
    udescription.place(x=250,y=160)
    color.place(x=20,y=230)
    ucolor.place(x=250,y=230)
    secure.place(x=20,y=330)
    secure_bt.place(x=250,y=330)
    password.place(x=20,y=380)
    upassword.place(x=250,y=380)
    fnl_add_nt_btn.place(x=200,y=420)
def db_update_note():
    insert_query="update add_note set description='%s',color='%s' where title='%s'"%(sel_title.get(sel_title.curselection()[0]),ucolor.get(ucolor.curselection()[0]),udescription.get())
    cur.execute(insert_query)
    con.commit()
def get_update_wd():
    global sel_title,udescription
    upload_query="select title from add_note"
    result=cur.execute(upload_query)
    window=Tk()
    window.title("Update")
    window.minsize(650,650)
    window.config(bg="#99CC66")
    sel_update_title=Label(window,text="Select title \nto update",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    sel_title=Listbox(window,height=2,selectmode="single",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    m=0
    for i in range(result):
        g=cur.fetchone()
        sel_title.insert(m,g[0])
        m+=1
    description=Label(window,text="Description: ",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    udescription=Entry(window,font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    color=Label(window,text="color: ",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    ucolor=Listbox(window,height=2,selectmode="single",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    ucolor.insert(0,"WhiteSmoke")#F5F5F5
    ucolor.insert(1,"SaddleBrown")#8B4513
    ucolor.insert(2,"Salmon")#FA8072
    ucolor.insert(3,"MediumSeaGreen")#3CB371
    ucolor.insert(4,"MintCream")#F5FFFA
    ucolor.insert(5,"MediumPurple")#9370DB
    ucolor.insert(6,"LightCoral")#F08080
    update_btn=Button(window,text="Submit",font=("Colonna MT",20),fg="#330000",bg="#99CC66",command=db_update_note)
    sel_update_title.place(x=10,y=10)
    sel_title.place(x=200,y=10)
    description.place(x=10,y=100)
    udescription.place(x=200,y=100)
    color.place(x=10,y=150)
    ucolor.place(x=200,y=150)
    update_btn.place(x=250,y=300)
def db_delete_note():
    delete_query="delete from add_note where title='%s'"%(sel_title.get(sel_title.curselection()[0]))
    cur.execute(delete_query)
    con.commit()
def get_delete_wd():
    global sel_title
    upload_query="select title from add_note"
    result=cur.execute(upload_query)
    window=Tk()
    window.title("Delete")
    window.minsize(650,650)
    window.config(bg="#99CC66")
    sel_update_title=Label(window,text="Select title to delete",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    sel_title=Listbox(window,height=2,selectmode="single",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    m=0
    for i in range(result):
        g=cur.fetchone()
        sel_title.insert(m,g[0])
        m+=1
    update_btn=Button(window,text="Submit",font=("Colonna MT",20),fg="#330000",bg="#99CC66",command=db_delete_note)
    sel_update_title.place(x=10,y=10)
    sel_title.place(x=180,y=10)
    update_btn.place(x=200,y=200)
def get_search_wd():
    window=Tk()
    window.title("Search")
    window.minsize(650,650)
    window.config(bg="#99CC66")
def printSelectedTitleData():
    window=Tk()
    window.title(" View DATA")
    window.minsize(650,650)
    window.config(bg="#99CC66")
    s=""
    for i in selTitleData:
        s=s+str(i)+"\t"
    s=s+"\n"
    lbl=Label(window,text=s,font=("Times New Roman",15),fg="#CC9900",bg="#FFFFCC")
    lbl.place(x=20,y=20) 
    #print(selTitleData)
def view_display_data():
    if upassword.get()==selTitleData[3]:
        printSelectedTitleData()
    else:
        print("password not matched")
def db_view_note():
    global selTitleData,upassword
    m=sel_title.get(sel_title.curselection()[0])
    """
    print(m)
    for i in range(result):
        g=cur.fetchone()
        if len(g)>=4 and (m==g[0]):
            window=Tk()
            window.title("Search")
            window.minsize(650,650)
            window.config(bg="#99CC66")
            password=Label(window,text="Password:",font=("Times New Roman",15),fg="#330000",bg="#99CC66")
            upassword=Entry(window,show="*",state=NORMAL,font=("Times New Roman",15),fg="#330000",bg="#99CC66")
            if upassword.get()==g[3]:
                window.config(bg=g[1])
                sel_update_title=Label(window,text="TITLE:",font=("Times New Roman",20),fg="#330000",bg=g[1])
                sel_title=Label(window,text=g[0],font=("Times New Roman",20),fg="#330000",bg=g[1])
                description=Label(window,text="Description: ",font=("Times New Roman",20),fg="#330000",bg=g[1])
                udescription=Label(window,text=g[2],font=("Times New Roman",20),fg="#330000",bg=g[1])
    """
    for i in notedata:
        if m==i[0]:
            selTitleData=i
            if i[3]=='':
                printSelectedTitleData()
            else:
                window=Tk()
                window.title("Encrypt View")
                window.minsize(650,650)
                window.config(bg="#99CC66")
                password=Label(window,text="Password:",font=("Times New Roman",15),fg="#330000",bg="#99CC66")
                upassword=Entry(window,show="*",state=NORMAL,font=("Times New Roman",15),fg="#330000",bg="#99CC66")
                btn=Button(window,text="Submit",font=("Colonna MT",20),fg="#330000",bg="#99CC66",command=view_display_data)
                password.place(x=10,y=10)
                upassword.place(x=200,y=10)
                btn.place(x=250,y=50)
            
def get_view_wd():
    global sel_title,notedata
    notedata=[]
    upload_db_query="select title,color,description,password from add_note"
    result=cur.execute(upload_db_query)
    window=Tk()
    window.title("View")
    window.minsize(650,650)
    window.config(bg="#99CC66")
    sel_update_title=Label(window,text="Select title \nto view",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    sel_title=Listbox(window,height=2,selectmode="single",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    m=0
    for i in range(result):
        g=cur.fetchone()
        notedata.append(g)
        sel_title.insert(m,g[0])
        m+=1
    update_btn=Button(window,text="Submit",font=("Colonna MT",20),fg="#330000",bg="#99CC66",command=db_view_note)
    sel_update_title.place(x=10,y=10)
    sel_title.place(x=200,y=10)
    update_btn.place(x=250,y=300)
def password_check():
    upload_db_query="select user,password from usertable"
    result=cur.execute(upload_db_query)
    for i in range(result):
        g=cur.fetchone()
        c=[]
        for j in g:
            c.append(j)
        if (uuser_name.get() in c)and (upassword.get() in c):
            window=Tk()
            window.title("Home")
            window.minsize(650,650)
            window.config(bg="#99CC66")
            mainMenu=Menu(window)
            add_note=Menu(window,tearoff=0)
            add_note.add_command(label="Addnote",command=get_addnote_wd)
            update=Menu(window,tearoff=0)
            update.add_command(label="Update",command=get_update_wd)
            delete=Menu(window,tearoff=0)
            delete.add_command(label="Delete",command=get_delete_wd)
            search=Menu(window,tearoff=0)
            search.add_command(label="Search",command=get_search_wd)
            view=Menu(window,tearoff=0)
            view.add_command(label="View",command=get_view_wd)
            mainMenu.add_cascade(label="Add note",menu=add_note)
            mainMenu.add_cascade(label="Update",menu=update)
            mainMenu.add_cascade(label="Delete",menu=delete)
            mainMenu.add_cascade(label="Search",menu=search)
            mainMenu.add_cascade(label="View",menu=view)
            window.config(menu=mainMenu)               
def db_datas_saved():
    insert_query="insert into usertable(name,user,password)values('%s','%s','%s')"%(uname.get(),uuser_name.get(),upassword.get())
    cur.execute(insert_query)
    con.commit()
def register_entry():
    global uname,uuser_name,upassword
    window=Tk()
    window.title("User Registration")
    window.minsize(650,650)
    window.config(bg="#99CC66")
    user_registration=Label(window,text="User Registration",font=("Berlin Sans FB Demi",35),fg="#330000",bg="#99CC66")
    name=Label(window,text="Name: ",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    uname=Entry(window,font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    user_name=Label(window,text="Username: ",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    uuser_name=Entry(window,font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    password=Label(window,text="Password: ",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    upassword=Entry(window,show="*",font=("Times New Roman",20),fg="#330000",bg="#99CC66")
    regst_bt=Button(window,text="Register",font=("Colonna MT",25),fg="#330000",bg="#99CC66",command=db_datas_saved)
    user_registration.place(x=220,y=20)
    name.place(x=20,y=90)
    uname.place(x=250,y=90)
    user_name.place(x=20,y=160)
    uuser_name.place(x=250,y=160)
    password.place(x=20,y=230)
    upassword.place(x=250,y=230)
    regst_bt.place(x=200,y=300)
window=Tk()
window.title("To_do_app")
window.minsize(650,650)
window.config(bg="#99CC66")
login=Label(window,text="Login",font=("Berlin Sans FB Demi",35),fg="#330000",bg="#99CC66")
user_name=Label(window,text="User Name: ",font=("Times New Roman",25),fg="#330000",bg="#99CC66")
uuser_name=Entry(window,font=("Times New Roman",25),fg="#330000",bg="#99CC66")
password=Label(window,text="Password: ",font=("Times New Roman",25),fg="#330000",bg="#99CC66")
upassword=Entry(window,show="*",font=("Times New Roman",25),fg="#330000",bg="#99CC66")
login_bt=Button(window,text="Login",font=("Colonna MT",25),fg="#330000",bg="#99CC66",command=password_check)
regstr_bt=Button(window,text="Register",font=("Colonna MT",25),fg="#330000",bg="#99CC66",command=register_entry)
login.place(x=220,y=0)
user_name.place(x=40,y=90)
uuser_name.place(x=250,y=90)
password.place(x=40,y=170)
upassword.place(x=250,y=170)
login_bt.place(x=200,y=270)
regstr_bt.place(x=350,y=270)
