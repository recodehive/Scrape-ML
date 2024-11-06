import streamlit as st
import json
import random
import os


def load_trivia_data():
    base_path = os.path.dirname(__file__)  # Get the directory of the current script
    json_path = os.path.join(base_path, "bollywood_trivia_data.json")
    with open(json_path, "r") as file:
        data = json.load(file)
    return data["questions"]


# Initialize session state for score and current question
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "questions" not in st.session_state:
    st.session_state.questions = load_trivia_data()
    random.shuffle(st.session_state.questions)  # Shuffle questions for randomness


# Display the question and options
def display_question():
    question = st.session_state.questions[st.session_state.question_index]
    st.write(
        f"**Question {st.session_state.question_index + 1}:** {question['question']}"
    )

    # Create buttons for options
    for option in question["options"]:
        if st.button(option):
            check_answer(option, question["answer"])


# Check if the answer is correct
def check_answer(selected_option, correct_answer):
    if selected_option == correct_answer:
        st.session_state.score += 1
        st.success("Correct!")
    else:
        st.error(f"Wrong! The correct answer is: {correct_answer}")

    # Move to the next question
    if st.session_state.question_index < len(st.session_state.questions) - 1:
        st.session_state.question_index += 1
    else:
        st.write(
            f"Game Over! Your final score is {st.session_state.score}/{len(st.session_state.questions)}"
        )
        reset_game()


# Reset the game
def reset_game():
    st.session_state.score = 0
    st.session_state.question_index = 0
    st.session_state.questions = load_trivia_data()
    random.shuffle(st.session_state.questions)


# Set up the Streamlit app
st.set_page_config(page_title="Bollywood Movie Trivia Game", page_icon="🎬")

st.title("Bollywood Movie Trivia Game")
display_question()
