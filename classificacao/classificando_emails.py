#!-*- coding: utf8 -*-

texto1 = "Se eu comprar cinco anos antecipados, eu ganho algum desconto?"
texto2 = "O exercício 15 do curso de Java 1 está com a resposta errada. Pode conferir pf?"
texto3 = "Existe algum curso para cuidar do marketing da minha empresa?"


import pandas as pd
classificacoes = pd.read_csv('emails.csv')
textosPuros = classificacoes['email']

print(classificacoes)


