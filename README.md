# Dental Appointment Booking System

## Overview

The Dental Appointment Booking System is a web application that allows users to book dental appointments, view existing appointments, and interact with an assistant to facilitate the booking process. The application uses Flask for the backend and Streamlit for the frontend.

### <img src="preview\preview.png" width="1000"/>
### <video width="1000" controls>
  <source src="preview\demo.mp4" type="video/mp4">
    </video>
## Features

- **Book Appointments**: Users can book dental appointments through a conversational interface.
- **View Appointments**: Users can view all booked appointments.
- **User Interaction**: Conversational UI powered by ChatGroq for a natural booking experience.

## Project Structure

- **`app.py`**: Flask application file containing route definitions for booking and viewing appointments.
- **`helper_functions.py`**: Contains business logic for booking appointments, date parsing, and availability checking.
- **`streamlit_app.py`**: Streamlit application for interacting with users through a web interface.
- **`requirements.txt`**: Lists Python packages required for the project.

## Setup and Installation

### Clone the Repository

```bash
git clone https://github.com/jagdish31502/dentist-appointment-booking.git
cd dentist-appointment-booking
```

### Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask Application

```bash
python app.py
```

The Flask server will run on `http://localhost:5000`.

### Run the Streamlit Application

In a new terminal window, run:

```bash
streamlit run streamlit_app.py
```

The Streamlit app will be accessible at `http://localhost:8501`.

## Code Overview

### `app.py`

Defines the Flask application and routes:

- **`/book_appointment`**: Handles appointment booking.
- **`/view_appointments`**: Handles viewing of booked appointments.

### `helper_functions.py`

Contains business logic:

- **`parse_and_standardize_datetime(date_str, time_str)`**: Parses and formats date and time.
- **`find_next_available_time(start_time)`**: Finds the next available time slot for an appointment.
- **`book_appointment(user_input, name, phone, date_str, time_str)`**: Books an appointment and returns a response.
- **`view_appointments_logic()`**: Returns the list of appointments.

### `streamlit_app.py`

Provides a user interface for booking appointments and viewing existing appointments using Streamlit.

## Usage

### Booking an Appointment

1. Open the Streamlit application in your browser.
2. Follow the prompts to enter your name, phone number, and preferred appointment time.
3. The system will confirm the appointment or provide an error message if the time slot is not available.

### Viewing Appointments

1. Click on the "View Appointments" button in the sidebar of the Streamlit app.
2. View the list of all booked appointments.
