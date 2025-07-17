from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

app = FastAPI(
    title="IA JW API",
    version="1.0",
    docs_url="/docs",       # Isso ativa o Swagger UI
    redoc_url="/redoc",     # Isso ativa o Redoc (opcional)
)

# 🔐 Habilita CORS para qualquer origem (ou especifique seu domínio do Vercel)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ia-jw-talks-y1ki.vercel.app"],  # substitua por ["https://seuprojeto.vercel.app"] se quiser mais seguro
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
