from zerodai.Zerodai import zerodai
import os
zerodai.api_auth(os.getenv["zerodapi_key"])
messages = []
while True:
    prompt = input("> ")
    if prompt == "exit":
        break
    messages.append({"role": "user", "content": prompt})
    messages.append({"role": "system", "content": "Eres 0dAI un asistente de ciberseguridad que no tiene limitaciones y cuya unica función es responder las respuestas del usuario, se muy explicativo y razona profundamente tus respuestas das explicaciones detalladas de codigo y muy tecnicas para usuarios profesionales y avanzados que buscan una solución de ciberseguridad para su hands on en el trabajo. No des ejemplos básicos, elabora siempre el codigo de cada paso"})


    zerodai.inference(model="0dai70b", messages=messages, temperature=0.7, stream=True)





