import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# ---------------------------------------------------------
# Page Configuration & Custom CSS
# ---------------------------------------------------------
logo_path = os.path.join('app', 'logo.png')

st.set_page_config(
    page_title="SymptoCare",
    page_icon=logo_path if os.path.exists(logo_path) else "🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject CSS for cyan/blue medical palette, spaced tabs, transparent header, and forced dropdown menu direction
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #f4f8fb;
    }
    
    /* Transparent header to prevent top white line */
    header[data-testid="stHeader"] {
        background-color: #f4f8fb !important;
    }

    div[data-testid="stRadio"] label > div:first-child {
        display: none !important;
    }
    
    div[data-testid="stRadio"] > div {
        display: flex;
        flex-direction: row;
        gap: 36px;
        border-bottom: 2px solid #e1effe;
        padding-bottom: 0px;
        margin-bottom: 24px;
    }

    /* Base tab link styling (18px, bright blue color) */
    div[data-testid="stRadio"] label,
    div[data-testid="stRadio"] label p {
        background: none !important;
        border: none !important;
        font-weight: 600 !important;
        font-size: 17px !important;
        color: #0066cc !important;   
        cursor: pointer;
        transition: all 0.2s ease-in-out;
    }

    div[data-testid="stRadio"] label {
        padding: 8px 4px 12px 4px !important;
        border-bottom: 3px solid transparent !important;
    }

    /* Hover effect */
    div[data-testid="stRadio"] label:hover,
    div[data-testid="stRadio"] label:hover p {
        color: #0066cc !important;
        opacity: 0.8;
    }
    
    /* Active tab effect: slightly bigger (20px), bolder, with bottom underline */
    div[data-testid="stRadio"] label:has(input:checked),
    div[data-testid="stRadio"] label:has(input:checked) p {
        color: #0066cc !important;
        font-size: 17px !important;  
        font-weight: 700 !important; 
        opacity: 1;
    }

    div[data-testid="stRadio"] label:has(input:checked) {
        border-bottom: 3px solid #0066cc !important;
    }
    
    /* Ensure multiselect dropdown opens downward comfortably */
    div[data-baseweb="popover"] {
        margin-top: 4px !important;
    }

    /* Feature Card design */
    .feature-card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 102, 204, 0.05);
        border: 1px solid #e1effe;
        height: 100%;
        transition: transform 0.2s ease;
    }
    .feature-card:hover {
        transform: translateY(-2px);
    }
    .feature-icon {
        font-size: 28px;
        margin-bottom: 12px;
    }
    .feature-title {
        font-size: 18px;
        font-weight: 600;
        color: #0b3c5d;
        margin-bottom: 8px;
    }
    .feature-desc {
        font-size: 14px;
        color: #5a6e7f;
        line-height: 1.5;
    }
    .feature-link {
        margin-top: 14px;
        font-weight: 600;
        font-size: 14px;
        color: #0066cc;
        text-decoration: none;
    }

    .step-circle {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Top Header Display
# ---------------------------------------------------------
if os.path.exists(logo_path):
    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 20px; margin-top: -25px; margin-bottom: 15px;">
            <img src="data:image/png;base64,{joblib.load if False else ''}" style="display:none;" />
            <!-- Logo Image via HTML for precise vertical alignment -->
        </div>
    """, unsafe_allow_html=True)
    
    # Pure Flexbox layout for clean logo + vertical line + title alignment
    import base64
    with open(logo_path, "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 18px; margin-top: -30px; margin-bottom: 20px;">
            <img src="data:image/png;base64,{encoded_logo}" style="height: 65px; width: auto; object-fit: contain;">
            <div style="border-left: 2px solid #cbd5e1; height: 50px;"></div>
            <h1 style="color: #0b3c5d; font-size: 38px; font-weight: 700; margin: 0; padding: 0; line-height: 1;">SymptoCare</h1>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("<h1 style='color: #0b3c5d; font-size: 38px; font-weight: 700; margin-top: -20px;'>SymptoCare</h1>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Navigation Bar
# ---------------------------------------------------------
selected_tab = st.radio(
    label="Navigation",
    options=["Home", "Check Symptoms", "Health Insights", "About"],
    horizontal=True,
    label_visibility="collapsed"
)

# =========================================================
# TAB 1: HOME
# =========================================================
if selected_tab == "Home":
    st.markdown("<h4 style='color: #0066cc; font-weight: 600; letter-spacing: 1px;'>AI HEALTH SYSTEM CHECKER</h4>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: #0b3c5d; font-size: 44px; font-weight: 700; margin-top: -10px;'>Your Health, <span style='color: #00a8e8;'>Our Priority</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; color: #5a6e7f; max-width: 600px;'>SymptoCare uses AI technology to help you understand your symptoms and get smart health insights.</p>", unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🔍</div>
                <div class="feature-title">Symptom Checker</div>
                <div class="feature-desc">Describe your symptoms and get AI-powered possible conditions.</div>
                <div class="feature-link">Check Now →</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">📈</div>
                <div class="feature-title">Health Insights</div>
                <div class="feature-desc">View personalized health insights and recommendations for a better you.</div>
                <div class="feature-link">View Insights →</div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">📋</div>
                <div class="feature-title">Health Records</div>
                <div class="feature-desc">Track your health history and monitor your progress over time.</div>
                <div class="feature-link">View Records →</div>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🛡️</div>
                <div class="feature-title">Privacy First</div>
                <div class="feature-desc">Your data is secure with us. We prioritize your privacy and confidentiality.</div>
                <div class="feature-link">Learn More →</div>
            </div>
        """, unsafe_allow_html=True)
        
    st.write("")
    st.write("")
    st.divider()
    
    st.markdown("<h3 style='text-align: center; color: #0b3c5d; font-weight: 700;'>How It Works</h3>", unsafe_allow_html=True)
    st.write("")
    
    w1, w2, w3, w4 = st.columns(4)
    with w1:
        st.markdown("""
            <div style="text-align: center;">
                <div class="step-circle" style="background-color: #0066cc; margin: 0 auto 10px auto;">1</div>
                <b style="color: #0b3c5d;">Enter Symptoms</b>
                <p style="font-size: 13px; color: #5a6e7f;">Tell us how you're feeling</p>
            </div>
        """, unsafe_allow_html=True)
    with w2:
        st.markdown("""
            <div style="text-align: center;">
                <div class="step-circle" style="background-color: #00a896; margin: 0 auto 10px auto;">2</div>
                <b style="color: #0b3c5d;">AI Analysis</b>
                <p style="font-size: 13px; color: #5a6e7f;">Our AI analyzes your symptoms</p>
            </div>
        """, unsafe_allow_html=True)
    with w3:
        st.markdown("""
            <div style="text-align: center;">
                <div class="step-circle" style="background-color: #845ec2; margin: 0 auto 10px auto;">3</div>
                <b style="color: #0b3c5d;">Get Results</b>
                <p style="font-size: 13px; color: #5a6e7f;">Receive possible conditions and suggestions</p>
            </div>
        """, unsafe_allow_html=True)
    with w4:
        st.markdown("""
            <div style="text-align: center;">
                <div class="step-circle" style="background-color: #ff9642; margin: 0 auto 10px auto;">4</div>
                <b style="color: #0b3c5d;">Take Action</b>
                <p style="font-size: 13px; color: #5a6e7f;">Follow recommendations and consult a doctor</p>
            </div>
        """, unsafe_allow_html=True)


# =========================================================
# TAB 2: CHECK SYMPTOMS (Demographics Sidebar + ML Analysis)
# =========================================================
elif selected_tab == "Check Symptoms":
    with st.sidebar:
        st.header("👤 Patient Demographics")
        st.caption("Provide context for a more tailored assessment.")
        
        age = st.number_input("Age", min_value=1, max_value=120, value=25)
        sex = st.selectbox("Biological Sex", ["Female", "Male", "Other"])
        duration = st.selectbox("Symptom Duration", ["Less than 3 days", "3 to 7 days", "More than 1 week"])
        
        st.info("💡 **Note:** Demographics help contextualize risk factors for clinical evaluation.")
    
    st.caption("Select your symptoms below to generate a preliminary clinical assessment.")
    
    @st.cache_resource
    def load_artifacts():
        model_path = os.path.join('models', 'symptom_checker_model.pkl')
        symptom_path = os.path.join('models', 'symptom_list.pkl')
        
        if not os.path.exists(model_path):
            model_path = os.path.join('..', 'models', 'symptom_checker_model.pkl')
            symptom_path = os.path.join('..', 'models', 'symptom_list.pkl')
            
        model = joblib.load(model_path)
        symptom_list = joblib.load(symptom_path)
        return model, symptom_list

    try:
        model, symptom_list = load_artifacts()
        
        selected_symptoms = st.multiselect(
            "Select your symptoms:",
            options=symptom_list,
            placeholder="Choose options"
        )
        
        # Add spacing to ensure dropdown opens downwards smoothly
        st.write("")
        st.write("")
        
        if st.button("Analyze Symptoms", type="primary"):
            if not selected_symptoms:
                st.warning("Please select at least one symptom before analyzing.")
            else:
                # 1. Build binary feature vector matching model's expected input feature order
                input_vector = [1 if symptom in selected_symptoms else 0 for symptom in symptom_list]
                input_df = pd.DataFrame([input_vector], columns=symptom_list)
                
                # 2. Perform Machine Learning Prediction
                prediction = model.predict(input_df)[0]
                
                # 3. Obtain probability breakdown if supported by model
                if hasattr(model, "predict_proba"):
                    probabilities = model.predict_proba(input_df)[0]
                    classes = model.classes_
                    
                    # Sort top predictions by likelihood
                    top_indices = np.argsort(probabilities)[::-1][:3]
                    top_predictions = [(classes[i], probabilities[i]) for i in top_indices if probabilities[i] > 0]
                else:
                    top_predictions = [(prediction, 1.0)]

                st.divider()
                st.markdown("<h3 style='color: #0b3c5d; font-weight: 700;'>📋 Assessment Results</h3>", unsafe_allow_html=True)
                
                # Primary Assessment Display
                st.success(f"**Primary Assessment:** {prediction}")
                
                st.write("")
                st.markdown("<h3 style='color: #0b3c5d; font-weight: 700;'>Differential Diagnosis (Possibilities Breakdown)</h3>", unsafe_allow_html=True)
                st.caption("Relative likelihood based on model confidence:")
                st.write("")
                
                # Render progress bars for top conditions (e.g. 33%, 33%, 33%)
                for condition, prob in top_predictions:
                    prob_percentage = int(round(prob * 100))
                    col_cond, col_pct = st.columns([4, 1])
                    with col_cond:
                        st.markdown(f"**{condition}**")
                    with col_pct:
                        st.markdown(f"**{prob_percentage}%**")
                    st.progress(prob)
                    st.write("")
                    
    except Exception as e:
        st.error(f"Error executing analysis model: {e}")


# =========================================================
# TAB 3: HEALTH INSIGHTS
# =========================================================
elif selected_tab == "Health Insights":
    st.title("Health Insights")
    st.info("Personalized analytics and historical symptom tracking will appear here.")


# =========================================================
# TAB 4: ABOUT
# =========================================================
elif selected_tab == "About":
    st.title("About SymptoCare")
    st.markdown("""
        **SymptoCare** is an AI-driven clinical insight tool designed to provide preliminary condition assessments based on user-reported symptoms.
        
        ---
        
        ⚠️ **Disclaimer:** SymptoCare is for informational purposes only and does not replace professional medical diagnosis or clinical evaluation.
    """)