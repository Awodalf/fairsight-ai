import streamlit as st
from fairsight_logic_module import process_user_response

st.set_page_config(page_title="FairSight AI", layout="centered")
st.title("🧠 FairSight AI – Workplace Insight Engine")

st.markdown("""
This diagnostic tool helps you explore how your emotional, cultural, and personal attributes may influence your organizational citizenship behavior (OCB).
""")

# Inputs
with st.form("user_form"):
    st.subheader("1. Demographic and Context")
    gender = st.selectbox("What gender do you identify with?", ["Male", "Female", "Non-binary", "Prefer not to say"])
    emotion = st.selectbox("How would you describe your emotional experience at work lately?", ["Low", "High"])
    culture = st.selectbox("Which best describes your cultural orientation?", [
        "Collectivist + High Power Distance",
        "Individualist + Low Power Distance"
    ])
    sd_score = st.slider("How important is it to you to appear helpful, loyal, and trustworthy to others?", 1.0, 5.0, 3.0, step=0.1)

    st.subheader("2. OCB Behavior Checklist (1 = Strongly Disagree, 5 = Strongly Agree)")
    ocb_inputs = {
        "HelpOthers": st.slider("I never hesitate to help someone in case of emergency.", 1, 5, 3),
        "KeepPromises": st.slider("When I have made a promise, I keep it – no ifs, ands, or buts.", 1, 5, 3),
        "SpeakBadly": st.slider("I occasionally speak badly of others behind their back.", 1, 5, 3),
        "LiveOffOthers": st.slider("I would never live off at other people’s expense.", 1, 5, 3),
        "FriendlyWhenStressed": st.slider("I stay friendly and courteous with others, even when stressed out.", 1, 5, 3),
        "ObjectiveInArguments": st.slider("During arguments I stay objective and matter-of-fact.", 1, 5, 3),
        "FailedToReturn": st.slider("There has been at least one occasion when I failed to return an item I borrowed.", 1, 5, 3),
        "HealthyDiet": st.slider("I eat a healthy diet.", 1, 5, 3),
        "HelpExpectReturn": st.slider("Sometimes I only help because I expect something in return.", 1, 5, 3)
    }

    submit = st.form_submit_button("Get My Diagnostic Report")

if submit:
    result = process_user_response({
        "Gender": gender,
        "Emotion": emotion,
        "Culture": culture,
        "SDScore": sd_score,
        "OCBItems": ocb_inputs
    })

    st.subheader("🔍 FairSight Diagnostic Summary")
    st.markdown(f"**OCB Score:** {result['OCBScore']} / 5")
    st.markdown(f"**Justice Sensitivity:** {result['JusticeSensitivity']}")
    st.markdown(f"**OCB Confidence:** {result['OCBConfidence']}")
    st.markdown(f"**Interpretation:** {result['Interpretation']}")
    st.markdown(f"**Bias Flag:** {result['ExaggerationNote']}")
