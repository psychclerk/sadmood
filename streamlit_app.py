import streamlit as st
import random

# -----------------------------------
# App Config
# -----------------------------------
st.set_page_config(
    page_title="Sad Mood Case Simulator",
    layout="centered"
)

st.title("😔 Sad Mood Case Simulator")
st.caption("Psychiatry OSCE & clinical reasoning – MBBS level")

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
            "exam": "Depressed affect, psychomotor retardation, reduced speech",
            "investigations": "CBC, TSH, B12 – normal",
            "suicide_risk": {
                "ideation": "Passive death wishes present",
                "plan": "No active plan",
                "risk_level": "Moderate"
            },
            "explanation": (
                "Symptoms lasting >2 weeks with biological features and functional impairment, "
                "without history of mania."
            ),
            "management": (
                "• Ensure safety and assess suicide risk\n"
                "• Start SSRI (sertraline / escitalopram)\n"
                "• Cognitive Behavioral Therapy\n"
                "• Follow-up in 2–4 weeks"
            )
        },

        {
            "diagnosis": "Persistent Depressive Disorder (Dysthymia)",
            "age": 42,
            "sex": "Male",
            "mood": "Chronic low mood most days",
            "duration": "3 years",
            "associated": "Low self-esteem, fatigue, pessimism",
            "risk_factors": ["Chronic psychosocial stress"],
            "exam": "Constricted affect, cooperative",
            "investigations": "Normal",
            "suicide_risk": {
                "ideation": "Occasional passive thoughts",
                "plan": "None",
                "risk_level": "Low–Moderate"
            },
            "explanation": (
                "Chronic depressive symptoms >2 years, less severe but persistent."
            ),
            "management": (
                "• Psychotherapy (CBT / interpersonal therapy)\n"
                "• SSRIs if functionally impairing\n"
                "• Long-term follow-up"
            )
        },

        {
            "diagnosis": "Adjustment Disorder with Depressed Mood",
            "age": 28,
            "sex": "Female",
            "mood": "Sadness and crying spells after stressor",
            "duration": "1 month",
            "associated": "Anxiety, poor concentration",
            "risk_factors": ["Recent job loss"],
            "exam": "Emotionally distressed but coherent",
            "investigations": "Not required",
            "suicide_risk": {
                "ideation": "Absent",
                "plan": "None",
                "risk_level": "Low"
            },
            "explanation": (
                "Emotional response to an identifiable stressor occurring within 3 months."
            ),
            "management": (
                "• Supportive counseling\n"
                "• Stress management\n"
                "• Usually self-limiting"
            )
        },

        {
            "diagnosis": "Bereavement (Normal Grief)",
            "age": 50,
            "sex": "Male",
            "mood": "Sadness with yearning for deceased spouse",
            "duration": "6 weeks",
            "associated": "Crying spells, preserved self-worth",
            "risk_factors": ["Recent death of spouse"],
            "exam": "Appropriate affect, emotional reactivity preserved",
            "investigations": "Not indicated",
            "suicide_risk": {
                "ideation": "Absent",
                "plan": "None",
                "risk_level": "Low"
            },
            "explanation": (
                "Normal grief reaction with preserved functioning and self-esteem."
            ),
            "management": (
                "• Reassurance and psychoeducation\n"
                "• Grief counseling\n"
                "• Monitor for depression"
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
            "exam": "Marked psychomotor retardation",
            "investigations": "Normal",
            "suicide_risk": {
                "ideation": "Active suicidal thoughts",
                "plan": "Vague plan present",
                "risk_level": "High"
            },
            "explanation": (
                "Depressive episode in bipolar disorder. Antidepressant monotherapy is unsafe."
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
            "exam": "Dry skin, bradycardia",
            "investigations": "Elevated TSH, low T4",
            "suicide_risk": {
                "ideation": "Absent",
                "plan": "None",
                "risk_level": "Low"
            },
            "explanation": (
                "Depressive symptoms secondary to endocrine disorder."
            ),
            "management": (
                "• Start levothyroxine\n"
                "• Monitor thyroid function\n"
                "• Reassess mood"
            )
        },

        {
            "diagnosis": "Substance-Induced Depressive Disorder",
            "age": 32,
            "sex": "Male",
            "mood": "Low mood after alcohol cessation",
            "duration": "2 weeks",
            "associated": "Insomnia, irritability",
            "risk_factors": ["Chronic alcohol use"],
            "exam": "Anxious, tremulous",
            "investigations": "Deranged liver enzymes",
            "suicide_risk": {
                "ideation": "Passive thoughts present",
                "plan": "None",
                "risk_level": "Moderate"
            },
            "explanation": (
                "Depressive symptoms temporally related to substance use or withdrawal."
            ),
            "management": (
                "• Abstinence and supportive care\n"
                "• Treat withdrawal\n"
                "• Reassess mood after abstinence"
            )
        },

        {
            "diagnosis": "Depression with Psychotic Features",
            "age": 60,
            "sex": "Female",
            "mood": "Severe depression",
            "duration": "2 months",
            "associated": "Delusions of guilt and worthlessness",
            "risk_factors": ["Elderly"],
            "exam": "Mood-congruent delusions",
            "investigations": "Normal",
            "suicide_risk": {
                "ideation": "Active",
                "plan": "Formed",
                "risk_level": "High"
            },
            "explanation": (
                "Severe depression accompanied by psychotic symptoms."
            ),
            "management": (
                "• Hospitalize\n"
                "• Antidepressant + antipsychotic\n"
                "• Consider ECT"
            )
        },

        {
            "diagnosis": "Depression due to Chronic Medical Illness",
            "age": 55,
            "sex": "Male",
            "mood": "Low mood and fatigue",
            "duration": "4 months",
            "associated": "Poor appetite, insomnia",
            "risk_factors": ["Chronic kidney disease"],
            "exam": "Ill-looking",
            "investigations": "Raised creatinine",
            "suicide_risk": {
                "ideation": "Absent",
                "plan": "None",
                "risk_level": "Low"
            },
            "explanation": (
                "Depression secondary to chronic medical illness."
            ),
            "management": (
                "• Treat underlying illness\n"
                "• Psychotherapy\n"
                "• Antidepressants if required"
            )
        },

        {
            "diagnosis": "Premenstrual Dysphoric Disorder (PMDD)",
            "age": 26,
            "sex": "Female",
            "mood": "Cyclical depressive symptoms premenstrually",
            "duration": "Last week of menstrual cycle",
            "associated": "Irritability, mood swings",
            "risk_factors": ["Hormonal sensitivity"],
            "exam": "Normal",
            "investigations": "Clinical diagnosis",
            "suicide_risk": {
                "ideation": "Absent",
                "plan": "None",
                "risk_level": "Low"
            },
            "explanation": (
                "Mood symptoms occur in luteal phase and resolve after menstruation."
            ),
            "management": (
                "• SSRIs (continuous or luteal phase)\n"
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
    st.session_state.revealed = {
        "history": False,
        "exam": False,
        "investigations": False,
        "suicide": False,
        "explanation": False,
        "management": False
    }

case = st.session_state.case

# -----------------------------------
# UI Sections
# -----------------------------------

# History
st.header("📜 History")
if st.button("Reveal History"):
    st.session_state.revealed["history"] = True

if st.session_state.revealed["history"]:
    st.write(f"**Age / Sex:** {case['age']} / {case['sex']}")
    st.write(f"**Mood Complaint:** {case['mood']}")
    st.write(f"**Duration:** {case['duration']}")
    st.write(f"**Associated Symptoms:** {case['associated']}")
    st.write(f"**Risk Factors:** {', '.join(case['risk_factors'])}")

# Examination
st.header("🩺 Mental Status Examination")
if st.button("Reveal Mental Status Examination"):
    st.session_state.revealed["exam"] = True

if st.session_state.revealed["exam"]:
    st.write(case["exam"])

# Investigations
st.header("🧪 Investigations")
if st.button("Order Investigations"):
    st.session_state.revealed["investigations"] = True

if st.session_state.revealed["investigations"]:
    st.write(case["investigations"])

# Suicide Risk
st.header("⚠️ Suicide Risk Assessment")
if st.button("Assess Suicide Risk"):
    st.session_state.revealed["suicide"] = True

if st.session_state.revealed["suicide"]:
    sr = case["suicide_risk"]
    st.write(f"**Ideation:** {sr['ideation']}")
    st.write(f"**Plan:** {sr['plan']}")
    st.write(f"**Risk Level:** {sr['risk_level']}")

# Diagnosis
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

user_dx = st.selectbox("Choose diagnosis", options)

if st.button("Submit Diagnosis"):
    if user_dx == case["diagnosis"]:
        st.success("✅ Correct diagnosis")
    else:
        st.error(f"❌ Incorrect. Correct answer: **{case['diagnosis']}**")

# Explanation
st.header("📖 Clinical Explanation")
if st.button("Show Explanation"):
    st.session_state.revealed["explanation"] = True

if st.session_state.revealed["explanation"]:
    st.info(case["explanation"])

# Management
st.header("💊 Management Plan")
if st.button("Show Management"):
    st.session_state.revealed["management"] = True

if st.session_state.revealed["management"]:
    st.success(case["management"])

# Reset
st.divider()
if st.button("🔄 New Case"):
    st.session_state.clear()
    st.rerun()
