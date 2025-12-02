import streamlit as st
from textstat import textstat

# Streamlit App Title
st.title("English Passage Readability Checker")

# Input area
st.subheader("Enter Your English Passage Below:")
text = st.text_area("Paste your passage here:", height=250)

if st.button("Check Readability"):
    if not text.strip():
        st.warning("Please enter a passage to analyze.")
    else:
        # Calculate Flesch Reading Ease Score
        flesch_score = textstat.flesch_reading_ease(text)

        # Determine difficulty level
        if flesch_score >= 90:
            level = "Very Easy (5th grade)"
            color = "green"
        elif flesch_score >= 80:
            level = "Easy (6th grade)"
            color = "lightgreen"
        elif flesch_score >= 70:
            level = "Fairly Easy (7th grade)"
            color = "yellowgreen"
        elif flesch_score >= 60:
            level = "Standard (8th–9th grade)"
            color = "gold"
        elif flesch_score >= 50:
            level = "Fairly Difficult (10th–12th grade)"
            color = "orange"
        elif flesch_score >= 30:
            level = "Difficult (College level)"
            color = "tomato"
        else:
            level = "Very Difficult (College graduate)"
            color = "red"

        # --- CEFR Level Estimation Based on Flesch Score ---
        if flesch_score >= 90:
            cefr = "A1 (Beginner)"
        elif flesch_score >= 80:
            cefr = "A2 (Elementary)"
        elif flesch_score >= 65:
            cefr = "B1 (Intermediate)"
        elif flesch_score >= 50:
            cefr = "B2 (Upper-Intermediate)"
        elif flesch_score >= 30:
            cefr = "C1 (Advanced)"
        else:
            cefr = "C2 (Proficient)"

        # Display results
        st.markdown(f"### Flesch Reading Ease Score: **{flesch_score:.2f}**")
        st.markdown(f"<h4 style='color:{color};'>Difficulty Level: {level}</h4>", unsafe_allow_html=True)
        st.markdown(f"### CEFR Level: **{cefr}**")

        # Add interpretation scale
        st.markdown("### Interpretation Scale (Flesch Reading Ease)")
        st.write("""
| Score Range | Interpretation | Approx. Education Level |
|--------------|----------------|--------------------------|
| 90–100 | Very Easy | 5th grade |
| 80–89 | Easy | 6th grade |
| 70–79 | Fairly Easy | 7th grade |
| 60–69 | Standard | 8th–9th grade |
| 50–59 | Fairly Difficult | 10th–12th grade |
| 30–49 | Difficult | College |
| 0–29 | Very Difficult | College graduate |
        """)

        # CEFR Table
        st.markdown("### CEFR Readability Scale")
        st.write("""
| CEFR Level | Description | Typical Reader |
|------------|-------------|----------------|
| A1 | Beginner | Basic English user |
| A2 | Elementary | Simple communication |
| B1 | Intermediate | Everyday language |
| B2 | Upper-Intermediate | Professional/academic |
| C1 | Advanced | Complex texts |
| C2 | Proficient | Expert-level comprehension |
        """)
