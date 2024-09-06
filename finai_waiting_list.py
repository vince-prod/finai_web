import streamlit as st
import pandas as pd

# Function to save the user's details to a CSV file
def save_to_csv(name, email):
    new_entry = pd.DataFrame([[name, email]], columns=['Name', 'Email'])
    
    try:

        existing_data = pd.read_csv('finai_waiting_list.csv')
        updated_data = pd.concat([existing_data, new_entry], ignore_index=True)
    except FileNotFoundError:
        
        updated_data = new_entry

    # updated_data.to_csv('finai_waiting_list.csv', index=False)
    st.success("You've successfully joined the waiting list!")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #000000;
        font-family: 'Helvetica', sans-serif;
    }
    .title {
        font-size: 3.5em;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        margin-bottom: 30px;
    }
    .subtitle {
        font-size: 1.7em;
        color: #ffffff;
        text-align: center;
        margin-bottom: 40px;
    }
    .description {
        font-size: 1.2em;
        color: #dcdcdc;
        text-align: center;
        margin-bottom: 60px;
    }
    .input {
        font-size: 1.3em;
        color: #ffffff;
        margin-bottom: 20px;
    }
    input {
        color: #ffffff !important;
        background-color: #333333 !important; /* Dark background for input fields */
        border: 1px solid #ffffff !important; /* White border for input fields */
    }
    .btn {
        background-color: #3498db;
        color: white;
        font-size: 1.3em;
        padding: 12px 24px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .btn:hover {
        background-color: #2980b9;
    }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.markdown('<div class="title">FinAI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your Personal Finance & Investment AI Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Join the waitlist to be the first to experience FinAI - the next-generation AI-powered financial advisor that helps you manage your investments, optimize your savings, and secure your financial future with ease. </div>', unsafe_allow_html=True)

# Hero Image (Add your image URL)

# Input fields for name and email
name = st.text_input('Name', '', key='name')
email = st.text_input('Email', '', key='email')

# Submit button
if st.button('Join the Waitlist', key='join_btn'):
    if name and email:
        save_to_csv(name, email)
    else:
        st.error('Please enter both your name and email!')

# Additional Information Section
st.markdown('<div class="description">Why FinAI?</div>', unsafe_allow_html=True)
st.markdown("""
<ul class="description">
    <li>📈 Personalized investment advice tailored to your financial goals</li>
    <li>💰 Automated savings and budget management</li>
    <li>📊 Real-time market analysis and insights</li>
    <li>🤖 AI-driven portfolio optimization</li>
    <li>🕒 24/7 support from your virtual financial assistant</li>
</ul>
""", unsafe_allow_html=True)

st.markdown('<div class="description">Be part of the financial revolution. Join the FinAI waitlist today!</div>', unsafe_allow_html=True)
