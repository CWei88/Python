import tkinter as tk
from tkinter import ttk

import CCmain as ccm

grade_entry = {}
credit_entry = {}
uni = None
page_entry = []
init_gpa = 0.0
bef_credit = 0
this_sem_grades = []
this_sem_credits = []

###################
###Program Start###
###################

def quit():
    exit(0)

def popupmsg(string, title):
    popup = tk.Tk()
    popup.tk.call('tk','scaling',2.0)

    #title of popup
    popup.wm_title(title)
    label = ttk.Label(popup, text = string, font = ("Segoe UI", 10), justify="center")
    label.pack(side = "top", fill = "both", pady=10)
    label.configure

    #button to click in popup
    b1 = ttk.Button(popup, text = "Ok", command = popup.destroy)
    b1.pack()
    popup.mainloop()

def abtMenu():
    root = tk.Tk()
    root.tk.call('tk','scaling', 2.0)
    root.resizable(0,0)

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side = "right", fill = "y")

    text = tk.Text(root, height=20, width=85)
    text.pack(side = "left")
    text.tag_configure('big', font=('Helvetica', 20, 'bold'))
    text.tag_configure('heading', font=('Helvetica', 14, 'bold'))
    text.tag_configure('body', font=('Helvetica', 10))
    text.tag_configure('center', justify='center')

    text.insert(tk.END, 'About \n', ['big', 'center'])
    text.insert(tk.END, '\nVersion 0.9.5 \n', 'heading')
    text.insert(tk.END, 'This is a beta version of this application and thus may be buggy. \nPlease use it with caution.', 'body')
    text.insert(tk.END, '\n \nChangelog', 'heading')
    ans2= '''
- Added a new page to the SU Calculator
- SU Calculator now gives basic functionality of SUing subjects with same credits.
- SU Calculator may not work for different credits across modules.
'''
    text.insert(tk.END, ans2, 'body')
    
    text.insert(tk.END, '\nVersion 0.8.0 \n', 'heading')
    text.insert(tk.END, '\n \nChangelog', 'heading')
    ans1= '''
- Edited errors so that they are more informative.
- Added basic functionality for a SU Calculator.
- Some errors now appear on the main Semester page instead when hitting the Calculate button.
- Remove duplicate CAP when editing Semester results.
- Added a Changelog.'''

    text.insert(tk.END, ans1, 'body')

    root.mainloop()


def helpMenu():
    root = tk.Tk()
    root.tk.call('tk','scaling',2.0)

    #Adding scrollbar
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side = "right", fill = "y")

    #Adding text widget and configuring the tags
    text1 = tk.Text(root, height=50, width=150)
    text1.pack(side = "left")
    text1.tag_configure('big', font=('Helvetica', 20, 'bold'))
    text1.tag_configure('heading', font=('Helvetica', 14, 'bold'))
    text1.tag_configure('body', font=('Helvetica', 10))
    text1.tag_configure('center', justify='center')

    text1.insert(tk.END, '\nHELP \n', ['big', 'center'])
    text1.insert(tk.END, '\n \nHow does this app work? \n', 'heading')

    ans1 = '''
This app works by calculating your grades and credits from each module respectively.
By inputting your grades, it will use what you have to calculate your CAP/GPA.
Ensure that the grade that you input corresponds to your grade.
For example, if you scored A for a 4 credits module and B for a 2 credist module, the input will be: a,b for grades and 4,2 for credits.
Or else this may result in your GPA not being calculated properly. \n
'''

    text1.insert(tk.END, ans1, 'body')

    text1.insert(tk.END, 'Help! The app looks blurry. \n', 'heading')

    ans2 = '''
This is due to Windows scale and layout. You can either change the scale in the Display Settings to 100%.
Alternatively, right click on the app, select Properties, Compatibility, Change high DPI Settings.
Check the box under High DPI Scaling Override and click Apply.
'''
    text1.insert(tk.END, ans2, 'body')

    root.mainloop()

def getGrades(entry):
    res = entry.get()
    if res:
        res = res.strip()
        res = res.split(",")
        res = list(map(lambda x: x.upper(), res))
        return res

def getCredits(entry):
    res = entry.get()
    if res:
        res = res.strip()
        res = res.split(",")
        try:
            res = list(map(lambda x: int(x), res))
        except ValueError:
            return popupmsg("Credit input cannot contain non-integers. Please try again.", "Non-Integer Error")
        except Exception:
            return popupmsg("An unexpected error occurred. Please try again.", "Unexpected Error")
        return res

def previousButton(controller, entry1, entry2, key, prevPage):
    global grade_entry
    global credit_entry

    grade = getGrades(entry1)
    credit = getCredits(entry2)

    if grade and credit:
        if len(grade) > len(credit):
            return popupmsg("You have entered more grades than the number of credited modules. \nPlease try again.", "Non-tally Error")
        elif len(credit) > len(grade):
            return popupmsg("You have entered more number of credited modules than the number of grades. \nPlease try again.", "Non-tally Error")

        grade_entry[key] = grade
        credit_entry[key] = credit
    
    return controller.show_frame(prevPage) 

def nextButton(controller, entry1, entry2, key, nextPage):
    global grade_entry
    global credit_entry
    global page_entry
        
    grade = getGrades(entry1)
    credit = getCredits(entry2)

    if grade and credit:
        if len(grade) > len(credit):
            return popupmsg("You have entered more grades than the number of credited modules. \nPlease try again.", "Non-tally Error")
        elif len(credit) > len(grade):
            return popupmsg("You have entered more number of credited modules than the number of grades. \nPlease try again.", "Non-tally Error")

        grade_entry[key] = grade
        credit_entry[key] = credit
        
    page_entry.append(page_dict[key])
    
    return controller.show_frame(nextPage)

def finishButton(controller, entry1, entry2, key):
    global grade_entry
    global credit_entry
    global page_entry
    
    grade = getGrades(entry1)
    credit = getCredits(entry2)
    if grade and credit:
        if len(grade) > len(credit):
            return popupmsg("You have entered more grades than the number of credited modules. \nPlease try again.", "Non-tally Error")
        elif len(credit) > len(grade):
            return popupmsg("You have entered more number of credited modules than the number of grades. \nPlease try again.", "Non-tally Error")

        grade_entry[key] = grade
        credit_entry[key] = credit
        
    page_entry.append(page_dict[key])
        
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
        filemenu.add_command(label = "About", command = lambda: abtMenu())
        filemenu.add_command(label = "Quit", command = quit)

        menubar.add_cascade(label = "File", menu = filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label = "Help", command = lambda: helpMenu())

        menubar.add_cascade(label = "Help", menu = helpmenu)

        tk.Tk.config(self, menu=menubar)

        self.frames = {}
        for fr in (StartPage, CAPorSU, Y1S1, Y1S2, Y2S1, Y2S2, Y3S1, Y3S2, Y4S1, Y4S2, SUCalc, SUable, FinalPage):
            frame = fr(container, self)

            self.frames[fr] = frame

            frame.grid(row=0, column=0, sticky = "nsew")

        self.show_frame(StartPage)

        tk.Tk.iconbitmap(self, default = "CCicon.ico")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text = "Please choose your university.", justify="center")
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
        return controller.show_frame(CAPorSU)

class CAPorSU(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text = "What would you like to do?", justify="center")
        label.config(font = ("Segoe UI", 14))
        label.pack()

        button1 = ttk.Button(self, text = "CAP Calculator", command=lambda: controller.show_frame(Y1S1))
        button1.pack()

        button2 = ttk.Button(self, text = "SU Calculator", command=lambda: controller.show_frame(SUCalc))
        button2.pack()

class Y1S1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label0 = ttk.Label(self, text="Year 1 Semester 1", justify="center")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = ttk.Label(self, text="Please enter your grades, seperated by commas.", justify="center")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self, justify="center")
        entry1.pack()
        
        label2 = ttk.Label(self, text = "Please enter your credits per module, seperated by commas.", justify="center")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()
        
        entry2 = ttk.Entry(self, justify="center")
        entry2.pack()

        button1 = ttk.Button(self, text = "< Previous", command = lambda: previousButton(self.controller, entry1, entry2, "Y1S1", StartPage))
        button1.pack(side='left', fill='x')

        button2 = ttk.Button(self, text="Next >", command=lambda: nextButton(self.controller, entry1, entry2, "Y1S1", Y1S2))
        button2.pack(side='right', fill='x')

        button3 = ttk.Button(self, text="Finish", command=lambda: finishButton(self.controller, entry1, entry2, "Y1S1"))
        button3.pack(side = 'top')


class Y1S2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label0 = tk.Label(self, text="Year 1 Semester 2", justify="center")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = tk.Label(self, text="Please enter your grades, seperated by commas.", justify="center")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self, justify="center")
        entry1.pack()

        label2 = tk.Label(self, text = "Please enter your credits per module, seperated by commas.", justify="center")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        entry2 = ttk.Entry(self, justify="center")
        entry2.pack()

        button1 = ttk.Button(self, text = "Previous <", command = lambda: previousButton(self.controller, entry1, entry2, "Y1S2", Y1S1))
        button1.pack(side = "left")

        button2 = ttk.Button(self, text="Next >", command=lambda: nextButton(self.controller, entry1, entry2, "Y1S2", Y2S1))
        button2.pack(side = "right")

        button3 = ttk.Button(self, text="Finish", command=lambda: finishButton(self.controller, entry1, entry2, "Y1S2"))
        button3.pack(side = "top")

class Y2S1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label0 = tk.Label(self, text="Year 2 Semester 1", justify="center")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = tk.Label(self, text="Please enter your grades, seperated by commas.", justify="center")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self, justify="center")
        entry1.pack()

        label2 = tk.Label(self, text = "Please enter your credits per module, seperated by commas.", justify="center")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        entry2 = ttk.Entry(self, justify="center")
        entry2.pack()

        button1 = ttk.Button(self, text = "Previous <", command = lambda: previousButton(self.controller, entry1, entry2, "Y2S1", Y1S2))
        button1.pack(side = "left")

        button2 = ttk.Button(self, text="Next >", command=lambda: nextButton(self.controller, entry1, entry2, "Y2S1", Y2S2))
        button2.pack(side = "right")

        button3 = ttk.Button(self, text="Finish", command=lambda: finishButton(self.controller, entry1, entry2, "Y2S1"))
        button3.pack(side = "top")

class Y2S2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label0 = ttk.Label(self, text="Year 2 Semester 2", justify="center")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = ttk.Label(self, text="Please enter your grades, seperated by commas.", justify="center")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self, justify="center")
        entry1.pack()

        label2 = ttk.Label(self, text = "Please enter your credits per module, seperated by commas.", justify="center")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        entry2 = ttk.Entry(self, justify="center")
        entry2.pack()

        button1 = ttk.Button(self, text = "Previous <", command = lambda: previousButton(self.controller, entry1, entry2, "Y2S2", Y2S1))
        button1.pack(side = "left")

        button2 = ttk.Button(self, text="Next >", command=lambda: nextButton(self.controller, entry1, entry2, "Y2S2", FinalPage))
        button2.pack(side = "right")

        button3 = ttk.Button(self, text="Finish", command=lambda: finishButton(self.controller, entry1, entry2, "Y2S2"))
        button3.pack(side = "top")

class Y3S1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label0 = ttk.Label(self, text="Year 3 Semester 1", justify="center")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = ttk.Label(self, text="Please enter your grades, seperated by commas.", justify="center")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self, justify="center")
        entry1.pack()

        label2 = ttk.Label(self, text = "Please enter your credits per module, seperated by commas.", justify="center")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        entry2 = ttk.Entry(self, justify="center")
        entry2.pack()

        button1 = ttk.Button(self, text = "Previous <", command = lambda: previousButton(self.controller, entry1, entry2, "Y3S1", Y2S2))
        button1.pack(side = "left")

        button2 = ttk.Button(self, text="Next >", command=lambda: nextButton(self.controller, entry1, entry2, "Y3S1", Y3S2))
        button2.pack(side = "right")

        button3 = ttk.Button(self, text="Finish", command=lambda: finishButton(self.controller, entry1, entry2, "Y3S1"))
        button3.pack(side = "top")

class Y3S2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label0 = ttk.Label(self, text="Year 3 Semester 2", justify="center")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = ttk.Label(self, text="Please enter your grades, seperated by commas.", justify="center")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self, justify="center")
        entry1.pack()

        label2 = ttk.Label(self, text = "Please enter your credits per module, seperated by commas.", justify="center")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        entry2 = ttk.Entry(self, justify="center")
        entry2.pack()

        button1 = ttk.Button(self, text = "Previous <", command = lambda: previousButton(self.controller, entry1, entry2, "Y3S2", Y3S1))
        button1.pack(side = "left")

        button2 = ttk.Button(self, text="Next >", command=lambda: nextButton(self.controller, entry1, entry2, "Y3S2", Y4S1))
        button2.pack(side = "right")

        button3 = ttk.Button(self, text="Finish", command=lambda: finishButton(self.controller, entry1, entry2, "Y3S2"))
        button3.pack(side = "top")

class Y4S1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label0 = ttk.Label(self, text="Year 4 Semester 1", justify="center")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = ttk.Label(self, text="Please enter your grades, seperated by commas.", justify="center")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self, justify="center")
        entry1.pack()

        label2 = ttk.Label(self, text = "Please enter your credits per module, seperated by commas.", justify="center")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        entry2 = ttk.Entry(self, justify="center")
        entry2.pack()

        button1 = ttk.Button(self, text = "Previous <", command = lambda: previousButton(self.controller, entry1, entry2, "Y4S1", Y3S2))
        button1.pack(side = "left")

        button2 = ttk.Button(self, text="Next >", command=lambda: nextButton(self.controller, entry1, entry2, "Y4S1", Y4S2))
        button2.pack(side = "right")

        button3 = ttk.Button(self, text="Finish", command=lambda: finishButton(self.controller, entry1, entry2, "Y4S1"))
        button3.pack(side = "top")

class Y4S2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label0 = ttk.Label(self, text="Year 4 Semester 2")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = ttk.Label(self, text="Please enter your grades, seperated by commas.", justify="center")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self, justify="center")
        entry1.pack()

        label2 = ttk.Label(self, text = "Please enter your credits per module, seperated by commas.", justify="center")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        entry2 = ttk.Entry(self, justify="center")
        entry2.pack()

        button1 = ttk.Button(self, text = "Previous <", command = lambda: previousButton(self.controller, entry1, entry2, "Y4S2", Y4S1))
        button1.pack(side = "left")

        button2 = ttk.Button(self, text="Next >", command=lambda: nextButton(self.controller, entry1, entry2, "Y4S2", FinalPage))
        button2.pack(side = "right")

        button3 = ttk.Button(self, text="Finish", command=lambda: finishButton(self.controller, entry1, entry2, "Y4S2"))
        button3.pack(side = "top")

class SUCalc(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label0 = ttk.Label(self, text="SU Calculator")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = ttk.Label(self, text="Please enter your current CAP/GPA given.", justify="center")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self, justify="center")
        entry1.pack()

        label2 = ttk.Label(self, text = "Please enter the total number of credits you have taken so far.", justify="center")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        entry2 = ttk.Entry(self, justify="center")
        entry2.pack()

        label3 = ttk.Label(self, text = "Please enter your grades for this semester, seperated by commas.", justify="center", font=("Segoe UI", 12))
        label3.pack()

        entry3 = ttk.Entry(self, justify="center")
        entry3.pack()

        label4 = ttk.Label(self, text="Please enter your number of credits for each module for this semester, seperated by commas.", justify="center", font=("Segoe UI", 12))
        label4.pack()

        entry4 = ttk.Entry(self, justify="center")
        entry4.pack()

        button1 = ttk.Button(self, text = "Previous <", command = lambda: controller.show_frame(CAPorSU))
        button1.pack(side = "left")

        button2 = ttk.Button(self, text="Next >", command=lambda: SUnext(entry1, entry2, entry3, entry4))
        button2.pack(side = "right")

        def SUnext(ent1, ent2, ent3, ent4):
            global uni
            global init_gpa
            global bef_credit
            global this_sem_grades
            global this_sem_credits

            ent1 = ent1.get()
            ent2 = ent2.get()
            
            grades = getGrades(ent3)
            this_sem_credits = getCredits(ent4)
            total_cre = sum(this_sem_credits)

            bef_credit = int(ent2) - total_cre

            res = ccm.CAPCal(uni)
            this_sem_grades = res.sem_grades(grades, this_sem_credits, "This Sem")
            final = res.grade_count((this_sem_grades,))

            if bef_credit > 0:
                init_gpa = ((float(ent1) * int(ent2)) - (final * total_cre))/bef_credit
            else:
                init_gpa = 0

            return controller.show_frame(SUable)
            


class SUable(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label0 = ttk.Label(self, text="SUable modules")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = ttk.Label(self, text="Please enter your grades for the modules that you can SU, seperated by commas.", justify="center")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self, justify="center")
        entry1.pack()

        label2 = ttk.Label(self, text = "Plase enter your number of credits for each module you can SU, seperated by commas.", justify="center")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        entry2 = ttk.Entry(self, justify="center")
        entry2.pack()

        button1 = ttk.Button(self, text="Calculate", command=lambda: calculate(entry1, entry2))
        button1.pack()

        def calculate(ent1, ent2):
            global this_sem_grades
            global init_gpa
            global bef_credit
            global uni
            global this_sem_credits

            orig = None

            grades = getGrades(ent1)
            credit = getCredits(ent2)

            res = ccm.CAPCal(uni)
            su_grades = res.sem_grades(grades, credit, "SU")
            su_grades.sort(key=lambda x: ccm.grade_dict[uni][x[0]])
            su_grades.sort(key=lambda x: x[1], reverse = True)

            for grade in su_grades:
                for j in range(len(this_sem_grades)):
                    if grade == this_sem_grades[j]:
                        orig = this_sem_grades[j]
                        this_sem_grades[j] = ('S',0)
                        for k in range(len(this_sem_credits)):
                            if this_sem_credits[k] == orig[1]:
                                this_sem_credits[k] = 0
                                break
                        break
                final = res.grade_count((this_sem_grades,))
                actual = ((final * sum(this_sem_credits)) + (init_gpa * bef_credit))/(bef_credit + sum(this_sem_credits))
                actual = round(actual, 2)

                label3 = ttk.Label(self, text = f"{actual} if you SU the next {orig[0]} with {orig[1]} credits.", justify="center")
                label3.pack()
        

class FinalPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = ttk.Label(self, text="Your estimated GPA is: ", justify="center")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        button1 = ttk.Button(self, text="Calculate", command=lambda: self.calculate(button1, self.controller))
        button1.pack()
        
    def calculate(self, but, cont):
        global uni
        global grade_entry
        global credit_entry
        all_results = []
        
        res = ccm.CAPCal(uni)
        if len(grade_entry) > 0 and len(credit_entry) > 0:
            for grade_key, credit_key in zip(grade_entry, credit_entry):
                grade_val = grade_entry[grade_key]
                credit_val = credit_entry[credit_key]
                try:
                    graded = res.sem_grades(grade_val, credit_val, grade_key)
                    all_results.append(graded)
                except Exception:
                    all_results = "Error! \nNo input was detected for any semester. \nPlease try again."
        else:
            all_results = "Error! \nNo input was detected for any semester. \nPlease try again."

        if type(all_results) != str:
            final = res.grade_count(all_results)
        else:
            final = all_results

        but.destroy()

        label2 = ttk.Label(self, text=str(final), justify="center")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        button3 = ttk.Button(self, text = "< Back", command=lambda: doneBut(label2, button3))
        button3.pack()

        def doneBut(lb, bt):
            lb.destroy()
            bt.destroy()

            global page_entry
        
            button1 = ttk.Button(self, text="Calculate", command=lambda: self.calculate(button1))
            button1.pack()

            return cont.show_frame(page_entry[-1])
       

page_dict = {"Y1S1":Y1S1, "Y1S2":Y1S2,
             "Y2S1":Y2S1, "Y2S2":Y2S2,
             "Y3S1":Y3S1, "Y3S2":Y3S2,
             "Y4S1":Y4S1, "Y4S2":Y4S2}

app = CAPCalc()
app.geometry("1024x600")
app.mainloop() 
