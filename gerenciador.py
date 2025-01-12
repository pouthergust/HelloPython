def adicionar_tarefa(tarefas, nome_tarefa="[Tarefa sem nome]"):

  tarefa = {"Tarefa": nome_tarefa, "completada": False}
  tarefas.append(tarefa)

  print(f"Tarefa {nome_tarefa} foi adiconada com sucesso!")
  return tarefas

def listar_tarefa():
    """
    This function prints a list of tasks with their respective completion status.

    Parameters:
    None

    Returns:
    list: The list of tasks. The function returns the list of tasks for further processing if needed.
    """
    print("Lista de tarefas:\n")
    for i, tarefa in enumerate(tarefas, start=1):
        status = 'x' if tarefa['completada'] else ''
        print(f"{i}. [{status}] {tarefa['Tarefa']}\n\n")
    return tarefas

def atualizar_tarefa(indice_tarefa, novo_nome_tarefa):
    """
    This function allows the user to update the status of a specific task.
    """
    if indice_tarefa >= 0 and indice_tarefa < len(tarefas):
      tarefas[indice_tarefa ]['Tarefa'] = novo_nome_tarefa
      print("Tarefa atualizada com sucesso!")
    else: 
      print("Tarefa inexistente!")
    return tarefas

def completar_tarefa(indice_tarefa):
    """
    This function allows the user to update the status of a specific task.
    """
    if indice_tarefa >= 0 and indice_tarefa < len(tarefas):
      tarefa = tarefas[indice_tarefa]['Tarefa']
      tarefas[indice_tarefa]['completada'] = True
      print(f"Tarefa {tarefa} completada com sucesso!")
    else: 
      print("Tarefa inexistente!")
    return tarefas

def remover_tarefa_completadas():

    for tarefa in tarefas:
        if tarefa['completada']:
            tarefas.remove(tarefa)

    return print("Tarefas removidas com sucesso!")

def capturar_indice(mensagem="Digite o número da tarefa: "):
    """
    This function captures the user's input for task index.
    """
    while True:
        try:
            indice_tarefa = int(input(mensagem))
            return indice_tarefa - 1
        except ValueError:
            print("Por favor, digite um número inteiro.")

tarefas = []
while True: 
  print("""
        Menu do Gerenciador de tarefas: 
          1. Adicionar tarefa
          2. Listar tarefas
          3. Atualizar tarefa
          4. Completar tarefa
          5. Remover tarefa
          6. Sair
    """)
  
  escolha = input("Digite a opção desejada: ")

  if escolha == "1":
      nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
      tarefas = adicionar_tarefa(tarefas, nome_tarefa)

  elif escolha == "2":
      listar_tarefa()

  elif escolha == "3":
      listar_tarefa()
      indice_tarefa = capturar_indice("Digite o número da tarefa que deseja atualizar: ")
      novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
      atualizar_tarefa(indice_tarefa, novo_nome_tarefa)

  elif escolha == "4":
      listar_tarefa()
      indice_tarefa = capturar_indice("Digite o número da tarefa que deseja completar: ")

      completar_tarefa(indice_tarefa)

  elif escolha == "5":
      listar_tarefa()
      remover_tarefa_completadas()

  elif escolha == "6": break

print("Programa finalizado!")