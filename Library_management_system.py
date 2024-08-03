from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import mysql.connector 
from tkinter import messagebox
import datetime
import tkinter

class LibraryManagementSystem:
    def __init__ (self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")


        #----------------------------------------------VARIABLE----------------------------------------------------
        self.member_VAR =StringVar()
        self.prn_VAR =StringVar()
        self.id_VAR =StringVar()
        self.firstname_VAR =StringVar()
        self.lastname_VAR =StringVar()
        self.address1_VAR =StringVar()
        self.address2_VAR =StringVar()
        self.postcode_VAR =StringVar()
        self.mobile_VAR =StringVar()
        self.bookid_VAR =StringVar()
        self.booktitle_VAR =StringVar()
        self.author_VAR =StringVar()
        self.dateborrowed_VAR =StringVar()
        self.deudate_VAR =StringVar()
        self.daysonbook_VAR =StringVar()
        self.latereturnfine_VAR =StringVar()
        self.dateoverduedate_VAR =StringVar()
        self.actualprice_VAR =StringVar()







        #----------------------------------------------------------------------------------------------------------

        lbltitle =Label(self.root, text='Library Management System', bg ='dark blue', fg = 'white', bd = 20, relief = RIDGE,font =("times new roman",50,"bold"),padx = 2, pady = 6)
        lbltitle.pack(side = TOP, fill= X)

        frame = Frame(self.root,bd =12, relief =RIDGE, padx=20,bg ='grey')
        frame.place(x=0, y =130,width= 1530, height=450)

        #---------------------------------------------DATAFRAME LEFT-----------------------------------------------

        DataFrameLeft = LabelFrame(frame,text='Library Membership Information', bg ='light blue', fg = 'black', bd = 12, relief = RIDGE,font =("times new roman",20,"bold"))
        DataFrameLeft.place(x=0,y=5, width =980, height= 400)

        lblMember = Label(DataFrameLeft, text ='MEMBER TYPE', bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft,font =("times new roman",15,"bold"),textvariable= self.member_VAR,width = 27, state ="readonly")
        comMember['value'] = ('Admins Staf', 'Student','Lectures')
        comMember.current(0)
        comMember.grid(row=0, column =1)

        lblPRN_No = Label(DataFrameLeft, text ='PRN NUMBER', bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No = Entry(DataFrameLeft,font =("times new roman",15,"bold"),textvariable= self.prn_VAR, width =29)
        txtPRN_No.grid(row = 1, column= 1)

        lblID_No = Label(DataFrameLeft, text ='ID NUMBER', bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblID_No.grid(row=2, column=0, sticky=W)
        txtID_No = Entry(DataFrameLeft,font =("times new roman",15,"bold"), textvariable= self.id_VAR, width =29)
        txtID_No.grid(row = 2, column= 1)

        lblFIRST_NAME = Label(DataFrameLeft, text ='FIRST_NAME', bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblFIRST_NAME.grid(row=3, column=0, sticky=W)
        txtFIRST_NAME= Entry(DataFrameLeft,font =("times new roman",15,"bold"),textvariable=self.firstname_VAR, width =29)
        txtFIRST_NAME.grid(row = 3, column= 1)

        lblLAST_NAME = Label(DataFrameLeft, text ='LAST_NAME', bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblLAST_NAME.grid(row=4, column=0, sticky=W)
        txtLAST_NAME = Entry(DataFrameLeft,font =("times new roman",15,"bold"),textvariable=self.lastname_VAR, width =29)
        txtLAST_NAME.grid(row = 4, column= 1)

        lblADDRESS = Label(DataFrameLeft, text ='ADDRESS 1',  bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblADDRESS.grid(row=5, column=0, sticky=W)
        txtADRESS = Entry(DataFrameLeft,font =("times new roman",15,"bold"),textvariable=self.address1_VAR, width =29)
        txtADRESS.grid(row = 5, column= 1)

        lblADDRESS2 = Label(DataFrameLeft, text ='ADDRESS 2', bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblADDRESS2.grid(row=6, column=0, sticky=W)
        txtADRESS2 = Entry(DataFrameLeft,font =("times new roman",15,"bold"),textvariable=self.address2_VAR, width =29)
        txtADRESS2.grid(row = 6, column= 1)

        lblPOST = Label(DataFrameLeft, text ='POST CODE',bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblPOST.grid(row=7, column=0, sticky=W)
        txtPOST = Entry(DataFrameLeft,font =("times new roman",15,"bold"),textvariable= self.postcode_VAR, width =29)
        txtPOST.grid(row = 7, column= 1)



        lblMOB = Label(DataFrameLeft, text ='MOBILE NUMBER', bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblMOB.grid(row=8, column=0, sticky=W)
        txtMOB = Entry(DataFrameLeft,font =("times new roman",15,"bold"),textvariable= self.mobile_VAR, width =29)
        txtMOB.grid(row = 8, column= 1)

        lblBOOKID = Label(DataFrameLeft, text ='BOOK ID', bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblBOOKID.grid(row=0, column=2, sticky=W)
        txtBOOKID = Entry(DataFrameLeft,font =("times new roman",15,"bold"), textvariable=self.bookid_VAR, width =29)
        txtBOOKID.grid(row = 0, column= 3)

        lblBOOKTITLE = Label(DataFrameLeft, text ='BOOK TITLE', bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblBOOKTITLE.grid(row=1, column=2, sticky=W)
        txtBOOKTITLE= Entry(DataFrameLeft,font =("times new roman",15,"bold"),textvariable=self.booktitle_VAR,  width =29)
        txtBOOKTITLE.grid(row = 1, column= 3)

        lblAUTHOR = Label(DataFrameLeft, text ='AUTHOR', bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblAUTHOR.grid(row=2, column=2, sticky=W)
        txtAUTHOR = Entry(DataFrameLeft,font =("times new roman",15,"bold"),textvariable=self.author_VAR ,width =29)
        txtAUTHOR.grid(row = 2, column= 3)

        lblDATE_BORROWED = Label(DataFrameLeft, text ='DATE BORROWED', bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblDATE_BORROWED.grid(row=3, column=2, sticky=W)
        txtDATE_BORROWED = Entry(DataFrameLeft,font =("times new roman",15,"bold"),textvariable=self.dateborrowed_VAR, width =29)
        txtDATE_BORROWED.grid(row = 3, column= 3)

        lblDUE_DATE= Label(DataFrameLeft, text ='DUE DATE', bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblDUE_DATE.grid(row=4, column=2, sticky=W)
        txtDUE_DATE= Entry(DataFrameLeft,font =("times new roman",15,"bold"),textvariable=self.deudate_VAR, width =29)
        txtDUE_DATE.grid(row = 4, column= 3)

        lblDAYS_ON_BOOK = Label(DataFrameLeft, text ='DAYS ON BOOK',bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblDAYS_ON_BOOK.grid(row=5, column=2, sticky=W)
        txtDAYS_ON_BOOK = Entry(DataFrameLeft,font =("times new roman",15,"bold"),textvariable=self.daysonbook_VAR, width =29)
        txtDAYS_ON_BOOK.grid(row = 5, column= 3)

        lblLATERETURNFINE = Label(DataFrameLeft, text ='LATE RETURN FINE', bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblLATERETURNFINE.grid(row=6, column=2, sticky=W)
        txtLATERETURNFINE= Entry(DataFrameLeft,font =("times new roman",15,"bold"), textvariable=self.latereturnfine_VAR,width =29)
        txtLATERETURNFINE.grid(row = 6, column= 3)

        lblDATE_OVER_DUEDATE = Label(DataFrameLeft, text ='DATE OVER DUEDATE',  bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblDATE_OVER_DUEDATE.grid(row=7, column=2, sticky=W)
        txtDATE_OVER_DUEDATE = Entry(DataFrameLeft,font =("times new roman",15,"bold"),textvariable=self.dateoverduedate_VAR ,width =29)
        txtDATE_OVER_DUEDATE.grid(row = 7, column= 3)

        lblACTUAL_PRICE = Label(DataFrameLeft, text ='ACTUAL PRICE', bg = 'light blue',font =("times new roman",15,"bold"), padx=2, pady=6)
        lblACTUAL_PRICE.grid(row=8, column=2, sticky=W)
        txtACTUAL_PRICE = Entry(DataFrameLeft,font =("times new roman",15,"bold"),textvariable=self.actualprice_VAR, width =29)
        txtACTUAL_PRICE.grid(row = 8, column= 3)




        
        












        #-----------------------------------------------DATAFRAME RIGHT--------------------------------------

        

        DataFrameright = LabelFrame(frame,text='Book Details', bg ='light blue', fg = 'black', bd = 12, relief = RIDGE,font =("times new roman",20,"bold"))
        DataFrameright.place(x=950,y=5, width =540, height= 400)

        self.txtBox = Text(DataFrameright, font = ("arial",12, "bold"), width = 32, height= 16, padx= 3, pady=8)
        self.txtBox.grid(row = 0, column= 2)

        listScrollbar = Scrollbar(DataFrameright)
        listScrollbar.grid(row =0,column=1, sticky ="ns")

        Listbooks = ["Python Crash Course","Fluent Python","Think Python","Head First Python","Effective Python","Programming Python",
                  "Python Cookbook","Learning Python","Python Tricks","Python Pocket Reference","Mastering Python","Python Basics",
                  "Python Playground","Python Testing","Python Essentials","Data Science Python", "Beginning Python","Advanced Python",
                   "Modern Python"]
        
        
        def selectbook (event = " "):

            value = str(listbox.get(listbox.curselection()))
            x = value
            
            if  x =="Python Crash Course" :
                self.bookid_VAR.set("BKIDPCC")
                self.booktitle_VAR.set("python Manual")
                self.author_VAR.set("Eric Matthes")
                price = 3305.06
            elif  x == "Fluent Python":
                self.bookid_VAR.set("BKIDFP")
                self.booktitle_VAR.set("Fluent Python")
                self.author_VAR.set("Luciano Ramalho")
                price = 2765.00
            elif x == "Think Python":
                 self.bookid_VAR.set("BKIDTP")
                 self.booktitle_VAR.set("Think Python")
                 self.author_VAR.set("Allen B. Downey")
                 price = 1599.00
            elif x== "Head First Python":
                 self.bookid_VAR.set("BKIDHFP")
                 self.booktitle_VAR.set("Head First Python")
                 self.author_VAR.set("Paul Barry")
                 price = 3050.00
            elif x == "Effective Python":
                 self.bookid_VAR.set("BKIDEP")
                 self.booktitle_VAR.set("Effective Python")
                 self.author_VAR.set("Brett Slatkin")
                 price = 2300.00
            elif x == "Programming Python":
                 self.bookid_VAR.set("BKIDPP")
                 self.booktitle_VAR.set("Programming Python")
                 self.author_VAR.set("Mark Lutz")
                 price = 3999.00
            elif x == "Python Cookbook":
                 self.bookid_VAR.set("BKIDPC")
                 self.booktitle_VAR.set("Python Cookbook")
                 self.author_VAR.set("David Beazley")
                 price = 3500.00
            elif x == "Learning Python":
                 self.bookid_VAR.set("BKIDLP")
                 self.booktitle_VAR.set("Learning Python")
                 self.author_VAR.set("Mark Lutz")
                 price = 4050.00
            elif x == "Python Tricks":
                 self.bookid_VAR.set("BKIDPT")
                 self.booktitle_VAR.set("Python Tricks")
                 self.author_VAR.set("Dan Bader")
                 price = 2200.00
            elif x == "Python Pocket Reference":
                 self.bookid_VAR.set("BKIDPPR")
                 self.booktitle_VAR.set("Python Pocket Reference")
                 self.author_VAR.set("Mark Lutz")
                 price = 1200.00
            elif x == "Mastering Python":
                 self.bookid_VAR.set("BKIDMP")
                 self.booktitle_VAR.set("Mastering Python")
                 self.author_VAR.set("Rick van Hattem")
                 price = 2800.00
            elif x == "Python Basics":
                 self.bookid_VAR.set("BKIDPB")
                 self.booktitle_VAR.set("Python Basics")
                 self.author_VAR.set("Dan Bader")
                 price = 1900.00
            elif x == "Python Playground":
                 self.bookid_VAR.set("BKIDPPG")
                 self.booktitle_VAR.set("Python Playground")
                 self.author_VAR.set("Mahesh Venkitachalam")
                 price = 2700.00
            elif x== "Python Testing":
                self.bookid_VAR.set("BKIDPTT")
                self.booktitle_VAR.set("Python Testing")
                self.author_VAR.set("Brian Okken")
                price = 2500.00
            elif x == "Python Essentials":
                self.bookid_VAR.set("BKIDPE")
                self.booktitle_VAR.set("Python Essentials")
                self.author_VAR.set("Steven F. Lott")
                price = 1800.00
            elif x == "Data Science Python":
                self.bookid_VAR.set("BKIDDSP")
                self.booktitle_VAR.set("Data Science Python")
                self.author_VAR.set("Jake VanderPlas")
                price = 3300.00
            elif x == "Beginning Python":
                self.bookid_VAR.set("BKIDBP")
                self.booktitle_VAR.set("Beginning Python")
                self.author_VAR.set("Magnus Lie Hetland")
                price = 2200.00
            elif x == "Advanced Python":
                self.bookid_VAR.set("BKIDAP")
                self.booktitle_VAR.set("Advanced Python")
                self.author_VAR.set("David M. Beazley")
                price = 3200.00
            elif x== "Modern Python":
                self.bookid_VAR.set("BKIDMPY")
                self.booktitle_VAR.set("Modern Python")
                self.author_VAR.set("Brett Slatkin")
                price = 2800.00
            else:
                print("Book not found in list.")
                return
    
            d1 = datetime.datetime.today()
            d2= datetime.timedelta(days=15)
            d3 = d1+d2
            self.dateborrowed_VAR.set(d1)
            self.deudate_VAR.set(d3)
            self.daysonbook_VAR.set(15)
            self.latereturnfine_VAR.set("Rs.50")
            self.dateoverduedate_VAR.set("No")
            self.actualprice_VAR.set(f"Rs{price}")



        
        listbox = Listbox (DataFrameright, font=("arial",12,"bold"), width = 20, height = 16)
        listbox.bind("<<ListboxSelect>>",selectbook)
        listbox.grid(row= 0, column=0, padx= 4)
        listScrollbar.config(command=listbox.yview)

        for item in Listbooks:
            listbox.insert(END,item)
















        #----------------------------------------------Button frame-------------------------------------------

        btnFrame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='light blue')
        btnFrame.place(x=0, y=530, width=1530, height=70)

        
        btnAdd = Button(btnFrame, text="Add Data", command=self.add_data,font=("times new roman", 12, "bold"), width=23, bg='dark blue', fg='white')
        btnAdd.grid(row=0, column=0, padx=10, pady=10)

        btnAdd = Button(btnFrame, text="Show Data",command=self.showData, font=("times new roman", 12, "bold"), width=23, bg='dark blue', fg='white')
        btnAdd.grid(row=0, column=1, padx=10, pady=10)

        btnAdd = Button(btnFrame, text="Update",command=self.update, font=("times new roman", 12, "bold"), width=23, bg='dark blue', fg='white')
        btnAdd.grid(row=0, column=2, padx=10, pady=10)

        btnAdd = Button(btnFrame, text="Delete", command=self.delete,font=("times new roman", 12, "bold"), width=23, bg='dark blue', fg='white')
        btnAdd.grid(row=0, column=3, padx=10, pady=10)

        btnAdd = Button(btnFrame, text="Reset",command=self.reset, font=("times new roman", 12, "bold"), width=23, bg='dark blue', fg='white')
        btnAdd.grid(row=0, column=4, padx=10, pady=10)

        btnAdd = Button(btnFrame, text="Exit", command = self.iExit,font=("times new roman", 12, "bold"), width=23, bg='dark blue', fg='white')
        btnAdd.grid(row=0, column=5, padx=10, pady=10)
        
        
    
         #---------------------------------------------Information Frame----------------------------------------
        Framedetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='light blue')
        Framedetails.place(x=0, y=600, width=1530, height=195)

        Table_frame = Frame ( Framedetails, bd=6, relief =RIDGE,  bg='light blue')
        Table_frame.place(x=0, y =2, width=1460, height=190)

        
        xscroll = ttk.Scrollbar(Table_frame, orient = HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame, column = ("MEMBER TYPE",'PRN NO','ID NUMBER','FIRST NAME','LAST NAME',
                                                                 'ADDRESS1','ADDRESS2','POST ID','MOBILE','BOOK ID','BOOK TITLE',
                                                                 'AUTHOR','DATE BORROWED','DUE DATE','DATE ON BOOKS','LATE RETURN FINE',
                                                                 'DATE OVER DUEDATE','ACTUAL PRICE' ), xscrollcommand=xscroll.set,
                                                                 yscrollcommand=yscroll.set)
        
        xscroll.pack(side =TOP, fill= X)
        yscroll.pack(side=RIGHT, fill = Y)

        xscroll.config(command = self.library_table.xview)
        yscroll.config(command = self.library_table.yview)


        
        self.library_table.heading("MEMBER TYPE",text = "MEMBER TYPE")
        self.library_table.heading("PRN NO",text = "PRN NUMBER")
        self.library_table.heading("ID NUMBER",text = "ID NUMBER")
        self.library_table.heading("FIRST NAME",text = "FIRST NAME")
        self.library_table.heading("LAST NAME",text = "LAST NAME")
        self.library_table.heading("ADDRESS1",text = "ADDRESS 1")
        self.library_table.heading("ADDRESS2",text = "ADDRESS 2")
        self.library_table.heading("POST ID",text = "POST CODE")
        self.library_table.heading("MOBILE",text = "MOBILE NUMBER")
        self.library_table.heading("BOOK ID",text = "BOOK ID")
        self.library_table.heading("BOOK TITLE",text = "BOOK TITLE")
        self.library_table.heading("AUTHOR",text = "AUTHOR")
        self.library_table.heading("DATE BORROWED",text = "DATE BORROWED")
        self.library_table.heading("DUE DATE",text = "DUE DATE")
        self.library_table.heading("DATE ON BOOKS",text = "DATE ON BOOKS")
        self.library_table.heading("LATE RETURN FINE",text = "LATE RETURN FINE")
        self.library_table.heading("DATE OVER DUEDATE",text = "DATE OVER DUEDATE")
        self.library_table.heading("ACTUAL PRICE",text = "ACTUAL PRICE")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("MEMBER TYPE",width = 100)
        self.library_table.column("PRN NO",width = 100)
        self.library_table.column("ID NUMBER",width = 100)
        self.library_table.column("FIRST NAME",width = 120)
        self.library_table.column("LAST NAME",width = 120)
        self.library_table.column("ADDRESS1",width = 150)
        self.library_table.column("ADDRESS2",width = 150)
        self.library_table.column("POST ID",width = 100)
        self.library_table.column("MOBILE",width = 100)
        self.library_table.column("BOOK ID",width = 100)
        self.library_table.column("BOOK TITLE",width = 100)
        self.library_table.column("AUTHOR",width = 100)
        self.library_table.column("DATE BORROWED",width = 120)
        self.library_table.column("DUE DATE",width = 100)
        self.library_table.column("DATE ON BOOKS",width = 120)
        self.library_table.column("LATE RETURN FINE",width = 120)
        self.library_table.column("DATE OVER DUEDATE",width = 120)
        self.library_table.column("ACTUAL PRICE",width = 100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)
        

    def add_data(self):   
        try:
            con = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Shivani@56",
            database="python"
            )
        
            my_cursor = con.cursor()

            sql_insert_query = """
            INSERT INTO library (
                MEMBER_TYPE,PRN_NO,ID_NUMBER, FIRST_NAME , LAST_NAME ,ADDRESS1,ADDRESS2,POSTCODE,MOBILE_NUMBER ,
                BOOK_ID,BOOK_TITLE,AUTHOR,DATE_BORROWED,DUE_DATE,DAYS_ON_BOOKS,LATE_RETURN_FINE,DATE_OVER_DUEDATE, ACTUAL_PRICE 
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            my_cursor.execute(sql_insert_query, (
            self.member_VAR.get(),
            self.prn_VAR.get(),
            self.id_VAR.get(),
            self.firstname_VAR.get(),
            self.lastname_VAR.get(),
            self.address1_VAR.get(),
            self.address2_VAR.get(),
            self.postcode_VAR.get(),
            self.mobile_VAR.get(),
            self.bookid_VAR.get(),
            self.booktitle_VAR.get(),
            self.author_VAR.get(),
            self.dateborrowed_VAR.get(),
            self.deudate_VAR.get(),
            self.daysonbook_VAR.get(),
            self.latereturnfine_VAR.get(),
            self.dateoverduedate_VAR.get(),
            self.actualprice_VAR.get()
            ))

    
            con.commit()
            self.fetch_data()

            messagebox.showinfo("Success", "Member has been inserted successfully")

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error inserting data: {err}")

        finally:

            if con.is_connected():
                con.close()    

    def update(self):
        
        try:
            con = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Shivani@56",
            database='python'
            )
            my_cursor = con.cursor()
        
        
            sql = """
            UPDATE library 
                SET MEMBER_TYPE = %s, ID_NUMBER = %s, FIRST_NAME = %s, LAST_NAME = %s, ADDRESS1 = %s, ADDRESS2 = %s, POSTCODE = %s, 
                MOBILE_NUMBER = %s, BOOK_ID = %s, BOOK_TITLE = %s, AUTHOR = %s, DATE_BORROWED = %s, DUE_DATE = %s, 
                DAYS_ON_BOOKS = %s, LATE_RETURN_FINE = %s, DATE_OVER_DUEDATE = %s, ACTUAL_PRICE = %s 
                WHERE PRN_NO = %s
            """
    
            my_cursor.execute(sql, (
            self.member_VAR.get(),
            self.id_VAR.get(),
            self.firstname_VAR.get(),
            self.lastname_VAR.get(),
            self.address1_VAR.get(),
            self.address2_VAR.get(),
            self.postcode_VAR.get(),
            self.mobile_VAR.get(),
            self.bookid_VAR.get(),
            self.booktitle_VAR.get(),
            self.author_VAR.get(),
            self.dateborrowed_VAR.get(),
            self.deudate_VAR.get(),
            self.daysonbook_VAR.get(),
            self.latereturnfine_VAR.get(),
            self.dateoverduedate_VAR.get(),
            self.actualprice_VAR.get(),
            self.prn_VAR.get()  
            ))
        
    
            con.commit()
        
    
            self.fetch_data()
            self.reset()
        
            messagebox.showinfo("Success", "Member has been updated")
    
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error updating member: {err}")
    
        finally:
    
           if con.is_connected():
               con.close()


    def fetch_data(self):
        con = mysql.connector.connect(host ="localhost",username = "root", password = "Shivani@56", database='python')
        my_cursor =con.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END, values=i)

            con.commit()
        con.close()        

    def get_cursor(self, event =""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_VAR.set(row[0]),
        self.prn_VAR.set(row[1]),
        self.id_VAR.set(row[2]),
        self.firstname_VAR.set(row[3]),
        self.lastname_VAR.set(row[4]),
        self.address1_VAR.set(row[5]),
        self.address2_VAR.set(row[6]),
        self.postcode_VAR.set(row[7]),
        self.mobile_VAR.set(row[8]),
        self.bookid_VAR.set(row[9]),
        self.booktitle_VAR.set(row[10]),
        self.author_VAR.set(row[11]),
        self.dateborrowed_VAR.set(row[12]),
        self.deudate_VAR.set(row[13]),
        self.daysonbook_VAR.set(row[14]),
        self.latereturnfine_VAR.set(row[15]),
        self.dateoverduedate_VAR.set(row[16]),
        self.actualprice_VAR.set(row[17])

    def showData(self):  
        self.txtBox.insert(END,"MEMBER TYPE\t\t"+ self.member_VAR.get()+"\n")
        self.txtBox.insert(END,"PRN NO\t\t"+ self.prn_VAR.get()+"\n")
        self.txtBox.insert(END,"ID NO\t\t"+ self.id_VAR.get()+"\n") 
        self.txtBox.insert(END,"FIRST NAME\t\t"+ self.firstname_VAR.get()+"\n")
        self.txtBox.insert(END,"LAST NAME\t\t"+ self.lastname_VAR.get()+"\n")
        self.txtBox.insert(END,"ADDRESS1\t\t"+ self.address1_VAR.get()+"\n")
        self.txtBox.insert(END,"ADDRESS2\t\t"+ self.address2_VAR.get()+"\n") 
        self.txtBox.insert(END,"POST CODE\t\t"+ self.postcode_VAR.get()+"\n")
        self.txtBox.insert(END,"MOBILE NO\t\t"+ self.mobile_VAR.get()+"\n") 
        self.txtBox.insert(END,"BOOK ID\t\t"+ self.bookid_VAR.get()+"\n")
        self.txtBox.insert(END,"BOOK TITLE\t\t"+ self.booktitle_VAR.get()+"\n")
        self.txtBox.insert(END,"AUTHOR\t\t"+ self.author_VAR.get()+"\n")  
        self.txtBox.insert(END,"DATE BORROWED\t\t"+ self.dateborrowed_VAR.get()+"\n")  
        self.txtBox.insert(END,"DUE DATE\t\t"+ self.deudate_VAR.get()+"\n")  
        self.txtBox.insert(END,"DAYS ON BOOK\t\t"+ self.daysonbook_VAR.get()+"\n")
        self.txtBox.insert(END,"LATE RETURN FINE\t\t"+ self.latereturnfine_VAR.get()+"\n") 
        self.txtBox.insert(END,"DATE OVER DUEDATE\t\t"+ self.dateoverduedate_VAR.get()+"\n")
        self.txtBox.insert(END,"ACTUAL PRICE\t\t"+ self.actualprice_VAR.get()+"\n") 

    def reset(self):
        self.member_VAR.set(""),
        self.prn_VAR.set(""),
        self.id_VAR.set(""),
        self.firstname_VAR.set(""),
        self.lastname_VAR.set(""),
        self.address1_VAR.set(""),
        self.address2_VAR.set(""),
        self.postcode_VAR.set(""),
        self.mobile_VAR.set(""),
        self.bookid_VAR.set(""),
        self.booktitle_VAR.set(""),
        self.author_VAR.set(""),
        self.dateborrowed_VAR.set(""),
        self.deudate_VAR.set(""),
        self.daysonbook_VAR.set(""),
        self.latereturnfine_VAR.set(""),
        self.dateoverduedate_VAR.set(""),
        self.actualprice_VAR.set(""),
        self.txtBox.delete("1.0", END)
    
    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library management system", "D you want to exit")
        if iExit > 0:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_VAR.get() ==" " or self.id_VAR.get()=="":
            messagebox.showerror("Error","first select the member")
        else:
           
            try:
                con = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Shivani@56",
                database="python"
                )

                my_cursor = con.cursor()


                query = "DELETE FROM library WHERE PRN_NO = %s"
                value = (self.prn_VAR.get(),)

        
                my_cursor.execute(query, value)

        
                con.commit()
                self.fetch_data()
                self.reset()

                messagebox.showinfo("Success", "Member has been deleted")

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error deleting data: {err}")

            finally:
                if con.is_connected():
                    con.close()



        





if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()



