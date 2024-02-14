from flask import Flask, render_template, request
from weather_api.weather import main as get_weather



app = Flask(__name__)

@app.route("/", methods= ["GET", "POST"])
def index():
    """
    Renders the index page and handles form submission to retrieve weather data.

    Returns:
        str: Rendered HTML template with weather data or error message.
    """
    data=None
    if request.method == "POST":
        city, state, country = request.form["cityName"],request.form["stateName"], request.form["countryName"]
        if city == "" or state == "" or country == "":
            return render_template("index.html", message = "Please fill all the details...") 
        data = get_weather(city, state, country)
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)