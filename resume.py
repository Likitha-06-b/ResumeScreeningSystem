from fpdf import FPDF
import random
import os

# Create a folder for resumes
folder = "resumes"
os.makedirs(folder, exist_ok=True)

# Sample data
names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ivan", "Julia"]
roles = ["Machine Learning", "Web Development", "Machine Learning", "Data Science", "Machine Learning",
         "Web Development", "Machine Learning", "Machine Learning", "Web Development", "Machine Learning"]
skills_ml = ["Python, ML, NLP", "Python, Deep Learning, TensorFlow", "Python, ML, Data Analysis",
             "Python, ML, PyTorch", "Python, ML, AI Projects"]
skills_web = ["HTML, CSS, JavaScript, React", "JavaScript, Node.js, Express", "HTML, CSS, Django", "React, Angular"]
skills_ds = ["Python, SQL, Data Analysis", "Python, Pandas, Visualization"]

# Generate 10 PDF resumes
for i in range(10):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    
    # Basic info
    pdf.cell(0, 10, f"Name: {names[i]}", ln=True)
    pdf.cell(0, 10, f"Role: {roles[i]}", ln=True)
    experience = random.randint(2, 8)
    pdf.cell(0, 10, f"Experience: {experience} years", ln=True)
    
    # Skills based on role
    if roles[i] == "Machine Learning":
        skills = random.choice(skills_ml)
    elif roles[i] == "Web Development":
        skills = random.choice(skills_web)
    else:
        skills = random.choice(skills_ds)
    
    pdf.cell(0, 10, f"Skills: {skills}", ln=True)
    
    # Save PDF
    pdf_file = os.path.join(folder, f"{names[i]}_Resume.pdf")
    pdf.output(pdf_file)

print("10 PDF resumes generated in the 'resumes' folder!")

