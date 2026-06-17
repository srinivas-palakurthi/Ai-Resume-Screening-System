SKILLS = [

    "python",
    "sql",
    "power bi",
    "tableau",
    "excel",

    "machine learning",
    "deep learning",
    "nlp",

    "tensorflow",
    "pytorch",

    "pandas",
    "numpy",
    "scikit-learn",

    "java",
    "aws",
    "azure",
    "git",
    "docker"
]

def extract_skills(text):

    text = text.lower()

    found = []

    for skill in SKILLS:

        if skill in text:
            found.append(skill)

    return found
