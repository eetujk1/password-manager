import customtkinter as ctk
import generator

class main_window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.setup()
        self.create_frames()
        self.layout_widgets()

    def setup(self):   
        self.title("Password Manager")
        self.geometry("500x400")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.mainframe = ctk.CTkFrame(self, fg_color="transparent")
        self.mainframe.grid(row=0, column=0)
        self.mainframe.columnconfigure(0, weight = 1)
        self.mainframe.rowconfigure(0, weight = 1)

    def create_frames(self):
        
        self.frame = ctk.CTkFrame(self.mainframe)  
        self.frame.grid(row=0, column=0)
        self.label = ctk.CTkLabel(
            self.frame,
            text="Password Manager"

        )
        self.frame.grid_columnconfigure(0, weight = 1)
        self.frame.grid_rowconfigure(0, weight = 1)

    def layout_widgets(self):

        self.label.grid(row = 0, column = 0)  
        
        self.length_entry = ctk.CTkEntry(self.frame, placeholder_text = "Enter password")
        self.length_entry.grid(row = 1, column = 0)

        self.generate_button = ctk.CTkButton(
            self.frame,
            text="Generate",
            command=self.generate
        )

        self.generate_button.grid(row=2, column=0, padx=20, pady=10)

        self.password_label = ctk.CTkLabel(
        self.frame,
        text="Generated password will appear here",
        wraplength=500
    )
        self.password_label.grid(row=3, column=0, pady=(20, 10))

        

    def generate(self):
        length = self.length_entry.get()
        password, chars, length = generator.generate_password(length)
        self.password_label.configure(text=password)


if __name__ == "__main__":
    app = mainwindow()
    app.mainloop()