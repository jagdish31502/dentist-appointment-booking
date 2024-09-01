import streamlit as st
from utils.st_functions import *

st.title("Dentist 🦷 Appointment Booking.")

# Initialize chat history and user data
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to dental appointment booking. Please enter your full name."}
    ]
    st.session_state.name = ""
    st.session_state.phone = ""
    st.session_state.time = ""
    st.session_state.booking_done = True

# Function to view appointments
def view_appointments():
    appointments = fetch_appointments()
    if "error" in appointments:
        st.error(appointments["error"])
    elif appointments:
        st.write("### Appointments List")
        for appt_id, details in appointments.items():
            st.write(f"**Appointment ID:** {appt_id}")
            st.write(f"**Name:** {details['name']}")
            st.write(f"**Phone:** {details['phone']}")
            st.write(f"**Time:** {details['time']}")
            st.write("---")
    else:
        st.write("No appointments found.")

# Sidebar for View Appointments button
with st.sidebar:
    st.header("MENU 📄")
    if st.button("View Appointments"):
        view_appointments()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input and chat flow
if user_input := st.chat_input("Your message..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Handle agent's response based on user input
    if len(st.session_state.messages) == 2:  # After the first user input (name entry)
        st.session_state.name = user_input  # Store user's name
        agent_message = f"Thank you, {st.session_state.name}. Please provide your phone number."

    elif len(st.session_state.messages) == 4:  # After the phone number input
        st.session_state.phone = user_input  # Store user's phone number
        agent_message = "How can I help you today?"

    elif len(st.session_state.messages) == 6:  # After the user mentions booking an appointment
        agent_message = "Sure, can you provide the date and time for the appointment?"

    elif len(st.session_state.messages) == 8:  # After the user provides date and time
        st.session_state.time = user_input  # Store appointment time

        # Make API request to book the appointment
        date, time = st.session_state.time.split(",")[1].strip(), st.session_state.time.split(",")[0].strip()
        response_data = book_appointment(st.session_state.name, st.session_state.phone, date, time)

        if response_data.get("response") == "Error booking appointment":
            agent_message = response_data.get("response")
        else:
            agent_message = f"Booking your appointment for {user_input}... Done! Your appointment is confirmed."

    # Display agent message
    with st.chat_message("assistant"):
        st.markdown(agent_message)
    st.session_state.messages.append({"role": "assistant", "content": agent_message})
