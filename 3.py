import tkinter as tk # создаем графический пользовательский интерфейс

class IceCreamStand(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ice Cream Stand")
        self.geometry("500x500")  # Устанавливаем размер окна

        self.configure(background='#FFC0CB')  # Устанавливаем цвет фона

        pink_frame = tk.Frame(self, bg='#696969')  # Создаем розовый фрейм
        pink_frame.pack(pady=30, padx=30, fill='both', expand=True)  # Устанавливаем отступы

        info_text = "Добро пожаловать в кафе-мороженное Sweet Treats!\n\nВкусы нашего мороженого:\nВанильное\nШоколадное\nКлубничное\nМятное\n\nЧасы работы:\n10:00-21:00 "
        info_label = tk.Label(pink_frame, text=info_text, bg='white', font=('Inter', 12), padx=10, pady=10)  # Создаем метку с информацией о кафе
        info_label.pack()
if __name__ == "__main__":
    app = IceCreamStand()
    app.mainloop()