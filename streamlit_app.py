import streamlit as st
import random

# -----------------------------------
# App Config
# -----------------------------------
st.set_page_config(page_title="Sad Mood Case Simulator", layout="centered")

st.title("😔 Sad Mood Case Simulator")
st.caption("Psychiatry OSCE & Clinical Reasoning – MBBS Level")

# -----------------------------------
# Case Generator
# -----------------------------------
def generate_case():
    cases = [
        {
            "diagnosis": "Major Depressive Disorder",
            "age": 35,
            "sex": "Female",
            "mood": "Persistent sadness and hopelessness most of the day",
            "duration": "8 weeks",
            "associated": "Anhedonia, early morning awakening, guilt, low energy",
            "risk_factors": ["Past depressive episode"],
            "mse": "Depressed affect, psychomotor retardation, reduced speech",
            "investigations": "CBC, TSH, Vitamin B12 – all normal",
            "suicide_risk": {
                "ideation": "Passive death wishes present",
                "plan": "No active plan",
                "risk_level": "Moderate"
            },
            "explanation": (
                "Depressive symptoms >2 weeks with biological features "
                "and no history of mania."
            ),
            "management": (
                "• Ensure safety and suicide risk assessment\n"
                "• Start SSRI (sertraline / escitalopram)\n"
                "• Cognitive Behavioral Therapy\n"
                "• Regular follow-up"
            )
        },

        {
            "diagnosis": "Bipolar Disorder – Depressive Episode",
            "age": 24,
            "sex": "Female",
            "mood": "Severe low mood with hypersomnia",
            "duration": "3 weeks",
            "associated": "Psychomotor slowing, increased appetite",
            "risk_factors": ["Past manic episode"],
            "mse": "Marked psychomotor retardation",
            "investigations": "Routine labs normal",
            "suicide_risk": {
                "ideation": "Active suicidal thoughts",
                "plan": "Vague plan present",
                "risk_level": "High"
            },
            "explanation": (
                "Depressive episode in bipolar disorder. "
                "Antidepressant monotherapy is contraindicated."
            ),
            "management": (
                "• Immediate suicide risk management\n"
                "• Mood stabilizers (lithium / valproate)\n"
                "• Hospitalization if required"
            )
        },

        {
            "diagnosis": "Hypothyroidism",
            "age": 45,
            "sex": "Female",
            "mood": "Low mood and apathy",
            "duration": "Several months",
            "associated": "Weight gain, cold intolerance",
            "risk_factors": ["Autoimmune disease"],
            "mse": "Slow speech, dull affect",
            "investigations": "↑ TSH, ↓ Free T4",
            "suicide_risk": {
                "ideation": "Absent",
                "plan": "None",
                "risk_level": "Low"
            },
            "explanation": (
                "Depressive symptoms secondary to hypothyroidism."
            ),
            "management": (
                "• Start levothyroxine\n"
                "• Monitor thyroid profile\n"
                "• Reassess mood symptoms"
            )
        }
    ]

    return random.choice(cases)

# -----------------------------------
# Session State Initialization
# -----------------------------------
if "case" not in st.session_state:
    st.session_state.case = generate_case()
    st.session_state.reveal = {
        "history": False,
        "mse": False,
        "investigations": False,
        "suicide": False,
        "explanation": False,
        "management": False
    }

case = st.session_state.case

# -----------------------------------
# HISTORY
# -----------------------------------
st.header("📜 History")
if st.button("Reveal History"):
    st.session_state.reveal["history"] = True

if st.session_state.reveal["history"]:
    st.write(f"**Age / Sex:** {case['age']} / {case['sex']}")
    st.write(f"**Presenting Complaint:** {case['mood']}")
    st.write(f"**Duration:** {case['duration']}")
    st.write(f"**Associated Symptoms:** {case['associated']}")
    st.write(f"**Risk Factors:** {', '.join(case['risk_factors'])}")

# -----------------------------------
# MENTAL STATUS EXAMINATION
# -----------------------------------
st.header("🩺 Mental Status Examination")
if st.button("Reveal MSE"):
    st.session_state.reveal["mse"] = True

if st.session_state.reveal["mse"]:
    st.write(case["mse"])

# -----------------------------------
# INVESTIGATIONS
# -----------------------------------
st.header("🧪 Investigations")
if st.button("Reveal Investigations"):
    st.session_state.reveal["investigations"] = True

if st.session_state.reveal["investigations"]:
    st.write(case["investigations"])

# -----------------------------------
# SUICIDE RISK
# -----------------------------------
st.header("⚠️ Suicide Risk Assessment")
if st.button("Assess Suicide Risk"):
    st.session_state.reveal["suicide"] = True

if st.session_state.reveal["suicide"]:
    sr = case["suicide_risk"]
    st.write(f"**Ideation:** {sr['ideation']}")
    st.write(f"**Plan:** {sr['plan']}")
    st.write(f"**Overall Risk:** {sr['risk_level']}")

# -----------------------------------
# DIAGNOSIS
# -----------------------------------
st.header("🧠 Most Likely Diagnosis")

diagnosis_options = [
    "Major Depressive Disorder",
    "Bipolar Disorder – Depressive Episode",
    "Hypothyroidism"
]

user_dx = st.selectbox("Select diagnosis", diagnosis_options)

if st.button("Submit Diagnosis"):
    if user_dx == case["diagnosis"]:
        st.success("✅ Correct diagnosis")
    else:
        st.error(f"❌ Incorrect. Correct answer: **{case['diagnosis']}**")

# -----------------------------------
# EXPLANATION
# -----------------------------------
st.header("📖 Clinical Explanation")
if st.button("Reveal Explanation"):
    st.session_state.reveal["explanation"] = True

if st.session_state.reveal["explanation"]:
    st.info(case["explanation"])

# -----------------------------------
# MANAGEMENT
# -----------------------------------
st.header("💊 Management Plan")
if st.button("Reveal Management"):
    st.session_state.reveal["management"] = True

if st.session_state.reveal["management"]:
    st.success(case["management"])

# -----------------------------------
# RESET
# -----------------------------------
st.divider()
if st.button("🔄 New Case"):
    st.session_state.clear()
    st.rerun()
