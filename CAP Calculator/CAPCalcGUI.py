import tkinter as tk
from tkinter import ttk

grade_entry = {}
credit_entry = {}
uni = None
page_entry = []

######################
###CAP Cal Classes###
######################
grade_dict ={"NUS":{"A+":5.0, "A":5.0, "A-":4.5,
                    "B+":4.0, "B":3.5, "B-":3.0,
                    "C+":2.5, "C":2.0, "D+":1.5,
                    "D":1.0, "F":0.0, "S":0.0, "U":0.0},
             "NTU":{"A+":5.0, "A":5.0, "A-":4.5,
                    "B+":4.0, "B":3.5, "B-":3.0,
                    "C+":2.5, "C":2.0, "D+":1.5,
                    "D":1.0, "F":0.0, "S":0.0, "U":0.0},
             "SMU":{"A+":4.3, "A":4.0, "A-":3.7,
                    "B+":3.3, "B":3.0, "B-":2.7,
                    "C+":2.3, "C":2.0, "C-":1.7,
                    "D+":1.3, "D":1.0, "F":0.0,
                    "S":0.0, "U":0.0}}


def is_int(string):
    vale = 0
    for char in string:
        try:
            int(char)
        except ValueError:
            vale += 1
            continue
    if vale == len(string):
        return False
    elif vale == 0:
        return True
    else:
        return None


class CAPCal:
    def __init__(self, uni):
        self.uni = uni

    def get_uni(self):
        return self.uni

    def sem_grades(self, grades, credit, key):
        if is_int(grades) or is_int(grades) is None:
            return popupmsg(f"Result field cannot contain integers in {key}, please try again.", "Integer Error")
        sem_res = tuple(map(lambda x: x.upper(), grades))

        for grade in sem_res:
            if grade not in grade_dict[self.uni]:
                return popupmsg(f"Sorry, you have entered an invalid grade in {key}. Please try again.", "Grade not found")
        
        ## Find number of credits
        sem_mc = tuple(map(lambda x: int(x), credit))

        ## Checking if the number of results given is more than the number of credits
        if len(sem_res) > len(sem_mc): 
            return popupmsg(f"You have input more grades than the number of credited modules in {key}. Please try again.", "Non-tally Error")
        
        ##Checking if the number of credits given is more than the number of results
        elif len(sem_mc) > len(sem_res):
            return popupmsg(f"You have more number of credited modules than the number of grades input in {key}. Please try again.", "Non-tally Error")
        
        ## Combining them into a list
        res = []
        for grad, mc in zip(sem_res, sem_mc):
            res.append((grad, mc))
        return res

    def grade_count(self, grades):
        curr_grades = []
        for grade in grades:
            for i in range(len(grade)):
                ## Making S grade to be 0 MC
                if 'S' in grade[i] or 'CS' in grade[i]:
                    grade.pop(i)
                    grade.insert(i,('S', 0))
                ## Making U grade to be 0 MC
                elif 'U' in grade[i] or 'CU' in grade[i]:
                    grade.pop(i)
                    grade.insert(i, ('U', 0))

        ## Adding grades to curr_grades
        for grade in grades:
            curr_grades.extend(grade)
            
        total_points = list(map(lambda x:grade_dict[self.uni][x[0]], curr_grades))
        mcs = list(map(lambda x: x[1], curr_grades))
        total_mc = 0

        ##Calculating total MC
        for pt, mc in zip(total_points, mcs):
            total_mc += pt * mc
        result = round(total_mc/sum(mcs),2)
        
        return result

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
    label = ttk.Label(popup, text = string, font = ("Segoe UI", 12), anchor="center")
    label.pack(side = "top", fill = "x", pady=10)

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

    text = tk.Text(root, height=20, width=70)
    text.pack(side = "left")
    text.tag_configure('big', font=('Helvetica', 20, 'bold'))
    text.tag_configure('heading', font=('Helvetica', 14, 'bold'))
    text.tag_configure('body', font=('Helvetica', 10))
    text.tag_configure('center', justify='center')

    text.insert(tk.END, 'About \n', ['big', 'center'])
    text.insert(tk.END, '\nVersion 0.7.0 \n', 'heading')
    text.insert(tk.END, 'This is a beta version of this application and may be buggy. \nPlease use it with caution.', 'body')

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
        return res

def previousButton(controller, entry1, entry2, key, prevPage):
    global grade_entry
    global credit_entry

    grade = getGrades(entry1)
    credit = getCredits(entry2)

    grade_entry[key] = grade
    credit_entry[key] = credit
    
    return controller.show_frame(prevPage) 

def nextButton(controller, entry1, entry2, key, nextPage):
    global grade_entry
    global credit_entry
    global page_entry
        
    grade = getGrades(entry1)
    credit = getCredits(entry2)

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
        for fr in (StartPage, Y1S1, Y1S2, Y2S1, Y2S2, Y3S1, Y3S2, Y4S1, Y4S2, FinalPage):
            frame = fr(container, self)

            self.frames[fr] = frame

            frame.grid(row=0, column=0, sticky = "nsew")

        self.show_frame(StartPage)

        tk.Tk.iconbitmap(self, default = "CAPCalculator.ico")

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

        label0 = ttk.Label(self, text="Year 1 Semester 1")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = ttk.Label(self, text="Please enter your grades, seperated by commas.")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self)
        entry1.pack()
        
        label2 = ttk.Label(self, text = "Please enter your credits per module, seperated by commas.")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()
        
        entry2 = ttk.Entry(self)
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
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label0 = ttk.Label(self, text="Year 2 Semester 2")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = ttk.Label(self, text="Please enter your grades, seperated by commas.")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self)
        entry1.pack()

        label2 = ttk.Label(self, text = "Please enter your credits per module, seperated by commas.")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        entry2 = ttk.Entry(self)
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
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label0 = ttk.Label(self, text="Year 3 Semester 1")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = ttk.Label(self, text="Please enter your grades, seperated by commas.")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self)
        entry1.pack()

        label2 = ttk.Label(self, text = "Please enter your credits per module, seperated by commas.")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        entry2 = ttk.Entry(self)
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
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label0 = ttk.Label(self, text="Year 3 Semester 2")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = ttk.Label(self, text="Please enter your grades, seperated by commas.")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self)
        entry1.pack()

        label2 = ttk.Label(self, text = "Please enter your credits per module, seperated by commas.")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        entry2 = ttk.Entry(self)
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
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label0 = ttk.Label(self, text="Year 4 Semester 1")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = ttk.Label(self, text="Please enter your grades, seperated by commas.")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self)
        entry1.pack()

        label2 = ttk.Label(self, text = "Please enter your credits per module, seperated by commas.")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        entry2 = ttk.Entry(self)
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
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label0 = ttk.Label(self, text="Year 4 Semester 2")
        label0.config(font=("Segoe UI", 14))
        label0.pack()
        
        label1 = ttk.Label(self, text="Please enter your grades, seperated by commas.")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        entry1 = ttk.Entry(self)
        entry1.pack()

        label2 = ttk.Label(self, text = "Please enter your credits per module, seperated by commas.")
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

        entry2 = ttk.Entry(self)
        entry2.pack()

        button1 = ttk.Button(self, text = "Previous <", command = lambda: previousButton(self.controller, entry1, entry2, "Y4S2", Y4S1))
        button1.pack(side = "left")

        button2 = ttk.Button(self, text="Next >", command=lambda: nextButton(self.controller, entry1, entry2, "Y4S2", FinalPage))
        button2.pack(side = "right")

        button3 = ttk.Button(self, text="Finish", command=lambda: finishButton(self.controller, entry1, entry2, "Y4S2"))
        button3.pack(side = "top")


class FinalPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.controller = controller

        label1 = ttk.Label(self, text="Your estimated GPA is: ")
        label1.config(font = ("Segoe UI", 12))
        label1.pack()

        button1 = ttk.Button(self, text="Calculate", command=lambda: self.calculate(button1))
        button1.pack()

        button2 = ttk.Button(self, text= "Previous", command=lambda: self.prevButton(self.controller))
        button2.pack(side = "left")
        
    def calculate(self,but):
        global uni
        global grade_entry
        global credit_entry
        all_results = []
        
        res = CAPCal(uni)
        for grade_key, credit_key in zip(grade_entry, credit_entry):
            grade_val = grade_entry[grade_key]
            credit_val = credit_entry[credit_key]
            try:
                graded = res.sem_grades(grade_val, credit_val, grade_key)
                all_results.append(graded)
            except Exception:
                all_results = "                   Error! \nNo input was detected for any semester. \n             Please try again."

        if type(all_results) != str:
            final = res.grade_count(all_results)
        else:
            final = all_results

        but.destroy()

        label2 = ttk.Label(self, text=str(final))
        label2.config(font = ("Segoe UI", 12))
        label2.pack()

    def prevButton(self, controller):
        global page_entry
        
        button1 = ttk.Button(self, text="Calculate", command=lambda: self.calculate(button1))
        button1.pack()

        return controller.show_frame(page_entry[-1])
       

page_dict = {"Y1S1":Y1S1, "Y1S2":Y1S2,
             "Y2S1":Y2S1, "Y2S2":Y2S2,
             "Y3S1":Y3S1, "Y3S2":Y3S2,
             "Y4S1":Y4S1, "Y4S2":Y4S2}


app = CAPCalc()
app.geometry("650x275")
app.mainloop()



        
    
