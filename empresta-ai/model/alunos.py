class Alunos:
  def __init__(self, nome, matricula, ano, turma):
    self.nome = nome
    self.matricula = matricula
    self.ano = ano
    self.turma = turma

  def getNome(self):
    return self.nome

  def setNome(self, nome):
    self.nome = nome

  def getMatricula(self):
    return self.matricula

  def setMatricula(self, matricula):
    self.matricula = matricula

  def getAno(self):
    return self.ano

  def setAno(self, ano):
    self.ano = ano

  def getTurma(self):
    return self.turma

  def setTurma(self, turma):
    self.turma = turma