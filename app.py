import requests
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/character', methods=['POST'])
def character():
    character_id = request.form.get("character")
    character_url = f"https://swapi.py4e.com/api/people/{character_id}"

    try:
        character = requests.get(character_url).json()
        print(character)
        return render_template('character.html', character=character)
    except requests.exceptions.RequestException as e:
        error_message = f"Error: {e}"
        return render_template('character.html', error_message=error_message)
    # character = requests.get("https://swapi.py4e.com/api/people/1").json()
    # print(character)
    # return render_template('index.html', character=character)
# app.add_url_rule('/', 'index', homepage, methods= ["GET"])
# app.add_url_rule('/character', 'character', character, methods= ["POST"])
if __name__ == "__main__":
    app.run(debug=True)
