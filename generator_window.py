import generator

def generate(self):
        length = self.length_entry.get()
        password, chars, length = generator.generate_password(length)
        self.password_label.configure(text=password)