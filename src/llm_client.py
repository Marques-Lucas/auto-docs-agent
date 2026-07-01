"""
llm_client: a unica parte do projeto que fala com a LLM (Groq).

Deixamos isolado DE PROPOSITO: se um dia voce trocar Groq por Gemini,
so mexe neste arquivo e o resto do agente nem percebe.

Documentacao rapida da Groq: https://console.groq.com/docs/quickstart
"""

import os
from dotenv import load_dotenv

# from groq import Groq   # TODO: descomente depois de 'pip install groq'

load_dotenv()  # carrega as variaveis do arquivo .env pra dentro do os.environ


def chamar_llm(prompt, system=None):
    """
    Manda um prompt pra Groq e devolve o TEXTO da resposta.

    Dicas de implementacao:
    1. Leia a chave:      api_key = os.getenv("GROQ_API_KEY")
    2. Leia o modelo:     modelo  = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    3. Crie o client:     client  = Groq(api_key=api_key)
    4. Monte as mensagens: uma lista de dicts com "role" e "content".
       - Se 'system' foi passado, o primeiro item e {"role": "system", "content": system}
       - Depois {"role": "user", "content": prompt}
    5. Chame:             resposta = client.chat.completions.create(model=modelo, messages=...)
    6. Retorne:           resposta.choices[0].message.content
    """
    # TODO: implementar
    pass
