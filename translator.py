import os
from deep_translator import GoogleTranslator

def split_text(text, max_length=5000):
    """Rozdelí text na menšie časti"""
    parts = []
    current_part = []
    current_length = 0

    for line in text.split("\n"):
        if current_length + len(line) + 1 > max_length:
            parts.append("\n".join(current_part))
            current_part = []
            current_length = 0
        current_part.append(line)
        current_length += len(line) + 1

    if current_part:
        parts.append("\n".join(current_part))

    return parts

def translate_text(text, target_language="sk"):
    """Preloží text do cieľového jazyka"""
    return GoogleTranslator(source="auto", target=target_language).translate(text)

def translate_file(input_file, output_file, target_language="sk"):
    """Preloží obsah súboru po častiach a uloží výsledok"""
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    parts = split_text(text)
    translated_parts = [translate_text(part, target_language) for part in parts]

    translated_text = "\n".join(translated_parts)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(translated_text)

    print(f"Preložený text bol uložený do {output_file}")

# Hlavný program
input_file = input("Zadajte názov vstupného súboru (napr. questions.txt): ")
output_file = input("Zadajte názov výstupného súboru (napr. translated_questions.txt): ")

if os.path.exists(input_file):
    translate_file(input_file, output_file)
else:
    print("Chyba: Súbor neexistuje, skontrolujte názov a skúste znova.")
