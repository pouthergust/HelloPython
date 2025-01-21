class Bicicleta:
  def __init__(self, cor, modelo, ano, valor): 
    # pass
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor

  def buzinar(self):
    print("BEEP!")

  def parar(self):
    print("Parando...")

  def correr(self):
    print("Correndo...")
  
  # def __str__(self):
  #   return f"""
  #     Bicicleta: {self.modelo} 
  #     Cor: {self.cor} 
  #     Ano: {self.ano} 
  #     Valor: {self.valor}
  #   """
  
  def __str__(self):
    return f"""
    {self.__class__.__name__}
    {''.join([f"""{chave}: {valor}\n""" for chave, valor in self.__dict__.items()])}      
    """

caloi = Bicicleta("vermelha", "caloi", 2022, 600)

caloi.buzinar() # Bicicleta.buzinar(caloi)

caloi.correr() # Bicicleta.correr(caloi)

caloi.parar() # Bicicleta.parar(caloi)

print(caloi.__str__()) # Bicicleta.__str__(caloi)


class Veiculo():
  def __init__(self, cor, placa, numero_rodas):
    self.cor = cor
    self.placa = placa
    self.numero_rodas = numero_rodas