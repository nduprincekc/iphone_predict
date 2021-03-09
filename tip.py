from tkinter import Label,IntVar,Entry,Button,Radiobutton,Tk,StringVar


class TipCalculator():
    def __init__(self):
        window = Tk()
        window.geometry('320x220')

        window.title('tip calculator')
        window.config(background = 'gray')

        window.resizable(width=False,height=False)
        self.meal_cost = StringVar()
        self.tip_percent = IntVar()
        self.tip = StringVar()
        self.total_cost = StringVar()



        tip_percent = Label(window, text='Tip percentage', bg='purple', fg='white')
        tip_percent.grid(column=0, row=0, pady=5, padx=5)

        bills_amount = Label(window, text='Bills Amount', bg='purple', fg='white')
        bills_amount.grid(column=1, row=0, pady=5, padx=9)

        bills_amount_entry = Entry(window,textvariable=self.meal_cost,width=14)
        bills_amount_entry.grid(column=2, row=0)



        five_percent_tip = (Radiobutton(window,text ='0.5%', variable = self.tip_percent,value= 5))
        five_percent_tip.grid(column=0 , row = 1)

        ten_percent_tip = (Radiobutton(window,text ='0.5%', variable = self.tip_percent,value= 10,bg = 'red'))
        ten_percent_tip.grid(column=0 , row = 2)

        fiftheen_percent_tip = (Radiobutton(window,text ='0.5%', variable = self.tip_percent,value= 15))
        fiftheen_percent_tip.grid(column=0 , row = 3)

        twenty_percent_tip = (Radiobutton(window,text ='0.5%', variable = self.tip_percent,value= 20,bg='blue'))
        twenty_percent_tip.grid(column=0 , row = 4)

        twenty_five_percent_tip = (Radiobutton(window,text ='0.5%', variable = self.tip_percent,value= 25))
        twenty_five_percent_tip.grid(column=0 , row = 5)

        Thirty_percent_tip = (Radiobutton(window,text ='0.5%', variable = self.tip_percent,value= 30, bg='green'))
        Thirty_percent_tip.grid(column=0 , row = 6)

        tip_amount_lbl = Label(window,text='Tip Amount',bg='brown',fg='white')
        tip_amount_lbl.grid(column=1,row=2,padx=15)

        tip_amount_entry = Entry(window, text='Tip Amount', bg='white',textvariable=self.total_cost, fg='white',width=14)
        tip_amount_entry.grid(column=2, row=2, )

        cal_btn= Button(window,text='calculate',bg='green',fg='white',command=self.cal())
        cal_btn.grid(row=4,column=1)

        clear_btn= Button(window,text='clear',bg='green',fg='white',command='')
        clear_btn.grid(row=4,column=2)


        design=Label(window, text='Design by kc emma ')
        design.grid(row=6,column=1,)


        window.mainloop()



    def cal(self):
        pre_tip = float(self.meal_cost.get())
        percentage = self.tip_percent.get() / 100
        tip_amount_entry=pre_tip * percentage
        self.tip.set(tip_amount_entry)

        final_bill = pre_tip + tip_amount_entry
        self.total_cost.set(final_bill)

TipCalculator()
