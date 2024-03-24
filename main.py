import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        termine = input("Quale parola vuoi aggiungere?")
        print(termine.split(" "))
        t.handleAdd(termine.split(" ", 1))
        print("Aggiunta!")
    if int(txtIn) == 2:
        termine = input("Quale parola vuoi tradurre?")
        print(t.handleTranslate(termine))
    if int(txtIn) == 3:
        termine = input("Inserisci la wild card: ")
        wild = t.handleWildCard(termine)
        print(wild[0])
        if len(wild)>1:
            print(wild[1])
    if int(txtIn) == 4:
        break
