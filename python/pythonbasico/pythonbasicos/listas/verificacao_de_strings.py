arquivo = 'prog.py'
print(arquivo.startswith('p'))

print(arquivo.endswith('py'))

resposta = 'Sim'
print(resposta.lower())
print(resposta.upper())
print(resposta.lower() in 'sim não yes no')

s = 'um tigre, dois tigres, três tigres'
print(s.find('tigre'))

print(s.replace('tigre', 'gato'))

txt = 'battatinha quando nasce'
print(txt.split())

data = '21/02/2011'
print(data.split('/'))

ip = '192.188.10.144'
print(ip.split('.'))

times = ['Palmeiras', 'Santos', 'Corintias']
print('/'.join(times))
