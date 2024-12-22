# Hiring Assistant Llama

![Result 1](https://github.com/abdulghaffaransari/Hiring-Assistant-Llama/blob/main/Results/Result1.png)

## Problem Statement
In today's competitive job market, professionals often struggle to craft personalized, impactful emails tailored to job postings. This process can be time-consuming, requiring applicants to align their skills, experiences, and portfolios with job descriptions. Moreover, the lack of automation in creating customized emails limits the efficiency and effectiveness of outreach, reducing the chances of standing out to potential employers.

## Project Description
**Hiring Assistant Llama** is a cutting-edge application designed to automate the process of crafting professional, personalized cold emails for job applications. Leveraging state-of-the-art AI technologies such as Llama 3.1, the platform extracts job details from postings, processes resumes, and generates tailored emails that highlight the applicant's skills and experiences, ensuring alignment with job requirements.

This tool empowers job seekers by:
- Saving time in crafting application emails.
- Ensuring relevance by dynamically aligning resumes with job descriptions.
- Enhancing the chances of securing interviews through professional and impactful communication.

---

## Features
### 1. Job Posting Analysis
- Extracts key details from job postings using advanced AI techniques.
- Processes job descriptions to identify required skills, responsibilities, and experience levels.

### 2. Resume Integration
- Allows users to upload their resumes in PDF format.
- Extracts relevant information from resumes to align with job descriptions.

### 3. Tailored Email Generation
- Generates concise, professional, and personalized emails.
- Highlights relevant projects, certifications, and portfolio links.

### 4. Portfolio Matching
- Uses a **ChromaDB**-powered vector store to recommend relevant projects from the user’s portfolio.
- Dynamically matches projects with the skills required in the job description.

---

## Workflow
1. **Input Job Posting**: Enter the URL of the job posting.
2. **Upload Resume**: Upload your resume in PDF format.
3. **Generate Email**: Click the button to receive a personalized email tailored to the job description and your profile.

---

## Results
Here are some sample outputs from the **Hiring Assistant Llama**:

### Example 1
![Result 1](https://github.com/abdulghaffaransari/Hiring-Assistant-Llama/blob/main/Results/Result1.png)

### Example 2
![Result 3](https://github.com/abdulghaffaransari/Hiring-Assistant-Llama/blob/main/Results/Result3.png)

---

## Project Structure
```
Hiring-Assistant-Llama/
├── app/
│   ├── chains.py              # Core logic for email generation
│   ├── main.py                # Streamlit application
│   ├── portfolio.py           # Portfolio management using ChromaDB
│   ├── utils.py               # Helper functions for text cleaning
│   └── recource/my_portfolio.csv  # Portfolio data
├── Experiments/
│   ├── chromadb_Experiment.ipynb   # Experimentation with ChromaDB
│   ├── email_generating.ipynb      # Email generation experiments
├── Results/
│   ├── Result1.png
│   ├── Result2.png
│   ├── Result3.png
├── vectorstore/              # Vector store for portfolio matching
├── requirements.txt          # Dependencies for the project
└── README.md                 # Project documentation
```

---

## Installation and Usage

### Prerequisites
Ensure you have the following installed:
- Python 3.9+
- Streamlit
- Required Python libraries listed in `requirements.txt`

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/abdulghaffaransari/Hiring-Assistant-Llama.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Hiring-Assistant-Llama
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:
   ```bash
   streamlit run app/main.py
   ```

5. Open the application in your browser at `http://localhost:8501`.

---

## Technologies Used
- **Llama 3.1**: Advanced language model for text generation.
- **Streamlit**: Front-end framework for interactive applications.
- **ChromaDB**: Vector database for portfolio matching.
- **PyPDF2**: PDF processing library.
- **LangChain**: Framework for building language model-powered applications.

---

## Future Enhancements
- **Multi-language Support**: Enable email generation in multiple languages.
- **Improved Matching**: Enhance portfolio matching using advanced embeddings.
- **Analytics Dashboard**: Provide insights on email engagement metrics.

---

## Author
**Abdul Ghaffar Ansari**  
AI & MLOps Enthusiast  
[LinkedIn](https://www.linkedin.com/in/abdulghaffaransari/) | [GitHub](https://github.com/abdulghaffaransari/)

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- Thanks to the open-source community for providing excellent tools and libraries.
- Special recognition to the creators of **LangChain** and **Llama 3.1** for their innovative contributions to AI.

