
import streamlit as st
from fairsight_logic_module import process_user_response

st.set_page_config(page_title="FairSight AI", layout="centered")
st.title("🧠 FairSight AI – Workplace Insight Engine")

st.markdown("""
This diagnostic tool helps you explore how your emotional, cultural, and personal attributes may influence your organizational citizenship behavior (OCB).
""")

with st.form("user_form"):
    st.subheader("1. Demographic and Context")
    gender = st.selectbox("What gender do you identify with?", ["Male", "Female", "Non-binary", "Prefer not to say"])

    st.subheader("2. Emotion Experience Scale (Past Week)")
    emotion_items = {
        "Joy": st.slider("Joy", 1, 5, 3),
        "Hope": st.slider("Hope", 1, 5, 3),
        "Gratitude": st.slider("Gratitude", 1, 5, 3),
        "Anger": st.slider("Anger", 1, 5, 3),
        "Anxiety": st.slider("Anxiety", 1, 5, 3)
    }

    st.subheader("3. Cultural Orientation")
    culture_items = {
        "RelyOnSelf": st.slider("I usually rely on myself rather than on others.", 1, 5, 3),
        "TeamHarmony": st.slider("I enjoy working in teams and value group harmony.", 1, 5, 3),
        "ClearRules": st.slider("I prefer clear rules and leadership structures at work.", 1, 5, 3),
        "GroupOverSelf": st.slider("I make decisions based on what's best for the group.", 1, 5, 3)
    }

    st.subheader("4. Justice Perception")
    justice_items = {
        "DJ_EffortReward": st.slider("My work rewards reflect the effort I put in.", 1, 5, 3),
        "DJ_AppropriateOutcome": st.slider("My outcomes are appropriate for the work I’ve done.", 1, 5, 3),
        "DJ_ComparedFair": st.slider("The rewards I receive are fair compared to others.", 1, 5, 3),
        "PJ_Consistency": st.slider("Procedures are consistent across people.", 1, 5, 3),
        "PJ_NoBias": st.slider("Procedures are free from bias.", 1, 5, 3),
        "PJ_Voice": st.slider("I can express my views during procedures.", 1, 5, 3),
        "PJ_InfoAccuracy": st.slider("Procedures are based on accurate information.", 1, 5, 3),
        "IJ_Respect": st.slider("I am treated with dignity and respect.", 1, 5, 3),
        "IJ_Explanation": st.slider("Explanations are provided for decisions.", 1, 5, 3),
        "IJ_Sincerity": st.slider("I’m treated with sincerity.", 1, 5, 3),
        "IJ_ProperRemarks": st.slider("Supervisors avoid improper remarks.", 1, 5, 3)
    }

    st.subheader("5. Social Desirability")
    sd_score = st.slider("How important is it to you to appear helpful, loyal, and trustworthy to others?", 1.0, 5.0, 3.0, step=0.1)

    st.subheader("6. OCB Behavior Checklist")
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
        "Emotion": emotion_items,
        "Culture": culture_items,
        "Justice": justice_items,
        "SDScore": sd_score,
        "OCBItems": ocb_inputs
    })

    st.subheader("🔍 FairSight Diagnostic Summary")
    st.markdown(f"**OCB Score:** {result['OCBScore']} / 5")
    st.markdown(f"**Distributive Justice:** {result['JusticeScores']['Distributive']} / 5")
    st.markdown(f"**Procedural Justice:** {result['JusticeScores']['Procedural']} / 5")
    st.markdown(f"**Interactional Justice:** {result['JusticeScores']['Interactional']} / 5")
    st.markdown(f"**Justice Sensitivity:** {result['JusticeSensitivity']}")
    st.markdown(f"**OCB Confidence:** {result['OCBConfidence']}")
    st.markdown(f"**Interpretation:** {result['Interpretation']}")
    st.markdown(f"**Bias Flag:** {result['ExaggerationNote']}")
