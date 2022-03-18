from datetime import date, datetime
from distutils.log import debug
from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/time')
def home():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S")
    return "<p> The time is now "+date_time +"</p>"


@app.route('/index')
def green_house():
    temp = float(25.05)
    humidity = float(67.35)
    light_level = float(490.01)
    sensor_id = float(4683218)
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S")
    return render_template('index.html',temp = temp,
    humidity=humidity, light_level=light_level, sensor_id=sensor_id, date_time=date_time)





if __name__ == "__main__":
    app.run(debug=True)