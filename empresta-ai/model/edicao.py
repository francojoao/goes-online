class Edicao:
  def __init__(self, n_de_edicao, data_de_publicacao):
    self.n_de_edicao = n_de_edicao
    self.data_de_publicacao = data_de_publicacao
  
  def getN_de_edicao(self):
    return self.n_de_edicao

  def setN_de_edicao(self, n_de_edicao):
    self.n_de_edicao = n_de_edicao

  def getData_de_publicacao(self):
    return self.data_de_publicacao

  def setData_de_publicacao(self, data_de_publicacao):
    self.data_de_publicacao = data_de_publicacao