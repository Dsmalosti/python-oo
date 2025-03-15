from classes import Escritor, Caneta

escritor = Escritor('Joao')
caneta01 = Caneta('Bic')

escritora = Escritor('Ana')
caneta02 = Caneta('Senna')


escritor.ferramenta = caneta01
escritor.ferramenta.escrever()

escritora.ferramenta = caneta02
escritora.ferramenta.escrever()