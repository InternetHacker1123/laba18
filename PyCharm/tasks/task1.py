#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def extract_quotes_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        quotes = []
        in_quote = False
        current_quote = ""

        for char in text:
            if char == '"':
                if in_quote:
                    quotes.append(current_quote)
                    current_quote = ""
                    in_quote = False
                else:
                    in_quote = True
            elif in_quote:
                current_quote += char

        for quote in quotes:
            print(quote)


if __name__ == "__main__":

    file_path = "path/to/your/file.txt"
    extract_quotes_from_file(file_path)
