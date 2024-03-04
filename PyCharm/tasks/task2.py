#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def remove_comments(source_file, destination_file):
    try:
        with open(source_file, 'r') as file:
            lines = file.readlines()

        with open(destination_file, 'w') as file:
            for line in lines:
                if '#' in line:
                    # Удаляем все после символа #
                    line = line[:line.index('#')]
                file.write(line)
    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Запрос имени файла источника у пользователя
source_file = input("Введите имя файла источника: ")

# Запрос имени файла назначения у пользователя
destination_file = input("Введите имя файла назначения: ")

if __name__ == "__main__":
    remove_comments(source_file, destination_file)
