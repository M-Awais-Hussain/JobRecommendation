# CV Matcher - Job Recommendation System

A web-based application that analyzes your uploaded CV and recommends matching job listings based on your skills. Built with Flask and Bootstrap.

## 🚀 Features

- Upload your CV
- Automatic extraction of key skills
- Recommends jobs from a dataset of internship/job listings
- Beautiful, responsive UI using Bootstrap
- Supports uploading new CVs anytime

## 📂 Project Structure
├── app.py
├── templates/
│ ├── index.html
│ ├── result.html
│ └── recommendation.html
├── static/
│ └── (optional: CSS/JS files)
├── data/
│ └── Internship_job_listings_with_skills.csv
├── requirements.txt
└── README.md


## ⚙️ Installation

1. **Clone the repository:**
   Create virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

2. **Install dependencies:**
   pip install -r requirements.txt

3. **Run the application:**
    python app.py
Then open http://127.0.0.1:5000 in your browser.

## 📄 Dataset
Place your Internship_job_listings_with_skills.csv inside the data/ folder. The CSV must include columns like:

- title

- address

- level

- link

- required_skills

## 💻 Tech Stack
Python + Flask

Bootstrap 5

Pandas

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss improvements.

## 📄 License
MIT License
