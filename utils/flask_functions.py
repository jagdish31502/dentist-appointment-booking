from datetime import datetime, timedelta
from dateutil import parser

# Store booked appointments
appointments = {}

# Function to parse and standardize date and time
def parse_and_standardize_datetime(date_str, time_str):
    try:
        combined_str = f"{date_str}, {time_str}"
        parsed_datetime = parser.parse(combined_str, fuzzy=True)
        formatted_datetime = parsed_datetime.strftime("%d/%m/%Y %I:%M %p")
        return formatted_datetime
    except (ValueError, TypeError) as e:
        print(f"Error parsing date and time: {e}")
        return None

# Function to find the next available time slot
def find_next_available_time(start_time):
    try:
        start_dt = datetime.strptime(start_time, "%d/%m/%Y %I:%M %p")
        sorted_appointments = sorted(appointments.values(), key=lambda x: x['time'])
        
        for appointment in sorted_appointments:
            appt_time = datetime.strptime(appointment['time'], "%d/%m/%Y %I:%M %p")
            if appt_time <= start_dt < appt_time + timedelta(minutes=30):
                return appt_time + timedelta(minutes=30)

        return start_dt
    except Exception as e:
        print(f"Error finding next available time: {e}")
        return None

def book_appointment(user_input, name, phone, date_str, time_str):
    formatted_datetime = parse_and_standardize_datetime(date_str, time_str)
    if not formatted_datetime:
        return "Invalid date or time format. Please provide a valid format.", 400

    today = datetime.now()
    appointment_datetime = datetime.strptime(formatted_datetime, "%d/%m/%Y %I:%M %p")

    if appointment_datetime < today:
        return "Cannot book an appointment in the past. Please provide a future date.", 400

    next_available_time = find_next_available_time(formatted_datetime)
    
    if next_available_time:
        appointment_time = next_available_time.strftime("%d/%m/%Y %I:%M %p")
        appointments[len(appointments) + 1] = {
            "name": name,
            "phone": phone,
            "time": appointment_time
        }
        response_text = f"Booking your appointment for {appointment_time}... Done! Your appointment is confirmed."
    else:
        response_text = "No available slots at the moment."

    return response_text, 200

def view_appointments_logic():
    return appointments
