class BaseDeDados:
    def __init__(self):
        self._dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})

    def listar_clietes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)

    def apagar_cliente(self, id):
        del self._dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Stephanie')
bd.inserir_cliente(2, 'Diogo')
bd.inserir_cliente(3, 'Sofia')
bd.inserir_cliente(4, 'Leticia')
bd.apagar_cliente(4)
bd.listar_clietes()

