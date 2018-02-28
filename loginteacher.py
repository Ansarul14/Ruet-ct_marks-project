

from PyQt5 import QtCore, QtGui, QtWidgets

from tkinter import  *
import  sqlite3
from tkinter import  messagebox

class Ui_MainWindow(object):


    def login(self):

        name=self.textEdit.toPlainText()
        passw=self.textEdit_2.toPlainText()
        if (name=="ruetcse" and passw=="ruetcse"):

           flag=0
           self.choice()


        else:
            messagebox.showerror("Log-IN error","Sorry invalid entry")




    def choice(self):

        self.root1 = Tk()
        self.root1.geometry("600x500")
        self.root1.config(bg="skyblue")
        self.root1.title("marks calculations")
        self.label=Label(self.root1,text="Please select any option",fg="green",bg="gold",font=25)
        self.label.pack(padx=15,pady=70)
        handler1=lambda :self.marks()
        self.btn1=Button(self.root1,text="Marks Calculations",font=25,fg="Red",bg="white",command=handler1)
        self.btn1.pack(padx=20)
        handler2=lambda :self.resultshow()
        self.btn2 = Button(self.root1, text="View the full result", font=25, fg="Red", bg="white",command=handler2)
        self.btn2.pack(padx=20,pady=20)
        handlerd=lambda :self.delete()
        self.btn3 = Button(self.root1, text="Delete the previous result", font=25, fg="Red", bg="white",command=handlerd)
        self.btn3.pack(padx=20, pady=20)

        handler4=lambda :self.searchresult()
        self.btn4= Button(self.root1, text="Search result", font=25, fg="Red", bg="white",command=handler4)
        self.btn4.pack(padx=20, pady=20)
        self.root1.mainloop()

    def delete(self):
        con=sqlite3.connect("lab_final.db")
        c=con.cursor()
        c.execute("Delete from ct_fmarks")
        con.commit()
        c.close()
        con.close()
        messagebox.showinfo("CT_marks","Successfully deleted previous ct_marks")
    def choices(self):
        self.root1.destroy()
        self.choice()
    def searchresult(self):
        self.root1.destroy()
        self.root1=Tk()
        self.root1.minsize(height=500,width=700)
        self.label=Label(text="Please enter the roll number",font=30,fg="light blue",bg="red")

        self.label.grid(row=1)
        self.entrys=Entry(font=25)
        #self.entrys.grid(row=3,column=5)

        self.entrys.grid(row=2)
        handler1=lambda :self.search()
        self.btn=Button(text="Submit->",fg="green",bg="orange",font=25,command=handler1)
        self.btn.grid(row=4)


        handler2=lambda :self.choices()

        self.btn1 = Button(text="Back<-", fg="green", bg="orange", font=25,command=handler2)
        self.btn1.grid(row=5,pady=10)
        self.root1.mainloop()
    def search(self):



        self.labelroll = Label(self.root1, text="Roll", font=10, fg="green")
        self.labelroll.grid(row=10, column=0, pady=10)
        self.labelatnd = Label(self.root1, text="Attendence percentage", font=10, fg="green")
        self.labelatnd.grid(row=10, column=1)
        self.labelatndm = Label(self.root1, text="Attendence mark", font=10, fg="green")
        self.labelatndm.grid(row=10, column=2)
        self.labelavgct = Label(self.root1, text="Average ct_mark", font=10, fg="green")
        self.labelavgct.grid(row=10, column=4)
        self.labeltmark = Label(self.root1, text="Total mark", font=10, fg="green", padx=10)
        self.labeltmark.grid(row=10, column=5)



        con = sqlite3.connect("lab_final.db")
        self.c = con.cursor()
        p=self.entrys.get()
        p=int(p)
        data = self.readfromdatabases()
        for index, data in enumerate(data):
            if data[0]!=p:
                messagebox.showwarning("Error","Sorry your roll doesnot match")
                break
            else:
                Label(self.root1, text=data[0], font=25, fg="red").grid(row=index + 12, column=0)
                Label(self.root1, text=data[1], font=25, fg="red").grid(row=index + 12, column=1)
                Label(self.root1, text=data[2], font=25, fg="red").grid(row=index + 12, column=2)
                Label(self.root1, text=data[3], font=25, fg="red").grid(row=index + 12, column=4)
                Label(self.root1, text=data[4], font=25, fg="red").grid(row=index + 12, column=5)
                handleroll = lambda: self.roll_delete()

                self.btnd = Button(text="Delete this roll", font=10, fg="green", command=handleroll)
                self.btnd.grid()



    def roll_delete(self):
        con=sqlite3.connect("lab_final.db")
        c=con.cursor()
        p=self.entrys.get()
        c.execute("Delete from ct_fmarks where Roll=?",(p,))
        con.commit()
        messagebox.showinfo("Done","Roll hasbeen deleted")
    def readfromdatabases(self):
        p=self.entrys.get()

        self.c.execute("Select * from ct_fmarks where Roll=?",(p,))
        return self.c.fetchall()
    def resultshow(self):
        self.root1.destroy()
        self.root2=Tk()
        self.root2.config()
        self.root2.geometry("700x600")
        self.label=Label(self.root2,text="Final ct_marks",fg="green",bg="white",font=29,padx=10)
        self.label.grid(row=0,column=5)
        self.labelroll = Label(self.root2,text="Roll", font=10, fg="green",padx=10)
        self.labelroll.grid(row=1, column=0, pady=10)
        self.labelatnd = Label(self.root2,text="Attendence percentage", font=10, fg="green",padx=10)
        self.labelatnd.grid(row=1, column=3)
        self.labelatndm = Label(self.root2,text="Attendence mark", font=10, fg="green",padx=10)
        self.labelatndm.grid(row=1, column=5)
        self.labelavgct = Label(self.root2,text="Average ct_mark", font=10, fg="green",padx=10)
        self.labelavgct.grid(row=1, column=7)
        self.labeltmark = Label(self.root2,text="Total mark", font=10, fg="green",padx=10)
        self.labeltmark.grid(row=1, column=9)
        handler1=lambda :self.choiceb()
        self.btn1 = Button(self.root2, text="Back", font=25, fg="Red", bg="white", command=handler1)
        self.btn1.grid(row=20,pady=20)

        con=sqlite3.connect("lab_final.db")
        self.c=con.cursor()

        data=self.readfromdatabase()
        for index,data in enumerate(data):
            Label(self.root2,text=data[0],font=25,fg="red").grid(row=index+2,column=0)
            Label(self.root2, text=data[1],font=25,fg="red").grid(row=index + 2, column=3)
            Label(self.root2, text=data[2],font=25,fg="red").grid(row=index + 2, column=5)
            Label(self.root2, text=data[3],font=25,fg="red").grid(row=index + 2, column=7)
            Label(self.root2, text=data[4],font=25,fg="red").grid(row=index + 2, column=9)

        self.root2.mainloop()

    def readfromdatabase(self):
        self.c.execute("Select * from ct_fmarks order by Roll")
        return self.c.fetchall()
    def choiceb(self):
        self.root2.destroy()
        self.choice()
    def marks(self):
        self.root1.destroy()
        self.root=Tk()
        self.p=1
        self.root.minsize(height=600,width=750)
        self.label=Label(self.root,text="Please enter the marks ",fg="red",bg="white",font=25)
        self.label.grid(row=0,column=1)
        self.label1=Label(self.root,text="Enter the student  roll number",font=20,fg="green")
        self.label1.grid(row=1,column=0,pady=20)
        self.entry1=Entry(self.root,font=25)
        self.entry1.grid(row=1,column=1)
        self.labelt=Label(self.root,text="Total Classes",font=20,fg="green")
        self.labelt.grid(row=2,column=0,pady=20)
        self.entryt=Entry(self.root,font=20)
        self.entryt.grid(row=2,column=1)
        self.label1 = Label(self.root, text="Total Number Of Classes Present", font=20, fg="green")
        self.label1.grid(row=3, column=0, pady=20)
        self.entry2 = Entry(self.root, font=25)
        self.entry2.grid(row=3, column=1)
        self.label1 = Label(self.root, text="Mark of CT-1", font=20, fg="green")
        self.label1.grid(row=4, column=0, pady=20)
        self.entry3 = Entry(self.root, font=25)
        self.entry3.grid(row=4, column=1)
        self.label1 = Label(self.root, text="Mark of CT-2", font=20, fg="green")
        self.label1.grid(row=5, column=0, pady=20)
        self.entry4 = Entry(self.root, font=25)
        self.entry4.grid(row=5, column=1)
        self.label1 = Label(self.root, text="Mark of CT-3", font=20, fg="green")
        self.label1.grid(row=6, column=0, pady=20)
        self.entry5 = Entry(self.root, font=25)
        self.entry5.grid(row=6, column=1)
        self.label1 = Label(self.root, text="Mark of CT-4", font=20, fg="green")
        self.label1.grid(row=7, column=0, pady=20)
        self.entry6 = Entry(self.root, font=25)
        self.entry6.grid(row=7, column=1)
        handler1=lambda :self.choicea()
        self.btn=Button(self.root,text="Back",font=25,fg="blue",command=handler1)
        self.btn.grid(row=8,column=0)
        handler2 = lambda: self.result()
        self.btn = Button(self.root, text="Submit", font=25, fg="blue", command=handler2)
        self.btn.grid(row=8, column=1)

        self.root.mainloop()
    def choicea(self):
        self.root.destroy()
        self.choice()
    def result(self):

        roll=self.entry1.get()
        roll=int(roll)
        classes=self.entryt.get()
        classes=int(classes)
        tclass=self.entry2.get()
        tclass=int(tclass)
        ct1=self.entry3.get()
        ct1=float(ct1)
        ct2=self.entry4.get()
        ct2=float(ct2)
        ct3=self.entry5.get()
        ct3=float(ct3)
        ct4=self.entry6.get()
        ct4=float(ct4)
        atnd=float(100*tclass)/classes
        patnd=atnd
        patnd=round(patnd,2)
        li=[]
        li.append(ct1)
        li.append(ct2)
        li.append(ct3)

        li.append(ct4)
        lic=[]
        lic=li
        li.sort(reverse=True)

        if atnd>=90:
            atnd=8
        elif atnd>=85 and atnd<90:
            atnd=7
        elif atnd>=80 and atnd<85:
            atnd=6
        elif atnd>=70 and atnd<80:
            atnd=5
        elif atnd>=60 and atnd<70:
            atnd=4
        else:
            atnd=0
        avg=(li[0]+li[1]+li[2])/3
        avg=round(avg,2)
        tmark=avg+atnd
        tmark=round(tmark,2)
        self.labelroll=Label(text="Roll",font=10,fg="green")
        self.labelroll.grid(row=12,column=0,pady=10)
        self.labelatnd = Label(text="Attendence percentage", font=10, fg="green")
        self.labelatnd.grid(row=12, column=1)
        self.labelatndm = Label(text="Attendence mark", font=10, fg="green")
        self.labelatndm.grid(row=12, column=2)
        self.labelavgct = Label(text="Average ct_mark", font=10, fg="green")
        self.labelavgct.grid(row=12, column=4)
        self.labeltmark = Label(text="Total mark", font=10, fg="green")
        self.labeltmark.grid(row=12, column=5)
        con = sqlite3.connect("lab_final.db")
        self.c = con.cursor()

        data=self.readfromdatabase()
        for index,data in enumerate(data):

            if data[0]==roll:

                messagebox.showwarning("Warning","Roll already exists")

                break
        else:

            self.labelrolls = Label(text=roll, font=10, fg="green")
            self.labelrolls.grid(row=13, column=0)
            self.labelatnds = Label(text=patnd, font=10, fg="green")
            self.labelatnds.grid(row=13, column=1)
            self.labelatndms = Label(text=atnd, font=10, fg="green")
            self.labelatndms.grid(row=13, column=2)
            self.labelavgcts = Label(text=avg, font=10, fg="green")
            self.labelavgcts.grid(row=13, column=4)
            self.labeltmarks = Label(text=tmark, font=10, fg="green")
            self.labeltmarks.grid(row=13, column=5)


            self.c.execute("insert into ct_fmarks (Roll,patnd,atndm,avgct,fmark)values(?,?,?,?,?)",
                      (roll, patnd, atnd, avg, tmark))
            con.commit()









    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 476)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("color:orange")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 140, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Umbrella")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(300, 140, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 240, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Storybook")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:red")
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(300, 230, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(300, 310, 185, 41))
        self.commandLinkButton.clicked.connect(self.login)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton.setGeometry(QtCore.QRect(30, 370, 141, 51))

        font = QtGui.QFont()
        font.setFamily("Umbrella")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.commandLinkButton.setText(_translate("MainWindow", "Log-In"))
        self.pushButton.setText(_translate("MainWindow", "BACK"))



if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

