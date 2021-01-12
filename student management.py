from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql.cursors
import re
window=Tk()
class Student:
    def __init__(self,window):
        self.window=window
        self.window.title("Welcome to Student Management System")
        self.window.geometry("1350x750+0+0")
        self.window.config(bg="white")
        title=Label(window,text="Student Management",font="Helvetica 25 bold",bg="yellow",bd=8,relief="groove",fg="red")
        title.pack(side=TOP,fill=X)

        #======ALL VARIABLES======
        self.Inst_Id =StringVar()
        self.StdId = StringVar()
        self.Name = StringVar()
        self.STD = StringVar()
        self.Gender = StringVar()
        self.DoB= StringVar()
        self.Address = StringVar()
        self.Ph_No = StringVar()
        self.School = StringVar()
        self.Email_id = StringVar()
        self.Weak_sub = StringVar()
        self.Branch = StringVar()
        self.Fees = StringVar()
        self.perc = StringVar()
        
        #====================================================================FRAMES======================================================================
        #frame1
        frame=LabelFrame(window,bd=5,relief="groove",bg="light blue",text="ENTER STUDENT DATA :",font="Helvetica 16 bold")
        frame.place(x=8,y=60,width=1350,height=350)
        
        Dataframe=Frame(window,bd=5,relief="groove",bg="light blue")
        Dataframe.place(x=8,y=420,width=650,height=275)

        classframe=Frame(window,bd=5,relief="groove",bg="light blue")
        classframe.place(x=675,y=420,width=680,height=275)
        
        #====================================================================LABELS & ENTRY======================================================================


        #Institute label and entry
        lbl_InstId=Label(frame,text="INSTITUTE_ID:",font="Helvetica 15 bold",bg="light blue")
        lbl_InstId.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        e_InstId=Entry(frame,font="Helvetica 12 bold",textvar=self.Inst_Id,bd=2,relief="groove")
        e_InstId.grid(row=0,column=1,pady=10,padx=20,sticky="w")


        #StdId label and entry
        lbl_StdId=Label(frame,text="STD_ID:",font="Helvetica 15 bold",bg="light blue")
        lbl_StdId.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        e_StdId=Entry(frame,font="Helvetica 12 bold",textvar=self.StdId,bd=2,relief="groove")
        e_StdId.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        #name label and entry
        lbl_name=Label(frame,text="NAME:",font="Helvetica 15 bold",bg="light blue")
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        e_name=Entry(frame,font="Helvetica 12 bold",textvar=self.Name,bd=2,relief="groove")
        e_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        
        #std label and entry
        lbl_std=Label(frame,text="STD:",font="Helvetica 15 bold",bg="light blue")
        lbl_std.grid(row=3,column=0,pady=15,padx=30,sticky="w")

        combo_std=ttk.Combobox(frame,font="Helvetica 11 bold",textvar=self.STD,values=["I","II","III","VI","V","VI","VII","VIII","IX","X","XI-SCIENCE",\
                                                                                        "XI-COMMERCE","XI-ARTS","XII-SCIENCE","XII-COMMERCE","XII-ARTS"],\
                                state="readonly")
        combo_std.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        #gender label and entry
        lbl_gender=Label(frame,text="GENDER:",font="Helvetica 15 bold",bg="light blue")
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(frame,font="Helvetica 11 bold",textvar=self.Gender,values=["MALE","FEMALE","OTHERS"],state="readonly")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        
        #d_o_b label and entry
        lbl_dob=Label(frame,text="D_O_B(YYYY-MM-DD)",font="Helvetica 15 bold",bg="light blue")
        lbl_dob.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        
        e_dob=Entry(frame,font="Helvetica 12 bold",textvar=self.DoB,bd=2,relief="groove")
        e_dob.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        #address label and entry
        lbl_add=Label(frame,text="ADDRESS:",font="Helvetica 15 bold",bg="light blue")
        lbl_add.grid(row=0,column=2,pady=10,padx=20,sticky="w")
       
        e_add=Entry(frame,font="Helvetica 12 bold",textvar=self.Address,bd=2,relief="groove")
        e_add.grid(row=0,column=3,pady=10,padx=20,sticky="w")

        #phone no label and entry
        lbl_no=Label(frame,text="PHONE NO:",font="Helvetica 15 bold",bg="light blue")
        lbl_no.grid(row=1,column=2,pady=10,padx=20,sticky="w")

        e_no=Entry(frame,font="Helvetica 12 bold",textvar=self.Ph_No,bd=2,relief="groove")
        e_no.grid(row=1,column=3,pady=10,padx=20,sticky="w")
        
        #school label and entry
        lbl_school=Label(frame,text="SCHOOL/COLLEGE:",font="Helvetica 15 bold",bg="light blue")
        lbl_school.grid(row=2,column=2,pady=10,padx=20,sticky="w")

        e_school=Entry(frame,font="Helvetica 12 bold",textvar=self.School,bd=2,relief="groove")
        e_school.grid(row=2,column=3,pady=10,padx=20,sticky="w")

        #email_id label and entry
        lbl_mail=Label(frame,text="EMAIL_ID:",font="Helvetica 15 bold",bg="light blue")
        lbl_mail.grid(row=3,column=2,pady=10,padx=20,sticky="w")

        e_mail=Entry(frame,font="Helvetica 12 bold",textvar=self.Email_id,bd=2,relief="groove")
        e_mail.grid(row=3,column=3,pady=10,padx=20,sticky="w")

        #weak subject label and entry
        lbl_sub=Label(frame,text="WEAK SUBJECT:",font="Helvetica 15 bold",bg="light blue")
        lbl_sub.grid(row=4,column=2,pady=10,padx=20,sticky="w")

        e_sub=Entry(frame,font="Helvetica 12 bold",textvar=self.Weak_sub,bd=2,relief="groove")
        e_sub.grid(row=4,column=3,pady=10,padx=20,sticky="w")

        #branch label and entry
        lbl_branch=Label(frame,text="BRANCH:",font="Helvetica 15 bold",bg="light blue")
        lbl_branch.grid(row=5,column=2,pady=10,padx=20,sticky="w")

        combo_branch=ttk.Combobox(frame,font="Helvetica 11 bold",textvar=self.Branch,values=["CHEMBUR","KING CIRCLE","CHURCHGATE","VASHI"],state="readonly")
        combo_branch.grid(row=5,column=3,pady=10,padx=20,sticky="w")

        #fees label and entry
        lbl_fees=Label(frame,text="FEES:",font="Helvetica 15 bold",bg="light blue")
        lbl_fees.grid(row=0,column=4,pady=10,padx=20,sticky="w")

        combo_fees=ttk.Combobox(frame,font="Helvetica 11 bold",textvar=self.Fees,values=["PAID","UNPAID"],state="readonly")
        combo_fees.grid(row=0,column=5,pady=10,padx=20,sticky="w")

        #last year percentage label and entry
        lbl_perc=Label(frame,text="LAST YEAR %:",font="Helvetica 15 bold",bg="light blue")
        lbl_perc.grid(row=1,column=4,pady=10,padx=20,sticky="w")

        e_perc=Entry(frame,font="Helvetica 12 bold",textvar = self.perc,bd=2,relief="groove")
        e_perc.grid(row=1,column=5,pady=10,padx=20,sticky="w")

        #Total_students textbox

        self.text_total=Text(frame,font="Helvetica",bd=2,relief="groove",height=1,width=15)
        self.text_total.grid(row=5,column=5,pady=10,padx=20,sticky="w")
        

        #===============================================================BUTTON======================================================================

        #add button
        add_btn=Button(frame,text="ADD",font="Helvetica 12 bold",bg="light blue",height=1,width=8,command=self.add_stu_Data)
        add_btn.grid(row=2,column=5,pady=10,padx=20,sticky="w")

        #clear button
        clear_btn=Button(frame,text="CLEAR",font="Helvetica 12 bold",bg="light blue",width=8,command=self.ClearData,height=1)
        clear_btn.grid(row=2,column=4,pady=10,padx=20,sticky="w")

        #search_StdId button
        search_StdId_btn=Button(frame,text="SEARCH(STDID)",font="Helvetica 12 bold",bg="light blue",command=self.Search_StdId)
        search_StdId_btn.grid(row=3,column=4,pady=10,padx=20,sticky="w")

        #search_Name button
        search_Name_btn=Button(frame,text="SEARCH(NAME)",font="Helvetica 12 bold",bg="light blue",command= self.Search_Name)
        search_Name_btn.grid(row=3,column=5,pady=10,padx=20,sticky="w")

        #TOTAL button
        TOTAL_btn=Button(frame,text="TOTAL STUDENTS",font="Helvetica 12 bold",bg="light blue",command=self.get_all_children)
        TOTAL_btn.grid(row=5,column=4,pady=10,padx=20,sticky="w")

        #search_InstId button
        search_InstId_btn=Button(frame,text="SEARCH(INST_ID)",font="Helvetica 12 bold",bg="light blue",command=self.Search_Inst_Id)
        search_InstId_btn.grid(row=4,column=5,pady=10,padx=20,sticky="w")
       
        #class_I  button
        class_I_btn=Button(classframe,text=" I",font="Helvetica 12 bold",bg="light blue",width=8,command=self.Stu_I)
        class_I_btn.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        #class_II  button
        class_II_btn=Button(classframe,text="II",font="Helvetica 12 bold",bg="light blue",width=8,command=self.Stu_II)
        class_II_btn.grid(row=0,column=1,pady=10,padx=20,sticky="w")

        #class_III  button
        class_III_btn=Button(classframe,text="III",font="Helvetica 12 bold",bg="light blue",width=8,command=self.Stu_III)
        class_III_btn.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        #class_IV  button
        class_IV_btn=Button(classframe,text="IV",font="Helvetica 12 bold",bg="light blue",width=8,command=self.Stu_IV)
        class_IV_btn.grid(row=0,column=3,pady=10,padx=20,sticky="w")

        #class_V  button
        class_V_btn=Button(classframe,text="V",font="Helvetica 12 bold",bg="light blue",width=8,command=self.Stu_V)
        class_V_btn.grid(row=0,column=4,pady=10,padx=20,sticky="w")

        #class_VI  button
        class_VI_btn=Button(classframe,text="VI",font="Helvetica 12 bold",bg="light blue",width=8,command=self.Stu_VI)
        class_VI_btn.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        #class_VII  button
        class_VII_btn=Button(classframe,text="VII",font="Helvetica 12 bold",bg="light blue",width=8,command=self.Stu_VII)
        class_VII_btn.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        #class_VIII  button
        class_VIII_btn=Button(classframe,text="VIII",font="Helvetica 13 bold",bg="light blue",width=8,command=self.Stu_VIII)
        class_VIII_btn.grid(row=1,column=2,pady=10,padx=20,sticky="w")

        #class_IX  button
        class_IX_btn=Button(classframe,text="IX",font="Helvetica 12 bold",bg="light blue",width=8,command=self.Stu_IX)
        class_IX_btn.grid(row=1,column=3,pady=10,padx=20,sticky="w")

        #class_X  button
        class_X_btn=Button(classframe,text="X",font="Helvetica 12 bold",bg="light blue",width=8,command=self.Stu_X)
        class_X_btn.grid(row=1,column=4,pady=10,padx=20,sticky="w")

        #class_XI(SCI)  button
        class_XI_SCI_btn=Button(classframe,text="XI(SCI)",font="Helvetica 12 bold",bg="light blue",width=8,command=self.Stu_XI_SCI)
        class_XI_SCI_btn.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        #class_XI(COMM)  button
        class_XI_COMM_btn=Button(classframe,text="XI(COMM) ",font="Helvetica 12 bold",bg="light blue",width=8,command=self.Stu_XI_COMM)
        class_XI_COMM_btn.grid(row=2,column=1,pady=10,padx=20,sticky="w")


        #class_XI(ARTS)  button
        class_XI_ARTS_btn=Button(classframe,text="XI(ARTS)",font="Helvetica 12 bold",bg="light blue",width=8,command=self.Stu_XI_ARTS)
        class_XI_ARTS_btn.grid(row=2,column=2,pady=10,padx=20,sticky="w")


        #class_XII(SCI)  button
        class_XII_SCI_btn=Button(classframe,text="XII(SCI)",font="Helvetica 12 bold",bg="light blue",width=8,command=self.Stu_XII_SCI)
        class_XII_SCI_btn.grid(row=2,column=3,pady=10,padx=20,sticky="w")


        #class_XII(COMM)  button
        class_XII_COMM_btn=Button(classframe,text="XII(COMM)",font="Helvetica 12 bold",bg="light blue",width=8,command=self.Stu_XII_COMM)
        class_XII_COMM_btn.grid(row=2,column=4,pady=10,padx=20,sticky="w")

        #class_XII(ARTS)  button
        class_XII_ARTS_btn=Button(classframe,text="XII(ARTS) ",font="Helvetica 12 bold",bg="light blue",width=8,command=self.Stu_XII_ARTS)
        class_XII_ARTS_btn.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        #delete button
        delete_btn=Button(classframe,text="DELETE",font="Helvetica 15 bold",bg="light blue",height=2,command=self.DeleteData)
        delete_btn.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        #show_all button
        show_all_btn=Button(classframe,text="SHOW ALL",font="Helvetica 13 bold",bg="light blue",height=3,command=self.DisplayData)
        show_all_btn.grid(row=3,column=2,pady=10,padx=20,sticky="w")

        #update button
        update_btn=Button(classframe,text="UPDATE",font="Helvetica 15 bold",bg="light blue",height=2,command=self.update_data)
        update_btn.grid(row=3,column=3,pady=10,padx=20,sticky="s")

        #EXIT button
        EXIT_btn=Button(classframe,text="EXIT",font="Helvetica 15 bold",bg="light blue",command=self.Exit,height=2)
        EXIT_btn.grid(row=3,column=4,pady=10,padx=20,sticky="w")


        





        #===============================================================SCROLLBAR======================================================================

        scrollbar_x= Scrollbar(Dataframe,orient=HORIZONTAL)
        scrollbar_y= Scrollbar(Dataframe,orient=VERTICAL)
        self.student_table=ttk.Treeview(Dataframe,columns=("STD_ID","NAME","STD","GENDER","D_O_B","ADDRESS","PHONE NO","SCHOOL/COLLEGE","EMAIL_ID","WEAK SUBJECT",\
                                                       "BRANCH","FEES","LAST YEAR %","INSTITUTE_ID"),xscrollcommand=scrollbar_x.set,yscrollcommand=scrollbar_y.set)
        
        scrollbar_x.pack(side=BOTTOM,fill=X)
        scrollbar_y.pack(side=RIGHT,fill=Y)
        scrollbar_x.config(command=self.student_table.xview)
        scrollbar_y.config(command=self.student_table.yview)
        self.student_table.heading("STD_ID",text="STD_ID")
        self.student_table.heading("NAME",text="NAME")
        self.student_table.heading("STD",text="STD")
        self.student_table.heading("GENDER",text="GENDER")
        self.student_table.heading("D_O_B",text="D_O_B")
        self.student_table.heading("ADDRESS",text="ADDRESS")
        self.student_table.heading("PHONE NO",text="PHONE NO")
        self.student_table.heading("SCHOOL/COLLEGE",text="SCHOOL/COLLEGE")
        self.student_table.heading("EMAIL_ID",text="EMAIL_ID")
        self.student_table.heading("WEAK SUBJECT",text="WEAK SUBJECT")
        self.student_table.heading("BRANCH",text="BRANCH")
        self.student_table.heading("FEES",text="FEES")
        self.student_table.heading("LAST YEAR %",text="LAST YEAR ")
        self.student_table.heading("INSTITUTE_ID",text="INSTITUTE_ID")
        self.student_table['show']='headings'
        self.student_table.column("STD_ID",width=100)
        self.student_table.column("NAME",width=100)
        self.student_table.column("STD",width=100)
        self.student_table.column("GENDER",width=100)
        self.student_table.column("D_O_B",width=100)
        self.student_table.column("ADDRESS",width=100)
        self.student_table.column("PHONE NO",width=100)
        self.student_table.column("SCHOOL/COLLEGE",width=120)
        self.student_table.column("EMAIL_ID",width=180)
        self.student_table.column("WEAK SUBJECT",width=100)
        self.student_table.column("BRANCH",width=100)
        self.student_table.column("FEES",width=100)
        self.student_table.column("LAST YEAR %",width=100)
        self.student_table.column("INSTITUTE_ID",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.DisplayData()
       
    #====================================================================FUNCTIONS====================================================================== 

    def Exit(self):
        MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
        if MsgBox == 'yes':
            window.destroy()
        else:
            messagebox.showinfo('Return','You will now return to the application screen')
        

    def ClearData(self):
        self.Inst_Id.set(" ")
        self.StdId.set(" ")
        self.Name.set(" ")
        self.STD.set(" ")
        self.Gender.set(" ")
        self.DoB.set(" ")
        self.Address.set(" ")
        self.Ph_No.set(" ")
        self.School.set(" ")
        self.Email_id.set(" ")
        self.Weak_sub.set(" ")
        self.Branch.set(" ")
        self.Fees.set(" ")
        self.perc.set(" ")

    def add_stu_Data(self):
        if (self.Inst_Id.get()=="" or self.StdId.get()=="" or self.Name.get()=="" or self.STD.get()=="" or self.Gender.get()=="" or self.DoB.get()=="" or self.Address.get()=="" or \
            self.Ph_No.get()=="" or self.School.get()=="" or self.Email_id.get()=="" or self.Weak_sub.get()=="" or self.Branch.get()=="" or self.Fees.get()=="" or \
            self.perc.get()==""):
            messagebox.showerror("Error","All Fields Are Required",icon='error')
        
            
        else:
            try:
                db=pymysql.connect("localhost","root","root","stm")
                print ("connected 1")
                cursor=db.cursor()
                cursor.execute(" select * from student where StdId=%s",self.StdId.get())
                row=cursor.fetchone()
                print(row)
                cursor.execute(" select * from Institute where Inst_Id=%s",self.Inst_Id.get())
                rows=cursor.fetchone()
                print(rows)
                if row!= None:
                    messagebox.showerror("Error","Enter Different StdID This ID Already Exist ",icon='error')
                elif rows!= None:
                    messagebox.showerror("Error","Enter Different Institute ID This ID Already Exist ",icon='error')
                elif re.search('[,.;:!@#$%&*?:"/\|]',self.Inst_Id.get()):
                    messagebox.showerror("Error","Enter Institute ID Only In Integer \n Don't Enter Any Special Character ",icon='error')
                elif re.search('[a-zA-Z]',self.Inst_Id.get()):
                    messagebox.showerror("Error","Enter Institute Id Only In Integer ",icon='error')
                elif re.search('[0-9]',self.Name.get()):
                    messagebox.showerror("Error","Enter Name Only In Alphabets ",icon='error')
                elif re.search('[,.;:!@#$%&*?:"/\|]',self.Name.get()):
                    messagebox.showerror("Error","Enter Name Only In Alphabets \n Don't Enter Any Special Character ",icon='error')
                elif re.search('[a-zA-Z]',self.StdId.get()):
                    messagebox.showerror("Error","Enter Student Id Only In Integer ",icon='error')
                elif re.search('[,.;:!@#$%&*?:"/\|]',self.StdId.get()):
                    messagebox.showerror("Error","Enter Student Id Only In Integer \n Don't Enter Any Special Character ",icon='error')
                elif re.search('[a-zA-Z]',self.DoB.get()):
                    messagebox.showerror("Error","Enter Date Of Birth in YYYY-MM-DD \n Don't write alphabets",icon='error')
                elif re.search('[,;:!@#$%&*?:"]',self.DoB.get()):
                    messagebox.showerror("Error","Enter Date Of Birth in YYYY-MM-DD  \n Don't Enter Any Special Character ",icon='error')
                elif re.search('[a-zA-Z]',self.Ph_No.get()):
                    messagebox.showerror("Error","Enter Phone Number Only In Integer ",icon='error')
                elif re.search('[,;:!@#$%&*?:"/\|]',self.Ph_No.get()):
                    messagebox.showerror("Error","Enter Phone Number Only In Integer \n Don't Enter Any Special Character ",icon='error')
                elif (len(self.Ph_No.get())>10):
                    messagebox.showerror("Error","Enter Phone Number of 10 digits only ",icon='error')
                elif (len(self.Ph_No.get())<10):
                    messagebox.showerror("Error","Enter Phone Number of 10 digits only ",icon='error')
                elif re.search('[0-9]',self.School.get()):
                    messagebox.showerror("Error","Enter School Name Only In Alphabets ",icon='error')
                elif re.search('[,;:!@#$%&*?:"/\|]',self.School.get()):
                    messagebox.showerror("Error","Enter School Name Only In Alphabets \n Don't Enter Any Special Character ",icon='error')
                elif re.search('[,;:!#$%&*?"/\|]',self.Email_id.get()):
                    messagebox.showerror("Error","Enter EMAIL_ID correctly(xxx@gmail.com)\nDon't Enter Any Special Character ",icon='error')
                elif re.search('[0-9]',self.Weak_sub.get()):
                    messagebox.showerror("Error","Enter Subject in Alphabets only  ",icon='error')
                elif re.search('[,;:!@#$%&*?"/\|]',self.Weak_sub.get()):
                    messagebox.showerror("Error","Enter Subject Only In Alphabets \n Don't Enter Any Special Character ",icon='error')
                elif re.search('[a-zA-Z]',self.perc.get()):
                    messagebox.showerror("Error","Enter Percentage  Only In Numbers ",icon='error')
                elif re.search('[,;:!@#$&*?"/\|]',self.perc.get()):
                    messagebox.showerror("Error","Enter Percentage  Only In Integer \n Don't Enter Any Special Character ",icon='error')

                else:
                    cursor.execute("insert into Institute values(%s)",self.Inst_Id.get())
                    cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.StdId.get(),self.Name.get(),\
                                                                                                         self.STD.get(),self.Gender.get(),\
                                                                                                         self.DoB.get(),self.Address.get(),self.Ph_No.get(),\
                                                                                                         self.School.get(),self.Email_id.get(),self.Weak_sub.get(),\
                                                                                                         self.Branch.get(),self.Fees.get(),self.perc.get(),self.Inst_Id.get()))
                    
                    messagebox.showinfo("Success","Student Data Successfully Added",icon='info')
                    db.commit()
                    db.close()
                    #self.DisplayData()
                    self.ClearData()
            except:
                db.close()
                self.ClearData()            
                    
    def DisplayData(self):
        db=pymysql.connect("localhost","root","root","stm")
        cursor=db.cursor()
        cursor.execute("select * from student")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        db.close()
        return rows

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        #print(row)
        self.StdId.set(row[0])
        self.Name.set(row[1])
        self.STD.set(row[2])
        self.Gender.set(row[3])
        self.DoB.set(row[4])
        self.Address.set(row[5])
        self.Ph_No.set(row[6])
        self.School.set(row[7])
        self.Email_id.set(row[8])
        self.Weak_sub.set(row[9])
        self.Branch.set(row[10])
        self.Fees.set(row[11])
        self.perc.set(row[12])
        self.Inst_Id.set(row[13])


    def update_data(self):
        db=pymysql.connect("localhost","root","root","stm")
        cursor=db.cursor()
        cursor.execute("update student set  Name=%s,STD=%s,Gender=%s,Dob=%s,Address=%s,Ph_No=%s,School=%s,Email_id=%s,Weak_sub=%s,Branch=%s,\
                        Fees=%s,l_y_perc=%s where StdId=%s",(self.Name.get(),self.STD.get(),self.Gender.get(),self.DoB.get(),self.Address.get(),self.Ph_No.get(),\
                                                             self.School.get(),self.Email_id.get(),self.Weak_sub.get(),self.Branch.get(),self.Fees.get(),\
                                                             self.perc.get(),self.StdId.get()))
        messagebox.showinfo("Success","Student Data Successfully Updated",icon='info')
        
                            
        db.commit()
        db.close()
        self.DisplayData()
        self.ClearData()



    def DeleteData(self):
        db=pymysql.connect("localhost","root","root","stm")
        cursor=db.cursor()
        cursor.execute("delete from student where StdId=%s",self.StdId.get())
        cursor.execute("delete from Institute where Inst_Id=%s",self.Inst_Id.get())
        messagebox.showinfo("Success","Student Data Successfully Deleted",icon='info')
        db.commit()
        db.close()
        self.DisplayData()
        self.ClearData()

    def Search_Name(self):
        db=pymysql.connect("localhost","root","root","stm")
        cursor=db.cursor()
        cursor.execute("select * from student where Name= %s", self.Name.get())
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            messagebox.showerror("Error","INVALID NAME",icon='error')
            
        db.close()
        return rows
    
    def Search_StdId(self):
        db=pymysql.connect("localhost","root","root","stm")
        cursor=db.cursor()
        cursor.execute("select * from student where StdId=%s",self.StdId.get())
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            messagebox.showerror("Error","INVALID STUDENT ID",icon='error')
        db.close()
        return rows

    def Search_Inst_Id(self):
        db=pymysql.connect("localhost","root","root","stm")
        cursor=db.cursor()
        cursor.execute("select * from student where Inst_Id=%s",self.Inst_Id.get())
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            messagebox.showerror("Error","INVALID INSTITUTE ID",icon='error')
        db.close()
        return rows


    def Stu_I(self):
        db=pymysql.connect("localhost","root","root","stm")
        cursor=db.cursor()
        cursor.execute("select * from student where STD='I' ")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()

        else:
            self.student_table.delete(* self.student_table.get_children())
        db.close()
        return rows

    def Stu_II(self):
        db=pymysql.connect("localhost","root","root","stm")
        cursor=db.cursor()
        cursor.execute("select * from student where STD='II' ")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            self.student_table.delete(* self.student_table.get_children())
            
            
            
        db.close()
        return rows


    def Stu_III(self):
        db=pymysql.connect("localhost","root","root","stm")
        print ("connected 9")
        cursor=db.cursor()
        cursor.execute("select * from student where STD='III' ")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            self.student_table.delete(* self.student_table.get_children())
            
            
            
        db.close()
        return rows


    def Stu_IV(self):
        db=pymysql.connect("localhost","root","root","stm")
        print ("connected 9")
        cursor=db.cursor()
        cursor.execute("select * from student where STD='IV' ")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            self.student_table.delete(* self.student_table.get_children())
            
            
            
        db.close()
        return rows


    def Stu_V(self):
        db=pymysql.connect("localhost","root","root","stm")
        print ("connected 9")
        cursor=db.cursor()
        cursor.execute("select * from student where STD='V' ")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            self.student_table.delete(* self.student_table.get_children())
            
            
            
        db.close()
        return rows


    def Stu_VI(self):
        db=pymysql.connect("localhost","root","root","stm")
        print ("connected 9")
        cursor=db.cursor()
        cursor.execute("select * from student where STD='VI' ")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            self.student_table.delete(* self.student_table.get_children())
            
        db.close()
        return rows


    def Stu_VII(self):
        db=pymysql.connect("localhost","root","root","stm")
        print ("connected 9")
        cursor=db.cursor()
        cursor.execute("select * from student where STD='VII' ")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            self.student_table.delete(* self.student_table.get_children())
            
        db.close()
        return rows


    def Stu_VIII(self):
        db=pymysql.connect("localhost","root","root","stm")
        print ("connected 9")
        cursor=db.cursor()
        cursor.execute("select * from student where STD='VIII' ")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            self.student_table.delete(* self.student_table.get_children())
            
        db.close()
        return rows

    def Stu_IX(self):
        db=pymysql.connect("localhost","root","root","stm")
        print ("connected 9")
        cursor=db.cursor()
        cursor.execute("select * from student where STD='IX' ")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            self.student_table.delete(* self.student_table.get_children())
            
        db.close()
        return rows


    def Stu_X(self):
        db=pymysql.connect("localhost","root","root","stm")
        print ("connected 9")
        cursor=db.cursor()
        cursor.execute("select * from student where STD='X' ")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            self.student_table.delete(* self.student_table.get_children())
            
        db.close()
        return rows


    def Stu_XI_SCI(self):
        db=pymysql.connect("localhost","root","root","stm")
        print ("connected 9")
        cursor=db.cursor()
        cursor.execute("select * from student where STD='XI-SCIENCE' ")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            self.student_table.delete(* self.student_table.get_children())
            
        db.close()
        return rows

    def Stu_XI_COMM(self):
        db=pymysql.connect("localhost","root","root","stm")
        print ("connected 9")
        cursor=db.cursor()
        cursor.execute("select * from student where STD='XI-COMMERCE' ")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            self.student_table.delete(* self.student_table.get_children())
            
        db.close()
        return rows


    def Stu_XI_ARTS(self):
        db=pymysql.connect("localhost","root","root","stm")
        print ("connected 9")
        cursor=db.cursor()
        cursor.execute("select * from student where STD='XI-ARTS' ")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            self.student_table.delete(* self.student_table.get_children())
            
        db.close()
        return rows

    def Stu_XII_SCI(self):
        db=pymysql.connect("localhost","root","root","stm")
        print ("connected 9")
        cursor=db.cursor()
        cursor.execute("select * from student where STD='XII-SCIENCE' ")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            self.student_table.delete(* self.student_table.get_children())
            
        db.close()
        return rows


    def Stu_XII_COMM(self):
        db=pymysql.connect("localhost","root","root","stm")
        print ("connected 9")
        cursor=db.cursor()
        cursor.execute("select * from student where STD='XII-COMMERCE' ")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            self.student_table.delete(* self.student_table.get_children())
            
        db.close()
        return rows

    def Stu_XII_ARTS(self):
        db=pymysql.connect("localhost","root","root","stm")
        print ("connected 9")
        cursor=db.cursor()
        cursor.execute("select * from student where STD='XII-ARTS' ")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values = row)
                db.commit()
        else:
            self.student_table.delete(* self.student_table.get_children())
            
        db.close()
        return rows
    

    def get_all_children(self):
        children = len(self.student_table.get_children())
        if (children)!=0:
            self.text_total.delete(1.0,END)
            self.text_total.insert(1.0,children)
        else:
            self.text_total.delete(1.0,END)
            self.text_total.insert(1.0,0)
        return children
    


application=Student(window)
window.mainloop()
