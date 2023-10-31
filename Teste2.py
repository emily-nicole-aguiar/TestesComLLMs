import openai

openai.api_key = 'YOU-KEY-API'

# Prompt para gerar scripts de teste
prompt = """
I want you to act as an expert Python programmer. 
Task 1: Please review the following API documentation 
for networkx.find_cycle
Task 2: Use the Python library hypothesis to write a 
function that generates random values for the 
networkx.Graph object.
"""
#Gera uma resposta com base em um único prompt de entrada do usuário. 
response = openai.ChatCompletion.create( model="gpt-4", messages=[{"role": "user", "content": prompt}])
#Conversa mais complexa e interativa
#response = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}

# Obtém a resposta do modelo
message = response.choices[0].message['content']

# Imprime o script gerado
print("Script de Teste Gerado:")
print(message)
