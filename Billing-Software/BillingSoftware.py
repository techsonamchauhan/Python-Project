from tkinter import*
import math,random,os
from tkinter import messagebox
class Billing_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #============variable============
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_shampoo=IntVar()
        self.hair_oil=IntVar()
        self.body_wash=IntVar()

        #=============Grocery=======
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.pulses=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        #============Cold Drinks======
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        #==============Total Product Price & Tax Variable===
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        #========Customer======
        self.c_name=StringVar()
        self.c_phon=StringVar()

        self.bill_no=StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

        #=============Customer Detail Frame
        F1= LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15,textvariable=self.c_phon, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15,textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)


        #==============Cosmetic Frame============
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=190,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Face_cream_txt = Entry(F2, width=10,textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        Face_wash_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Face_wash_txt = Entry(F2, width=10,textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        Shampoo_lbl = Label(F2, text="Hair Shampoo", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Shampoo_txt = Entry(F2, width=10,textvariable=self.hair_shampoo, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        Hair_oil_lbl = Label(F2, text="Hair Oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Hair_oil_txt = Entry(F2, width=10,textvariable=self.hair_oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        Body_wash_lbl = Label(F2, text="Body Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Body_wash_txt = Entry(F2, width=10,textvariable=self.body_wash, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

        # ==============Grocery Frame============
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F3.place(x=340, y=190, width=325, height=380)

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10,textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        g2_lbl = Label(F3, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10,textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl = Label(F3, text="Pulses", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10,textvariable=self.pulses, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10,textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10,textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10,textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # ==============Cold Drink Frame============
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drink", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F4.place(x=675, y=190, width=325, height=380)

        c1_lbl = Label(F4, text="Maza", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        c1_txt = Entry(F4, width=10,textvariable=self.maza, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        c2_lbl = Label(F4, text="Cock", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10,textvariable=self.cock, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10,textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        c4_lbl = Label(F4, text="Thumbs Up", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=10,textvariable=self.thumbsup, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        c5_txt = Entry(F4, width=10,textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F4, width=10,textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)# ==============Grocery Frame============

        #============Bill Area=======

        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=190, width=400, height=380)

        bill_title = Label(F5,text="Bill Area", font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        # F7 = Frame(self.root, bd=10, relief=GROOVE)
        # F7.place(x=1415, y=190, width=125, height=380)
        #
        # path = "C:/Users/user/OneDrive/Desktop/New folder (2)/1.jpg"
        # img = ImageTk.PhotoImage(Image.open(path))
        # L23 = Label(F7, image=img)
        # L23.pack()

         #-------------Button--------------------
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F6.place(x=0, y=580, relwidth=1, height=140)

        m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1,column=0, padx=20, pady=1,sticky="w")
        m2_txt = Entry(F6, width=18,textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2,column=0, padx=20, pady=1,sticky="w")
        m3_txt = Entry(F6, width=18,textvariable=self.cold_drink_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        m4_lbl = Label(F6, text="Cosmetic Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        m4_txt = Entry(F6, width=18,textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        m5_lbl = Label(F6, text="Grocery Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        m5_txt = Entry(F6, width=18,textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        m6_lbl = Label(F6, text="Cold Drinks Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        m6_txt = Entry(F6, width=18,textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)


        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",pady=15,bd=5,width=11,font="arial 12 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn = Button(btn_F, text="Genrate Bill",command=self.bill_area, bg="cadetblue", fg="white", pady=15, bd=5, width=11,font="arial 12 bold").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_F, text="Clear",command=self.clear_data, bg="cadetblue", fg="white", pady=15, bd=5, width=11,font="arial 12 bold").grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_F, text="Exit",command=self.Exit_app, bg="cadetblue", fg="white", pady=15, bd=5, width=11,font="arial 12 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()


    def total(self):
            self.c_s_p=  self.soap.get() * 40
            self.c_fc_p= self.face_cream.get() * 120
            self.c_fw_p= self.face_wash.get() * 60
            self.c_hs_p= self.hair_shampoo.get() * 180
            self.c_ho_p= self.hair_oil.get() * 140
            self.c_bw_p= self.body_wash.get() * 180

            self.total_cosmetic_Price=float(
                                         self.c_s_p+
                                         self.c_fc_p+
                                         self.c_fw_p+
                                         self.c_hs_p+
                                         self.c_ho_p+
                                         self.c_bw_p

                                         )
            self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_Price))
            self.c_tax=round((self.total_cosmetic_Price*0.05),2)
            self.cosmetic_tax.set("Rs. "+str(self.c_tax))

            self.g_r_p = self.rice.get() * 80
            self.g_fo_p = self.food_oil.get() * 120
            self.g_pl_p = self.pulses.get() * 140
            self.g_s_p =  self.sugar.get() * 100
            self.g_w_p = self.wheat.get() * 150
            self.g_t_p = self.tea.get() * 60


            self.total_Grocery_price = float(
                                         self.g_r_p+
                                         self.g_fo_p+
                                         self.g_pl_p+
                                         self.g_s_p+
                                         self.g_w_p+
                                         self.g_t_p
                                         )
            self.grocery_price.set("Rs. "+str(self.total_Grocery_price))
            self.g_tax = round((self.total_Grocery_price*0.1),2)
            self.grocery_tax.set("Rs. "+str(self.g_tax))

            self.d_s_p = self.sprite.get() * 40
            self.d_c_p = self.cock.get() * 40
            self.d_m_p = self.maza.get() * 60
            self.d_l_p = self.limca.get() * 90
            self.d_t_p = self.thumbsup.get() * 100
            self.d_f_p = self.frooti.get() * 120

            self.total_drinks_price = float(
                                         self.d_s_p+
                                         self.d_c_p+
                                         self.d_m_p+
                                         self.d_l_p+
                                         self.d_t_p+
                                         self.d_f_p

                                        )
            self.cold_drink_price.set("Rs. "+str(self.total_drinks_price))
            self.d_tax = round((self.total_drinks_price*0.05),2)
            self.cold_drink_tax.set("Rs. "+str(self.d_tax))

            self.Total_bill=float(  self.total_cosmetic_Price+
                                    self.total_Grocery_price+
                                    self.total_drinks_price+
                                    self.c_tax+
                                    self.g_tax+
                                    self.d_tax
                                 )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Webcode Reatil\n")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END, f"\n=========================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n=========================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error","Customer details are must")

        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            #======cosmetics=======
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")

            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")


            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")

            if self.hair_oil.get()!=0:
                self.txtarea.insert(END,f"\n Hair Oil\t\t{self.hair_oil.get()}\t\t{self.c_ho_p}")

            if self.hair_shampoo.get()!=0:
                self.txtarea.insert(END,f"\n Hair Shampoo\t\t{self.hair_shampoo.get()}\t\t{self.c_hs_p}")

            if self.body_wash.get()!=0:
                self.txtarea.insert(END,f"\n Body Wash\t\t{self.body_wash.get()}\t\t{self.c_bw_p}")

            #==========Grocery=========
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")

            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")

            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")

            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")

            if self.pulses.get()!=0:
                self.txtarea.insert(END,f"\n Pulses\t\t{self.pulses.get()}\t\t{self.g_w_p}")

            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")


            #==========Cold Drink=======

            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")

            if self.thumbsup.get()!=0:
                self.txtarea.insert(END,f"\n ThumbsUp\t\t{self.thumbsup.get()}\t\t{self.d_t_p}")

            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")

            if self.cock.get()!=0:
                self.txtarea.insert(END,f"\n Cock\t\t{self.cock.get()}\t\t{self.d_c_p}")

            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t\t{self.d_m_p}")

            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")

            self.txtarea.insert(END, f"\n-----------------------------------------")
            if self.cosmetic_tax.get()!= "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cosmetic Tax\t\t\t\t{self.cosmetic_tax.get()}")

            if self.grocery_tax.get()!= "Rs. 0.0":
                self.txtarea.insert(END, f"\n Grocery Tax\t\t\t\t{self.grocery_tax.get()}")

            if self.cold_drink_tax.get()!= "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cold Drink Tax\t\t\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END, f"\n Total Bill\t\t\t\tRs. {self.Total_bill}")
            self.txtarea.insert(END, f"\n-----------------------------------------")
            self.save_bill()


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/" +str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} saved Successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present== "no" :
            messagebox.showerror("Error","Invalid Bsill No.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear?")
        if op > 0:

            # ============variable============
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_shampoo.set(0)
            self.hair_oil.set(0)
            self.body_wash.set(0)

            # =============Grocery=======
            self.rice.set(0)
            self.food_oil.set(0)
            self.pulses.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            # ============Cold Drinks======
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            # ==============Total Product Price & Tax Variable===
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            # ========Customer======
            self.c_name.set("")
            self.c_phon.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()

root=Tk()
obj = Billing_App(root)
root.mainloop()

