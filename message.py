class Message :
    def __init__(self, mittente, destinatario,):
        self._mittente = mittente
        self._destinatario = destinatario
        self._corpoMessaggio = []

    def append(self, dettato):
         self._corpoMessaggio.append(dettato)
    
    def toString(self):
        valore= "Mittente: \n  "+ self._mittente + "\nDestinatario:\n  "+ self._destinatario + "\nMeassaggio: \n  "+ "\n  ".join(self._corpoMessaggio)
        return valore






messaggio = Message("Massimo", "Andrea")
messaggio.append("ciao")
messaggio.append("oggi è una bella giornta")
messaggio.append("tanti saluti")
messaggio.append("grigio")

print(messaggio.toString())