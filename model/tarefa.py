from database import Database 

class Tarefa:
    def __init__(self, titulo, data_conclusao, id):
        self.titulo = titulo
        self.id = id
        self.data_conclusao = data_conclusao

    def salvarTarefa(self):
        """Salva uma nova tarefa no banco de dados!?"""
        db = Database()
        db.connectar()

        sql = 'INSERT INTO tarefa (titulo, data_conclusao) VALUES (%s, %s)'
        params = (self.titulo, self.data_conclusao)
        db.executar(sql, params)
        db.desconectar()

    def listarTarefa():
        """Retornar uma lista com todas as tarefas..."""
        db = Database()
        db.connectar()

        sql = 'SELECT id, titulo, data_conclusao FROM tarefa'
        tarefas = db.consultar(sql)
        db.desconectar()
        return tarefas if tarefas else []

    def apagarTarefa(self):
        """Apaga uma tarefa cadastrada no banco de dados?"""
        db = Database()
        db.conectar()

        sql = 'DELETE FROM tarefa WHERE id = %s'
        params = (self.id,) # Precisa ser uma tupla?
        db.executar(sql, params)
        db.desconectar()

tarefa = Tarefa(2, 'Teste de tarefa', None)
tarefa.apagarTarefa()