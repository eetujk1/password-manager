import generator
import customtkinter as ctk




class generator_window(ctk.CTkToplevel):
        def __init__(self, parent):
                super().__init__(parent)
                self.parent = parent
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

                self.digits_var = ctk.BooleanVar(value=True)
                self.digits_checkbox = ctk.CTkCheckBox(
                self,
                text = "digits",
                variable=self.digits_var)


                self.digits_checkbox.grid(
                row=4,
                column=0,
                padx=20,
                pady=5,
                sticky="w"
                        )

                self.special_var = ctk.BooleanVar(value=True)
                self.special_checkbox = ctk.CTkCheckBox(
                self,
                text = "special",
                variable=self.special_var)


                self.special_checkbox.grid(
                row=5,
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

                self.generate_button.grid(row=7, column=0, padx=(0, 10), pady=20)

                self.password_label = ctk.CTkLabel(self, text = "")
                self.password_label.grid(row = 6, column = 0, padx = 20, pady =10)

                self.copy_button = ctk.CTkButton(
                        self,
                        text="Copy",
                        command=self.copy_password
                )    

                self.copy_button.grid(row=9, column=0, padx=(0, 10), pady=20)

                self.use_button = ctk.CTkButton(
                        self, 
                        text = "Use password",
                        command = self.use_password)

                self.use_button.grid(
                row=8,
                column=0,
                pady=10
                )

      
        def generate(self):
                length = int(self.length_entry.get())
                password, chars, length = generator.generate_password(
                        length,
                        upper = self.uppercase_var.get(),
                        lower = self.lowercase_var.get(),
                        digits = self.digits_var.get(),
                        special = self.special_var.get()
                )

                self.password_label.configure(text=password)


        def copy_password(self):
                password = self.password_label.cget("text")
                self.clipboard_clear()
                self.clipboard_append(password)
                self.copy_button.configure(text="Copied!")

        def use_password(self):
                password = self.password_label.cget("text")
                self.parent.password_entry.delete(0,"end")
                self.parent.password_entry.insert(0,password)
                self.destroy()





