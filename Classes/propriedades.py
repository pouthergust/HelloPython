class ContaBancaria: 
  def __init__(self, saldo=None):
    self.__saldo = saldo

  @property # Permite acesso ao método de abstraída, ou seja, podemos acessa-lo como uma propriedade de fato
  def saldo(self):
      return self.__saldo or 0
  
  @saldo.setter # Podemos adicionar um setter para alterar o valor da propriedade
  def saldo(self, value):
      self.__saldo += value
    
  @saldo.deleter # Podemos adicionar um deleter para esaldocluir o valor da propriedade
  def saldo(self):
      self.__saldo = 0
  
conta = ContaBancaria(10)
print(conta.saldo)
conta.saldo = 5
print(conta.saldo)
# del conta.x
# print(conta.x)