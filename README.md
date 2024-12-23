# Hiring Assistant Llama

![Result 1](https://github.com/abdulghaffaransari/Hiring-Assistant-Llama/blob/main/Results/Result1.png)

---

## Problem Statement
In today’s competitive job market, applicants face significant challenges in crafting tailored and impactful emails for job applications. This process is often tedious, requiring alignment between job descriptions and resumes. The lack of automation in this process can lead to inefficient and generic outreach, reducing an applicant's chances of standing out to potential employers.

---

## Project Description
**Hiring Assistant Llama** is an AI-powered platform that streamlines the process of crafting professional and personalized cold emails for job applications. Using state-of-the-art technologies, such as **Llama 3.1**, **Streamlit**, and **ChromaDB**, the application extracts key details from job postings, processes user resumes, and generates custom-tailored emails. This ensures high-quality and relevant communication, enhancing the chances of securing interviews.

### Key Benefits:
- Saves time by automating email generation.
- Personalizes outreach by aligning resumes with job descriptions.
- Highlights user skills and portfolios effectively, boosting chances of interview calls.
- Implements a robust **CI/CD pipeline** for seamless deployment and updates to AWS infrastructure.

---

## Features

### 1. Job Posting Analysis
- Automatically extracts and analyzes job requirements, skills, and responsibilities from URLs.
- Uses AI to identify key details from job descriptions.

### 2. Resume Integration
- Allows users to upload their resumes in PDF format.
- Extracts and cleans data from resumes to ensure proper alignment with job postings.

### 3. Tailored Email Generation
- Crafts professional and personalized emails highlighting relevant skills and experiences.
- Integrates portfolio projects dynamically into the generated email.

### 4. Portfolio Matching
- Leverages **ChromaDB** to match relevant projects from the user’s portfolio.
- Dynamically selects portfolio links based on job posting requirements.

### 5. Continuous Integration & Continuous Delivery (CI/CD) Pipeline
- Automates code integration, testing, and deployment using **GitHub Actions**.
- Deploys containerized applications seamlessly on **AWS** with Docker and EC2.

---

## Workflow

1. **Input Job Posting**: Enter the URL of the job posting.
2. **Upload Resume**: Upload your resume in PDF format.
3. **Generate Email**: Click the button to receive a personalized email tailored to the job description and your profile.
4. **Deploy and Access**: Use the integrated CI/CD pipeline to deploy the application seamlessly to AWS.

---

## CICD Pipeline and Deployment

### Overview:
The CI/CD pipeline automates the integration, testing, and deployment of the application using **GitHub Actions** and **AWS**. Dockerized deployments ensure scalability and reliability.

### Important Steps for Deployment:

#### 1. Key Files in the Pipeline:
- `.github/workflows/aws.yaml`: Defines CI/CD steps, including testing, building, and deploying to AWS.
- `Dockerfile`: Defines the containerization process for deploying the Streamlit app.
- `requirements.txt`: Lists all dependencies for the project.

#### 2. CI/CD Workflow:
1. **Continuous Integration**:
   - Linting the codebase.
   - Running unit tests to validate functionality.
2. **Build and Push Docker Image**:
   - Build the Docker image.
   - Push the image to Amazon Elastic Container Registry (ECR).
3. **Continuous Deployment**:
   - Pull the Docker image from ECR.
   - Deploy the containerized app to an AWS EC2 instance.

#### 3. Commands for Deployment via AWS EC2 Connect:
Run the following commands after connecting to your AWS EC2 instance:

1. **Update and Install Docker**:
   ```bash
   sudo apt-get update -y
   sudo apt-get install -y docker.io
   ```

2. **Login to Amazon ECR**:
   ```bash
   aws ecr get-login-password --region <AWS_REGION> | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com
   ```

3. **Pull Docker Image**:
   ```bash
   docker pull <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/<REPOSITORY_NAME>:latest
   ```

4. **Run Docker Container**:
   ```bash
   docker stop cnncls || true
   docker rm cnncls || true
   docker run -d -p 8501:8501 --name=cnncls \
       -e AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY> \
       -e AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_KEY> \
       -e AWS_REGION=<AWS_REGION> \
       -e GROQ_API_KEY=<YOUR_GROQ_API_KEY> \
       <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/<REPOSITORY_NAME>:latest
   ```

5. **Clean Docker Resources**:
   ```bash
   docker system prune -f
   ```

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
├── .github/
│   ├── workflows/aws.yaml     # CI/CD pipeline configuration
├── Experiments/
│   ├── chromadb_Experiment.ipynb   # Experimentation with ChromaDB
│   ├── email_generating.ipynb      # Email generation experiments
├── Results/
│   ├── Result1.png
│   ├── Result2.png
│   ├── Result3.png
├── vectorstore/              # Vector store for portfolio matching
├── Dockerfile                # Docker configuration
├── requirements.txt          # Dependencies for the project
└── README.md                 # Project documentation
```

---

## Installation and Usage

### Prerequisites
Ensure you have the following installed:
- Python 3.9+
- Docker
- AWS CLI

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

4. Run the Streamlit application locally:
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
- **GitHub Actions**: CI/CD pipeline automation.
- **AWS**: Cloud infrastructure for deployment.

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
- Special recognition to the creators of **LangChain**, **Llama 3.1**, and **Streamlit** for their innovative contributions to AI.

