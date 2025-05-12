import numpy as np

def reverse_code(x):
    return 6 - x

def compute_ocb_score(responses):
    reverse_items = ["SpeakBadly", "FailedToReturn", "HelpExpectReturn"]
    scored = []
    for item, val in responses.items():
        if item in reverse_items:
            scored.append(reverse_code(val))
        else:
            scored.append(val)
    return np.round(np.mean(scored), 2)

def compute_justice_averages(justice_dict):
    dj_keys = [k for k in justice_dict if k.startswith("DJ_")]
    pj_keys = [k for k in justice_dict if k.startswith("PJ_")]
    ij_keys = [k for k in justice_dict if k.startswith("IJ_")]
    distributive = np.mean([justice_dict[k] for k in dj_keys])
    procedural = np.mean([justice_dict[k] for k in pj_keys])
    interactional = np.mean([justice_dict[k] for k in ij_keys])
    return {
        "Distributive": round(distributive, 2),
        "Procedural": round(procedural, 2),
        "Interactional": round(interactional, 2)
    }

def interpret_profile(gender, emotion_dict, culture_dict):
    gender = gender.lower()
    emotion = "Low" if np.mean([emotion_dict[k] for k in emotion_dict if k in ["Anger", "Anxiety"]]) > 3.5 else "High"
    culture = "Collectivist_HighPowerDistance" if culture_dict["TeamHarmony"] > 3 and culture_dict["ClearRules"] > 3 else "Individualist_LowPowerDistance"

    profile = {
        "justice_sensitivity": "Unknown",
        "ocb_confidence": "Unknown",
        "interpretation": ""
    }

    if emotion == "Low" and culture == "Collectivist_HighPowerDistance":
        profile["justice_sensitivity"] = "High"
        profile["ocb_confidence"] = "Very High"
        profile["interpretation"] = "High procedural justice sensitivity with strong likelihood of OCB display."
    elif emotion == "Low" and culture == "Individualist_LowPowerDistance":
        profile["justice_sensitivity"] = "Moderate"
        profile["ocb_confidence"] = "Moderate"
        profile["interpretation"] = "Moderate reactivity to fairness, outcome-focused tendencies."
    elif emotion == "High" and culture == "Collectivist_HighPowerDistance":
        profile["justice_sensitivity"] = "Moderate"
        profile["ocb_confidence"] = "Moderate"
        profile["interpretation"] = "Emotionally positive but less sensitive to procedural signals."
    elif emotion == "High" and culture == "Individualist_LowPowerDistance":
        profile["justice_sensitivity"] = "Low"
        profile["ocb_confidence"] = "Likely Inflated"
        profile["interpretation"] = "May overestimate self-report due to emotional and individualist traits."

    if gender == "female" and emotion == "Low" and culture == "Collectivist_HighPowerDistance":
        profile["justice_sensitivity"] = "Very High"
        profile["ocb_confidence"] = "Strong Display"
        profile["interpretation"] = "Ideal fairness orientation for high OCB engagement."

    if gender == "male" and emotion == "Low" and culture == "Individualist_LowPowerDistance":
        profile["justice_sensitivity"] = "Low"
        profile["ocb_confidence"] = "Likely Suppressed"
        profile["interpretation"] = "Lower engagement and justice sensitivity likely."

    return profile

def check_exaggeration(sd_score):
    if sd_score > 4.0:
        return "⚠️ High social desirability detected — OCB score may be inflated."
    elif sd_score < 3.0:
        return "👍 Low social desirability — response likely genuine."
    else:
        return "Moderate SD — interpret with context."

def process_user_response(data):
    ocb_score = compute_ocb_score(data["OCBItems"])
    justice_scores = compute_justice_averages(data["Justice"])
    profile = interpret_profile(data["Gender"], data["Emotion"], data["Culture"])
    exaggeration_flag = check_exaggeration(data["SDScore"])

    return {
        "OCBScore": ocb_score,
        "JusticeScores": justice_scores,
        "JusticeSensitivity": profile["justice_sensitivity"],
        "OCBConfidence": profile["ocb_confidence"],
        "Interpretation": profile["interpretation"],
        "ExaggerationNote": exaggeration_flag
    }
