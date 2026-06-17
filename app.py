import streamlit as st
import pandas as pd

from src.parser import extract_text
from src.embedding import generate_embedding
from src.ranking import calculate_score
from src.ats import (
    calculate_ats_score,
    extract_experience,
    extract_education
)

st.set_page_config(
    page_title="ATS Resume Screening System",
    layout="wide"
)

st.title("🤖 ATS Resume Screening System")

jd = st.text_area(
    "Paste Job Description"
)

uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Analyze Resumes"):

    if jd and uploaded_files:

        results = []

        jd_embedding = generate_embedding(jd)

        for file in uploaded_files:

            with open(file.name, "wb") as f:
                f.write(file.getbuffer())

            resume_text = extract_text(
                file.name
            )

            resume_embedding = (
                generate_embedding(
                    resume_text
                )
            )

            semantic_score = (
                calculate_score(
                    resume_embedding,
                    jd_embedding
                )
            )

            ats_score, matched, missing = (
                calculate_ats_score(
                    resume_text,
                    jd
                )
            )

            experience = (
                extract_experience(
                    resume_text
                )
            )

            education = (
                extract_education(
                    resume_text
                )
            )

            results.append(
                {
                    "Resume": file.name,
                    "Semantic Score":
                        round(
                            semantic_score,
                            2
                        ),
                    "ATS Score":
                        ats_score,
                    "Experience":
                        experience,
                    "Education":
                        ", ".join(
                            education
                        ),
                    "Matched Skills":
                        ", ".join(
                            matched
                        ),
                    "Missing Skills":
                        ", ".join(
                            missing
                        )
                }
            )

        df = pd.DataFrame(
            results
        )

        df = df.sort_values(
            by=[
                "ATS Score",
                "Semantic Score"
            ],
            ascending=False
        )

        st.dataframe(df)

        csv = df.to_csv(
            index=False
        )

        st.download_button(
            "Download Results",
            csv,
            "candidate_ranking.csv",
            "text/csv"
        )
