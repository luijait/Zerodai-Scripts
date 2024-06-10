from zerodai.Zerodai import zerodai
import os
zerodai.api_auth(os.environ["zerodapi_key"])
while True:
    prompt = input("> ")
    if prompt == "exit":
        break
    zerodai.Osint(prompt)
