import tkinter.font                 # -----------------------------------------------
from tkinter import *               # Библиотеки для написания интерфейса приложения
from tkinter import ttk             # -----------------------------------------------
from tkinter import messagebox
from signal import Signal           # Импортируем из нашего файла класс Signal


# Класс описывающий общие параметры приложения
class SampleApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.wm_title("Быстрое преобразование Фурье")   # Заголовок приложения
        self.wm_geometry("500x250")                     # Размер приложения
        self.eval('tk::PlaceWindow . center')
        self.gen_data = []                              # Общие данные которые вводит пользователь (Время и частота дискритизации)
        self.data = []                                  # Данные каждой волны
        self.max_signal = 0
        self.skv_signal = 0
        self.max_spectrum = 0
        self.sr_spectrum = 0
        self.title_font = tkinter.font.Font(family='Helvetica', size=18, weight="bold", slant="italic") # Шрифт

        # Контейнер это место где будут храниться все страницы (Frames) приложения
        # та страница которую мы хотим увидеть будет расположена поверх остальных
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # ------------------------------------
        # Создание всех страниц
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        # ------------------------------------
        self.show_frame("StartPage")                # Переносит на стартовую страницу

    # Функция которая выводит на экран ту строницу название которой мы ей передадим
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# Класс описывающий стартовую страницу
class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller    # Контроллер это класс SampleApp в котором хранятся общие данные приложения
        self.data = []                  # Массив в котором будут хранится данные которые введ пользователь на стартовой странице
        label = Label(self, text="Общие параметры волн", font=controller.title_font) # Выводит на экран текст который ты ему передашь
        label.pack(side="top", fill="x", pady=10)
        Label(self, text='Введите частоту дистуритизации:').pack()
        self.entry1 = ttk.Entry(self)   # Поле для ввода данных волны
        self.entry1.pack()
        Label(self, text='Введите продолжительность волн(мс):').pack()
        self.entry2 = ttk.Entry(self)
        self.entry2.pack()
        button1 = Button(self, text="Далее",    # Кнопка которая при нажатии вызывает функцию submit_data
                            command=lambda: self.submit_data())
        button1.pack()

    # Функция которая проверяет корректность введенных данных, сохраняет их и переносит на след страницу
    def submit_data(self):
        if (self.entry1.get() == '') or (self.entry2.get() == ''):
            messagebox.showerror("Некорректно введенные данные", "Заполните все поля без пропусков")
        elif (int(self.entry1.get()) > 0) & (int(self.entry2.get()) > 0):
            self.data.append(self.entry1.get())
            self.data.append(self.entry2.get())
            self.controller.gen_data.append(self.data)
            self.controller.show_frame("PageOne")
        else:
            messagebox.showerror("Некорректно введенные данные", "Частота дискритизации и продолжительность волн должны быть больше 0")


# Класс описывающий страницу для первой волны (в нем почти все тоже самое что и в стартовой странице)
# Все последующие классы схожи с этим кроме класса PageFive и класса Result
class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.data = []
        label = Label(self, text="Параметры для первой волны", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Label(self, text='Введите частоту:').pack()
        self.entry1 = ttk.Entry(self)
        self.entry1.pack()
        Label(self, text='Введите амплитуду:').pack()
        self.entry2 = ttk.Entry(self)
        self.entry2.pack()
        Label(self, text='Введите фазу:').pack()
        self.entry3 = ttk.Entry(self)
        self.entry3.pack()
        button = Button(self, text="Далее",
                           command=lambda: self.submit_data())
        button.pack()

    def submit_data(self):
        if (self.entry1.get() == '') or (self.entry2.get() == '') or (self.entry3.get() == ''):
            messagebox.showerror("Некорректно введенные данные", "Заполните все поля без пропусков")
        elif (int(self.entry1.get()) > 0) & (int(self.entry2.get()) > 0):
            self.data.append(self.entry1.get())
            self.data.append(self.entry2.get())
            self.data.append(self.entry3.get())
            self.controller.data.append(self.data)
            self.controller.show_frame("PageTwo")
        else:
            messagebox.showerror("Некорректно введенные данные", "Частота и амплитуда должны быть больше 0")


# Класс описывающий страницу для второй волны
class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.data = []
        label = Label(self, text="Параметры для второй волны", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Label(self, text='Введите частоту:').pack()
        self.entry1 = ttk.Entry(self)
        self.entry1.pack()
        Label(self, text='Введите амплитуду:').pack()
        self.entry2 = ttk.Entry(self)
        self.entry2.pack()
        Label(self, text='Введите фазу:').pack()
        self.entry3 = ttk.Entry(self)
        self.entry3.pack()
        button = Button(self, text="Далее",
                           command=lambda: self.submit_data())
        button.pack()

    def submit_data(self):
        if (self.entry1.get() == '') or (self.entry2.get() == '') or (self.entry3.get() == ''):
            messagebox.showerror("Некорректно введенные данные", "Заполните все поля без пропусков")
        elif (int(self.entry1.get()) > 0) & (int(self.entry2.get()) > 0):
            self.data.append(self.entry1.get())
            self.data.append(self.entry2.get())
            self.data.append(self.entry3.get())
            self.controller.data.append(self.data)
            self.controller.show_frame("PageThree")
        else:
            messagebox.showerror("Некорректно введенные данные", "Частота и амплитуда должны быть больше 0")


# Класс описывающий страницу для третьей волны
class PageThree(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.data = []
        label = Label(self, text="Параметры для третьей волны", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Label(self, text='Введите частоту:').pack()
        self.entry1 = ttk.Entry(self)
        self.entry1.pack()
        Label(self, text='Введите амплитуду:').pack()
        self.entry2 = ttk.Entry(self)
        self.entry2.pack()
        Label(self, text='Введите фазу:').pack()
        self.entry3 = ttk.Entry(self)
        self.entry3.pack()
        button = Button(self, text="Далее",
                           command=lambda: self.submit_data())
        button.pack()

    def submit_data(self):
        if (self.entry1.get() == '') or (self.entry2.get() == '') or (self.entry3.get() == ''):
            messagebox.showerror("Некорректно введенные данные", "Заполните все поля без пропусков")
        elif (int(self.entry1.get()) > 0) & (int(self.entry2.get()) > 0):
            self.data.append(self.entry1.get())
            self.data.append(self.entry2.get())
            self.data.append(self.entry3.get())
            self.controller.data.append(self.data)
            self.controller.show_frame("PageFour")
        else:
            messagebox.showerror("Некорректно введенные данные", "Частота и амплитуда должны быть больше 0")


# Класс описывающий страницу для четвертой волны
class PageFour(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.data = []
        label = Label(self, text="Параметры для четвертой волны", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Label(self, text='Введите частоту:').pack()
        self.entry1 = ttk.Entry(self)
        self.entry1.pack()
        Label(self, text='Введите амплитуду:').pack()
        self.entry2 = ttk.Entry(self)
        self.entry2.pack()
        Label(self, text='Введите фазу:').pack()
        self.entry3 = ttk.Entry(self)
        self.entry3.pack()
        button = Button(self, text="Далее",
                           command=lambda: self.submit_data())
        button.pack()

    def submit_data(self):
        if (self.entry1.get() == '') or (self.entry2.get() == '') or (self.entry3.get() == ''):
            messagebox.showerror("Некорректно введенные данные", "Заполните все поля без пропусков")
        elif (int(self.entry1.get()) > 0) & (int(self.entry2.get()) > 0):
            self.data.append(self.entry1.get())
            self.data.append(self.entry2.get())
            self.data.append(self.entry3.get())
            self.controller.data.append(self.data)
            self.controller.show_frame("PageFive")
        else:
            messagebox.showerror("Некорректно введенные данные", "Частота и амплитуда должны быть больше 0")


# Класс описывающий страницу для пятой волны
class PageFive(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.data = []
        label = Label(self, text="Параметры для пятой волны", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Label(self, text='Введите частоту:').pack()
        self.entry1 = ttk.Entry(self)
        self.entry1.pack()
        Label(self, text='Введите амплитуду:').pack()
        self.entry2 = ttk.Entry(self)
        self.entry2.pack()
        Label(self, text='Введите фазу:').pack()
        self.entry3 = ttk.Entry(self)
        self.entry3.pack()
        button = Button(self, text="Далее",
                           command=lambda: self.submit_data())
        button.pack()

    # Функция такая же как и в предыдущих классах только в конце вызывается функция fft
    def submit_data(self):
        if (self.entry1.get() == '') or (self.entry2.get() == '') or (self.entry3.get() == ''):
            messagebox.showerror("Некорректно введенные данные", "Заполните все поля без пропусков")
        elif (int(self.entry1.get()) > 0) & (int(self.entry2.get()) > 0):
            self.data.append(self.entry1.get())
            self.data.append(self.entry2.get())
            self.data.append(self.entry3.get())
            self.controller.data.append(self.data)
            self.fft()
        else:
            messagebox.showerror("Некорректно введенные данные", "Частота и амплитуда должны быть больше 0")

    # Функция создающая объект класса Signal и передающая ему все данные которые ввел пользователь
    def fft(self):
        wave = Signal(int(self.controller.gen_data[0][0]), int(self.controller.gen_data[0][1]))
        for i in self.controller.data:
            wave.freq.append(int(i[0]))
            wave.altitude.append(int(i[1]))
            wave.phase.append(float(i[2]))
        wave.fourier_transform()                            # Вызывается функция преобразования Фурье
        self.controller.max_signal = wave.max_signal        #----------------
        self.controller.skv_signal = wave.skv_signal        # Сохраняются все итоговые данные
        self.controller.max_spectrum = wave.max_spectrum    # (макс сред значения сигнала и спектра)
        self.controller.sr_spectrum = wave.sr_spectrum      #----------------
        self.gen_last_page()                                # Вызывается функция которая создает последнюю страницу
        self.controller.show_frame("Result")

    # Функция которая создает последнюю страницу с итоговыми значениями сигнала и спектра
    def gen_last_page(self):
        f = Result
        page_name = f.__name__
        frame = f(parent=self.parent, controller=self.controller)
        self.controller.frames[page_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")


# Класс описывающий страницу с итоговыми значениями сигнала и спектра
class Result(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Итоговые показатели", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Label(self, text="Пиковое значение сигнала:").pack()
        Label(self, text=str(f"{self.controller.max_signal:.3f}")).pack()
        Label(self, text="Среднеквадратичное значение сигнала:").pack()
        Label(self, text=str(f"{self.controller.skv_signal:.3f}")).pack()
        Label(self, text="Максимальное значение спектра:").pack()
        Label(self, text=str(f"{self.controller.max_spectrum:.3f}")).pack()
        Label(self, text="Среднее значение спектра:").pack()
        Label(self, text=str(f"{self.controller.sr_spectrum:.3f}")).pack()
        button = Button(self, text="Заново",
                           command=lambda: self.del_data())
        button.pack()

    # Функция которая удаляет объект главного класса SampleApp и создает новый чтобы программа запустилась заново
    def del_data(self):
        global app
        app.quit()
        app.destroy()
        app = SampleApp()
        app.mainloop()


# При запуске программы создается объект главного класса которое создает само приложение
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
