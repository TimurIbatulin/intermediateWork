import json



def write(file1):
    with open('notebook.json', 'w', encoding='utf-8') as file:
        json.dump(file1, file, indent = 4)

def editing(file1):
    with open('notebook.json', 'a', encoding='utf-8') as file:
        json.dump(file1, file, indent = 4)

def read():
    with open('notebook.json', 'r', encoding = 'utf-8') as file:
        return json.load(file)
    
    
notebook = read()
for note in notebook:
        print('ID:', note)
        for key in notebook[note]:
            print(key + ':', notebook[note][key])
        print()
 