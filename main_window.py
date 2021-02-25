from tkinter import *
from tkinter import messagebox
from information_window import InformationWindow


def button_upload_to_sql(entry_text):  # here will be map of all entry field
    choice = messagebox.askyesno('Загрузка в базу данных', 'Действительно подтверждаете загрузку в базу данных?')
    # TODO
    #  query for DB
    if choice:
        messagebox.showinfo('Выгрузка в базу данных', 'Данные загружены в базу')
        print(entry_text.get())
        # TODO
        #  clear oll data after upload to DB
        entry_text.delete(0, END)


def button_clear_text_field(entry_text):
    choice = messagebox.askyesno('Очистка поля', 'Вы дествительно хотите очистить содержимое поля')
    if choice:
        print(entry_text.get())
        entry_text.delete(0, END)


class MainWindow:
    def __init__(self, width, height, x, y, title):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

        #  <editor-fold desc="Edit text variables">
        self.invoke_date = Entry(self.root, font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.owner = Entry(self.root, font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.contract_number_date = Entry(self.root, font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.contract_cost = Entry(self.root, font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        # </editor-folds>

    def draw_widgets(self):
        self.draw_menu_bar()

        button_width = 15
        message_text_width = 250

        # <editor-fold desc="buttons group">
        Button(self.root,
               text='Выход',
               width=button_width,
               command=self.exit_check,
               relief=GROOVE,
               bd=3) \
            .grid(row=0, column=1, sticky=E)

        Button(self.root,
               text='Загрузить в базу',
               width=button_width,
               command=lambda: button_upload_to_sql(self.invoke_date),
               relief=GROOVE,
               bd=3) \
            .grid(row=0, column=0, sticky=W)

        Button(self.root,
               text='Очистить',
               width=button_width,
               command=lambda: button_clear_text_field(self.invoke_date),
               relief=GROOVE,
               bd=3) \
            .grid(row=1, column=2, sticky=E)

        Button(self.root,
               text='Очистить',
               width=button_width,
               command=lambda: button_clear_text_field(self.owner),
               relief=GROOVE,
               bd=3) \
            .grid(row=2, column=2, sticky=E)

        Button(self.root,
               text='Очистить',
               width=button_width,
               command=lambda: button_clear_text_field(self.contract_number_date),
               relief=GROOVE,
               bd=3) \
            .grid(row=3, column=2, sticky=E)

        Button(self.root,
               text='Очистить',
               width=button_width,
               command=lambda: button_clear_text_field(self.contract_cost),
               relief=GROOVE,
               bd=3) \
            .grid(row=4, column=2, sticky=E)
        # </editor-fold>

        # <editor-fold desc="message_text + edit text group">
        Message(self.root,
                text='Дата извещения о проведении приемки',
                width=message_text_width,
                font=('Consoles', 12)) \
            .grid(row=1, column=0, sticky=W)
        self.invoke_date.grid(row=1, column=1, sticky=W + E)

        Message(self.root,
                text='Владелец договора',
                width=message_text_width,
                font=('Consoles', 12)) \
            .grid(row=2, column=0, sticky=W)
        self.owner.grid(row=2, column=1, sticky=W + E)

        Message(self.root,
                text='№ договора, дата',
                width=message_text_width,
                font=('Consoles', 12)) \
            .grid(row=3, column=0, sticky=W)
        self.contract_number_date.grid(row=3, column=1, sticky=W + E)

        Message(self.root,
                text='Сумма договора, руб. с НДС',
                width=message_text_width,
                font=('Consoles', 12)) \
            .grid(row=4, column=0, sticky=W)
        self.contract_cost.grid(row=4, column=1, sticky=W + E)
        # </editor-fold>

    # this method will invoke from draw_widgets method
    def draw_menu_bar(self):
        menu_bar = Menu(self.root)
        menu_bar.add_command(label='File')
        menu_bar.add_command(label='Edit')
        menu_bar.add_command(label='Help')

        self.root.configure(menu=menu_bar)

    @staticmethod
    def menu_bar_cmd():
        messagebox.showinfo('Useless message', 'No one will help you')

    def exit_check(self):
        choice = messagebox.askyesno('Выход', 'Хотите выйти?')
        if choice:
            self.root.destroy()

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def init_information_window(self, width, height, x, y, title, resizable=(False, False)):
        InformationWindow(self.root, width, height, x, y, title, resizable)
