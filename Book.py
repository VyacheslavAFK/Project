from tkinter import *
from tkinter import scrolledtext
import tkinter.messagebox as messagebox
import os

def append_password():
    user_letter = []
    global Enter
    Enter = enter_0.get()
    for low in Enter:
        user_letter.extend(low.lower())
    alphabet = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l",
                "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "_"]
    a = [0]
    if not enter_0.get():
        Err.config(text="Пароль не может быть пустым!", font=("Arial", 13, "bold"))
        a[0] = 1
    for letter in user_letter:
        if letter not in alphabet:
            if letter == " ":
                letter = "пробел"
            Err.config(text='Недопустимый символ - "' + letter + '" \nПароль должен'
                ' содержать только латинские буквы A-Z, цифры от 0-9 и знаки "_", "."', font=("Arial", 13, "bold"))
            L0.config(text="Придумайте другой пароль")
            a[0] = 1
            break
    if a[0] == 0:
        file = open("password.txt", "w")
        file.write(Enter)
        file.close()

        Err.config(text="")
        Err.pack_forget()
        L0.pack_forget()
        enter_0.pack_forget()
        btn1.pack_forget()
        exit_front.pack_forget()
        main_menu_del("load")
        messagebox.showinfo("Создание пароля", "Пароль сохранён!")
# Добавление и проверка пароля

def login():
    with open("password.txt") as Ps:
        Pass = Ps.readline()
    if enter_pass.get() == Pass:
        main_menu_del("load")
        enter_pass.pack_forget()
        btn_login.pack_forget()
        go.pack_forget()
    else:
        go.config(text="Неверный пароль!", fg="Red", font=", 12")
# Окно ввода пароля для входа в приложение (если он есть)

def pass_exists():
    main_menu_del("del")
    Full.pack(pady=10)
    Exit.pack(pady=15, ipadx=103)
    reload.pack()
    delete_pass.pack(pady=15, ipadx=41)
# Окно с информацией о том что пароль для приложения уже создан

def back_to_home_from_passsave():
    Full.pack_forget()
    Exit.pack_forget()
    reload.pack_forget()
    delete_pass.pack_forget()
    Err.pack_forget()
    main_menu_del("load")
# Выход в главное меню из окна с информацией о созданном пароле для приложения

def back_to_home_from_passgen():
    L0.pack_forget()
    enter_0.pack_forget()
    btn1.pack_forget()
    Err.pack_forget()
    exit_front.pack_forget()
    main_menu_del("load")
# Выход в главное меню из вкладки создания пароля для приложения

def delete_and_refactor():
    os.remove("password.txt")
    Full.pack_forget()
    Exit.pack_forget()
    reload.pack_forget()
    delete_pass.pack_forget()
    L0.config(text="Придумайте новый пароль")
    passfound()
    exit_front.pack_forget()
# Удаление старого пароля от приложения и создание нового

def delete():
    os.remove("password.txt")
    Full.pack_forget()
    Exit.pack_forget()
    reload.pack_forget()
    delete_pass.pack_forget()
    main_menu_del("load")
# Удаления старого пароля от приложения и выход на главный экран

#################################\
A = 1 # /\                                        | Буквы +
B = 1 # || - Переменные задающие параметры пароля | Цифры +
C = 1 # \/                                        | Знаки +
def FLetters(): # Буквы - нет
    Letters.config(text="нет", command=FLetters_Yes)
    global A
    A = 0
def FLetters_Yes(): # Буквы - да
    Letters.config(text="да", command=FLetters)
    global A
    A = 1
def FNumbers(): # Цифры - нет
    Numbers.config(text="нет", command=FNumbers_Yes)
    global B
    B = 0
def FNumbers_Yes(): # Цифры - да
    Numbers.config(text="да", command=FNumbers)
    global B
    B = 1
def FSymbols(): # Знаки - нет
    Symbols.config(text="нет", command=FSymbols_Yes)
    global C
    C = 0
def FSymbols_Yes(): # Знаки - да
    Symbols.config(text="да", command=FSymbols)
    global C
    C = 1
#################################/

def generation():
    print(A, B, C)
    global X
    if not sim.get():
        Err.config(text="Введите длину пароля", font=("Arial", 14, "bold"))
        Err.place(anchor=N, relx=0.5, y=375)
    X = int(sim.get())
    if X > 40:
        Err.config(text="максимальная длина\nпароля - 40 символов")
        Err.place(anchor=N, relx=0.5, y=375)
    elif X < 1:
        Err.config(text="некореткное значение")
        Err.place(anchor=N, relx=0.5, y=375)
    elif ((A & B == 1 and C == 0) or (B & C == 1 and A == 0) or (A & C == 1 and B == 0)) and X < 2:
        Err.config(text="Длина пароля не может быть\n меньше 2-х символов")
        Err.place(anchor=N, relx=0.5, y=375)
    elif (A & B & C == 1) and X < 3:
        Err.config(text="Длина пароля не может быть\n меньше 3-х символов")
        Err.place(anchor=N, relx=0.5, y=375)
    else:
        Err.place_forget()
        randpass(X)
        check_list_components()
        print(X)
# Сохранение длины пароля, проверка на допустимость зачения (+ ошибки) и передача Х в функцию для генерации пароля

def randpass(qantity):
    from random import randint
    global rand
    rand = []

    global alp
    alp = {1: "q", 2: "w", 3: "e", 4: "r", 5: "t", 6: "y", 7: "u", 8: "i", 9: "o", 10: "p", 11: "a", 12: "s",
           13: "d", 14: "f", 15: "g", 16: "h", 17: "j", 18: "k", 19: "l", 20: "z", 21: "x", 22: "c", 23: "v",
           24: "b", 25: "n", 26: "m", 27: "!", 28: "@", 29: "#", 30: ".", 31: "-", 32: "_", 33: "-", 34: "+",
           35: "=", 36: "?", 37: ";"}

    for i in range(qantity):
        if A == 1 and B == 0 and C == 0:
            capitalize = randint(0, 1)
            if capitalize == 1:
                rand.append(alp[randint(1, 26)])
            if capitalize == 0:
                rand.append(alp[randint(1, 26)].capitalize())

        if B == 1 and A == 0 and C == 0:
            rand.append(str(randint(0, 9)))

        if C == 1 and A == 0 and B == 0:
            rand.append(alp[randint(27, 37)])

        if A & B == 1 and C == 0:
            ot = randint(0,1)
            if ot == 1:
                rand.append(str(randint(0, 9)))
            if ot == 0:
                capitalize = randint(0, 1)
                if capitalize == 1:
                    rand.append(alp[randint(1, 26)])
                if capitalize == 0:
                    rand.append(alp[randint(1, 26)].capitalize())

        if A & B & C == 1:
            frand = randint(0,1)
            if frand == 1:
                rand.append(str(randint(0, 9)))
            if frand == 0:
                capitalize = randint(0, 1)
                if capitalize == 1:
                    rand.append(alp[randint(1, 37)])
                if capitalize == 0:
                    rand.append(alp[randint(1, 37)].capitalize())

        if B & C == 1 and A == 0:
            frand = randint(0, 1)
            if frand == 1:
                rand.append(str(randint(0, 9)))
            if frand == 0:
                rand.append(alp[randint(27, 37)])

        if A & C == 1 and B == 0:
            capitalize = randint(0, 1)
            if capitalize == 1:
                rand.append(alp[randint(1, 37)])
            if capitalize == 0:
                rand.append(alp[randint(1, 37)].capitalize())
    return rand
# Генерация пароля в зависимости от параметров

def check_list_components():
    global pass_join
    pass_join = "".join(rand)
    while True:
        has_letters = False
        has_digits = False
        has_symbols = False
        for item in rand:
            if item.isalpha():
                has_letters = True
            elif item.isdigit():
                has_digits = True
            else:
                has_symbols = True

        if A & B & C == 1:
            if not has_letters or not has_digits or not has_symbols:
                randpass(X)
                print("В этом списке нет букв, цифр или знаков")
            else:
                print("В списке присутствуют буквы, цифры и знаки")
                pass_join = "".join(rand)
                out.config(text=pass_join)
                break

        elif A & B == 1 and C == 0:
            if not has_letters or not has_digits:
                randpass(X)
                print("В этом списке нет букв или цифр")
            else:
                print("В списке присутствуют буквы и цифры")
                pass_join = "".join(rand)
                out.config(text=pass_join)
                break

        elif A & C == 1 and B == 0:
            if not has_letters or not has_symbols:
                randpass(X)
                print("В этом списке нет букв или знаков")
            else:
                print("В списке присутствуют буквы и знаки")
                pass_join = "".join(rand)
                out.config(text=pass_join)
                break

        elif B & C == 1 and A == 0:
            if not has_digits or not has_symbols:
                randpass(X)
                print("В этом списке нет цифр или знаков")
            else:
                print("В списке присутствуют цифры и знаки")
                pass_join = "".join(rand)
                out.config(text=pass_join)
                break
        else:
            out.config(text=pass_join)
            break
# Проверка пароля на соответствие параметрам

def on_canvas_configure(event): # ?
    canvas.configure(scrollregion=canvas.bbox("all"))

def pass_open():
    pass_menager.place_forget()
    main_menu_del("del")

    global canvas
    canvas = Canvas(window)
    canvas.pack(side=LEFT, pady=50, fill=BOTH, expand=True)
    global scrollbar
    scrollbar = Scrollbar(window, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=canvas.yview)
    content_frame = Frame(canvas)
    content_frame.pack()

    canvas.create_window(0, 0, anchor="nw", window=content_frame)
    canvas.bind("<Configure>", on_canvas_configure)

    clear.place(anchor=SE, y=595, x=377)
    copy_info.place(anchor=NW, x=5, y=14)
    global labels
    labels = []
    global safe
    save_pass = open("Data_Pass")
    lenght = len(save_pass.readlines())
    save_pass.close()
    save_pass = open("Data_Pass")
    for i in range(1,(int(lenght / 2) + 1)):
        line1 = save_pass.readline()
        line2 = save_pass.readline().strip()
        print("от чего:", line1)
        print("пароль:", line2, "\n\n")
        safe = Label(content_frame, bg="Light Gray", text=f"{line1}\nпароль: {line2}",
                     bd=10, font=("Arial", 16, "bold"), relief="ridge", width=27, wraplength=340)
        safe.pack(pady=4, padx=4)
        safe.bind("<Button-1>", copy_to_clipboard)
        safe.bind("<Enter>", lambda event: event.widget.config(bg="Gray"))
        safe.bind("<Leave>", lambda event: event.widget.config(bg="Light Gray"))
        password = line2
        labels.append(safe)
    for safe, copy in zip(labels, range(len(labels))):
        safe.update()
        x_p = safe.winfo_x()
        y_p = safe.winfo_y()
        delete_pass = Button(content_frame, bg="Light Gray", width=2, command=None)
        delete_pass.place(anchor=NW, x=x_p + 12, y=y_p + 12)
    print(list(zip(labels, range(len(labels)))))
    save_pass.close()
# Вывод паролей в прокручивающееся окно

def copy_to_clipboard(event):
    full_text = event.widget.cget("text")
    lines = full_text.split("\n")
    if len(lines) >= 3:
        password = lines[2][8:]
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Копирование", "Пароль скопирован!")
# Копирование пароля

def remove_duplicates():
    canvas.pack_forget()
    scrollbar.pack_forget()
    clear.place_forget()
    copy_info.place_forget()
    main_menu_del("load")
    for dup in range(len(labels)):
        labels[dup].pack_forget()
# Закрытие окна с паролями

def passfound():
    try:
        test = open("password.txt")
        test.close()
    except FileNotFoundError:
        main_menu_del("del")
        L0.config(text="Придумайте пароль")
        L0.pack(pady=4)
        enter_0.pack(pady=4)
        enter_0.focus()
        exit_front.pack(side=BOTTOM, pady=40)
        btn1.pack(pady=6)
        Err.config(text="")
        Err.pack()
    else:
        pass_exists()
# Проверка наличия пароля и дальнейщий переход

def main_menu_del(del_or_load):
    if del_or_load == "del":
        out.place_forget()
        lock.pack_forget()
        Gen.pack_forget()
        L_choise.place_forget()
        N_choise.place_forget()
        S_choise.place_forget()
        Letters.place_forget()
        Numbers.place_forget()
        Symbols.place_forget()
        Qantity_sim.place_forget()
        sim.place_forget()
        pass_menager.place_forget()
        password_saving.place_forget()
    if del_or_load == "load":
        lock.pack(anchor=NE, padx=12, pady=13.6)
        Gen.pack(pady=60)
        out.place(x=10, y=17)
        Letters.place(anchor=W, y=200, x=28, relx=0.5)
        L_choise.place(anchor=E, y=200, x=26, relx=0.5)
        Numbers.place(anchor=W, y=230, x=28, relx=0.5)
        N_choise.place(anchor=E, y=230, x=26, relx=0.5)
        Symbols.place(anchor=W, y=260, x=28, relx=0.5)
        S_choise.place(anchor=E, y=260, x=26, relx=0.5)
        Qantity_sim.place(anchor=E, y=305, relx=0.515)
        sim.place(anchor=W, y=305, relx=0.538)
        sim.focus()
        pass_menager.place(anchor=SW, y=590, x=10)
        password_saving.place(anchor=N, relx=0.5, y=335)
# Удаление или размещение главного экрана

def pass_saver():
    try:
        pass_join
    except NameError:
        Err.config(text="сначала сгенерируйте\n пароль", font=("Arial", 14, "bold"))
        Err.place(anchor=N, relx=0.5, y=375)
    else:
        Err.place_forget()
        global child_window
        child_window = Toplevel(window)
        child_window.geometry("200x160")
        child_window.resizable(width=False, height=False)
        child_window.title("подтверждение")
        global give_name
        global name_pass
        give_name = Entry(child_window, font="Arial, 15", bg="Light Gray", width=16)
        name_pass = Label(child_window, text="oт чего этот пароль?", font="Arial, 14")
        not_save = Button(child_window, text="отмена", font="Arial, 12", bg="Light Gray", command=exit_from_save)
        save_name = Button(child_window, text="готово", font="Arial, 12", bg="Light Gray", command=save)
        name_pass.pack()
        give_name.focus()
        give_name.pack(pady=10)
        save_name.place(anchor=SW, y=155, x=5)
        not_save.place(anchor=SE, y=155, x=195)
# Открытие окна для охранения сгенерированного пароля (если out не пустое)

def save():
    if not give_name.get():
        name_pass.config(text="введите название!", fg="Red", font="bold")
    elif len(give_name.get()) > 16:
        name_pass.config(text="длинна не может\n быть больше\n 16 символов!", fg="Red", font=10)
    else:
        name = give_name.get()
        child_window.destroy()
        save_pass = open("Data_Pass", "a")
        save_pass.write(f"{name}\n{pass_join}\n")
        save_pass.close()
# Сохранение пароля (+ошибки)

def exit_from_save(): # Выход из окна сохранения сгенерированного пароля
    child_window.destroy()


# Виджеты:
window = Tk()
window.geometry("400x600")
window.resizable(height=False, width=False)
window.title("Генератор паролей")


L0 = Label(window, font="Arial, 18", text="Придумайте пароль")                          # /\
                                                                                        # ||
btn1 = Button(window, text="Создать пароль", command=append_password, font="Arial 16",  # ||
    width=20, bg="Light Gray", activebackground="Gray")                                 # ||
                                                                                        # ||
Err = Label(window, font=("Arial", 13, "bold"), text="", wraplength=300, fg="Red")      # ||
                                                                                        # || - Создание пароля
enter_0 = Entry(window, font="Arial, 20", width=22)                                     # ||
                                                                                        # ||
L_and = Label(window, text="Пароль сохранён!", font=("Arial", 20, "bold"), fg="Green")  # ||
                                                                                        # ||
exit_front = Button(window, text="Назад", command=back_to_home_from_passgen,            # ||
                    bg="Light gray", font="Arial 16")                                   # \/



lock = Button(window, command=passfound, bg="Light Gray", width=4, height=2)                    # /\
lock.pack(anchor=NE, padx=12, pady=13.6)                                                        # ||
                                                                                                # ||
Gen = Button(window, text="cгенерировать пароль", command=generation,                           # ||
             font=("Arial", 16, "bold"), bg="Light Gray")                                       # ||
Gen.pack(pady=60)                                                                               # ||
                                                                                                # ||
out = Label(window, font="Arial, 20", bg="Light Gray", width=20, wraplength=300)                # ||
out.place(x=10, y=17)                                                                           # ||
                                                                                                # ||
Letters = Button(window, text="да",command=FLetters, bg="Light gray", width=3)                  # ||
Letters.place(anchor=W, y=200, x=28, relx=0.5)                                                  # ||
                                                                                                # ||
L_choise = Label(window, text="буквы", font=("Arial", 13, "bold"), bg="Light Gray", width=8)    # ||
L_choise.place(anchor=E, y=200, x=26, relx=0.5)                                                 # ||
                                                                                                # ||
Numbers = Button(window, text="да",command=FNumbers, bg="Light gray", width=3)                  # ||
Numbers.place(anchor=W, y=230, x=28, relx=0.5)                                                  # ||
                                                                                                # ||
N_choise = Label(window, text="цифры", font=("Arial", 13, "bold"), bg="Light Gray", width=8)    # ||
N_choise.place(anchor=E, y=230, x=26, relx=0.5)                                                 # ||
                                                                                                # ||
Symbols = Button(window, text="да",command=FSymbols, bg="Light gray", width=3)                  # ||
Symbols.place(anchor=W, y=260, x=28, relx=0.5)                                                  # || - Главное меню
                                                                                                # ||
S_choise = Label(window, text="символы", font=("Arial", 13, "bold"),                            # ||
                 bg="Light Gray", width=8)                                                      # ||
                                                                                                # ||
S_choise.place(anchor=E, y=260, x=26, relx=0.5)                                                 # ||
                                                                                                # ||
Qantity_sim = Label(window, text="длина\nпароля", font=("Arial", 13, "bold"),                   # ||
                    bg="Light Gray")                                                            # ||
Qantity_sim.place(anchor=E, y=305, relx=0.515)                                                  # ||
                                                                                                # ||
sim = Entry(window, width=2, font="Arial, 27")                                                  # ||
sim.place(anchor=W, y=305, relx=0.538)                                                          # ||
                                                                                                # ||
pass_menager = Button(window, bg="Light Gray", font=("Arial", 12, "bold"),                      # ||
                      text="пароли", command=pass_open)                                         # ||
pass_menager.place(anchor=SW, y=590, x=10)                                                      # ||
                                                                                                # ||
password_saving = Button(window, text="сохранить пароль", font=("Arial", 14, "bold"),           # ||
                         bg="Light Gray", command=pass_saver)                                   # ||
password_saving.place(anchor=N, relx=0.5, y=335)                                                # \/


enter_pass = Entry(window, font="Arial, 25", width=18)                          # /\
                                                                                # ||
go = Label(window, text="Введите пароль")                                       # ||
                                                                                # || - меню входа
btn_login = Button(window, text="Войти", command=login, font="Arial 16",        # ||
                   width=10, bg="Light Gray", activebackground="Gray")          # \/



Full = Label(window, text="У вас уже есть пароль :-)", font="Arial, 20")                  # /\
                                                                                          # ||
Exit = Button(window, text="выход", command=back_to_home_from_passsave,                   # ||
              bg="Light Gray", font="Arial, 20")                                          # ||
                                                                                          # ||
reload = Button(window, text="создать новый пароль", command=delete_and_refactor,         # || - Если уже есть пароль
                bg="Light Gray", font="Arial, 20")                                        # ||
                                                                                          # ||
delete_pass = Button(window, text="удалить пароль", bg="Light Gray",                      # ||
                     font="Arial, 20", command=delete)                                    # \/


clear = Button(window, text="выход", font="Arial, 14", bg="Light Gray",                 # /\
               command=remove_duplicates)                                               # || - Менеджер паролей
                                                                                        # ||
copy_info = Label(window, text="ЛКМ - скопировать", font=("Arial", 16, "bold"))         # \/


try:    # Проверка наличия пароля от приложения
    file = open("password.txt")
    file.close()
except FileNotFoundError:
    pass
else:
    enter_pass.pack(pady=6)
    enter_pass.focus()
    btn_login.pack(pady=6)
    go.pack()
    main_menu_del("del")

window.mainloop()
