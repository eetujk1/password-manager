import customtkinter as ctk

class vaultFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text="Password vault"
                )
        self.title_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
                )
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="ew")
        self.header_frame.grid_columnconfigure(1, weight=1)

        self.back_button = ctk.CTkButton(
            self.header_frame,
            text="Back",
            width=80,
            command=self.go_back
        )
        self.back_button.grid(row=0, column=0, sticky="w")

        
        self.search_entry = ctk.CTkEntry(self, placeholder_text="Search password")
        self.search_entry.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
            sticky = "ew"   ) 

        self.password_list = ctk.CTkScrollableFrame(self)
        self.password_list.grid(row=2, column=0, padx = 20, pady = 10, sticky = "nsew")

    def go_back(self):
        self.grid_remove()
        self.parent.main_frame.grid() 

    def add_password(self, password_data):
        item = passwordItem(
            self.password_list,
            password_data
        )

        item.pack(
            fill="x",
            padx=10,
            pady=5
        )

class passwordItem(ctk.CTkFrame):
    def __init__(self, parent, password_data):
        super().__init__(parent)
        self.password_data = password_data
        
        self.website_label = ctk.CTkLabel(
            self,
            text=password_data["website"]
        )
        self.website_label.pack(
            padx=10,
            pady=10,
            anchor="w"
        ) 

        self.username_label = ctk.CTkLabel(
            self,
            text=password_data["username"]
        )
        self.username_label.pack(
            padx=10,
            pady=10,
            anchor="w"
        )         

class PasswordDetailFrame(ctk.CTkFrame):

    def __init__(self, parent, password_data):
        super().__init__(parent)

        self.password_data = password_data

