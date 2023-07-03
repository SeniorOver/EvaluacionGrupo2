import openai
from pydantic import BaseModel

class Document(BaseModel):
    prompt: str = ''

def inference(prompt: str) -> list:
    #token creado en este momento con correo de efcazan@uce.edu.ec
    openai.organization = 'org-Q2H3HSYHfhYH1R3rqBi9Z2e7'
    openai.api_key = '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'
    print('[PROCESANDO]'.center(40, '-'))

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres una calculadora factorial, cada que un numero ingrese me calculas el factorial y si es texto muestrame un error que diga "syntax error""
            E.G: 10
            -claro el factorial de 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800.
            E.G: hola
            - syntax error"""
             },
            {"role": "user", "content": prompt}
        ]
    )

    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens
    print('[SE TERMINÓ DE PROCESAR]'.center(40, '-'))
    print("Tokens utilizados: " + total_tokens)
    return [content, total_tokens]