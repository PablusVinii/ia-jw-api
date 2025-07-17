from fastapi import FastAPI, Request
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/gerar-discurso")
async def gerar_discurso(req: Request):
    dados = await req.json()
    tema = dados.get("tema", "")
    tipo = dados.get("tipo_discurso", "")

    prompt = f"Crie um esboço sobre o tema: {tema}, no estilo: {tipo}. Seja claro, objetivo, e use textos bíblicos."

    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )

    return {"texto": resposta["choices"][0]["message"]["content"]}
