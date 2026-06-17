import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.parser import extract_text
from src.embedding import generate_embedding
from src.ranking import calculate_score
from src.ats import calculate_ats_score
from src.quality import resume_quality
from src.recommendations import suggestions
from src.career_paths import recommend_roles

st.set_page_config(
    page_title="AIResume Analyzer",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AIResume Analyzer")

st.markdown("""
Analyze your resume against a job description and receive:

✅ ATS Score

✅ Skill Match Analysis

✅ Missing Skills Detection

✅ Resume Quality Assessment

✅ Career Recommendations

✅ Learning Roadmap
""")
