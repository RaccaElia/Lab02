from dictionary import Dictionary
class Translator:

    def __init__(self):
        self._dic = Dictionary()

    def printMenu(self):
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Exit")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        self._dic.clear()
        infile = open(dict, "r")
        for line in infile:
            self._dic.addWord(line.strip())
        infile.close()

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        if not entry[0].isalpha():
            print("Si accettano solo caratteri alfabetici")
        else:
            for trad in entry[1].split(" "):
                if not trad.isalpha():
                    print("Si accettano solo caratteri alfabetici")
                    break
                str = entry[0]+" "+trad
                self._dic.addWord(str)
                try:
                    infile = open("dictionary.txt", "a")
                    infile.write("\n"+str)
                    infile.close()
                except IOError:
                    print("Si è verificato un errore")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        return self._dic.translate(query.lower())

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        return self._dic.translateWordWildCard(query)