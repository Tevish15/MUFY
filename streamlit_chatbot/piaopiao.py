import streamlit as st

# Set up Streamlit UI
st.title("Simple Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input box
user_input = st.text_input("You:", "")

# Respond when user submits input
if user_input:
    st.session_state.messages.append(("You", user_input))

    # Simple logic to respond
    if "piao" in user_input.lower():
        bot_reply = "Your piao piao is ready"
    else:
        bot_reply = "I'm just a simple bot. Try saying 'piao'!"

    st.session_state.messages.append(("Bot", bot_reply))

# Display messages
for sender, message in st.session_state.messages:
    st.markdown(f"**{sender}:** {message}")
