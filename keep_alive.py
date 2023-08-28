from flask import Flask
from threading import Thread

app = Flask('')

header = "None"
body = "The next thing generated will show here!"

@app.route('/')
def home():
    return f"""<h1>Latest - {header}</h1>

    {body}
    """

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()