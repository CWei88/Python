import tkinter as tk
from tkinter import ttk

import CAP_calc_classes as ccc

grade_entry = []
credit_entry = []
uni = None

def popupmsg(string, title):
    popup = tk.Tk()
    popup.tk.call('tk','scaling',2.0)

    #title of popup
    popup.wm_title(title)
    label = ttk.Label(popup, text = string, font = ("Segoe UI", 12), anchor="center")
    label.pack(side = "top", fill = "x", pady=10)

    #button to click in popup
    b1 = ttk.Button(popup, text = "Ok", command = popup.destroy)
    b1.pack()
    popup.mainloop()

def getGrades(entry):

    res = entry.get()
    res = res.strip()
    res = res.split(",")
    res = list(map(lambda x: x.upper(), res))
    return res

def getCredits(entry):

    res = entry.get()
    res = res.strip()
    res = res.split(",")
    res = list(map(lambda x: int(x), res))
    return res

def previousButton(controller, entry1, entry2, page, prevPage):
    global grade_entry
    global credit_entry

    if not entry1.get():
        return controller.show_frame(prevPage)
    elif not entry2.get():
        return controller.show_frame(prevPage)

    grade = getGrades(entry1)
    credit = getCredits(entry2)

    if len(grade_entry) < page:
        grade_entry.append(grade)
    else:
        grade_entry[page - 1] = grade

    if len(credit_entry) < page:
        credit_entry.append(credit)
    else:
        credit_entry[page - 1] = credit
    
    return controller.show_frame(prevPage) 

def nextButton(controller, entry1, entry2, page, nextPage):
    global grade_entry
    global credit_entry
        
    if not entry1.get():
        return popupmsg("Please input your grades for the year and semester.", "Error: Input not detected")
    elif not entry2.get():
        return popupmsg("Please input your credits for the year and semester.", "Error: Input not detected")
        
    grade = getGrades(entry1)
    credit = getCredits(entry2)

    if len(grade_entry) < page:
        grade_entry.append(grade)
    else:
        grade_entry[page - 1] = grade

    if len(credit_entry) < page:
        credit_entry.append(credit)
    else:
        credit_entry[page - 1] = credit
    
    return controller.show_frame(nextPage)

def finishButton(controller, entry1, entry2, page):
    global grade_entry
    global credit_entry
    
    if not entry1.get():
        return popupmsg("Please input your grades for the year and semester.", "Error: Input not detected")
    elif not entry2.get():
        return popupmsg("Please input your credits for the year and semester.", "Error: Input not detected")

    grade = getGrades(entry1)
    credit = getCredits(entry2)

    if len(grade_entry) < page:
        grade_entry.append(grade)
    else:
        grade_entry[page - 1] = grade

    if len(credit_entry) < page:
        credit_entry.append(credit)
    else:
        credit_entry[page - 1] = credit
        
    return controller.show_frame(FinalPage)


class CAPCalc(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.tk.call('tk', 'scaling', 2.0)

        tk.Tk.wm_title(self, "CAP Calculator")
        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight = 1)

        menubar = tk.Menu(container)

        filemenu = tk.Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "About", command = lambda: popupmsg('''Version 0.3.0 Beta.\n This software may be buggy, please use it at your own discretion.''', "Version"))
        filemenu.add_command(label = "Quit", command = quit)

        menubar.add_cascade(label = "File", menu = filemenu)

        tk.Tk.config(self, menu=menubar)

        self.frames = {}
        for fr in (StartPage, Y1S1, Y1S2, FinalPage):
            frame = fr(container, self)

            self.frames[fr] = frame

            frame.grid(row=0, column=0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text = "Please choose your university.")
        label.config(font = ("Segoe UI", 14))

        label.pack()

        #Adds a button to select the page
        button1 = ttk.Button(self, text = "NUS", command=lambda: self.uni_choice("NUS", self.controller))
        button1.pack()
        
        button2 = ttk.Button(self, text = "NTU", command=lambda: self.uni_choice("NTU", self.controller))
        button2.pack()

        button3 = ttk.Button(self, text = "SMU", command=lambda: self.uni_choice("SMU", self.controller))
        button3.pack()

    def uni_choice(self, univ, controller):
        global uni
        uni = univ
        return controller.show_frame(Y1S1)

class Y1S1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label0 = tk.Label(self, text="Year 1 Semester 1")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = tk.Label(self, text="Please enter your grades, seperated by commas.")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self)
        entry1.pack()
        
        label2 = tk.Label(self, text = "Please enter your credits per module, seperated by commas.")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()
        
        entry2 = ttk.Entry(self)
        entry2.pack()

        button1 = ttk.Button(self, text = "< Previous", command = lambda: previousButton(self.controller, entry1, entry2, 1, StartPage))
        button1.pack(side='left', fill='x')

        button2 = ttk.Button(self, text="Next >", command=lambda: nextButton(self.controller, entry1, entry2, 1, Y1S2))
        button2.pack(side='right', fill='x')

        button3 = ttk.Button(self, text="Finish", command=lambda: finishButton(self.controller, entry1, entry2, 1))
        button3.pack(side = 'top')


class Y1S2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label0 = tk.Label(self, text="Year 1 Semester 2")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = tk.Label(self, text="Please enter your grades, seperated by commas.")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self)
        entry1.pack()

        label2 = tk.Label(self, text = "Please enter your credits per module, seperated by commas.")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        entry2 = ttk.Entry(self)
        entry2.pack()

        button1 = ttk.Button(self, text = "Previous <", command = lambda: previousButton(self.controller, entry1, entry2, 2, Y1S1))
        button1.pack(side = "left")

        button2 = ttk.Button(self, text="Next >", command=lambda: nextButton(self.controller, entry1, entry2, 2, Y2S1))
        button2.pack(side = "right")

        button3 = ttk.Button(self, text="Finish", command=lambda: finishButton(self.controller, entry1, entry2, 2))
        button3.pack(side = "top")

class Y2S1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label0 = tk.Label(self, text="Year 2 Semester 1")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = tk.Label(self, text="Please enter your grades, seperated by commas.")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self)
        entry1.pack()

        label2 = tk.Label(self, text = "Please enter your credits per module, seperated by commas.")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        entry2 = ttk.Entry(self)
        entry2.pack()

        button1 = ttk.Button(self, text = "Previous <", command = lambda: previousButton(self.controller, entry1, entry2, 3, Y1S2))
        button1.pack(side = "left")

        button2 = ttk.Button(self, text="Next >", command=lambda: nextButton(self.controller, entry1, entry2, 3, Y2S2))
        button2.pack(side = "right")

        button3 = ttk.Button(self, text="Finish", command=lambda: finishButton(self.controller, entry1, entry2, 3))
        button3.pack(side = "top")


class FinalPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label1 = tk.Label(self, text="Your estimated GPA is: ")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        button1 = ttk.Button(self, text="Calculate", command=lambda: self.calculate(button1))
        button1.pack()
        
    def calculate(self, but):
        global uni
        global grade_entry
        global credit_entry
        all_results = []
        
        res = ccc.CAPCalc(uni)
        for grade, credit in zip(grade_entry, credit_entry):
            graded = res.sem_grades(grade, credit)
            all_results.append(graded)
        print(all_results)
            
        final = res.grade_count(all_results)

        label2 = tk.Label(self, text = str(final))
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        but.destroy()

        grade_entry.clear()
        credit_entry.clear()
        

        

app = CAPCalc()
app.geometry("1280x720")
app.mainloop()



        
    
