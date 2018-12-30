from tkinter import *
root = Tk()
root.geometry('500x500')
root.title("Registration Form")

#Heading
label_0=Label(root, text="Registration form",width=20,font=("bold",20))
label_0.place(x=90,y=53)

#First Label
label_1=Label(root,text="Full Name",width=20,font=("bold",10))
label_1.place(x=80,y=130)

#Second Label
label_2=Label(root,text="E-mail",width=20,font=("bold",10))
label_2.place(x=68,y=180)

#Third Label
label_3=Label(root,text="Gender",width=20,font("bold",10))
label_3.place(x=240,y=180)
#Check box for Gender
var = IntVar()
Radiobutton(root.text="Male",padx=5,variable=var,value=1).place(x=235,y=230)
Radiobutton(root.text="Female",padx=20,variable=var,value=2).place(x=290,y=230)

#Submission Button
Button(root,text='Submit',width=20,bg=20,bg='brown',fg='white').place(x=180,y=380)
mainloop()
