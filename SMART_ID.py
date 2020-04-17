from tkinter import * 
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

# def hide(*widgets):
#     for widget in widgets:
#         widget.pack_forget();


def get():
    if (e_id.get() == ""):
        MessageBox.showinfo('Fetch status', 'Enrollment is compulsory!');
    else:
        con = mysql.connect(host="localhost", username="root", password="Karan@1998", database="BPIT");
        cursor = con.cursor();
        cursor.execute(f"select * FROM Student where Enrollment='{e_id.get()}'");
        rows = cursor.fetchall()

        for row in rows:
            First_name.insert(0, row[1])
            Last_name.insert(0, row[2])
            Branch.insert(0, row[3])
            Batch.insert(0, row[4])
            Balance.insert(0, "\u20b9"+str(row[8]))

        first_name.place(x=20, y=60);
        last_name.place(x=20, y=90)
        branch.place(x=20, y=120)
        batch.place(x=20, y=150)
        balance.place(x=20, y=180)
        amount.place(x=20, y=210)
        First_name.place(x=150, y=60);
        Last_name.place(x=150, y=90);
        Branch.place(x=150, y=120);
        Batch.place(x=150, y=150);
        Balance.place(x=150, y=180)
        Amount.place(x=150, y=210);

        con.close();
        scan.destroy();
        Button(root, text="Proceed to pay  ",image=proceed, font=("helvetica", 15), command=proceed_to_pay, compound=RIGHT).place(x=80, y=240)      

def proceed_to_pay():

    Pin.place(x=300, y=80)

    e_pin.place(x=400, y=80);

    Button(root, text="Pay" ,font=("helvetica", 15), bg="white", command=checkout).place(x=400, y=130)

def checkout():
    con = mysql.connect(host="localhost", username="root", password="Karan@1998", database="BPIT");
    cursor = con.cursor();
    cursor.execute(f"select pin from student where Enrollment='{e_id.get()}'")
    right_pin = cursor.fetchall()[0][0]
    cursor.execute(f"select MD5('{e_pin.get()}')")
    entered_pin = cursor.fetchall()[0][0]

    if (entered_pin!=right_pin):
        MessageBox.showinfo("WRONG PIN", "The provided pin is wrong!!! Kindly Try again!!!")
    else:
        cursor.execute(f"UPDATE Student SET balance = balance-{Amount.get()} where Enrollment='{e_id.get()}'");
        cursor.execute("commit");
        con.close()
        updated_bal = float(Balance.get()[1:])-float(Amount.get())
        MessageBox.showinfo("Transaction SUCCESSFUL!!", f"Transaction of \u20b9 {Amount.get()} is completed succefully. Updated Balance: \u20b9 {updated_bal}");
        Balance.delete(0, END)
        Balance.insert(0, "\u20b9"+str(updated_bal))
    
root = Tk()

root.geometry("960x480");
root.title("BPIT SMART ID");

photo = PhotoImage(file = "logo.png")
logo = Label( image = photo).place(x=400, y=0)

proceed = PhotoImage(file = "Proceed.png").subsample(3, 3)

enrollment = Label(root, text="Enrollment Number", font=('bold', 10));
enrollment.place(x=20, y=30);

first_name = Label(root, text="First Name", font=('bold', 10));
#first_name.place(x=20, y=60);

last_name = Label(root, text="Last Name", font=('bold', 10));
#last_name.place(x=20, y=90)

branch = Label(root, text="Brach", font=('bold', 10));
#branch.place(x=20, y=120)

batch=Label(root, text="Batch", font=('bold', 10));
#batch.place(x=20, y=150)

balance = Label(root, text="Balance", font=("bold", 10));
#balance.place(x=20, y=180)

amount = Label(root, text="Amount", font=("bold", 10));

Pin=Label(root, text="Enter Pin", font=('bold', 10));

e_id = Entry();
e_id.place(x=150, y=30);

First_name = Entry();
#First_name.place(x=150, y=60);

Last_name = Entry();
#Last_name.place(x=150, y=90);

Branch = Entry();
#Branch.place(x=150, y=120);

Batch = Entry();
#Batch.place(x=150, y=150);

Balance = Entry();
#Balance.place(x=150, y=180)
#Balance.insert(0, "\u20b9")

Amount = Entry();

e_pin = Entry(show="*");

scan = Button(root, text="SCAN", font=("helvetica", 15), bg="white", command=get)
scan.place(x=190, y=80)
root.mainloop() 
