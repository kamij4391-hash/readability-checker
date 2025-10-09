import streamlit as st
from textstat import textstat

# Streamlit App Title
st.title(" English Passage Readability Checker")

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

        # Display results
        st.markdown(f"### Flesch Reading Ease Score: **{flesch_score:.2f}**")
        st.markdown(f"<h4 style='color:{color};'>Difficulty Level: {level}</h4>", unsafe_allow_html=True)

        # Analyze components
        num_sentences = textstat.sentence_count(text)
        num_words = textstat.lexicon_count(text, removepunct=True)
        num_syllables = textstat.syllable_count(text)

        avg_sentence_length = num_words / num_sentences if num_sentences > 0 else 0
        avg_syllables_per_word = num_syllables / num_words if num_words > 0 else 0

        st.markdown("###  Why this score?")
        st.write(f"- **Average Sentence Length:** {avg_sentence_length:.2f} words per sentence")
        st.write(f"- **Average Syllables per Word:** {avg_syllables_per_word:.2f} syllables per word")

        # Explanation based on complexity
        if flesch_score >= 80:
            st.info(" Your passage uses **short sentences** and **simple words**, making it very easy to understand.")
        elif flesch_score >= 60:
            st.warning(" Your passage has **moderately long sentences** or **some complex words**, making it standard to read.")
        else:
            st.error(" Your passage contains **long sentences** and **many multi-syllable words**, making it difficult to read.")

        # Interpretation scale
        st.markdown("###  Interpretation Scale (Flesch Reading Ease)")
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
