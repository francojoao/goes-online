class Professores:
  def __init__(self, nome, matricula, series_que_leciona):
    self.nome = nome
    self.matricula = matricula
    self.series_que_leciona = series_que_leciona

  def getNome(self):
    return self.nome

  def setNome(self, nome):
    self.nome = nome

  def getMatricula(self):
    return self.matricula

  def setMatricula(self, matricula):
    self.matricula = matricula

  def getSeries_que_leciona(self):
    return self.series_que_leciona

  def setSeries_que_leciona(self, series_que_leciona):
    self.series_que_leciona = series_que_leciona