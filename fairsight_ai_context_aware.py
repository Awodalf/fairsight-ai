
import streamlit as st

st.set_page_config(page_title='FairSight AI', layout='centered')
st.title('🤖 FairSight AI – Context-Aware Diagnostic')

st.markdown("""
This diagnostic tool adapts to your cultural, emotional, and personal profile to assess workplace behavior and fairness engagement.
""")

# Gender input
gender = st.selectbox("1. What gender do you identify with?", ["Male", "Female", "Non-binary", "Prefer not to say"])
# Emotion input
emotion = st.selectbox("2. How would you describe your emotional experience at work?", ["Low", "High"])
# Culture input
culture = st.selectbox("3. Which best describes your cultural tendency?", [
    "Collectivist + High Power Distance",
    "Individualist + Low Power Distance"
])

# Logic engine
def interpret_user_profile(gender, emotion, culture):
    profile = {
        "justice_sensitivity": "Unknown",
        "ocb_confidence": "Unknown",
        "explanation": ""
    }

    # Normalize inputs
    gender = gender.lower()
    emotion = emotion.capitalize()
    culture = culture.replace(" ", "_").replace("+", "").replace("__", "_")

    if emotion == "Low" and culture == "Collectivist_HighPowerDistance":
        profile["justice_sensitivity"] = "High"
        profile["ocb_confidence"] = "Very High"
        profile["explanation"] = "Strong procedural justice sensitivity and likely high OCB display."

    elif emotion == "Low" and culture == "Individualist_LowPowerDistance":
        profile["justice_sensitivity"] = "Moderate"
        profile["ocb_confidence"] = "Moderate"
        profile["explanation"] = "You may be less reactive to fairness cues but respond to outcomes."

    elif emotion == "High" and culture == "Collectivist_HighPowerDistance":
        profile["justice_sensitivity"] = "Moderate"
        profile["ocb_confidence"] = "Moderate"
        profile["explanation"] = "Positive emotion supports engagement; justice sensitivity buffered."

    elif emotion == "High" and culture == "Individualist_LowPowerDistance":
        profile["justice_sensitivity"] = "Low"
        profile["ocb_confidence"] = "Likely Inflated"
        profile["explanation"] = "High emotion with individualist orientation may lead to idealized responses."

    if gender == "female" and emotion == "Low" and culture == "Collectivist_HighPowerDistance":
        profile["justice_sensitivity"] = "Very High"
        profile["ocb_confidence"] = "Strong Display"
        profile["explanation"] = "Best-case scenario: high sensitivity to justice and strong citizenship behavior."

    if gender == "male" and emotion == "Low" and culture == "Individualist_LowPowerDistance":
        profile["justice_sensitivity"] = "Low"
        profile["ocb_confidence"] = "Likely Suppressed"
        profile["explanation"] = "Lower emotional engagement and justice reactivity; may underreport OCB."

    return profile

# Display result
if st.button("Submit"):
    profile_result = interpret_user_profile(gender, emotion, culture)
    st.markdown("### 🔍 Context-Aware Profile Summary")
    st.markdown(f"**Justice Sensitivity**: {profile_result['justice_sensitivity']}")
    st.markdown(f"**OCB Confidence**: {profile_result['ocb_confidence']}")
    st.markdown(f"**Explanation**: {profile_result['explanation']}")
