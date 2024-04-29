# FASTAPI-Tarefa

# API de gerenciamento de tarefas
Esta é uma API simples para gerenciar tarefas. 

A API utiliza o framework FastAPI em Python.

# Instalação
Após ter dado git clone no projeto, para executar, você precisará do Python instalado em seu sistema. 

Em seguida, instale as dependências usando o pip:
- pip install fastapi uvicorn

# Para iniciar o servidor da API, execute o seguinte comando:
- uvicorn main:app --reload

Isso iniciará o servidor na porta padrão 8000. 
Você pode acessar a documentação interativa da API em http://127.0.0.1:8000/docs.

# Endpoints
Listar Tarefas
- URL: /tarefas/
- Método: GET
- Resposta de Sucesso: Lista de todas as tarefas.

Adicionar Tarefa
- URL: /tarefas/
- Método: POST
- Corpo da Requisição: JSON com os campos "titulo" (string) e "concluida" (boolean).
- Resposta de Sucesso: Retorna os detalhes da tarefa adicionada.

Editar Tarefa
- URL: /tarefas/{tarefa_id}
- Método: PUT
- Parâmetros de Path: tarefa_id (int) - ID da tarefa a ser editada.
- Corpo da Requisição: JSON com os campos "titulo" (string) e "concluida" (boolean).
- Resposta de Sucesso: Retorna os detalhes da tarefa editada.

Excluir Tarefa
- URL: /tarefas/{tarefa_id}
- Método: DELETE
- Parâmetros de Path: tarefa_id (int) - ID da tarefa a ser excluída.
- Resposta de Sucesso: Retorna uma mensagem indicando que a tarefa foi excluída com sucesso.
