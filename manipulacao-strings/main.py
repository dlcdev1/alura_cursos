from ExtratorArgumentosUrl import ExtratorArgumentosUrl
'''
argumento = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valva=1500"
subString = argumento[:]
print(subString)
'''

url = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar"
# print(ExtratorArgumentosUrl.urlEhValida(url))

argumentosUrl = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()

print(moedaOrigem, moedaDestino)

