import csv


list_dict=[]
dictionary_headers=("Name", "Genre", "Developer", "ESRB")
amount_games=int(input("Enter the amount of games you'd like to provide information on: "))
counter=0
while counter<amount_games:
    name=input("Enter the game's name: ")
    genre=input("Enter the game's genre: ")
    developer=input("Enter the game's developer: ")
    esrb=input("Enter the game's ESRB Classification: ")
    dictionary_content={"Name": name, "Genre": genre, "Developer": developer, "ESRB": esrb}
    list_dict.append(dictionary_content)
    counter=counter+1

with open("Test.tsv", 'w+', encoding='utf-8') as file:
    file = csv.DictWriter(file,dictionary_headers)
    file.writeheader() #no entiendo porqué en esta parte del código tiene que ir sin nada en los paréntesis y no de donde se están tomando los headers como tal, lo digo porque la función se llama "writeheader"
    file.writerows(list_dict)
    


