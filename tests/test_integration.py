import joblib 
import pandas as pd 

def test_model_loading_and_prediction():
    # 1. Load model assets 
    model = joblib.load("models/symptom_checker_model.pkl")
    symptoms = joblib.load("models/symptom_list.pkl")

    # 2. Build feature vector matching model inputs
    feature_cols = list(symptoms)
    dummy_vector = [0] * len(feature_cols)
    dummy_vector[0] = 1 # Activate first symptom 

    df = pd.DataFrame([dummy_vector], columns=feature_cols)

    # 3. Test prediction execution 
    prediction = model.predict(df)
    assert prediction is not None, "Model prediction failed!"
    print("Integration Test Passed: Model and feature vector match perfectly!")

if__name__ == "__main__":
    test_model_loading_and_prediction()