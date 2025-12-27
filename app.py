import streamlit as st
from openai import OpenAI

# Title of the App
st.title("🇩🇪 Germany Relocation Assistant")
st.write("Welcome! I am Chioma's AI Assistant. Describe your profile below to check your visa eligibility.")

# 1. Get the API Key securely
try:
    api_key = st.secrets["OPENAI_API_KEY"]
    client = OpenAI(api_key=api_key)
except Exception:
    st.error("Missing API Key. Please add it to Streamlit Secrets.")
    st.stop()

# 2. User Input Area
user_input = st.text_area("Enter your details (e.g., Age, Degree, Job Title, Savings in Euro):", height=150)

# 3. The "Brain" (The Analysis Button)
if st.button("Analyze My Chances"):
    if not user_input:
        st.warning("Please enter your details first.")
    else:
        with st.spinner("Analyzing your profile against German Immigration Laws..."):
            try:
                # Ask OpenAI to analyze the text
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a friendly and professional expert on German Immigration and Relocation for Nigerians. Analyze the user's profile and suggest the best visa route (e.g., Opportunity Card, Student Visa, Blue Card) and estimate their success chance percentage. Be encouraging but realistic."},
                        {"role": "user", "content": user_input}
                    ]
                )
                # Show the result
                st.success("Analysis Complete!")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")
              
