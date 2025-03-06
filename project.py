import streamlit as st
import random

st.title("➕ Plus Master 🎮")

# Initialize session state variables
if "level" not in st.session_state:
    st.session_state.level = 1
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.num1 = random.randint(1, 10)
    st.session_state.num2 = random.randint(1, 10)
    st.session_state.correct = None  # Track correct/incorrect answer


# Function to generate new question
def generate_numbers():
    max_value = st.session_state.level * 10  # Increase difficulty with level
    st.session_state.num1 = random.randint(1, max_value)
    st.session_state.num2 = random.randint(1, max_value)
    st.session_state.correct = None  # Reset answer tracking


# Restart game function
def restart_game():
    st.session_state.level = 1
    st.session_state.score = 0
    st.session_state.game_over = False
    generate_numbers()
    st.rerun()  # Restart game instantly


# Motivational Quotes List
quotes = [
    "🌟 “Failure is simply the opportunity to begin again, this time more intelligently.” – Henry Ford",
    "🔥 “It’s not whether you get knocked down, it’s whether you get up.” – Vince Lombardi",
    "💡 “Success is not final, failure is not fatal: It is the courage to continue that counts.” – Winston Churchill",
    "🚀 “Believe you can and you’re halfway there.” – Theodore Roosevelt",
    "⏳ “Don’t watch the clock; do what it does. Keep going.” – Sam Levenson"
]

# Game Over Page
if st.session_state.game_over:
    st.markdown("<h2 style='color: red;'>❌ Game Over! Better Luck Next Time 🎮</h2>", unsafe_allow_html=True)

    # Game Over Emoji
    st.markdown("<h1 style='text-align: center;'>💀</h1>", unsafe_allow_html=True)

    # Display Total Score
    st.subheader(f"🏆 Your Total Score: *{st.session_state.score}*")

    # Motivation Emoji
    st.markdown("<h1 style='text-align: center;'>💪</h1>", unsafe_allow_html=True)

    # Show Motivational Quote
    st.write(f"*💡 Motivation:* {random.choice(quotes)}")

    # Restart Button
    if st.button("🔄 New Game"):
        restart_game()

    st.stop()  # Stop further execution

# Display score
st.write(f"*Level: {st.session_state.level}* | *Score: {st.session_state.score}*")

# Game running
st.write(f"What is {st.session_state.num1} + {st.session_state.num2}?")

# User input
user_answer = st.number_input("Enter your answer:", min_value=0, step=1, key="answer")

# Check answer button
if st.button("✅ Check Answer"):
    correct_answer = st.session_state.num1 + st.session_state.num2
    if user_answer == correct_answer:
        st.success("🎉 Correct! You earned 10 points.")
        st.session_state.score += 10
        st.session_state.level += 1
        generate_numbers()  # Auto-generate next question
        st.rerun()  # Refresh page for new question
    else:
        st.session_state.game_over = True
        st.rerun()  # Move to Game Over Page