from flask import Flask, request, jsonify
from models.task import Task

# __name__ = "__main__"
app = Flask(__name__)

tasks = []
task_id_ctrl = 1

@app.route('/tasks', methods=['POST'])
def create_task():
  global task_id_ctrl
  data = request.get_json()
  new_task = Task(id=task_id_ctrl, title=data['title'], description=data.get('description', ''))
  task_id_ctrl += 1
  tasks.append(new_task)
  print(tasks)
  return jsonify({ "message": "Nova tarefa criada com sucesso" }), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
  task_list = [task.to_dict() for task in tasks]
  # for task in tasks:
  #   task_list.append(task.to_dict())

  output = {
    "tasks": task_list,
    "total_tasks": len(task_list)
  }

  return jsonify(output)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
  # Essa função busca uma tarefa específica pelo ID
  # Usa next() com uma generator expression para encontrar a primeira tarefa que corresponde ao ID
  # Se encontrar a tarefa, retorna ela convertida em dicionário
  # Se não encontrar, retorna erro 404 com mensagem
  task = next((task for task in tasks if task.id == task_id), None)
  if task:
    return jsonify(task.to_dict())
  else:
    return jsonify({"error": "Tarefa não encontrada"}), 404


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task.id == task_id), None)
    
    if not task:
        return jsonify({"error": "Tarefa não encontrada"}), 404
        
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    return jsonify({"message": "Tarefa atualizada com sucesso"})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return jsonify({"message": "Tarefa deletada com sucesso"})

if __name__ == '__main__':
  app.run(debug=True)