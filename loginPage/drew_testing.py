import tkinter as tk
from tkinter import messagebox
import customtkinter

class NewDocument:

    def submitted_doc(self, dropdown1, dropdown2, doc_file_entry):
        # This function will be called when the button is clicked
        selected_option1 = dropdown1.get()
        selected_option2 = dropdown2.get()
        print(f"Grade: {selected_option2}, Subject: {selected_option1}")
        print(f"Filepath: {doc_file_entry.get()}")

    def __init__(self, root):
        # Create a frame to hold the widgets in a horizontal line
        frame = tk.Frame(root)
        frame.pack()

        self.doc_file_label = tk.Label(frame, text="Document Filepath")
        self.doc_file_label.pack(side="left")
        self.doc_file_entry = tk.Entry(frame)
        self.doc_file_entry.pack(side="left")

        # Create the first dropdown
        dropdown1 = tk.StringVar(root)
        # Dropdown menu options
        subject_filter = [
            "Math",
            "English",
            "Science",
            "History",
            "PE",
            "Art",
            "Chemistry",
            "Other"
        ]
        dropdown1.set(subject_filter[0])  # Set the default selection
        dropdown_menu1 = customtkinter.CTkOptionMenu(frame, dropdown1, *subject_filter)
        dropdown_menu1.pack(side="left")

        # Create the second dropdown
        dropdown2 = tk.StringVar(root)
        # Dropdown menu options
        grade_filter = [
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th",
            "6th",
            "7th",
            "8th",
            "Freshmen (High School)",
            "Sophomore (High School)",
            "Junior (High School)",
            "Senior (High School)",
            "Freshmen (College)",
            "Sophomore (College)",
            "Junior (College)",
            "Senior(College"
        ]
        dropdown2.set(grade_filter[0])  # Set the default selection
        dropdown_menu2 = tk.OptionMenu(frame, dropdown2, *grade_filter)
        dropdown_menu2.pack(side="left")

        # Create a button
        button = tk.Button(frame, text="Submit Document", command=self.submitted_doc(dropdown1, dropdown2, self.doc_file_entry))
        button.pack(side="right")

class RatingApp:
    def __init__(self, root):
        self.root = root
        root = customtkinter.CTk()
        self.root.title("Rating App")

        self.rating = 0  # Initialize the rating to 0

        # Create and configure labels
        self.label = tk.Label(root, text="Rate this product:")
        self.label.pack()

        # Create and configure rating buttons
        self.rating_buttons = []
        for i in range(1, 6):
            button = tk.Button(root, text=str(i), command=lambda i=i: self.set_rating(i))
            button.config(width=2, height=1)
            button.pack(side=CTk.LEFT, padx=10)
            self.rating_buttons.append(button)

        # Create a submit button
        self.submit_button = customtkinter.CTkButton(master=root, text="Submit Rating", command=self.submit_rating)
        self.submit_button.pack()

    def set_rating(self, rating):
        self.rating = rating
        for button in self.rating_buttons:
            button.config(state=tk.NORMAL)
        for button in self.rating_buttons[:rating]:
            button.config(state=tk.DISABLED)

    def submit_rating(self):
        if self.rating == 0:
            messagebox.showerror("Error", "Please select a rating.")
        else:
            messagebox.showinfo("Success", f"You have rated this product {self.rating} stars.")
            print(self.rating)
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = NewDocument(root)
    root.NewDocument()
