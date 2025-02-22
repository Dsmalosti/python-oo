from pessoa import Pessoa

p1 = Pessoa('joao', 23)
p2 = Pessoa('Gabriel', 30)

p1.falar('filme')
p2.comer('salgado')
p1.parar_falar()
p2.parar_comer()
p1.comer('salgado')
p2.falar('filme')
p3 = Pessoa.bebendo('Luiz', 'Agua')