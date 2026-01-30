from customtkinter import *
from tkinter import messagebox
import tkinter as tk

root = CTk()

root.geometry('800x500+100+100')
root.title('Login')

frame = CTkFrame(root,width=350,height=400,fg_color='#222')
frame.place(x=220,y=20)

lbl_Login = CTkLabel(root,text='Login',fg_color='#222',font=('arial',24,'bold'),text_color='#eee')
lbl_Login.place(x=350,y=50)

var1 = StringVar()
inp_user = CTkEntry(root,width=250,placeholder_text='user',textvariable=var1)
inp_user.place(x=250,y=150)

var2 = StringVar()
inp_pw = CTkEntry(root,width=250,placeholder_text='password',textvariable=var2,show='*')
inp_pw.place(x=250,y=200)

def open():
    win1 = CTkToplevel(root)
    win1.geometry('800x500+100+100')
    win1.title('liste du tache')

    lbl_Dash = CTkLabel(win1,text='Liste du tache',fg_color='#000',text_color='#fff',font=('arial',20,'bold'))
    lbl_Dash.pack(fill=X)
    
    fram2 = CTkFrame(win1,width=400,height=300,fg_color='gray')
    fram2.place(x=300,y=50)
    list_box = tk.Listbox(win1,selectbackground='green',selectforeground='yellow',font=('arila',16,'bold'))
    list_box.place(x=20,y=50)
    list_box.insert(END,'Ajouter tache')
    list_box.insert(END,'Supprimer tache')
    list_box.insert(END,'Afficher Les taches')

    # add 
    var_add = StringVar()
    tasks = []
    def add_Btn():
        tache = var_add.get()
        if tache.strip() == '':
            lbl_res_add.configure(text='please ajouter un tache')
            return
        else:
            tasks.append(tache)
            lbl_res_add.configure(text='bien ajouter')
            var_add.set('')
          
    lbl_ajouter = CTkLabel(win1,text='ajouter un tache',fg_color='gray')
    inp_tache_add = CTkEntry(win1,placeholder_text='entre un tache',textvariable=var_add)
    btn_add = CTkButton(win1,text='add',command=add_Btn)
    lbl_res_add = CTkLabel(win1,text='')

    #supprimer
    var_supp = StringVar()
    def supp():
        tache_supp = var_supp.get()
        if tache_supp in tasks:
            tasks.remove(tache_supp)
            lbl_res_del.configure(text='bien supprimer')
        elif tache_supp == '':
            lbl_res_del.configure(text='please supprimer un tache')
        else:
            lbl_res_del.configure(text='ne trouver pas')

        var_supp.set('')

    lbl_supp = CTkLabel(win1,text='supprimer un tache',fg_color='gray')
    inp_tache_supp = CTkEntry(win1,placeholder_text='supprimer un tache',textvariable=var_supp)
    btn_del = CTkButton(win1,text='supp',command=supp)
    lbl_res_del = CTkLabel(win1,text='')

    #afficher
    def aff():
        list_aff.delete(0,END)
        for t in tasks:
            list_aff.insert(END,t)
        if not tasks:
            list_aff.insert(END,'aucun tache')
    # supp dans la list
    def supp_list():
        index = list_aff.curselection()[0]
        del tasks[index]
        list_aff.delete(index)

    # supp All dans la list
    def supp_list_all():
        list_aff.delete(0,END)
        tasks.clear()

    lbl_aff = CTkLabel(win1,text='afficher un tache',fg_color='gray')
    list_aff = tk.Listbox(win1,width=60)
    btn_aff = CTkButton(win1,text='afficher',command=aff)
    btn_list_del = CTkButton(win1,text='supprimer',command=supp_list)
    btn_list_del_all = CTkButton(win1,text='supp all',command=supp_list_all)
    
    def add():
        deleteAll()
        lbl_ajouter.place(x=450,y=70)
        inp_tache_add.place(x=350,y=100)
        btn_add.place(x=500,y=100)
        lbl_res_add.place(x=350,y=200)

    def deleteEmp():
        deleteAll()
        lbl_supp.place(x=450,y=70)
        inp_tache_supp.place(x=350,y=100)
        btn_del.place(x=500,y=100)
        lbl_res_del.place(x=350,y=200)

    def affEmp():
        deleteAll()
        lbl_aff.place(x=450,y=70)
        list_aff.place(x=320,y=100)
        btn_aff.place(x=450,y=300)
        btn_list_del.place(x=320,y=300)
        btn_list_del_all.place(x=550,y=300)
    

    def deleteAll():
        # add
        lbl_ajouter.place_forget()
        inp_tache_add.place_forget()
        btn_add.place_forget()
        lbl_res_add.place_forget()
        # supp
        lbl_supp.place_forget()
        inp_tache_supp.place_forget()
        btn_del.place_forget()
        lbl_res_del.place_forget()
        # aff
        lbl_aff.place_forget()
        list_aff.place_forget()
        btn_aff.place_forget()
        btn_list_del.place_forget()
        btn_list_del_all.place_forget()
    
    def select_list(e):
        x = list_box.curselection()
        if not x:
            return
        index = x[0]
        if index == 0:
            add()
        elif index == 1:
            deleteEmp()
        elif index == 2:
            affEmp()

    list_box.bind('<<ListboxSelect>>',select_list)

def send():
    if var1.get() == 'admin' and var2.get() == '1234':
        open()
        root.withdraw()
    elif var1.get() == '' and var2.get() == '':
        messagebox.showwarning('entre un user or pw')
    else:
        messagebox.showwarning('invalid')

btn_Login = CTkButton(root,text='Login',command=send,fg_color='#eee',text_color='gray',font=('arial',20,'bold'),hover_color='#000',bg_color='black')
btn_Login.place(x=320,y=300)











root.mainloop()