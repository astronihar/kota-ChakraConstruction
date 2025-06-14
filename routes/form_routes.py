from flask import Blueprint, render_template, request, jsonify
import requests

form_routes = Blueprint('form_routes', __name__)

@form_routes.route('/form', methods=['GET', 'POST'])
def form_view():
    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('birthdate')  # format: dd-mm-yyyy
        time = request.form.get('birthtime')  # format: hh:mm AM/PM
        lat = request.form.get('latitude')
        lon = request.form.get('longitude')

        api_url = f"http://localhost:5000/api/astronihar/d1?date={date}&time={time}&lat={lat}&lon={lon}"
        response = requests.get(api_url)

        if response.status_code == 200:
            astro_data = response.json()
            return render_template('forms.html', result=astro_data, submitted=True)
        else:
            return render_template('forms.html', error="API Error", submitted=True)

    return render_template('forms.html', submitted=False)
