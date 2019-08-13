import tkinter as tk
from tkinter import filedialog

from file_reader import *
from missing_student import *
from matcher import *


class I2Gapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, StudentMatcher, CatCoursesMatcher):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="I2G Application")
        label.grid(column=1, row=1, padx=20, pady=20)

        self.minsize = (640, 400)

        self.button1 = tk.Button(
            self, text="Student Matcher",
            command=lambda: controller.show_frame(StudentMatcher))
        self.button1.grid(column=1, row=2, padx=20, pady=5)

        self.button2 = tk.Button(
            self, text="CatCourses Camparison",
            command=lambda: controller.show_frame(CatCoursesMatcher))
        self.button2.grid(column=1, row=3, padx=20, pady=5)

        self.button3 = tk.Button(
            self, text="Contract Creator")
        self.button3.grid(column=1, row=4, padx=20, pady=5)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)


class StudentMatcher(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Student Matcher")
        label.grid(column=1, row=1, padx=20, pady=20)

        self.minsize = (1000, 1000)
        self.student_file_button()
        self.project_file_button()
        self.output_directory_button()
        self.run_button()

        self.button = tk.Button(
            self, text="<- BACK",
            command=lambda: controller.show_frame(StartPage))
        self.button.grid(column=0, row=8, padx=20, pady=10)

    def student_file_button(self):
        self.button = tk.Button(
            self, text="Select Student Roster", 
            command=self.student_file_dialog)
        self.button.grid(column=1, row=2, padx=20, pady=5)

    def student_file_dialog(self):
        self.student_filename = filedialog.askopenfile(
            initialdir="/", 
            title="Select Student Roster", 
            filetype=(("Comma-sperated Values", "*.csv"), ("All Files", "*.*")))
        self.label = tk.Label(self, text=self.student_filename.name)
        self.label.grid(column=1, row=3, padx=20, pady=0)

    def project_file_button(self):
        self.button = tk.Button(
            self, text="Select Project Roster", 
            command=self.project_file_dialog)
        self.button.grid(column=1, row=4, padx=20, pady=5)

    def project_file_dialog(self):
        self.project_filename = filedialog.askopenfile(
            initialdir="/", 
            title="Select Project Roster", 
            filetype=(("Comma-sperated Values", "*.csv"), ("All Files", "*.*")))
        self.label = tk.Label(self, text=self.project_filename.name)
        self.label.grid(column=1, row=5, padx=20, pady=0)

    def output_directory_button(self):
        self.button = tk.Button(
            self, text="Select Output Location", command=lambda: self.output_directory_dialog())
        self.button.grid(column=1, row=6, padx=20, pady=5)

    def output_directory_dialog(self):
        self.output_location = filedialog.askdirectory()
        self.label = tk.Label(self, text=self.output_location)
        self.label.grid(column=1, row=7, padx=20, pady=0)

    def run_button(self):
        self.button = tk.Button(self, text="RUN ->", command = lambda:self.runner())
        self.button.grid(column=2, row=8, padx=20, pady=10)

    def runner(self):
        self.students = read_students(self.student_filename.name)
        self.projects = read_projects(self.project_filename.name)
        match(self.students, self.projects, self.output_location)


class CatCoursesMatcher(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="CatCourses Matcher")
        label.grid(column=1, row=1, padx=20, pady=20)

        self.minsize = (1000, 1000)
        self.qualtrics_file_button()
        self.catcources_file_button()
        self.output_directory_button()
        self.run_button()

        self.button = tk.Button(
            self, text="<- BACK",
            command=lambda: controller.show_frame(StartPage))
        self.button.grid(column=0, row=8, padx=20, pady=10)

    def qualtrics_file_button(self):
        self.button = tk.Button(
            self, text="Select Qualtrics Roster", command=self.qualtrics_file_dialog)
        self.button.grid(column=1, row=2, padx=20, pady=5)

    def qualtrics_file_dialog(self):
        self.qualtrics_filename = filedialog.askopenfile(
            initialdir="/", title="Select Qualtrics Roster", filetype=(("Comma-sperated Values", "*.csv"), ("All Files", "*.*")))
        self.label = tk.Label(self, text=self.qualtrics_filename.name)
        self.label.grid(column=1, row=3, padx=20, pady=0)

    def catcources_file_button(self):
        self.button = tk.Button(
            self, text="Select Catcources Roster", command=self.catcources_file_dialog)
        self.button.grid(column=1, row=4, padx=20, pady=5)

    def catcources_file_dialog(self):
        self.catcources_filename = filedialog.askopenfile(
            initialdir="/", title="Select Catcources Roster", filetype=(("Comma-sperated Values", "*.csv"), ("All Files", "*.*")))
        self.label = tk.Label(self, text=self.catcources_filename.name)
        self.label.grid(column=1, row=5, padx=20, pady=0)

    def output_directory_button(self):
        self.button = tk.Button(
            self, text="Select Output Location", command=lambda: self.output_directory_dialog())
        self.button.grid(column=1, row=6, padx=20, pady=5)

    def output_directory_dialog(self):
        self.output_location = filedialog.askdirectory()
        self.label = tk.Label(self, text=self.output_location.name)
        self.label.grid(column=1, row=7, padx=20, pady=0)

    def run_button(self):
        self.button = tk.Button(self, text="RUN ->")
        self.button.grid(column=2, row=8, padx=20, pady=10)

    def runner(self):
        self.qualtrics = read_qualtrix(self.qualtrix_filename.name)
        self.catcources = read_catcources(self.catcources_filename.name)
        print(list_missing(catcources, qualtrics))
        #TODO ask dev on the missing students


app = I2Gapp()
app.mainloop()
