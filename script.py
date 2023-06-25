import openai

# Configure sua chave da API do OpenAI
openai.api_key = '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'

# Defina o prompt de entrada para o modelo GPT
prompt = "Escreva aqui o texto que deseja completar."

# Gere a resposta do modelo
response = openai.Completion.create(
  engine="davinci",
  prompt=prompt,
  max_tokens=100,
  temperature=0.7,
  n=1,
  stop=None,
  timeout=None
)

# Exiba a resposta gerada pelo modelo
print(response.choices[0].text.strip())
