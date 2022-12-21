from tkinter import *
from tkinter import messagebox
import tempfile
import os
root=Tk()
root.title('Sreemoyees Rannaghar')
root.geometry('1280x720')
#=====variable====
Bread=IntVar()
Coke=IntVar()
Pizz=IntVar()
Bur=IntVar()
Momo=IntVar()
total=IntVar()

cb=StringVar()
cob=StringVar()
pb=StringVar()
cib=StringVar()
mocb=StringVar()
total_cost=StringVar()
#=======Function======
def Total():
    if Bread.get()==0 and Coke.get()==0 and Pizz.get()==0 and Bur.get()==0 and Momo.get()==0:
        messagebox.showerror('Error','Please select number of quantity')
    else:
        b=Bread.get()
        c=Coke.get()
        p=Pizz.get()
        bu=Bur.get()
        m=Momo.get()
        t=float(b*25+c*15+p*45+bu*35+m*60)
        total.set(b+c+p+bu+m)
        total_cost.set('₹'+str(round(t,2)))
        cb.set('₹'+str(round(b*25,2)))
        cob.set('₹'+str(round(c*15,2)))
        pb.set('₹'+str(round(p*45,2)))
        cib.set('₹'+str(round(bu*35,2)))
        mocb.set('₹'+str(round(m*60,2)))
def receipt():
    textarea.delete(1.0,END)
    textarea.insert(END,'Items \tNumber of Items \tCost of Items')
    textarea.insert(END,f'\n\nBread\t\t{Bread.get()}\t  {cb.get()}')
    textarea.insert(END,f'\n\nCoca Cola\t\t{Coke.get()}\t  {cob.get()}')
    textarea.insert(END,f'\n\nPizza\t\t{Pizz.get()}\t  {pb.get()}')
    textarea.insert(END,f'\n\nBurger\t\t{Bur.get()}\t  {cib.get()}')
    textarea.insert(END,f'\n\nMomo\t\t{Momo.get()}\t  {mocb.get()}')
    textarea.insert(END,'\n\n================================')
    textarea.insert(END,f'\nTotal Price\t\t{total.get()}\t  {total_cost.get()}')
    textarea.insert(END,'\n================================')

def grint():
    q=textarea.get('1.0','end-1c')
    filename=tempfile.mktemp('.txt')
    open (filename, "w"). write(q)
    os.startfile(filename,'print')
def reset():
    textarea.delete(1.0,END)
    Bread.set(0)
    Coke.set(0)
    Pizz.set(0)
    Bur.set(0)
    Momo.set(0)
    total.set(0)
    cb.set(' ')
    cob.set(' ')
    pb.set(' ')
    cib.set(' ')
    mocb.set(' ')
    total_cost.set(' ')

def exit():
    if messagebox.askyesno('Exit','Do you really want to Exit'):
        root.destroy()
    
        
        
        
        
        



title=Label(root,text='Billing Management System',bg='pink',fg='white',font=('times new roman',35,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)


#========Product Details=======
F1=LabelFrame(root,text='Product Details',font=('times new roman',18,'bold'),fg='magenta4',bg='pink',relief=RIDGE,bd=15)
F1.place(x=5,y=90,width=800,height=550)

#=====Headings======
item=Label(F1,text='Items',font=('Helvetic',25,'bold','underline'),fg='black',bg='pink')
item.grid(row=0,column=0,padx=20,pady=15)

n=Label(F1,text='Number of Items',font=('Helvetic',25,'bold','underline'),fg='black',bg='pink')
n.grid(row=0,column=1,padx=20,pady=15)

cost=Label(F1,text='Cost of Items',font=('Helvetic',25,'bold','underline'),fg='black',bg='pink')
cost.grid(row=0,column=2,padx=20,pady=15)

#=====Product1=====
bread=Label(F1,text='Bread',font=('times new roman',20,'bold'),fg='deeppink3',bg='pink')
bread.grid(row=1,column=0,padx=20,pady=15)
b_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Bread)
b_txt.grid(row=1,column=1,padx=20,pady=15)
cb_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cb)
cb_txt.grid(row=1,column=2,padx=20,pady=15)
#=====Product2===
coke=Label(F1,text='Coca-Coca',font=('times new roman',20,'bold'),fg='deeppink3',bg='pink')
coke.grid(row=2,column=0,padx=20,pady=15)
c_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Coke)
c_txt.grid(row=2,column=1,padx=20,pady=15)
cob_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cob)
cob_txt.grid(row=2,column=2,padx=20,pady=15)
#=====Product3=======
pizz=Label(F1,text='Pizza',font=('times new roman',20,'bold'),fg='deeppink3',bg='pink')
pizz.grid(row=3,column=0,padx=20,pady=15)
pib_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Pizz)
pib_txt.grid(row=3,column=1,padx=20,pady=15)
pb_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=pb)
pb_txt.grid(row=3,column=2,padx=20,pady=15)
#=====Product4=======
bur=Label(F1,text='Burger',font=('times new roman',20,'bold'),fg='deeppink3',bg='pink')
bur.grid(row=4,column=0,padx=20,pady=15)
bur_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Bur)
bur_txt.grid(row=4,column=1,padx=20,pady=15)
cib_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cib)
cib_txt.grid(row=4,column=2,padx=20,pady=15)
#=====Product5====
momo=Label(F1,text='Momo',font=('times new roman',20,'bold'),fg='deeppink3',bg='pink')
momo.grid(row=5,column=0,padx=20,pady=15)
mob_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Momo)
mob_txt.grid(row=5,column=1,padx=20,pady=15)
mocb_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=mocb)
mocb_txt.grid(row=5,column=2,padx=20,pady=15)

#===Total===
t=Label(F1,text='Total',font=('times new roman',20,'bold'),fg='deeppink3',bg='pink')
t.grid(row=6,column=0,padx=20,pady=15)
ttb_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=total)
ttb_txt.grid(row=6,column=1,padx=20,pady=15)
tttb_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=total_cost)
tttb_txt.grid(row=6,column=2,padx=20,pady=15)
#====bill Area===
F2=Frame(root,relief=GROOVE,bd=10)
F2.place(x=820,y=90,width=430,height=550)
bill_title=Label(F2,text='Receipt',font='arial 15 ',bd=7,relief=GROOVE).pack(fill=X)
scrol=Scrollbar(F2,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15 bold',yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview)
#===BUTTON=====
F3=Frame(root,relief=GROOVE,bd=10,bg='pink')
F3.place(x=5,y=650,width=1245,height=120)
btn1=Button(F3,text='Total',font='arial 25 bold' , bg='yellow',fg='crimson',padx=5,pady=5,command=Total)
btn1.grid(row=0,column=0,padx=20,pady=10)
btn2=Button(F3,text='Receipt',font='arial 25 bold' , bg='yellow',fg='crimson',padx=5,pady=5,command=receipt)
btn2.grid(row=0,column=1,padx=50,pady=10)
btn3=Button(F3,text='Print',font='arial 25 bold' , bg='yellow',fg='crimson',padx=5,pady=5,command=grint)
btn3.grid(row=0,column=2,padx=100,pady=10)
btn4=Button(F3,text='Reset',font='arial 25 bold' , bg='yellow',fg='crimson',padx=5,pady=5,command=reset)
btn4.grid(row=0,column=3,padx=50,pady=10)
btn5=Button(F3,text='Exit',font='arial 25 bold' , bg='yellow',fg='crimson',padx=5,pady=5,command=exit)
btn5.grid(row=0,column=4,padx=100,pady=10)
root.mainloop()
