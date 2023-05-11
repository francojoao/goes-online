class Refeicao:
  def __init__(self, data_hora, popularidade):
    self.data_hora = data_hora
    self.popularidade = popularidade

  def get_data_hora(self):
    return self.data_hora
  
  def set_data_hora(self, data_hora):
    self.data_hora = data_hora

  def get_popularidade(self):
    return self.popularidade
  
  def set_popularidade(self, popularidade):
    self.popularidade = popularidade