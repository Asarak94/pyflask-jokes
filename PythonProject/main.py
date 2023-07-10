import json
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/jokes/', methods=['GET'])
def joke():
    number = request.args.get('num')
    jokesarray = '[{"joke":"How do you catch a squirrel? Climb a tree and act like a nut!"}, \
                 {"joke":"Why dont eggs tell jokes? Because they might crack up!"},\
                 {"joke":"Why was the math book sad? Because it had too many problems!"}, \
                 {"joke":"What do you call a fish with no eyes? A fsh!"}, \
                 {"joke":"What did one wall say to the other wall? I will meet you at the corner!"},\
                 {"joke":"What do you call a bear with no teeth? A gummy bear!"}, \
                 {"joke":"Why did the calendar go on a diet? It had too many dates!"},\
                 {"joke":"Why did the computer take a nap? It had a hard drive!"},\
                 {"joke":"Why did the coffee file a police report? It got mugged!"},\
                 {"joke":"Why did the burglar break into the bakery? They needed some dough!"}]'

    jokeslist = json.loads(jokesarray)
    randomjoke = random.choices(jokeslist, k=int(number))
    return jsonify(randomjoke)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
