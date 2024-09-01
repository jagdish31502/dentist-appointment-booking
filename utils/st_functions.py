import requests

# Function to fetch and view appointments
def fetch_appointments():
    try:
        response = requests.get('http://localhost:5000/view_appointments')
        response.raise_for_status()  # Raises HTTPError for bad responses
        appointments = response.json().get('appointments', {})
        return appointments
    except requests.RequestException as e:
        return {"error": f"Error fetching appointments: {e}"}

# Function to book an appointment
def book_appointment(name, phone, date, time):
    try:
        response = requests.post('http://localhost:5000/book_appointment', json={
            'input': "Booking appointment",
            'name': name,
            'phone': phone,
            'date': date,
            'time': time
        })
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"response": f"Error booking appointment: {e}"}
