import streamlit as st

# Create a Streamlit app title
st.title("My Streamlit App")

# Add user input components (e.g., sliders, text inputs)
user_input = st.text_input("Enter a value:")

# Define a function that performs some Python logic
def process_data(input_value):
    # Your Python code here
    result = f"You entered: {input_value}"
    return result

# Call the function with user input and display the result
if st.button("Process"):
    result = process_data(user_input)
    st.write("Result:", result)
