# SYMPTOCARE 

An AI-powered web application built with Streamlit and Scikit-Learn that predicts potential medical conditions based on user-selected symptoms. 

**Live Application:** [Access SymptoCare on Streamlit Cloud](https://ai-symptom-checker-bczndgm5kfvjk7eflln3pm.streamlit.app/)

---

## Academic Project Metadata 
* **Course Code & Name:** BIT4543 ARTIFICIAL INTELLIGENCE 
* **Group Name:** Group 7
* **Project Title:** SymptoCare: AI Health Symptom Checker 

### Group Members
1. Nur Aliya Adriana Binti Haizat (2410-2200)
2. Haya Tasnim Binti Rafidi (2507-1592)
3. Davinya A/P Kumar (2507-1785) 
4. Hareesha Bharathy Pillai A/P Puspanathan (2410-2331)
5. Ho Jia Xin (2507-1590)
6. Nityashry A/P Thangaraju (2503-0761)

---

## Model Architecture & Technical Specs 

* **Algorithm:** Random Forest Classifier (`RandomForestClassifier`, `n_estimators=100`, Gini Impurity)
* **Dataset Size:** Kaggle Clinical Symptom Dataset (246,945 records; 80% train / 20% test split)
* **Input Features:** 377 binary symptom columns
* **Target Classes:** 41 medical condition categories 
* **Model Accuracy:** 81.44% on test evaluation dataset

---

## Repository Structure 
```text
ai-symptom-checker/
├── .streamlit/        # Streamlit theme & UI configuration
├── app/               # Main Streamlit web application interface
├── data/              # Processed dataset & feature mapping files
├── docs/              # Final report, slides, poster & architecture diagrams
├── models/            # Serialized model artifacts (.pkl files)
├── notebooks/         # Model training & EDA Jupyter Notebooks
├── tests/             # Unit & integration test scripts
├── .gitattributes     # Git LFS configuration for large model and dataset files
├── .gitignore         # Untracked files configuration
├── README.md          # Project documentation
└── requirements.txt   # Python dependency list
```

---

## How to Run the Application

### 1. Clone the Repository

```bash
git clone https://github.com/hayatasnim/ai-symptom-checker.git
cd ai-symptom-checker
```
### 2. Install Dependencies 
```bash
pip install -r requirements.txt
```
### 3. Launch the App
```bash
streamlit run app/app.py
```
