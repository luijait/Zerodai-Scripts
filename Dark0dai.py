from Zerodai import ZeroDAI
ZeroDAI.api_auth(os.environ["0dAPI_KEY"])
messages = []
while True:
    prompt = input("> ")
    if prompt == "exit":
        break
    ZeroDAI.Osint(prompt)



