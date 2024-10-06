from flask import render_template, Blueprint, request
import requests
from ..models.city import City
from ..extensions import db


api = Blueprint('api/', __name__)

@api.route('/')
def index():
    cities = City.query.all()
    
    url = "http://api.weatherapi.com/v1/current.json?key={}&q={}"
    weather_data = []
    weather = {}

    for city in cities:
        r = requests.post(url.format(city)).json()
        weather = {
            'city': r['location']['name'],
            'description': r['current']['condition']['text'],
            'country': r['location']['country'],
            'icon': r['current']['condition']['icon'],
            'temperature': r['current']['temp_f']
        }
        weather_data.append(weather)
    
    return render_template('weather.html', weather_data=weather_data)

@api.route('/add', methods=['POST'])
def add_city():
    content = request.get_json()
    name = content['name']
    city =  City(name=name)
    db.session.add(city)
    db.session.commit()
    return 'Pune'