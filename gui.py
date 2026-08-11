import customtkinter as ctk
import generator_window
import password_vault


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Password manager")
        self.geometry("600x500")

        
        self.main_frame = ctk.CTkFrame(self)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=2)
        self.main_frame.grid_columnconfigure(2, weight=1)

        self.main_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky ="nsew",

        )
        self.websitelabel = ctk.CTkLabel(
            self.main_frame,
            text="Website"
        )

        self.websitelabel.grid(row=0, column=1, padx = 20, pady = 10, sticky ="w")


        self.website_entry = ctk.CTkEntry(self.main_frame, placeholder_text = "Website")
        self.website_entry.grid(row=1, column=1, padx = 20, pady = 5, sticky = "ew")

        self.usernameLabel = ctk.CTkLabel(self.main_frame, text="Username")

        self.usernameLabel.grid(row=2, column=1, padx = 20, pady = 5, sticky ="w")  

        self.username_entry = ctk.CTkEntry(self.main_frame, placeholder_text = "Username")
        self.username_entry.grid(row=3, column=1, padx = 20, pady = 5, sticky ="ew")

        self.passwordLabel = ctk.CTkLabel(self.main_frame, text="Password")
        self.passwordLabel.grid(row=4, column=1, padx = 20, pady = 5, sticky ="w") 

        self.password_entry = ctk.CTkEntry(self.main_frame, placeholder_text = "Password" )
        self.password_entry.grid(row=5, column=1, padx = 20, pady = 5, sticky ="ew")

        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.button_frame.grid(row=6, column=1, pady=20)
    

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

        self.passwords_button = ctk.CTkButton(self.button_frame, text="Show passwords", command = self.open_passwords)

        self.passwords_button.grid(row=7, column=0, columnspan=2, pady=10)


        self.generator_frame = generator_window.generatorFrame(self)
        self.generator_frame.grid(
            row=0,
            column=0,
            padx=20,
            pady=10,
            sticky="nsew"
        )

        self.generator_frame.grid_remove()

        self.password_vault_frame = password_vault.vaultFrame(self)

        self.password_vault_frame.grid(
            row=0,
            column=0,
            padx=20,
            pady=10,
            sticky="nsew"
                )

        self.password_vault_frame.grid_remove()


    def open_passwords(self):
        self.main_frame.grid_remove()
        self.password_vault_frame.grid()
        
    def open_generator(self):
        self.main_frame.grid_remove()
        self.generator_frame.grid()




if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()