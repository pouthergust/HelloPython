class Estudante:
  # Variaveis de classe
  escola = "DIO"

  def __init__(self, nome, matricula) -> None:
    # Variaveis de instancia
    self.__nome = nome
    self.__matricula = matricula

  def __str__(self):
    return f'{self.__nome} ({self.__matricula}) - {self.escola}'
  
print(Estudante("Gabriel", 123))