from zerodai import zerodai
ZeroDAI.api_auth(os.environ["zerodapi_key"])
messages = []
while True:
    prompt = input("> ")
    if prompt == "exit":
        break
    ZeroDAI.Osint(prompt)



