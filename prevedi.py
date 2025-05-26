import os
from googletrans import Translator
import sys

def translate_file(file_name, language_code, output_file):
    # če source file ne obstaja
    if not os.path.isfile(file_name):
        print(f"Error: The file '{file_name}' does not exist.")
        sys.exit(1)

    translator = Translator()

    # prebere source file
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()

    # prevede vsebino izvorne datoteke
    translated = translator.translate(text, dest=language_code)

    # preveri, če obstaja datoteka za izvoz prevoda, če ne, jo ustvari
    if not os.path.isfile(output_file):
        print(f"File '{output_file}' does not exist. Creating a new one.")
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("")  # ustvari prazno datoteko

    # zapiše prevedeno besedilo v ustrezno datoteko
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated.text)

    print(f"Translation completed. Translated file saved as '{output_file}'.")

if __name__ == "__main__":
    
    # definira imena datotek za izvod prevoda
    hr_file = "dokumentacija_hr.md"
    sr_file = "dokumentacija_sr.md"
    tr_file = "dokumentacija_tr.md"

    # zagon funkcije za prevod
    translate_file("dokumentacija.md", 'hr', hr_file)
    translate_file("dokumentacija.md", 'sr', sr_file)
    translate_file("dokumentacija.md", 'tr', tr_file)
