from classes import Cliente

cliente1 = Cliente('Ana', 21)
print(cliente1.nome)
cliente1.adicionar_endereco('Taubaté', 'SP')
cliente1.lista_enderecos()
del cliente1
print()
cliente2 = Cliente('João', 33)
print(cliente2.nome)
cliente2.adicionar_endereco('Salvador', 'BA')
cliente2.adicionar_endereco('Fortaleza', 'CE')
cliente2.lista_enderecos()
del cliente2
print()
cliente3 = Cliente('Kauany', 28)
print(cliente3.nome)
cliente3.adicionar_endereco('Rio', 'RJ')
cliente3.lista_enderecos()
del cliente3
print()

print('######################################')


