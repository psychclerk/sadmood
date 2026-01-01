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

        # 1. Major Depressive Disorder
        {
            "diagnosis": "Major Depressive Disorder",
            "age": 35,
            "sex": "Female",
            "mood": "Persistent sadness and hopelessness most of the day",
            "duration": "8 weeks",
            "associated": "Anhedonia, guilt, poor sleep, low energy",
            "risk_factors": ["Past depressive episode"],
            "mse": "Depressed affect, psychomotor retardation, reduced speech",
            "investigations": "CBC, TSH, Vitamin B12 – normal",
            "suicide_risk": {
                "ideation": "Passive death wishes",
                "plan": "Absent",
                "risk_level": "Moderate"
            },
            "explanation": "Symptoms >2 weeks with biological features and functional impairment.",
            "management": (
                "• Assess suicide risk\n"
                "• Start SSRI\n"
                "• Cognitive Behavioral Therapy\n"
                "• Regular follow-up"
            )
        },

        # 2. Persistent Depressive Disorder
        {
            "diagnosis": "Persistent Depressive Disorder (Dysthymia)",
            "age": 42,
            "sex": "Male",
            "mood": "Chronic low mood most days",
            "duration": "3 years",
            "associated": "Low self-esteem, fatigue, pessimism",
            "risk_factors": ["Chronic stress"],
            "mse": "Constricted affect, coherent speech",
            "investigations": "Normal",
            "suicide_risk": {
                "ideation": "Occasional passive thoughts",
                "plan": "Absent",
                "risk_level": "Low–Moderate"
            },
            "explanation": "Chronic depressive symptoms >2 years, less severe but persistent.",
            "management": (
                "• Psychotherapy\n"
                "• SSRIs if functionally impairing\n"
                "• Long-term follow-up"
            )
        },

        # 3. Adjustment Disorder
        {
            "diagnosis": "Adjustment Disorder with Depressed Mood",
            "age": 28,
            "sex": "Female",
            "mood": "Sadness and frequent crying",
            "duration": "1 month",
            "associated": "Anxiety, poor concentration",
            "risk_factors": ["Recent job loss"],
            "mse": "Emotionally distressed, appropriate responses",
            "investigations": "Not required",
            "suicide_risk": {
                "ideation": "Absent",
                "plan": "Absent",
                "risk_level": "Low"
            },
            "explanation": "Emotional response to identifiable stressor within 3 months.",
            "management": (
                "• Supportive psychotherapy\n"
                "• Stress management\n"
                "• Usually self-limiting"
            )
        },

        # 4. Bereavement
        {
            "diagnosis": "Bereavement (Normal Grief)",
            "age": 50,
            "sex": "Male",
            "mood": "Sadness with longing for deceased spouse",
            "duration": "6 weeks",
            "associated": "Crying spells, preserved self-esteem",
            "risk_factors": ["Recent death of spouse"],
            "mse": "Appropriate affect, emotional reactivity preserved",
            "investigations": "Not indicated",
            "suicide_risk": {
                "ideation": "Absent",
                "plan": "Absent",
                "risk_level": "Low"
            },
            "explanation": "Normal grief reaction without pathological guilt or worthlessness.",
            "management": (
                "• Reassurance\n"
                "• Grief counseling\n"
                "• Monitor for depression"
            )
        },

        # 5. Bipolar Depression
        {
            "diagnosis": "Bipolar Disorder – Depressive Episode",
            "age": 24,
            "sex": "Female",
            "mood": "Severe low mood and hypersomnia",
            "duration": "3 weeks",
            "associated": "Psychomotor retardation, increased appetite",
            "risk_factors": ["Past manic episode"],
            "mse": "Marked psychomotor slowing",
            "investigations": "Routine labs normal",
            "suicide_risk": {
                "ideation": "Active",
                "plan": "Vague plan",
                "risk_level": "High"
            },
            "explanation": "Depression occurring in bipolar disorder.",
            "management": (
                "• Urgent suicide risk management\n"
                "• Mood stabilizers\n"
                "• Avoid antidepressant monotherapy"
            )
        },

        # 6. Hypothyroidism
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
                "plan": "Absent",
                "risk_level": "Low"
            },
            "explanation": "Depressive symptoms secondary to endocrine disorder.",
            "management": (
                "• Start levothyroxine\n"
                "• Monitor thyroid function\n"
                "• Reassess mood"
            )
        },

        # 7. Substance-Induced Depression
        {
            "diagnosis": "Substance-Induced Depressive Disorder",
            "age": 32,
            "sex": "Male",
            "mood": "Low mood after alcohol cessation",
            "duration": "2 weeks",
            "associated": "Insomnia, irritability",
            "risk_factors": ["Chronic alcohol use"],
            "mse": "Anxious, restless",
            "investigations": "Deranged liver enzymes",
            "suicide_risk": {
                "ideation": "Passive",
                "plan": "Absent",
                "risk_level": "Moderate"
            },
            "explanation": "Mood symptoms temporally related to substance use or withdrawal.",
            "management": (
                "• Abstinence\n"
                "• Treat withdrawal\n"
                "• Reassess mood after detox"
            )
        },

        # 8. Psychotic Depression
        {
            "diagnosis": "Depression with Psychotic Features",
            "age": 60,
            "sex": "Female",
            "mood": "Severe depression",
            "duration": "2 months",
            "associated": "Delusions of guilt and worthlessness",
            "risk_factors": ["Elderly"],
            "mse": "Mood-congruent delusions",
            "investigations": "Normal",
            "suicide_risk": {
                "ideation": "Active",
                "plan": "Formed",
                "risk_level": "High"
            },
            "explanation": "Severe depression with psychotic symptoms.",
            "management": (
                "• Hospitalization\n"
                "• Antidepressant + antipsychotic\n"
                "• Consider ECT"
            )
        },

        # 9. Depression due to Medical Illness
        {
            "diagnosis": "Depression due to Chronic Medical Illness",
            "age": 55,
            "sex": "Male",
            "mood": "Low mood and fatigue",
            "duration": "4 months",
            "associated": "Poor sleep, reduced appetite",
            "risk_factors": ["Chronic kidney disease"],
            "mse": "Ill-looking, low affect",
            "investigations": "Raised creatinine",
            "suicide_risk": {
                "ideation": "Absent",
                "plan": "Absent",
                "risk_level": "Low"
            },
            "explanation": "Depression secondary to chronic medical condition.",
            "management": (
                "• Treat underlying illness\n"
                "• Psychotherapy\n"
                "• Antidepressants if needed"
            )
        },

        # 10. PMDD
        {
            "diagnosis": "Premenstrual Dysphoric Disorder (PMDD)",
            "age": 26,
            "sex": "Female",
            "mood": "Cyclical depressive symptoms before menses",
            "duration": "Last week of menstrual cycle",
            "associated": "Irritability, mood swings",
            "risk_factors": ["Hormonal sensitivity"],
            "mse": "Normal",
            "investigations": "Clinical diagnosis",
            "suicide_risk": {
                "ideation": "Absent",
                "plan": "Absent",
                "risk_level": "Low"
            },
            "explanation": "Mood symptoms limited to luteal phase.",
            "management": (
                "• SSRIs (continuous or luteal)\n"
                "• Lifestyle modification\n"
                "• Psychoeducation"
            )
        }
    ]

    return random.choice(cases)

# -----------------------------------
# Session State
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
# UI SECTIONS
# -----------------------------------

st.header("📜 History")
if st.button("Reveal History"):
    st.session_state.reveal["history"] = True
if st.session_state.reveal["history"]:
    st.write(f"**Age/Sex:** {case['age']} / {case['sex']}")
    st.write(f"**Mood:** {case['mood']}")
    st.write(f"**Duration:** {case['duration']}")
    st.write(f"**Associated:** {case['associated']}")
    st.write(f"**Risk Factors:** {', '.join(case['risk_factors'])}")

st.header("🩺 Mental Status Examination")
if st.button("Reveal MSE"):
    st.session_state.reveal["mse"] = True
if st.session_state.reveal["mse"]:
    st.write(case["mse"])

st.header("🧪 Investigations")
if st.button("Reveal Investigations"):
    st.session_state.reveal["investigations"] = True
if st.session_state.reveal["investigations"]:
    st.write(case["investigations"])

st.header("⚠️ Suicide Risk Assessment")
if st.button("Assess Suicide Risk"):
    st.session_state.reveal["suicide"] = True
if st.session_state.reveal["suicide"]:
    sr = case["suicide_risk"]
    st.write(f"Ideation: {sr['ideation']}")
    st.write(f"Plan: {sr['plan']}")
    st.write(f"Risk Level: {sr['risk_level']}")

st.header("🧠 Most Likely Diagnosis")
options = [
    "Major Depressive Disorder",
    "Persistent Depressive Disorder (Dysthymia)",
    "Adjustment Disorder with Depressed Mood",
    "Bereavement (Normal Grief)",
    "Bipolar Disorder – Depressive Episode",
    "Hypothyroidism",
    "Substance-Induced Depressive Disorder",
    "Depression with Psychotic Features",
    "Depression due to Chronic Medical Illness",
    "Premenstrual Dysphoric Disorder (PMDD)"
]
user_dx = st.selectbox("Select diagnosis", options)
if st.button("Submit Diagnosis"):
    if user_dx == case["diagnosis"]:
        st.success("✅ Correct diagnosis")
    else:
        st.error(f"❌ Correct answer: {case['diagnosis']}")

st.header("📖 Clinical Explanation")
if st.button("Reveal Explanation"):
    st.session_state.reveal["explanation"] = True
if st.session_state.reveal["explanation"]:
    st.info(case["explanation"])

st.header("💊 Management")
if st.button("Reveal Management"):
    st.session_state.reveal["management"] = True
if st.session_state.reveal["management"]:
    st.success(case["management"])

st.divider()
if st.button("🔄 New Case"):
    st.session_state.clear()
    st.rerun()
