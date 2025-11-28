import json

# načítanie zdrojového súboru
with open('alice.txt', encoding='utf-8') as file:
    text = file.read()

# vytvorenie prázdneho slovníka pre zápis hodnôt
result = {}

# postupná kontrola každého znaku v texte a počítanie počtu výskytu 
# požadovaných znakov
for letter in text.lower():
    if letter == '\n' or letter == ' ':
        pass
    else:
        result[letter] += 1

# zoradenie položiek pôvodného slovníka a vytvorenie nového slovníka
sorted = dict(sorted(result.items()))

# zápis do JSON súboru
with open("hw01_output.json", mode='w', encoding='utf-8') as output_file:
    json.dump(sorted, output_file, ensure_ascii=False, indent=4)
