import streamlit as st
import joblib

# Load vectorizer and models
@st.cache_resource
def load_models():
    vectorizer = joblib.load("vectorizer_A.pkl")  # TF-IDF vectorizer
    model_a = joblib.load("Model_A.pkl")        # Balanced-trained model
    model_b = joblib.load("ModelB2.pkl")        # Imbalanced-trained model
    return vectorizer, model_a, model_b

vectorizer, model_a, model_b = load_models()

# App Title
st.title("Automated Review Rating System")
st.write("Enter a customer review to see predictions from both models.")

# User input
user_review = st.text_area("Enter review text here:")

if st.button("Predict Ratings"):
    if user_review.strip():
        # Transform review using vectorizer
        user_review_transformed = vectorizer.transform([user_review])

        # Predict using both models
        pred_a = model_a.predict(user_review_transformed)[0]
        pred_b = model_b.predict(user_review_transformed)[0]

        # Show results
        st.subheader("Predictions")
        st.write(f"Model_A (Balanced-trained Logistic Regression): {pred_a}")
        st.write(f"Model_B (Imbalanced-trained SVM): {pred_b}")
    else:
        st.warning("Please enter a review before predicting.")

st.markdown("---")
st.caption("Built with Streamlit | Compare predictions from two trained models")
