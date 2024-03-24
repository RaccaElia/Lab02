class Dictionary:
    def __init__(self):
        self._dic = {}

    def __str__(self):
        str = ""
        for (key, val) in self._dic.items():
            str += f"{key} = {val}; "
        return str

    def clear(self):
        self._dic.clear()

    def addWord(self, stringa):
        termini = stringa.split(" ")
        if termini[0] in self._dic and termini[1]==self._dic[termini[0]]:
            pass
        else:
            if termini[0].lower() not in self._dic:
                self._dic[termini[0].lower()] = []
            self._dic[termini[0].lower()].append(termini[1].lower())

    def translate(self, parola):
        '''ris = []
        for (alien, ita) in self._dic.items():
            if parola.lower() == alien:
                ris.append(ita)
        if ris == []:
            return "Parola non trovata"
        return ris'''
        return self._dic.get(parola, "Parola non trovata")

    def translateWordWildCard(self, wild):
        ris = []
        for alien in self._dic:
            if len(wild) == len(alien) and wild.split("?")[0].lower() in alien.lower() and wild.split("?")[1].lower() in alien.lower():
                ris.append(alien)
                ris.append(self.translate(alien))
                return ris
        if ris == []:
            ris.append("Parola non trovata")
        return ris