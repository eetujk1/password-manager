import generator
import customtkinter as ctk




class generator_window(ctk.CTkToplevel):
        def __init__(self, parent):
                super().__init__(parent)
                self.title("Password Generation")
                self.geometry("600x500")

                self.grid_columnconfigure(0, weight=1)

                self.length_label = ctk.CTkLabel(
                           self,
                           text="Choose password length"
                       )
               
                self.length_label.grid(row=0, column=0, padx = 20, pady = 10, sticky ="ew") 

                self.length_entry = ctk.CTkEntry(self, placeholder_text="Password length")
                self.length_entry.grid(row=1, column=0, padx = 20, pady = 10)

                self.uppercase_var = ctk.BooleanVar(value=True)
                self.uppercase_checkbox = ctk.CTkCheckBox(
                self,
                text="Uppercase letters",
                variable=self.uppercase_var
                )

                self.uppercase_checkbox.grid(
                row=2,
                column=0,
                padx=20,
                pady=5,
                sticky="w"
                )

                self.lowercase_var = ctk.BooleanVar(value=True)
                self.lowercase_checkbox = ctk.CTkCheckBox(
                self,
                text = "Lowercase letters",
                variable=self.lowercase_var)


                self.lowercase_checkbox.grid(
                row=3,
                column=0,
                padx=20,
                pady=5,
                sticky="w"
                )

                self.numbers_var = ctk.BooleanVar(value=True)
                self.numbers_checkbox = ctk.CTkCheckBox(
                self,
                text = "Numbers",
                variable=self.numbers_var)


                self.numbers_checkbox.grid(
                row=4,
                column=0,
                padx=20,
                pady=5,
                sticky="w"
                        )

                self.generate_button = ctk.CTkButton(
                self,
                text="Generate password",
                command=self.generate
                )    

                self.generate_button.grid(row=6, column=0, padx=(0, 10), pady=20)

                self.password_label = ctk.CTkLabel(self, text = "")
                self.password_label.grid(padx = 5)


        def generate(self):
                length = self.length_entry.get()
                password = generator.generate_password(
                        length,
                        self.lowercase_var.get(),
                        self.uppercase_var.get(),
                        self.numbers_var.get()

                )
  

