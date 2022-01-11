from tkinter import *
from tkinter import messagebox


class Sav_App:
    def __init__(self, master):

        self.frame = Frame(master)
        self.frame.grid()

        self.top_label = Label(
            self.frame,
            text="Please enter the values to calculate your future savings.",
            font=("San Serif", 18, "italic bold"),
            fg="gray35",
            bg="gray90",
        )
        self.top_label.grid(row=0, columnspan=2)

        self.info_button = Button(
            self.frame,
            text="Info",
            width=10,
            activeforeground="white",
            highlightbackground="OrangeRed3",
            command=self.info_click,
        )
        self.info_button.grid(row=1, column=0, sticky="W")

        self.message_1 = "What is the principal amount of savings you already have?"
        self.text_box1 = Text(
            self.frame, height=7, width=20, wrap="word", font=("Arial", 16)
        )
        self.text_box1.insert(INSERT, self.message_1)
        self.text_box1.config(state="disabled")
        self.text_box1.grid(row=2, column=0, sticky="W")

        self.message_2 = "How much do you want to save per month?"
        self.text_box2 = Text(
            self.frame, height=7, width=20, wrap="word", font=("Arial", 16)
        )
        self.text_box2.insert(INSERT, self.message_2)
        self.text_box2.config(state="disabled")
        self.text_box2.grid(row=3, column=0, sticky="W")

        self.message_3 = "How many years do you want to save for?"
        self.text_box3 = Text(
            self.frame, height=7, width=20, wrap="word", font=("Arial", 16)
        )
        self.text_box3.insert(INSERT, self.message_3)
        self.text_box3.config(state="disabled")
        self.text_box3.grid(row=4, column=0, sticky="W")

        self.message_4 = "What is the APY?"
        self.text_box4 = Text(
            self.frame, height=7, width=20, wrap="word", font=("Arial", 16)
        )
        self.text_box4.insert(INSERT, self.message_4)
        self.text_box4.config(state="disabled")
        self.text_box4.grid(row=5, column=0, sticky="W")

        self.entry_1 = Entry(self.frame, width=15, borderwidth=4)
        self.entry_1.grid(row=2, column=1, sticky="NE")

        self.entry_2 = Entry(self.frame, width=15, borderwidth=4)
        self.entry_2.grid(row=3, column=1, sticky="NE")

        self.entry_3 = Entry(self.frame, width=15, borderwidth=4)
        self.entry_3.grid(row=4, column=1, sticky="NE")

        self.entry_4 = Entry(self.frame, width=15, borderwidth=4)
        self.entry_4.grid(row=5, column=1, sticky="NE")

        self.button_1 = Button(
            self.frame,
            text="CALCULATE",
            highlightbackground="lime green",
            activeforeground="white",
            bd=5,
            width=30,
            command=self.button_click,
        )
        self.button_1.grid(row=6, columnspan=2)

    # Function for when the "Info" button is clicked
    def info_click(self):
        messagebox.showinfo(
            "Information",
            "This program assumes that the annual interest rate is compounded monthly and the monthly saving amount is deposited at the end of each month.",
        )

    # Function for checking if the inputs are correct
    def check_input(self):
        try:
            float(self.entry_1.get()) and float(self.entry_2.get()) and float(
                self.entry_3.get()
            ) and float(self.entry_4.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid Input(s). Please enter again.")

    # Function for when the "Calculate" button is clicked
    def button_click(self):
        self.check_input()
        self.calculate_input()
        self.result_box()

    # Function for taking the user input for calculations
    def calculate_input(self):
        self.principal_amount = float(self.entry_1.get())
        self.saving_amount = float(self.entry_2.get())
        self.saving_time = float(self.entry_3.get())
        self.saving_apy = float(self.entry_4.get())

        self.apy_time = 12

        # Compound interest for principal amount
        self.comp_interest = (1 + self.saving_apy / self.apy_time) ** (
            self.apy_time * self.saving_time
        )

        # Formula for total amount with no deposit
        self.nodep_total_amount = self.principal_amount * self.comp_interest

        # Formula for total amount with monthly deposit at the end of each month
        self.dep_total_amount = self.nodep_total_amount + self.saving_amount * (
            (self.comp_interest - 1) / (self.saving_apy / self.apy_time)
        )

    def result_box(self):
        self.principal_amount = round(self.principal_amount, 2)
        self.nodep_total_amount = round(self.nodep_total_amount, 2)
        self.dep_total_amount = round(self.dep_total_amount, 2)
        self.saving_apy = round(self.saving_apy, 2)

        self.result_message = f"""
        Principal Amount = ${self.principal_amount}
        
        APY = {self.saving_apy}%
        
        Total Amount with no Deposit = ${self.nodep_total_amount}
        
        Total Amount with Deposit = ${self.dep_total_amount}
        """

        messagebox.showinfo("Calculations", self.result_message)


root = Tk()
root.title("Something To Do With Savings")

app = Sav_App(root)
root.mainloop()
