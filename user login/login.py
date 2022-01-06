from tkinter import*
from pymysql import*
from tkinter import messagebox
con=connect(host="localhost",user="root",password="",db="user_table")
cur=con.cursor()
def get_insert_value():
    lst_box_values=ucourse.get(ucourse.curselection()[0])
    for i in student_details:
        if i[1]==lst_box_values:
            lst_box_sno=i[0]
    insert_query="insert into studentinsertion(name,course,phone,address)values('%s',%d,'%s','%s')"%(uname.get(),lst_box_sno,uphone.get(),uaddress.get())
    cur.execute(insert_query)
    con.commit()
def student_insert():
    global uname,ucourse,uphone,uaddress,student_details
    upload_query_fdatebase="select sno,course_name from courseinsertion"
    result=cur.execute(upload_query_fdatebase)
    student_details=[]
    window=Tk()
    window.title("student insertion")
    window.minsize(650,650)
    window.config(bg="#FFFFCC")
    name=Label(window,text="Name: ",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    uname=Entry(window,font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    course=Label(window,text="Courses: ",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    ucourse=Listbox(window,height=2,selectmode="single",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    m=0
    for i in range(result):
        g=cur.fetchone()
        student_details.append(g)
        ucourse.insert(m,g[1])
        m+=1
    phone=Label(window,text="Phone no +91: ",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    uphone=Entry(window,font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    address=Label(window,text="Address: ",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    uaddress=Entry(window,font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    insert=Button(window,text="Insert",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC",command=get_insert_value)
    name.place(x=20,y=30)
    uname.place(x=200,y=30)
    course.place(x=20,y=90)
    ucourse.place(x=200,y=90)
    phone.place(x=20,y=200)
    uphone.place(x=200,y=200)
    address.place(x=20,y=260)
    uaddress.place(x=200,y=260)
    insert.place(x=250,y=320)
def get_update_value():
    select_student="update studentinsertion set phone='%s', address='%s' where name='%s'"%(uphone.get(),uaddress.get(),ustudent.get(ustudent.curselection()[0]))
    cur.execute(select_student)
    con.commit()
def student_update():
    global ustudent,uphone,uaddress
    upload_query_fdatebase="select name from studentinsertion"
    result=cur.execute(upload_query_fdatebase)
    window=Tk()
    window.title("student update")
    window.minsize(650,650)
    window.config(bg="#FFFFCC")
    student=Label(window,text="Select Student: ",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    ustudent=Listbox(window,height=2,selectmode="single",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    m=0
    for i in range(result):
        g=cur.fetchone()
        ustudent.insert(m,g[0])
        m+=1
    phone=Label(window,text="Phone no +91: ",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    uphone=Entry(window,font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    address=Label(window,text="Address: ",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    uaddress=Entry(window,font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    insert=Button(window,text="Insert",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC",command=get_update_value)
    student.place(x=20,y=30)
    ustudent.place(x=200,y=30)
    phone.place(x=20,y=200)
    uphone.place(x=200,y=200)
    address.place(x=20,y=260)
    uaddress.place(x=200,y=260)
    insert.place(x=250,y=320)
def get_delete():
    delete_query="delete from studentinsertion where name='%s'"%(ustudent.get(ustudent.curselection()[0]))
    cur.execute(delete_query)
    con.commit()
def student_delete():
    global ustudent
    upload_query_fdatebase="select name from studentinsertion"
    result=cur.execute(upload_query_fdatebase)
    window=Tk()
    window.title("student view")
    window.minsize(650,650)
    window.config(bg="#FFFFCC")
    student=Label(window,text="Select Student: ",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    ustudent=Listbox(window,height=2,selectmode="single",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    m=0
    for i in range(result):
        g=cur.fetchone()
        ustudent.insert(m,g[0])
        m+=1
    insert=Button(window,text="Insert",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC",command=get_delete)
    student.place(x=20,y=30)
    ustudent.place(x=200,y=30)
    insert.place(x=250,y=320)
def get_view_channel():
    window=Tk()
    window.title("student view")
    window.minsize(650,650)
    window.config(bg="#FFFFCC")
    h=sel_uname.get(sel_uname.curselection()[0])#h contain the name of student for which i want the table
    #ask how to upload single student data with natural join
    upload_db_query="select s.name,s.course,s.phone,s.address,c.course_name,c.course_category,c.course_duration,"
    upload_db_query="c.fees from studentinsertion s,courseinsertion c where s.course=c.sno and s.name='%s'"%(h)
    result=cur.execute(upload_db_query)
    s=""
    for i in range(result):
        g=cur.fetchone()
        for j in g:
            s=s+str(j)+"\t"
        s=s+"\n"
    lbl=Label(window,text=s,font=("Times New Roman",15),fg="#CC9900",bg="#FFFFCC")
    lbl.place(x=20,y=20)  
def student_view():
    global sel_uname
    upload_query_db="select name from studentinsertion"
    result=cur.execute(upload_query_db)
    window=Tk()
    window.title("student view")
    window.minsize(650,650)
    window.config(bg="#FFFFCC")
    sel_name=Label(window,text="Select Name of student: ",font=("Times New Roman",15),fg="#CC9900",bg="#FFFFCC")
    sel_uname=Listbox(window,height=2,selectmode="single",font=("Times New Roman",15),fg="#CC9900",bg="#FFFFCC")
    m=0
    for i in range(result):
        g=cur.fetchone()
        sel_uname.insert(m,g[0])
        m+=1
    view_btn=Button(window,text="view",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC",command=get_view_channel)
    sel_name.place(x=20,y=30)
    sel_uname.place(x=280,y=30)
    view_btn.place(x=250,y=250)
def get_course_insert_value():
    insert_query="insert into courseinsertion(course_name,course_category,course_duration,fees)values('%s','%s','%s',%d)"%(course_uname.get(),course_ucategory.get(course_ucategory.curselection()[0]),uduration.get(),int(ufees.get()))
    cur.execute(insert_query)
    con.commit()
def courses_insert():
    global course_uname, course_ucategory,uduration,ufees
    window=Tk()
    window.title("course insertion")
    window.minsize(650,650)
    window.config(bg="#FFFFCC")
    course_name=Label(window,text="Course Name: ",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    course_uname=Entry(window,font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    course_category=Label(window,text="Course Category: ",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    course_ucategory=Listbox(window,height=2,selectmode="single",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    course_ucategory.insert(0,"Technical")
    course_ucategory.insert(1,"Mechanical")
    course_ucategory.insert(2,"Management")
    course_ucategory.insert(3,"Non-Technical")
    duration=Label(window,text="Duration: ",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    uduration=Spinbox(window,from_=1,to=3,state="readonly",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    fees=Label(window,text="Fees: ",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    ufees=Entry(window,font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    insert=Button(window,text="Insert",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC",command=get_course_insert_value)
    course_name.place(x=20,y=30)
    course_uname.place(x=250,y=30)
    course_category.place(x=20,y=90)
    course_ucategory.place(x=250,y=90)
    duration.place(x=20,y=190)
    uduration.place(x=250,y=190)
    fees.place(x=20,y=250)
    ufees.place(x=250,y=250)
    insert.place(x=300,y=350)
def get_cupdate_value():
    #select_student="update courseinsertion set phone='%s', address='%s' where name='%s'"%(uphone.get(),uaddress.get(),ustudent.get(ustudent.curselection()[0]))
    #cur.execute(select_student)
    #con.commit()
    pass
def courses_update():
    global ucourse
    upload_query_fdatebase="select course_name from courseinsertion"
    result=cur.execute(upload_query_fdatebase)
    window=Tk()
    window.title("student view")
    window.minsize(650,650)
    window.config(bg="#FFFFCC")
    course=Label(window,text="Select Course: ",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    ucourse=Listbox(window,height=2,selectmode="single",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    m=0
    for  i in range(result):
        g=cur.fetchone()
        ustudent.insert(m,g[0])
        m+=1
    insert=Button(window,text="Insert",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC",command=get_cupdate_value)
    course.place(x=20,y=30)
    ucourse.place(x=200,y=30)
    insert.place(x=250,y=320)
def courses_delete():
    pass
def courses_view():
    pass
def view_details():
    window=Tk()
    window.title("view details")
    window.minsize(650,650)
    window.config(bg="#FFFFCC")
    #upload_query="select c.course_name,count(*) from courseinsertion c  group by c.course_name"
    #upload_query="select c.course_name,sum(fees) from courseinsertion c  group by c.course_name"
    upload_query="select c.course_name,count(*) from studentinsertion s,courseinsertion c where s.course=c.sno group by s.course"
    result=cur.execute(upload_query)
    #upload_db_query="select s.name,s.course,s.phone,s.address,c.course_name,c.course_category,c.course_duration"
    #upload_db_query+=",c.fees from studentinsertion s,courseinsertion c where s.course=c.sno "
    #result=cur.execute(upload_db_query)
    s=""
    for i in range(result):
        g=cur.fetchone()
        for j in g:
            s=s+str(j)+"\t"
        s=s+"\n"
    lbl=Label(window,text=s,font=("Times New Roman",15),fg="#CC9900",bg="#FFFFCC")
    lbl.place(x=20,y=20)
def changeConfig():
    p=messagebox.askokcancel("my title","hello")
    if p==True:
        print("saved")
    else:
        print("not saved")
    course_name.config(fg="blue",text="fgh")
    course_uname.config(state=NORMAL)
    course_uname.delete(0,END)
def view_management():
    global course_name,course_uname
    window=Tk()
    window.title("view query")
    window.minsize(650,650)
    window.config(bg="#FFFFCC")
    course_name=Label(window,text="Course Name: ",font=("Times New Roman",15),fg="#CC9900",bg="#FFFFCC")
    course_uname=Entry(window,font=("Times New Roman",15),fg="#CC9900",bg="#FFFFCC",state=DISABLED)
    btn=Button(window,text="view btn",font=("Times New Roman",15),fg="#CC9900",bg="#FFFFCC",command=changeConfig)
    course_name.place(x=20,y=20)
    course_uname.place(x=180,y=20)
    btn.place(x=250,y=250)
    '''global course_uname
    window=Tk()
    window.title("view query")
    window.minsize(650,650)
    window.config(bg="#FFFFCC")
    upload_db_query="select course_name from courseinsertion"
    result=cur.execute(upload_db_query)
    course_name=Label(window,text="Course Name: ",font=("Times New Roman",15),fg="#CC9900",bg="#FFFFCC")
    course_uname=Listbox(window,height=2,selectmode="single",font=("Times New Roman",15),fg="#CC9900",bg="#FFFFCC")
    m=0
    for i in range(result):
        g=cur.fetchone()
        course_uname.insert(m,g[0])
        m+=1
    btn=Button(window,text="view btn",font=("Times New Roman",15),fg="#CC9900",bg="#FFFFCC",command=view_details)
    course_name.place(x=20,y=20)
    course_uname.place(x=180,y=20)
    btn.place(x=250,y=250)'''
    '''
    upload_db_query="select * from studentinsertion"
    result=cur.execute(upload_db_query)
    s=""
    for i in range(result):
        g=cur.fetchone()
        for j in g:
            s=s+str(j)+"\t"
        s=s+"\n"
    lbl=Label(window,text=s,font=("Times New Roman",15),fg="#CC9900",bg="#FFFFCC")
    lbl.place(x=20,y=20)
    '''
def password_check():
    if uuser_name.get().lower()=="admin" and upassword.get().lower()=="admin":
        window=Tk()
        window.title("main page")
        window.minsize(650,650)
        window.config(bg="#FFFFCC")
        mainMenu=Menu(window)
        student=Menu(mainMenu,tearoff=0)
        student.add_command(label="Insert",command=student_insert)
        student.add_command(label="update",command=student_update)
        student.add_command(label="delete",command=student_delete)
        student.add_command(label="view",command=student_view)
        courses=Menu(mainMenu,tearoff=0)
        courses.add_command(label="Insert",command=courses_insert)
        courses.add_command(label="update",command=courses_update)
        courses.add_command(label="delete",command=courses_delete)
        courses.add_command(label="view",command=courses_view)
        show_managing=Menu(mainMenu,tearoff=0)
        show_managing.add_command(label="view",command=view_management)
        mainMenu.add_cascade(label="student",menu=student)
        mainMenu.add_cascade(label="courses",menu=courses)
        mainMenu.add_cascade(label="Show Management",menu=show_managing)
        window.config(menu=mainMenu)
    else:
        load_database_query="select name,password from user_table"
        result=cur.execute(load_database_query)
        for i in range(result):
            g=cur.fetchone()
            c=[]
            for j in g:
                c.append(j)
            if (uuser_name.get() in c) and (upassword.get() in c):
                window=Tk()
                window.title("User Table Exist")
                window.minsize(650,650)
                window.config(bg="#FFFFCC")
                reg=Label(window,text="Welcome to CMS",font=("Berlin Sans FB Demi",50),fg="#CC9900",bg="#FFFFCC")
                reg.place(x=300,y=300)
def get_rgstry_data():
    insert_query="insert into user_table(name,email,password)values('%s','%s','%s')"%(uname.get(),uemail.get(),upassword.get())
    cur.execute(insert_query)
    con.commit()
def register_entry():
    global uname,uemail,upassword
    window=Tk()
    window.title("Registration")
    window.minsize(650,650)
    window.config(bg="#FFFFCC")
    name=Label(window,text="Name: ",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    uname=Entry(window,font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    email=Label(window,text="Email: ",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    uemail=Entry(window,font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    password=Label(window,text="Password: ",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    upassword=Entry(window,show="*",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC")
    submit=Button(window,text="Submit",font=("Times New Roman",20),fg="#CC9900",bg="#FFFFCC",command=get_rgstry_data)
    name.place(x=20,y=30)
    uname.place(x=140,y=30)
    email.place(x=20,y=90)
    uemail.place(x=140,y=90)
    password.place(x=20,y=150)
    upassword.place(x=140,y=150)
    submit.place(x=250,y=240)
window=Tk()
window.title("Login")
window.minsize(650,650)
window.config(bg="#FFFFCC")
login=Label(window,text="Login",font=("Berlin Sans FB Demi",35),fg="#CC9900",bg="#FFFFCC")
user_name=Label(window,text="User Name: ",font=("Times New Roman",25),fg="#CC9900",bg="#FFFFCC")
uuser_name=Entry(window,font=("Times New Roman",25),fg="#CC9900",bg="#FFFFCC")
password=Label(window,text="Password: ",font=("Times New Roman",25),fg="#CC9900",bg="#FFFFCC")
upassword=Entry(window,show="*",font=("Times New Roman",25),fg="#CC9900",bg="#FFFFCC")
login_bt=Button(window,text="Login",font=("Colonna MT",25),fg="#CC9900",bg="#FFFFCC",command=password_check)
regstr_bt=Button(window,text="Register",font=("Colonna MT",25),fg="#CC9900",bg="#FFFFCC",command=register_entry)
login.place(x=220,y=0)
user_name.place(x=40,y=90)
uuser_name.place(x=250,y=90)
password.place(x=40,y=170)
upassword.place(x=250,y=170)
login_bt.place(x=200,y=270)
regstr_bt.place(x=350,y=270)
