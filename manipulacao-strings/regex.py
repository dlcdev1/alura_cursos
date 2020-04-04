import re

email1 = "Meu numero é 12134-1234"
email2 = "Fale comigo em 1234-1234"
email3 = "1234-1234 é o meu celular"
email4 = "number 995431254 llllslsll 987611234 new number 9876-1234"

padrao = "[0-9]{4,5}[-]*[0-9]{4}"

retorno = re.findall(padrao, email1)
print(retorno)

x = 200

print(len(x))

def __len__(self):
    return len(self)