import customtkinter as ctk
import generator_window


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Password manager")
        self.geometry("600x500")

        self.websitelabel = ctk.CTkLabel(
            self,
            text="Website"
        )

        self.grid_columnconfigure(0, weight=1)
        self.websitelabel.grid(row=0, column=0, padx = 20, pady = 10, sticky ="w")


        self.website_entry = ctk.CTkEntry(self, placeholder_text = "Website")
        self.website_entry.grid(row=1, column=0, padx = 20, pady = 5, sticky ="ew")

        self.usernameLabel = ctk.CTkLabel(self, text="Username")

        self.usernameLabel.grid(row=2, column=0, padx = 20, pady = 5, sticky ="w")  

        self.username_entry = ctk.CTkEntry(self, placeholder_text = "Username")
        self.username_entry.grid(row=3, column=0, padx = 20, pady = 5, sticky ="ew")

        self.passwordLabel = ctk.CTkLabel(self, text="Password")
        self.passwordLabel.grid(row=4, column=0, padx = 20, pady = 5, sticky ="w") 

        self.password_entry = ctk.CTkEntry(self, placeholder_text = "Password" )
        self.password_entry.grid(row=5, column=0, padx = 20, pady = 5, sticky ="ew")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.grid(row=6, column=0, pady=20)
    

        self.generate_button = ctk.CTkButton(
                    self.button_frame,
                    text="Generate password",
                    command=self.open_generator
                    )    

        self.generate_button.grid(row=6, column=0, padx=(0, 10), pady=20)

        self.password_label = ctk.CTkLabel(self.button_frame, text = "")
        self.password_label.grid(padx = 5)


        self.save_button = ctk.CTkButton(self.button_frame, text = "Save")
        self.save_button.grid(row=6, column=1)


    def open_generator(self):
        self.generator_window = generator_window.generator_window(self)



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()