import streamlit as st

def caesar_cipher(text, shifts):
    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            shift = shifts[i % len(shifts)] % 26
            char_code = ord(char) + shift
            if char.islower():
                if char_code > ord('z'):
                    char_code -= 26
            elif char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
            result += chr(char_code)
        else:
            result += char
    return result

def text_to_ascii(text):
    return ' '.join(str(ord(char)) for char in text)

st.title("Dla Oliwii: Szyfr Cezara z indywidualnymi przesunięciami + konwersja na ASCII")

text_input = st.text_input("Wprowadź tekst do zaszyfrowania:", "Przykładowy tekst")
shifts_input = st.text_input("Wprowadź klucz (liczby oddzielone SPACJAMI):", "5 2 3 1 9 7 3 4 1 5 3 8 9 0 7 4 5 3")

if st.button("Konwertuj", use_container_width=True):
    shifts = [int(num) for num in shifts_input.split()]
    ciphered_text = caesar_cipher(text_input, shifts)
    ascii_conversion = text_to_ascii(ciphered_text)
    st.write("Tekst po szyfrowaniu Cezarem:", ciphered_text)
    st.write("Tekst w kodzie ASCII:", ascii_conversion)
