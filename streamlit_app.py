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
st.caption("Psychiatry clinical reasoning simulator – MBBS level")

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
                "Symptoms >2 weeks with biological features and functional impairment, "
                "without history of mania. Meets criteria for Major Depressive Disorder."
            ),
            "management": (
                "• Assess suicide risk and ensure safety\n"
                "• Start SSRI (e.g., sertraline / escitalopram)\n"
                "• Cognitive Behavioral Therapy\n"
                "• Follow-up in 2–4 weeks\n"
                "• Psychiatric referral if poor response"
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
                "Chronic depressive symptoms lasting >2 years without symptom-free periods. "
                "Less severe than MDD but persistent."
            ),
            "management": (
                "• Psychotherapy (CBT / interpersonal therapy)\n"
                "• SSRIs if symptoms impair functioning\n"
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
                "Emotional response to an identifiable stressor within 3 months. "
                "Does not meet criteria for major depression."
            ),
            "management": (
                "• Supportive counseling\n"
                "• Stress management\n"
                "• Short-term psychotherapy\n"
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
                "Normal grief reaction with preserved functioning and self-esteem. "
                "Sadness is related to loss, not pervasive hopelessness."
            ),
            "management": (
                "• Reassurance and psychoeducation\n"
                "• Grief counseling\n"
                "• Monitor for progression to depression"
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
                "Depressive episode in a patient with history of mania. "
                "Antidepressant monotherapy may precipitate mania."
            ),
            "management": (
                "• Immediate suicide risk management\n"
                "• Hospital admission if required\n"
                "• Mood stabilizers (lithium / valproate)\n"
                "• Avoid antidepressant monotherapy"
            )
        },

        {
            "diagnosis": "Hypothyroidism",
            "age": 45,
            "sex": "Female",
            "mood": "Low mood and apathy",
            "duration": "Several months",
            "associated": "Weight gain, cold intolerance, constipation",
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
                "• Reassess mood after euthyroid state"
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
                "• Abstinence from substance\n"
                "• Supportive care\n"
                "• Treat withdrawal if present\n"
                "• Antidepressants only if symptoms persist"
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
                "• Ensure safety and hospitalize\n"
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
                "• Treat underlying medical condition\n"
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
    st.session_state.revealed = False

case = st.session_state.case

# -----------------------------------
# UI Sections
# -----------------------------------
st.header("📜 History")
if st.button("Reveal History"):
    st.session_state.revealed = True

if st.session_state.revealed:
    st.write(f"**Age / Sex:** {case['age']} / {case['sex']}")
    st.write(f"**Mood Complaint:** {case['mood']}")
    st.write(f"**Duration:** {case['duration']}")
    st.write(f"**Associated Symptoms:** {case['associated']}")
    st.write(f"**Risk Factors:** {', '.join(case['risk_factors'])}")

st.header("🩺 Mental Status Examination")
if st.session_state.revealed:
    st.write(case["exam"])

st.header("🧪 Investigations")
if st.session_state.revealed:
    st.write(case["investigations"])

st.header("⚠️ Suicide Risk Assessment")
if st.session_state.revealed:
    sr = case["suicide_risk"]
    st.write(f"**Ideation:** {sr['ideation']}")
    st.write(f"**Plan:** {sr['plan']}")
    st.write(f"**Overall Risk Level:** {sr['risk_level']}")

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

st.header("📖 Clinical Explanation")
if st.checkbox("Show Explanation"):
    st.info(case["explanation"])

st.header("💊 Management Plan")
if st.checkbox("Show Management"):
    st.success(case["management"])

st.divider()
if st.button("🔄 New Case"):
    st.session_state.clear()
    st.rerun()
