import os

def convertir_a_utf8(filepath):
    with open(filepath, 'r', encoding='latin-1') as file:
        contenido = file.read()
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(contenido)

for root, dirs, files in os.walk('docs'):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            convertir_a_utf8(filepath)
            print(f"Archivo convertido a UTF-8: {filepath}")
