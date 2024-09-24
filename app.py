from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.debug = True
app.config['DEBUG']=True

@app.route('/')
def index():
    url = "http://api.weatherapi.com/v1/current.json?key=855616563bfe4788972175036242409&q={}"
    city = 'paris'
    r = requests.post(url.format(city)).json()
    weather = {
        'city': r['location']['name'],
        'description': r['current']['condition']['text'],
        'country': r['location']['country'],
        'icon': r['current']['condition']['icon'],
        'temperature': r['current']['temp_f']
    }
    return render_template('weather.html', weather=weather)