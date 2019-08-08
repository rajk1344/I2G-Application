import tkinter as tk
from tkinter import filedialog


class I2Gapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, StudentMatcher):
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
            self, text="CatCource Camparison")
        self.button2.grid(column=1, row=3, padx=20, pady=5)

        self.button3 = tk.Button(
            self, text="Contract Creator")
        self.button3.grid(column=1, row=4, padx=20, pady=5)


class StudentMatcher(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="I2G Application")
        label.grid(column=1, row=1, padx=20, pady=20)

        self.minsize = (640, 400)
        self.student_file_button()
        self.project_file_button()
        self.run_button()
        self.back_button()

    def student_file_button(self):
        self.button = tk.Button(
            self, text="Select Student Roster", command=self.student_file_dialog)
        self.button.grid(column=1, row=2, padx=20, pady=5)

    def student_file_dialog(self):
        self.student_filename = filedialog.askopenfile(
            initialdir="/", title="Select Student Roster", filetype=(("Comma-sperated Values", "*.csv"), ("All Files", "*.*")))
        self.label = tk.Label(self, text=self.student_filename)
        self.label.grid(column=1, row=3, padx=20, pady=0)

    def project_file_button(self):
        self.button = tk.Button(
            self, text="Select Project Roster", command=self.project_file_dialog)
        self.button.grid(column=1, row=4, padx=20, pady=5)

    def project_file_dialog(self):
        self.project_filename = filedialog.askopenfile(
            initialdir="/", title="Select Project Roster", filetype=(("Comma-sperated Values", "*.csv"), ("All Files", "*.*")))
        self.label = tk.Label(self, text=self.project_filename)
        self.label.grid(column=1, row=5, padx=20, pady=0)

    def run_button(self):
        self.button = tk.Button(self, text="RUN ->")
        self.button.grid(column=2, row=6, padx=20, pady=10)

        # TODO add run

    def back_button(self):
        self.button = tk.Button(
            self, text="<- BACK", 
            command=lambda: __init__.controller.show_frame(StartPage))
        self.button.grid(column=0, row=6, padx=20, pady=10)


app = I2Gapp()
app.mainloop()
