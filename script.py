import openai

# Configure sua chave da API do OpenAI
openai.api_key = "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"

# Defina o prompt de entrada para o modelo GPT
prompt = "Me dê dicas de como montar um prompt em loop para gestão de um projeto de marketing"

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
