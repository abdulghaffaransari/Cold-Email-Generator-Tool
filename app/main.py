import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
import PyPDF2

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    # Set custom page configuration
    st.set_page_config(
        layout="centered",
        page_title="📧 Hiring Assistant Llama",
        page_icon="💼",
    )

    # Sidebar instructions
    st.sidebar.title("🛠️ Options")
    st.sidebar.markdown("""
        Use this tool to generate personalized cold emails based on a job posting and your CV profile.
        Customize your workflow:
        - **Step 1**: Enter the job posting URL or upload your resume (PDF).
        - **Step 2**: Submit to generate your email.
    """)

    # Header design
    st.markdown(
        """
        <div style="background-color: #0D6EFD; padding: 15px; border-radius: 8px; text-align: center;">
            <h1 style="color: white;">📧 Hiring Assistant Llama</h1>
            <p style="color: #e3f2fd;">Simplify your outreach process with professionally crafted emails.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Input for Job Posting URL
    st.write("### 📝 Enter the Job Posting URL")
    url_input = st.text_input(
        "Job URL:", value="https://jobs.nike.com/job/R-33460", help="Paste the URL of the job posting."
    )

    # PDF Upload Section
    st.write("### 📄 Upload Your Resume (PDF)")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    profile_text = ""
    if uploaded_file is not None:
        try:
            # Extract text from the uploaded PDF
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            profile_text = "".join(page.extract_text() for page in pdf_reader.pages)
            profile_text = clean_text(profile_text)
            st.success("📄 Resume uploaded and processed successfully!")
        except Exception as e:
            st.error(f"🚨 An error occurred while processing the PDF: {e}")

    # Submit button
    submit_button = st.button("✨ Generate Email", type="primary")

    # Process the inputs
    if submit_button:
        try:
            if not profile_text:
                st.warning("⚠️ Please upload a resume or paste your profile to generate an email.")
                return

            # Display loading information
            st.info("Processing your inputs... Please wait.")

            # Load and clean job posting data
            loader = WebBaseLoader([url_input])
            job_data = clean_text(loader.load().pop().page_content)

            # Load portfolio and extract jobs
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(job_data)

            if not jobs:
                st.warning("⚠️ No job details found in the provided URL. Please check the link and try again.")
                return

            # Use the first job as the most relevant
            job = jobs[0]
            skills = job.get("skills", [])
            links = portfolio.query_links(skills)

            # Dynamically generate email using both the job and profile inputs
            email = llm.write_mail(job, links, profile_text)

            # Display the generated email
            st.markdown("### 📧 Your Generated Email")
            st.code(email, language="markdown")

        except Exception as e:
            st.error(f"🚨 An error occurred: {e}")

    # Footer Section
    st.markdown(
        """
        <div style="text-align: center; margin-top: 30px; padding: 10px;">
            <p>💼 Built by Abdul Ghaffar Ansari | AI & MLOps Enthusiast</p>
            <p>🌐 <a href="https://www.linkedin.com/in/abdulghaffaransari/" target="_blank">LinkedIn</a> | 
            <a href="https://github.com/abdulghaffaransari/" target="_blank">GitHub</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )




if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)
