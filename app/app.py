import streamlit as st
import joblib 
import numpy as np 
import pandas as pd 
import os
import base64

# 1. Page Configuration 
st.set_page_config(
    page_title="SymptoCare",
    page_icon="app/logo.png",
    layout="centered"
)

# 2. Custom CSS for Clean Disclaimer Footer 
st.markdown(
    """
    <style>
    .disclaimer-footer {
        margin-top: 40px;
        padding: 12px 16px;
        border: 1px solid #CBD5E1;
        border-radius: 8px;
        background-color: transparent;
        color: #64748B;
        font-size: 0.85rem;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---LOAD TRAINED MODEL & SYMPTOM LIST ---
@st.cache_resource 
def load_model_and_symptoms():
    # Load model and symptom feature list from models folder 
    model = joblib.load("models/symptom_checker_model.pkl")
    symptom_list = joblib.load("models/symptom_list.pkl")
    return model, symptom_list

try:
    model, raw_symptom_list = load_model_and_symptoms()
    
    # Format symptom names for display (e.g., 'skin_rash' -> 'Skin Rash')
    symptom_display_map = {col: str(col).replace('_', ' ').strip().title() for col in raw_symptom_list}
    display_to_col_map = {v: k for k, v in symptom_display_map.items()}
    all_display_symptoms = sorted(list(symptom_display_map.values()))
except Exception as e:
    st.error(f"Error loading model files: {e}. Ensure both .pkl files are inside the 'models' folder.")
    all_display_symptoms = ["Skin Swelling", "Fever", "Headache", "Cough", "Fatigue", "Hair Loss", "Itching", "Rash"]

# 3. Sidebar: Patient Context Metrics 
with st.sidebar:
    st.header("👤 Patient Demographics")
    st.caption("Provide context for a more tailored assessment.")

    age = st.number_input("Age", min_value=1, max_value=120, value=25)
    gender = st.selectbox("Biological Sex", ["Female", "Male", "Other"])
    duration = st.selectbox("Symptom Duration", ["Less than 3 days", "3-7 days", "1-2 weeks", "More than 2 weeks"])

    st.divider()
    st.info("💡 **Note:** Demographics help contextualize risk factors for clinical evaluation.")

# 4. Main Header 
if os.path.exists("app/logo.png"):
    logo_path = "app/logo.png"
elif os.path.exists("logo.png"):
    logo_path = "logo.png"
else:
    logo_path = None

if logo_path:
    import base64
    with open(logo_path, "rb") as f:
        img_data = base64.b64encode(f.read()).decode()
    logo_html = f'<img src="data:image/png;base64,{img_data}" style="height: 60px; width: auto; object-fit: contain;">'
else: 
    logo_html = '<span style="font-size: 2.5rem; line-height: 1;">🩺</span>' 

st.markdown(
    f"""
    <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 4px;">
        {logo_html}
        <div style="border-left: 2px solid #CBD5E1; height: 45px;"></div>
        <h1 style="margin: 0; padding: 0; font-size: 2.6rem; font-weight: 700; color: #1E293B; line-height: 1;">
            SymptoCare
        </h1>
    </div>
    <p style="font-size: 1.05rem; color: #64748B; margin-top: 2px; margin-bottom: 12px;">
        <em>AI-Powered Clinical Insights</em>
    </p>
    """,
    unsafe_allow_html=True
)

st.caption("Select your symptoms below to generate a preliminary clinical assessment.")

# 5. Dynamic Symptom Selection from Trained Feature List 
symptoms = st.multiselect(
    "Select your symptoms:", 
    options=all_display_symptoms
)

# 6. Real AI Model Prediction Logic 
if st.button("Analyze Symptoms", type="primary"):
    if not symptoms:
        st.warning("Please select at least one symptom before analyzing.")
    else: 
        st.divider()
        st.subheader("📋 Assessment Results")

        # FIX: Ensure raw_symptom_list is a Python list once for exact index lookup
        feature_columns = list(raw_symptom_list)

        # Build 1D feature vector initialized to 0
        input_vector = [0] * len(feature_columns)
        
        for s in symptoms:
            if s in display_to_col_map:
                raw_col = display_to_col_map[s]
                if raw_col in feature_columns:
                    idx = feature_columns.index(raw_col)
                    input_vector[idx] = 1

        # Convert input vector to DataFrame matching model feature exactly
        input_data = pd.DataFrame([input_vector], columns=feature_columns)
        prediction = model.predict(input_data)[0]

        # Display top prediction 
        st.success(f"**Primary Assessment:** {str(prediction).title()}")

        # Extract probabilities for Differential Diagnosis 
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(input_data)[0]
            classes = model.classes_

            # Combine classes and probabilities into a sorted list 
            prob_pairs = sorted(zip(classes, probabilities), key=lambda x: x[1], reverse=True)
            top_3 = prob_pairs[:3]

            st.markdown("### **Differential Diagnosis (Possibilities Breakdown)**")
            st.caption("Relative likelihood based on model confidence:")

            for condition, prob in top_3:
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"**{str(condition).title()}**")
                    st.progress(float(prob))
                with col2:
                    st.write(f"**{int(prob * 100)}%**")
        
        # Clean Footer Disclaimer Card 
        st.markdown(
            """
            <div class="disclaimer-footer">
                ⚠️ <strong>Disclaimer:</strong> This tool is for educational purposes only and does not replace professional medical advice, diagnosis, or treatment.
            </div>
            """,
            unsafe_allow_html=True
        )