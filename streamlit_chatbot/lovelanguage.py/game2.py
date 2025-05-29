import streamlit as st

# Page config
st.set_page_config(page_title="Love Language Quiz", layout="centered")

languages = ["Words of Affirmation", "Quality Time", "Receiving Gifts", "Acts of Service", "Physical Touch"]

# Session state init
if "scores" not in st.session_state:
    st.session_state.scores = {lang: 0 for lang in languages}
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "answers" not in st.session_state:
    st.session_state.answers = []
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

# Reset

def reset_quiz():
    st.session_state.q_index = 0
    st.session_state.scores = {lang: 0 for lang in languages}
    st.session_state.answers = []
    st.session_state.submitted = False
    st.session_state.quiz_started = False

# Questions
questions = [
    {
        "question": "What makes you feel most cared for?",
        "image": "image.png",
        "options": {
            "A sincere compliment or affirmation.": "Words of Affirmation",
            "Spending focused, uninterrupted time together.": "Quality Time",
            "Receiving a meaningful, unexpected gift.": "Receiving Gifts",
            "Someone helping without being asked.": "Acts of Service",
        }
    },
    {
        "question": "How do you feel most loved on a special occasion?",
        "image": "image copy.png",
        "options": {
            "Reading a heartfelt letter or card.": "Words of Affirmation",
            "Going on an adventure together.": "Quality Time",
            "Getting a gift you’ve hinted at.": "Receiving Gifts",
            "Having everything planned for you.": "Acts of Service",
        }
    },
    {
        "question": "After a long day, what would mean the most?",
        "image": "image copy 2.png",
        "options": {
            "Hearing supportive, kind words.": "Words of Affirmation",
            "Having dinner together with no distractions.": "Quality Time",
            "Receiving a favorite snack or treat.": "Receiving Gifts",
            "Someone taking care of small details for you.": "Acts of Service",
        }
    },
    {
        "question": "Which moment brings you closer to someone?",
        "image": "image copy 3.png",
        "options": {
            "Holding hands while walking.": "Physical Touch",
            "Having a deep, uninterrupted talk.": "Quality Time",
            "Receiving a sentimental object.": "Receiving Gifts",
            "Being surprised with help on a stressful task.": "Acts of Service",
        }
    },
    {
        "question": "You're feeling down. What cheers you up?",
        "image": "image copy 4.png",
        "options": {
            "Being hugged tightly.": "Physical Touch",
            "Hearing 'I'm here for you.'": "Words of Affirmation",
            "Spending quiet time with a loved one.": "Quality Time",
            "Someone runs an errand on your behalf.": "Acts of Service",
        }
    },
    {
        "question": "What makes a regular day feel special?",
        "image": "image copy 5.png",
        "options": {
            "A spontaneous kiss or touch.": "Physical Touch",
            "Someone shares their appreciation verbally.": "Words of Affirmation",
            "Receiving a little 'just thinking of you' item.": "Receiving Gifts",
            "Having something taken off your plate.": "Acts of Service",
        }
    },
    {
        "question": "Which action builds the strongest bond?",
        "image": "image copy 6.png",
        "options": {
            "Physical closeness, like cuddling.": "Physical Touch",
            "Intentional time spent doing something you both enjoy.": "Quality Time",
            "Surprise gifts that show attention to detail.": "Receiving Gifts",
            "Acts of kindness that lighten your load.": "Acts of Service",
        }
    },
    {
        "question": "What makes you feel prioritized?",
        "image": "image copy 7.png",
        "options": {
            "Someone listens fully without distractions.": "Quality Time",
            "They remember what matters to you and bring it up.": "Words of Affirmation",
            "They do small things to make your day easier.": "Acts of Service",
            "They initiate physical closeness.": "Physical Touch",
        }
    },
    {
        "question": "Which of these makes you happiest in a relationship?",
        "image": "image copy 8.png",
        "options": {
            "Being frequently physically affectionate.": "Physical Touch",
            "Spending long periods in meaningful conversation.": "Quality Time",
            "Getting thoughtful gifts without occasion.": "Receiving Gifts",
            "Your partner noticing what you need done—and doing it.": "Acts of Service",
        }
    },
    {
        "question": "You're celebrating a big moment. What's ideal?",
        "image": "image copy 9.png",
        "options": {
            "A handwritten note of pride or love.": "Words of Affirmation",
            "A memorable shared experience.": "Quality Time",
            "A symbolic or significant present.": "Receiving Gifts",
            "A partner taking charge of all the planning.": "Acts of Service",
        }
    },
    {
        "question": "What makes you feel secure in love?",
        "image": "image copy 10.png",
        "options": {
            "Hearing consistent, caring words.": "Words of Affirmation",
            "Physical contact like a hand on your back.": "Physical Touch",
            "Presence during emotionally tough moments.": "Quality Time",
            "Help with things before you even ask.": "Acts of Service",
        }
    },
    {
        "question": "How do you prefer to reconnect after time apart?",
        "image": "image copy 11.png",
        "options": {
            "Getting a long hug or physical touch.": "Physical Touch",
            "Having a deep conversation.": "Quality Time",
            "Getting a gift that says 'I missed you.'": "Receiving Gifts",
            "They handle things to make your return easier.": "Acts of Service",
        }
    },
    {
        "question": "What’s most romantic to you?",
        "image": "image copy 12.png",
        "options": {
            "Spoken expressions of deep love.": "Words of Affirmation",
            "A planned date to do something new together.": "Quality Time",
            "A surprise you weren't expecting.": "Receiving Gifts",
            "A selfless gesture that helps you.": "Acts of Service",
        }
    },
    {
        "question": "You feel closest to someone when they...",
        "image": "image copy 13.png",
        "options": {
            "Say something meaningful about you.": "Words of Affirmation",
            "Spend hours doing anything with you.": "Quality Time",
            "Offer a gift with emotional value.": "Receiving Gifts",
            "Help without needing to be asked.": "Acts of Service",
        }
    },
    {
        "question": "Which speaks louder than words?",
        "image": "lovememe.png",
        "options": {
            "A warm embrace.": "Physical Touch",
            "A quiet walk spent side by side.": "Quality Time",
            "A sentimental object that says 'I see you.'": "Receiving Gifts",
            "Doing the things you hate doing.": "Acts of Service",
        }
    },
]

total_questions = len(questions)

# ---------- START PAGE ----------
if not st.session_state.quiz_started:
    st.title("💖 Discover Your Love Language")
    st.markdown("Welcome to the Love Language Quiz! Take this short 15-question journey to learn how you most naturally express and receive love.")
    st.image("lovememe1.png", use_column_width=True)
    if st.button("Start Quiz ▶️"):
        st.session_state.quiz_started = True
        st.rerun()

# ---------- QUIZ ----------
elif st.session_state.q_index < total_questions:
    q = questions[st.session_state.q_index]
    st.subheader(f"Question {st.session_state.q_index + 1} of {total_questions}")
    st.image(q["image"], use_column_width=True)
    selected = st.radio(q["question"], list(q["options"].keys()), key=f"q_{st.session_state.q_index}")

    if st.button("Next ➡️") and not st.session_state.submitted:
        lang = q["options"][selected]
        st.session_state.scores[lang] += 1
        st.session_state.answers.append(lang)
        st.session_state.q_index += 1
        st.session_state.submitted = True
        st.rerun()

    if st.session_state.submitted:
        st.session_state.submitted = False

# ---------- RESULTS ----------
else:
    st.success("🎉 You've completed the quiz!")
    st.subheader("🧠 Your Primary Love Language:")
    primary = max(st.session_state.scores, key=st.session_state.scores.get)
    st.markdown(f"### ❤️ **{primary}**")

    st.write("### Breakdown:")
    for lang, score in st.session_state.scores.items():
        st.write(f"- {lang}: {score} point(s)")

    if st.button("Restart Quiz 🔁"):
        reset_quiz()
        st.rerun()
