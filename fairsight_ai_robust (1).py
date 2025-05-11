
import streamlit as st

st.set_page_config(page_title='FairSight AI', layout='centered')
st.title('🤖 FairSight AI – Robust Citizenship & Justice Diagnostic')

st.markdown("""
Welcome to **FairSight AI** — a smart diagnostic tool for understanding workplace citizenship behavior and fairness perceptions.
Your honest responses help create a clearer picture of engagement and climate.
""")

# Gender input
gender = st.selectbox("1. What gender do you identify with?", ["Select an option", "Male", "Female", "Non-binary", "Prefer not to say", "Other"])
gender_val = 0 if gender == "Male" else 1

# Social Desirability input
sd_score = st.slider("2. On a scale from 1 to 5, how important is it to you to be seen as helpful, loyal, and trustworthy by others?", 1.0, 5.0, 3.0, step=0.1)

# Emotion input
st.subheader("3. Emotional Experience at Work (Past Week)")
emotion_score = st.slider("How often did you feel positive emotions at work? (Joy, Gratitude, Hope)", 1.0, 5.0, 3.0, step=0.1)

# Justice inputs
st.subheader("4. Perceived Fairness at Work (Justice Dimensions)")
distributive = st.slider("Outcomes I receive (e.g. pay, recognition) are fair.", 1, 5, 3)
procedural = st.slider("Processes for making decisions in my workplace are transparent and unbiased.", 1, 5, 3)
interactional = st.slider("Supervisors treat people with dignity and explain decisions respectfully.", 1, 5, 3)

# OCB Questions
st.subheader("5. Organizational Citizenship Behavior (Rate 1–5)")
likert = [1, 2, 3, 4, 5]
ocb_items = {
    "I never hesitate to help someone in case of emergency.": None,
    "When I have made a promise, I keep it – no ifs, ands, or buts.": None,
    "I occasionally speak badly of others behind their back.": None,
    "I would never live off at other people’s expense.": None,
    "I stay friendly and courteous with other people, even when I am stressed out.": None,
    "During arguments I stay objective and matter-of-fact.": None,
    "There has been at least one occasion when I failed to return an item that I borrowed.": None,
    "I eat a healthy diet.": None,
    "Sometimes I only help because I expect something in return.": None
}

for q in ocb_items:
    ocb_items[q] = st.radio(q, likert, horizontal=True)

# Compute OCB score
ocb_score = (
    ocb_items["I never hesitate to help someone in case of emergency."] +
    ocb_items["When I have made a promise, I keep it – no ifs, ands, or buts."] +
    (6 - ocb_items["I occasionally speak badly of others behind their back."]) +
    ocb_items["I would never live off at other people’s expense."] +
    ocb_items["I stay friendly and courteous with other people, even when I am stressed out."] +
    ocb_items["During arguments I stay objective and matter-of-fact."] +
    (6 - ocb_items["There has been at least one occasion when I failed to return an item that I borrowed."]) +
    ocb_items["I eat a healthy diet."] +
    (6 - ocb_items["Sometimes I only help because I expect something in return."])
) / 9

# Display feedback
if st.button("Submit"):
    st.success(f"🧾 Your OCB Score: {round(ocb_score, 2)} / 5")

    if ocb_score >= 4:
        st.info("✅ You exhibit strong citizenship behavior — you're likely a reliable and cooperative team player.")
    elif ocb_score >= 3:
        st.warning("⚠️ Moderate citizenship behavior. You may engage sometimes but there’s room for more consistency.")
    else:
        st.error("🚩 Low OCB detected. You might not be consistently engaged in extra-role behaviors.")

    # Social Desirability flag
    st.markdown("---")
    st.markdown(f"**🧠 Social Desirability Score: {round(sd_score, 2)} / 5**")
    if sd_score > 4.0:
        st.warning("⚠️ High social desirability. This may indicate that responses are idealized. Interpret with caution.")
    elif sd_score < 3.0:
        st.success("👍 Low social desirability. Responses likely reflect authentic behavior.")
    else:
        st.info("ℹ️ Moderate social desirability. Results should be viewed thoughtfully.")

    # Emotion feedback
    st.markdown(f"**💚 Emotion Score: {round(emotion_score, 2)} / 5**")
    if emotion_score >= 4:
        st.success("😊 You appear emotionally positive at work — this supports healthy engagement and fairness perception.")
    elif emotion_score < 3:
        st.warning("😟 Low emotional tone — this may suppress how justice is perceived or how you engage with others.")

    # Justice feedback
    st.markdown("---")
    st.markdown(f"**⚖️ Justice Ratings**")
    st.markdown(f"- Distributive Justice: {distributive}/5")
    st.markdown(f"- Procedural Justice: {procedural}/5")
    st.markdown(f"- Interactional Justice: {interactional}/5")

    if procedural >= 4:
        st.info("📊 You rate your workplace processes as fair and unbiased — this often leads to stronger OCB.")
    if interactional < 3:
        st.warning("👥 Low interactional justice — this may weaken team cohesion and trust.")
    if distributive < 3:
        st.warning("💰 You feel that outcomes are unfair — this can negatively impact morale.")
