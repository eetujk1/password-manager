import customtkinter as ctk
import generator

class password_generator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Password manager")
        self.geometry("600x500")

        self.label = ctk.CTkLabel(
            self,
            text="Password Generator"
        )

        self.label.grid(pady=20)  

        self.length_entry = ctk.CTkEntry(self, placeholder_text = "Enter password length")
        self.length_entry.grid(pady=10)

        self.generate_button = ctk.CTkButton(
            self,
            text="Generate",
            command=self.generate
        )

        self.generate_button.grid(row=0, column=0, padx=20, pady=10)

        self.password_label = ctk.CTkLabel(self, text = "")
        self.password_label.grid(rpady = 10)

        

    def generate(self):
        length = self.length_entry.get()
        password, chars, length = generator.generate_password(length)
        self.password_label.configure(text=password)


if __name__ == "__main__":
    app = password_generator()
    app.mainloop()