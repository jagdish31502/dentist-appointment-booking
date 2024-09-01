from flask import Flask, request, jsonify
from utils.flask_functions import *

app = Flask(__name__)

@app.route('/book_appointment', methods=['POST'])
def book_appointment_route():
    try:
        user_input = request.json.get('input')
        name = request.json.get('name')
        phone = request.json.get('phone')
        date_str = request.json.get('date')
        time_str = request.json.get('time')

        response_text, status_code = book_appointment(user_input, name, phone, date_str, time_str)
        return jsonify({"response": response_text, "appointments": view_appointments_logic()}), status_code
    except Exception as e:
        print(f"Error in booking appointment: {e}")
        return jsonify({"response": "An error occurred while booking the appointment."}), 500

@app.route('/view_appointments', methods=['GET'])
def view_appointments_route():
    try:
        return jsonify({"appointments": view_appointments_logic()})
    except Exception as e:
        print(f"Error in viewing appointments: {e}")
        return jsonify({"response": "An error occurred while retrieving the appointments."}), 500

if __name__ == '__main__':
    app.run(debug=True)
