import streamlit as st
import json
import datetime

st.set_page_config(page_title="TalentScout Hiring Assistant", layout="centered")

st.title("🤖 TalentScout Hiring Assistant")
st.write("Welcome! Let’s begin your technical screening interview.")

# ---------------------------
# Session state setup
# ---------------------------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.data = {}

# ---------------------------
# Helper: Generate questions
# ---------------------------
def generate_questions(tech_stack):
    questions = []

    tech_stack = tech_stack.lower()

    if "html" in tech_stack:
        questions.append("What is the full form of HTML?")
        questions.append("What is the difference between semantic and non-semantic HTML?")
    if "css" in tech_stack:
        questions.append("Why css is required for building a website?")
        questions.append("What is the difference between flexbox and grid?")
    if "javascript" in tech_stack:
        questions.append("Explain closures in JavaScript.")
        questions.append("What is a promise in Javascript?")
    if "react" in tech_stack:
        questions.append("What is the virtual DOM in React?")
    if "node" in tech_stack:
        questions.append("What is the event loop in Node.js?")
    if "python" in tech_stack:
        questions.append("Difference between list and tuple in Python?")
        questions.append("Explain mutable and immutable objects in Python.")
        questions.append("What benefits does immmutable object give for large scale projects?")
    if "java" in tech_stack:
        questions.append("What is JVM and why is Java platform independent?")
        questions.append("Does Java support call by reference?")
        questions.append("Is Java a pure object oriented language")
    if "ml" in tech_stack or "machine learning" in tech_stack:
        questions.append("Difference between supervised and unsupervised learning?")
        questions.append("Explain Cross Validation.")

    if not questions:
        questions.append("Explain one challenging project you worked on.")

    return questions[:5]

# ---------------------------
# Step 0: Name
# ---------------------------
if st.session_state.step == 0:
    name = st.text_input("👋 What is your full name?")
    if st.button("Next"):
        if name:
            st.session_state.data["name"] = name
            st.session_state.step += 1
            st.rerun()

# ---------------------------
# Step 1: Email
# ---------------------------
elif st.session_state.step == 1:
    email = st.text_input("📧 Enter your email:")
    if st.button("Next"):
        if email:
            st.session_state.data["email"] = email
            st.session_state.step += 1
            st.rerun()

# ---------------------------
# Step 2: Phone
# ---------------------------
elif st.session_state.step == 2:
    phone = st.text_input("📱 Enter your phone number:")
    if st.button("Next"):
        if phone:
            st.session_state.data["phone"] = phone
            st.session_state.step += 1
            st.rerun()

# ---------------------------
# Step 3: Experience
# ---------------------------
elif st.session_state.step == 3:
    exp = st.selectbox("💼 Years of experience", ["0 (Fresher)", "1-2", "3-5", "5+"])
    if st.button("Next"):
        st.session_state.data["experience"] = exp
        st.session_state.step += 1
        st.rerun()

# ---------------------------
# Step 4: Tech Stack
# ---------------------------
elif st.session_state.step == 4:
    tech = st.text_area("🛠️ Enter your tech stack (comma separated):")
    if st.button("Generate Questions"):
        if tech:
            st.session_state.data["tech_stack"] = tech
            st.session_state.questions = generate_questions(tech)
            st.session_state.answers = []
            st.session_state.q_index = 0
            st.session_state.step += 1
            st.rerun()

# ---------------------------
# Step 5: Ask Questions One-by-One
# ---------------------------
elif st.session_state.step == 5:
    questions = st.session_state.questions
    idx = st.session_state.q_index

    if idx < len(questions):
        st.subheader(f"🧠 Question {idx+1}:")
        st.write(questions[idx])

        ans = st.text_area("Your answer:")

        if st.button("Submit Answer"):
            if ans:
                st.session_state.answers.append(ans)
                st.session_state.q_index += 1
                st.rerun()
    else:
        st.session_state.step += 1
        st.rerun()

# ---------------------------
# Step 6: Save + Exit
# ---------------------------
elif st.session_state.step == 6:
    st.success("🎉 Interview completed!")

    # Save data
    result = {
        "timestamp": str(datetime.datetime.now()),
        "candidate_info": st.session_state.data,
        "questions": st.session_state.questions,
        "answers": st.session_state.answers
    }

    with open("responses.json", "a") as f:
        f.write(json.dumps(result) + "\n")

    st.write("✅ Your responses have been recorded.")
    st.write("Our team will contact you soon 🚀")