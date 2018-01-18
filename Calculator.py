# -*- coding: utf-8 -*-

from Tkinter import*

class kalkulator():
    def __init__(self):
        window=Tk()
        window.title('GJ Kalkulator')
        window.minsize(230, 200)
        window.maxsize(230, 200)
        
        # varijable 
        self.operand = ''
        self.broj = 0
        self.memorija = 0
        self.memPamti = 0

        self.screen = StringVar()
        e = Entry(window,textvariable=self.screen, font='Helvetica 14 bold')
        e.grid(row=0, column=0, columnspan=5)

    
        # atributi gumbi
        btnOne = Button(window, text='1', command=self.btn1)
        btnOne.grid(row=2, column=0, ipadx=6,ipady=3)
        btnTwo = Button(window, text='2', command=self.btn2)
        btnTwo.grid(row=2, column=1, ipadx=6,ipady=3)
        btnThree = Button(window, text='3', command=self.btn3)
        btnThree.grid(row=2, column=2, ipadx=6,ipady=3)
        btnFour = Button(window, text='4', command=self.btn4)
        btnFour.grid(row=3, column=0, ipadx=6,ipady=3)
        btnFive = Button(window, text='5', command=self.btn5)
        btnFive.grid(row=3, column=1, ipadx=6,ipady=3)
        btnSix = Button(window, text='6', command=self.btn6)
        btnSix.grid(row=3, column=2, ipadx=6,ipady=3)
        btnSeven = Button(window, text='7', command=self.btn7)
        btnSeven.grid(row=4, column=0, ipadx=6,ipady=3)
        btnEight = Button(window, text='8', command=self.btn8)
        btnEight.grid(row=4, column=1, ipadx=6,ipady=3)
        btnNine = Button(window, text='9', command=self.btn9)
        btnNine.grid(row=4, column=2, ipadx=6,ipady=3)
        btnZero = Button(window, text='0', command=self.btn0)
        btnZero.grid(row=5, column=1, ipadx=6,ipady=3)

        btnSigned = Button(window, text='±', command=self.btsigned)
        btnSigned.grid(row=4, column=4, ipadx=3,ipady=3)

        btnPoint = Button(window, text='.', command=self.btpoint)
        btnPoint.grid(row=5, column=2, ipadx=6,ipady=3)
        btnAbout = Button(window, text='©', font='Helvetica 12 ')
        btnAbout.grid(row=5, column=0, ipadx=2,ipady=1)
        
        # Memory sejv, recall, clear
        memPlus = Button(window, text='M+', command=self.btnmemPlus)
        memRecall = Button(window, text='RM', command=self.btnmemRecall)
        memClear = Button(window, text='CM', command=self.btnmemClear)
        memPlus.grid(row=1, column=0, ipadx=1,ipady=3)
        memRecall.grid(row=1, column=1, ipadx=1,ipady=3)
        memClear.grid(row=1, column=2, ipadx=1,ipady=3)

        # kvadriranje, korijen, clear
        xOverX = Button(window, text='x²', command=self.btxoverx)
        hHalf = Button(window, text='√', command=self.btsqrt)
        btnClear = Button(window, text='C', command=self.clearscr)
        xOverX.grid(row=3, column=4, ipadx=3,ipady=3)
        hHalf.grid(row=2, column=4, ipadx=3,ipady=3)
        btnClear.grid(row=1, column=3, ipadx=5,ipady=3)

        # Funkcije
        Sumy = Button(window, text='+', command=self.sumy)
        Subtract = Button(window, text='-', command=self.btsubtract)
        Multiply = Button(window, text='*', command=self.btMultiply)
        Divide = Button(window, text='/', command=self.btDivide)
        Sumy.grid(row=5, column=3, ipadx=4,ipady=3)
        Subtract.grid(row=4, column=3, ipadx=6,ipady=3)
        Multiply.grid(row=3, column=3, ipadx=6,ipady=3)
        Divide.grid(row=2, column=3, ipadx=6,ipady=3)

        Equals = Button(window, text='=', command=self.eq)
        Equals.grid(row=5, column=4, ipadx=3,ipady=3)
        
        window.mainloop()
    # Gumbi
    def btpoint(self):
        self.screen.set(self.screen.get()+(str('.')))
        
    def btsigned(self):
        self.current = -(float(self.screen.get()))
        self.screen.set(self.current)
  
    def btn1(self):
        self.screen.set(self.screen.get()+(str(1)))
    def btn2(self):
        self.screen.set(self.screen.get()+(str(2)))
    def btn3(self):
        self.screen.set(self.screen.get()+(str(3)))
    def btn4(self):
        self.screen.set(self.screen.get()+(str(4)))
    def btn5(self):
        self.screen.set(self.screen.get()+(str(5)))
    def btn6(self):
        self.screen.set(self.screen.get()+(str(6)))
    def btn7(self):
        self.screen.set(self.screen.get()+(str(7)))
    def btn8(self):
        self.screen.set(self.screen.get()+(str(8)))
    def btn9(self):
        self.screen.set(self.screen.get()+(str(9)))
    def btn0(self):
        self.screen.set(self.screen.get()+(str(0)))
        
    # Memorija
    def btnmemPlus(self):
        self.memorija += float (self.screen.get())
        self.memPamti + self.memorija
        self.screen.set(self.memPamti)
        #self.memorija += float(self.screen.get())
        #self.screen.set(self.memorija)
    def btnmemRecall(self):
        self.screen.set(self.memorija)    
    def btnmemClear(self):
        self.memorija= float(self.memorija)/float(self.memorija)-1.0
        
    def clearscr(self):
        self.screen.set('')

    def sumy(self):
        self.operand = '+'              
        self.broj = self.screen.get()   
        self.screen.set('')             

    def btsubtract(self):
        self.operand = '-'              
        self.broj = self.screen.get()   
        self.screen.set('')

    def btMultiply(self):
        self.operand = '*'              
        self.broj = self.screen.get()   
        self.screen.set('')

    def btDivide(self):
        self.operand = '/'              
        self.broj = self.screen.get()   
        self.screen.set('') 

    def btxoverx(self):
        self.operand = 'x²'              
        self.broj = self.screen.get()   
        if self.operand == 'x²':
            operationResult = float(self.broj) **2
        self.screen.set(operationResult)
        
    def btsqrt(self):
        self.operand = '√'              
        self.broj = self.screen.get()   
        if self.operand == '√':
            operationResult = float(self.broj) **0.5
        self.screen.set(operationResult)

    def eq(self):
        self.screen.set(self.operation())
        self.operand = ''

    def operation(self):
        if self.operand == '+':
            drugiBroj = self.screen.get()
            operationResult = float(self.broj) + float(drugiBroj)
            return operationResult
        if self.operand == '*':
            drugiBroj = self.screen.get()
            operationResult = float(self.broj) * float(drugiBroj)
            return operationResult
        if self.operand == '-':
            drugiBroj = self.screen.get()
            operationResult = float(self.broj) - float(drugiBroj)
            return operationResult
        if self.operand == '/':
            drugiBroj = self.screen.get()
            operationResult = float(self.broj) / float(drugiBroj)
            return operationResult
             
kalkulator()
