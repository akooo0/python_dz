import os
import shutil

def create_file(file_path):
    try:
        with open(file_path, 'w'):
            print(f"Файл {file_path} успешно создан.")
    except Exception as e:
        print(f"Ошибка при создании файла {file_path}: {e}")

def create_folder(folder_path):
    try:
        os.makedirs(folder_path)
        print(f"Папка {folder_path} успешно создана.")
    except Exception as e:
        print(f"Ошибка при создании папки {folder_path}: {e}")

def delete_file_or_folder(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"Файл {path} успешно удален.")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Папка {path} успешно удалена.")
        else:
            print(f"Файл или папка по пути {path} не существует.")
    except Exception as e:
        print(f"Ошибка при удалении {path}: {e}")

def move_or_copy(src, dest, is_copy=False):
    try:
        if is_copy:
            if os.path.isfile(src):
                shutil.copy(src, dest)
                print(f"Файл {src} успешно скопирован в {dest}.")
            elif os.path.isdir(src):
                shutil.copytree(src, dest)
                print(f"Папка {src} успешно скопирована в {dest}.")
            else:
                print(f"Файл или папка по пути {src} не существует.")
        else:
            shutil.move(src, dest)
            print(f"Файл или папка {src} успешно перемещена в {dest}.")
    except Exception as e:
        print(f"Ошибка при перемещении/копировании: {e}")

# Пример использования
if __name__ == "__main__":
    while True:
        print("\nВыберите операцию:")
        print("1. Создать файл")
        print("2. Создать папку")
        print("3. Удалить файл или папку")
        print("4. Переместить файл или папку")
        print("5. Скопировать файл или папку")
        print("0. Выйти")

        choice = input("Введите номер операции: ")

        if choice == "1":
            file_path = input("Введите путь и имя файла: ")
            create_file(file_path)
        elif choice == "2":
            folder_path = input("Введите путь и имя папки: ")
            create_folder(folder_path)
        elif choice == "3":
            path_to_delete = input("Введите путь к файлу или папке для удаления: ")
            delete_file_or_folder(path_to_delete)
        elif choice == "4":
            source_path = input("Введите путь к файлу или папке для перемещения: ")
            dest_path = input("Введите путь перемещения: ")
            move_or_copy(source_path, dest_path)
        elif choice == "5":
            source_path = input("Введите путь к файлу или папке для копирования: ")
            dest_path = input("Введите путь копирования: ")
            move_or_copy(source_path, dest_path, is_copy=True)
        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите существующую операцию.")
