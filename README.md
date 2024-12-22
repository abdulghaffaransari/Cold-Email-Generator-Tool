# Hiring Assistant Llama

![Result 1](https://github.com/abdulghaffaransari/Hiring-Assistant-Llama/blob/main/Results/Result1.png)

![Result 3](https://github.com/abdulghaffaransari/Hiring-Assistant-Llama/blob/main/Results/Result3.png)

---

## Problem Statement

Job hunting can be an overwhelming and time-consuming process, especially when crafting personalized emails for each job application. Candidates often face challenges such as:

- Identifying key requirements from lengthy job descriptions.
- Aligning their profiles with the job requirements in a concise manner.
- Writing professional and tailored cold emails for job applications.

On the other hand, hiring managers are inundated with generic applications that fail to stand out, resulting in lost opportunities for both parties.

### The Challenge
To simplify this process, there is a need for an intelligent tool that can:

1. Extract and analyze job requirements from job postings.
2. Integrate a candidate's resume seamlessly into the application process.
3. Automatically generate highly professional and tailored emails for job applications.

---

## Project Description

**Hiring Assistant Llama** is an advanced AI-powered tool designed to simplify and enhance the job application process. By leveraging cutting-edge LLM technology (Llama 3.1) and dynamic web scraping, this tool empowers candidates to create personalized, professional, and impactful cold emails tailored to job descriptions. The tool dynamically incorporates the candidate’s resume, projects, and certifications to showcase their relevance and potential contributions.

### Features

- **Job Description Parsing**: Automatically extracts key information such as role, skills, experience level, and responsibilities from job postings.
- **Resume Integration**: Upload your resume in PDF format to dynamically align your profile with the job requirements.
- **Email Generation**: Creates highly professional and tailored cold emails based on the extracted job description and resume.
- **Portfolio Matching**: Leverages a database of candidate projects and certifications to highlight the most relevant achievements in the email.
- **Streamlined Workflow**: Intuitive and user-friendly interface built with Streamlit.

---

## How It Works

### Workflow

1. **Enter Job Posting URL**: Paste the URL of the job posting you want to apply for.
2. **Upload Your Resume**: Upload your resume in PDF format.
3. **Generate Email**: With a single click, generate a personalized email aligned with the job posting and your profile.
4. **Copy & Send**: Copy the generated email and use it to apply for the job.

---

## Project Architecture

### Components

1. **Job Scraping & Parsing**
   - Utilizes `WebBaseLoader` to scrape job descriptions from URLs.
   - Extracts relevant job details such as role, responsibilities, required skills, and experience.

2. **Resume Parsing**
   - Processes uploaded PDF resumes using `PyPDF2`.
   - Cleans and extracts text using custom `clean_text` utility.

3. **Cold Email Generation**
   - Employs Llama 3.1 (via LangChain’s ChatGroq) to dynamically craft tailored emails.
   - Combines parsed job data, resume content, and portfolio links for a comprehensive and professional output.

4. **Portfolio Matching**
   - Powered by ChromaDB to query and retrieve the most relevant projects and certifications from the portfolio database.

5. **User Interface**
   - Built with Streamlit to provide a sleek and interactive user experience.
   - Features intuitive input fields for job URLs and resume uploads.

---

## Setup Instructions

### Prerequisites

- Python 3.9+
- Dependencies listed in `requirements.txt`
- API key for Llama 3.1 (via Groq)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abdulghaffaransari/Hiring-Assistant-Llama.git
   cd Hiring-Assistant-Llama
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

4. Run the application:
   ```bash
   streamlit run app/main.py
   ```

---

## File Structure

```plaintext
Hiring-Assistant-Llama/
├── app/
│   ├── chains.py              # Handles job parsing and email generation.
│   ├── main.py                # Main Streamlit app interface.
│   ├── portfolio.py           # Portfolio matching with ChromaDB.
│   ├── utils.py               # Utility functions for cleaning text.
│   └── recource/
│       └── my_portfolio.csv   # Portfolio data file.
├── Experiments/               # Jupyter notebooks for testing.
├── Results/                   # Screenshots and results.
├── vectorstore/               # ChromaDB persistent storage.
├── requirements.txt           # Python dependencies.
└── README.md                  # Project documentation.
```

---

## Technologies Used

- **LangChain**: For job parsing and LLM orchestration.
- **Streamlit**: Interactive web application.
- **ChromaDB**: Portfolio matching engine.
- **Llama 3.1**: Advanced language model for crafting emails.
- **PyPDF2**: Resume parsing.
- **Pandas**: Data manipulation.

---

## Future Enhancements

1. **Multi-Language Support**: Extend email generation to support multiple languages.
2. **Job Matching**: Integrate job matching capabilities based on candidate profiles.
3. **Email Templates**: Provide customizable email templates.
4. **Advanced Analytics**: Include metrics to track email performance.

---

## Author

**Abdul Ghaffar Ansari**

- **LinkedIn**: [linkedin.com/in/abdulghaffaransari](https://www.linkedin.com/in/abdulghaffaransari/)
- **GitHub**: [github.com/abdulghaffaransari](https://github.com/abdulghaffaransari/)

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

