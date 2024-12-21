import tkinter as tk
from tkinter import filedialog, messagebox
from database import Database
from person import Person


class App:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title("Управление данными о людях")

        self.root.geometry("350x250")
        self.root.resizable(False, False)

        tk.Button(root, text="Добавить запись", command=self.add_person).pack(pady=10)
        tk.Button(root, text="Найти запись", command=self.search_person).pack(pady=10)
        tk.Button(root, text="Сохранить в файл", command=self.save_to_file).pack(pady=10)
        tk.Button(root, text="Загрузить из файла", command=self.load_from_file).pack(pady=10)
        tk.Button(root, text="Выйти", command=self.root.quit).pack(pady=10)

    def add_person(self):
        """Окно для добавления новой записи."""
        def save_person():
            try:
                first_name = first_name_entry.get()
                last_name = last_name_entry.get()
                patronymic = patronymic_entry.get()
                birth_date = birth_date_entry.get()
                death_date = death_date_entry.get()
                gender = gender_var.get()

                person = Person(first_name, last_name, patronymic, birth_date, death_date, gender)
                self.db.add_person(person)
                messagebox.showinfo("Успех", "Человек добавлен!")
                add_window.destroy()
            except ValueError as e:
                messagebox.showerror("Ошибка", str(e))

        # Окно для добавления
        add_window = tk.Toplevel(self.root)
        add_window.title("Добавить запись")

        tk.Label(add_window, text="Имя:").grid(row=0, column=0, padx=10, pady=5)
        first_name_entry = tk.Entry(add_window)
        first_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(add_window, text="Фамилия:").grid(row=1, column=0, padx=10, pady=5)
        last_name_entry = tk.Entry(add_window)
        last_name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(add_window, text="Отчество:").grid(row=2, column=0, padx=10, pady=5)
        patronymic_entry = tk.Entry(add_window)
        patronymic_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(add_window, text="Дата рождения:").grid(row=3, column=0, padx=10, pady=5)
        birth_date_entry = tk.Entry(add_window)
        birth_date_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(add_window, text="Дата смерти:").grid(row=4, column=0, padx=10, pady=5)
        death_date_entry = tk.Entry(add_window)
        death_date_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(add_window, text="Пол:").grid(row=5, column=0, padx=10, pady=5)
        gender_var = tk.StringVar(value="m")
        tk.Radiobutton(add_window, text="Мужчина", variable=gender_var, value="m").grid(row=5, column=1, sticky="w")
        tk.Radiobutton(add_window, text="Женщина", variable=gender_var, value="f").grid(row=6, column=1, sticky="w")

        tk.Button(add_window, text="Сохранить", command=save_person).grid(row=7, column=0, columnspan=2, pady=10)

    def search_person(self):

        def perform_search():
            query = search_entry.get().lower()
            results = self.db.search(query)
            if results:
                result_text.delete("1.0", tk.END)
                for person in results:
                    result_text.insert(tk.END, f"{person}\n\n")
            else:
                result_text.delete("1.0", tk.END)
                result_text.insert(tk.END, "Ничего не найдено.")


        search_window = tk.Toplevel(self.root)
        search_window.title("Поиск записей")

        search_window.resizable(False, False)
        search_window.geometry("400x400")

        tk.Label(search_window, text="Введите запрос:").pack(pady=5)
        search_entry = tk.Entry(search_window)
        search_entry.pack(pady=5)

        tk.Button(search_window, text="Поиск", command=perform_search).pack(pady=5)

        result_text = tk.Text(search_window, height=15, width=80)
        result_text.pack(pady=5)

        scrollbar = tk.Scrollbar(search_window, command=result_text.yview)
        result_text.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def save_to_file(self):
        """Сохранение данных в файл."""
        filename = tk.filedialog.asksaveasfilename(defaultextension=".json",
                                                   filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")])
        if filename:
            self.db.save_to_file(filename)
            messagebox.showinfo("Успех", "Данные сохранены!")

    def load_from_file(self):
        """Загрузка данных из файла."""
        filename = tk.filedialog.askopenfilename(filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")])
        if filename:
            try:
                self.db.load_from_file(filename)
                messagebox.showinfo("Успех", "Данные загружены!")
            except FileNotFoundError:
                messagebox.showerror("Ошибка", "Файл не найден.")
