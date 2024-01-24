import tkinter as tk
import tkinter.messagebox as messagebox

# Функция для копирования текста в буфер обмена
def copy_to_clipboard():
    root.clipboard_clear()  # Очистка буфера обмена
    root.clipboard_append("Текст для копирования")  # Добавление текста в буфер обмена

    # Опционально: Всплывающее сообщение об успешном копировании
    messagebox.showinfo("Копирование", "Текст успешно скопирован в буфер обмена!")

# Создание главного окна Tkinter
root = tk.Tk()

# Создание кнопки
copy_button = tk.Button(root, text="Копировать", command=copy_to_clipboard)
copy_button.pack()

# Запуск главного цикла обработки событий
root.mainloop()
