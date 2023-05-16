class Funcionarios:
  def __init__(self, nome, cargo, matricula, setor):
    self.nome = nome
    self.cargo = cargo
    self.matricula = matricula
    self.setor = setor

  def getNome(self):
    return self.nome

  def setNome(self, nome):
    self.nome = nome

  def getCargo(self):
    return self.cargo

  def setCargo(self, cargo):
    self.cargo = cargo

  def getMatricula(self):
    return self.matricula

  def setMatricula(self, matricula):
    self.matricula = matricula

  def getSetor(self):
    return self.setor

  def setSetor(self, setor):
    self.setor = setor
    