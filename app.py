from flask import Flask, request, render_template
import pandas as pd
import re

app = Flask(__name__)

# Load job listings from CSV file
job_listings = pd.read_csv('data/Internship_job_listings_with_skills.csv')

# Function to extract skills from a CV (basic implementation)
def extract_skills(cv_text):
    # Example skills to look for; update as necessary
    skills = ['Python', 'Machine Learning', 'Data Analysis', 'SQL', 'Web Development', 'Deep Learning']
    extracted_skills = []

    for skill in skills:
        if re.search(r'\b' + re.escape(skill) + r'\b', cv_text, re.IGNORECASE):
            extracted_skills.append(skill)
    
    return extracted_skills

# Function to find matching jobs based on extracted skills
def find_matching_jobs(skills):
    matched_jobs = []
    normalized_skills = [skill.lower().strip() for skill in skills]

    for index, row in job_listings.iterrows():
        job_skills = row['required_skills'].lower().split(',')
        job_skills = [skill.strip() for skill in job_skills]

        # Debug: Print the skills being compared
        print(f"Comparing extracted skills: {normalized_skills} with job skills: {job_skills}")

        # Check if any extracted skill is in the job skills
        if any(skill in job_skills for skill in normalized_skills):
            matched_jobs.append({
                'title': row['title'],
                'address': row['address'],
                'level': row['level'],
                'link': row['link'],
                'required_skills': row['required_skills']
            })

    return matched_jobs

@app.route('/', methods=['GET', 'POST'])
def upload_cv():
    if request.method == 'POST':
        uploaded_file = request.files['cv']
        if uploaded_file.filename != '':
            try:
                # Try reading the file with UTF-8 encoding first
                cv_text = uploaded_file.read().decode('utf-8')
            except UnicodeDecodeError:
                # If UTF-8 fails, try ISO-8859-1
                try:
                    cv_text = uploaded_file.read().decode('ISO-8859-1')
                except UnicodeDecodeError:
                    return render_template('upload.html', error="File could not be decoded. Please upload a valid CV.")
                
            print("CV Text:", cv_text)  # Debug info
            extracted_skills = extract_skills(cv_text)  # Extract skills from the CV
            recommended_jobs = find_matching_jobs(extracted_skills)  # Find matching jobs

            print(f"Extracted skills: {extracted_skills}")  # Debug info
            print(f"Recommended jobs: {recommended_jobs}")  # Debug info

            return render_template('result.html', skills=extracted_skills, jobs=recommended_jobs)

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)