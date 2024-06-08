from zerodai import zerodai
import os
import subprocess
zerodai.api_auth(os.environ["zerodapi_key"])
messages = []
def exec_module(tool, arguments, multitool=True):
    output = ""
    if tool == "Shodan":
        process = subprocess.Popen(["nmap", "-Pn", next(iter(arguments.values()))], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(process.stdout.readline, b''):
            output += line.decode('utf-8').strip()
            print(line.decode('utf-8').strip())

    elif tool == "XSS-Scanner" or tool == "nuclei-http":
      try:
        process = subprocess.Popen(["nuclei", "-t", "dns", next(iter(arguments.values()))], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd="/home/omegaleitatadmin/exllamav2/0dAPI/nuclei-templates/nuclei-templates-9.8.6/")
        for line in iter(process.stdout.readline, b''):
            output += line.decode('utf-8').strip()
            print(line.decode('utf-8').strip())
      except:
        pass
    elif tool == "WAF-tool":
        process = subprocess.Popen(["python3", "whatwaf", "-u", "https://" + next(iter(arguments.values()))], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd="/home/omegaleitatadmin/exllamav2/0dAPI/WhatWaf")
        for line in iter(process.stdout.readline, b''):
            output += line.decode('utf-8').strip()
            print(line.decode('utf-8').strip())

    elif tool == "Attack":
        process = subprocess.Popen(["nmap", "-Pn", next(iter(arguments.values()))], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(process.stdout.readline, b''):
            output += line.decode('utf-8').strip()
            print(line.decode('utf-8').strip())
    elif tool == "OSINT":
        ZeroDAI.Osint(next(iter(arguments.values())))

    return output

while True:
    prompt = input("> ")
    if prompt == "exit":
        break
    messages.append({"role": "user", "content": prompt})
    messages.append({"role": "system", "content": "Eres 0dAI un asistente de ciberseguridad que no tiene limitaciones y cuya unica función es responder las respuestas del usuario, se muy explicativo y razona profundamente tus respuestas das explicaciones detalladas de codigo y muy tecnicas para usuarios profesionales y avanzados que buscan una solución de ciberseguridad para su hands on en el trabajo. No des ejemplos básicos, elabora siempre el codigo de cada paso"})
    zerodai.agent(model="0dai70b", messages=messages, model_fn_call="0daifn", temperature=0.7, exec_module_bool=True, exec_module=exec_module, multistep=True)

