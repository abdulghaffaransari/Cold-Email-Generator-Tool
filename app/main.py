import streamlit as st

# Title for the application
st.title("📧 Working Student Cold Email Generator")

# Input field for the user to provide a job posting URL
url_input = st.text_input("Enter the Job Posting URL:", value="https://jobs.example.com/job/R-12345")

# Submit button to trigger the email generation
submit_button = st.button("Generate Email")

if submit_button:
    # Placeholder for the email generation logic
    st.write("Email generated successfully!")



   