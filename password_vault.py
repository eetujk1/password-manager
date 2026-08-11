import customtkinter as ctk

class vaultFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)

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

        self.search_entry = ctk.CTkEntry(self, placeholder_text="Search password")

