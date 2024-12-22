import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text

# Create a function for a better layout and enhanced look
def create_streamlit_app(llm, portfolio, clean_text):
    # Set custom page configuration
    st.set_page_config(
        layout="centered",
        page_title="📧 Hiring Assistant Llama",
        page_icon="💼",

    )

    # Add a custom sidebar
    st.sidebar.title("🛠️ Options")
    st.sidebar.markdown(
        """
        Use this tool to generate personalized cold emails for working student positions.
        Customize your workflow:
        - **Step 1**: Enter the job posting URL.
        - **Step 2**: Submit to generate your email.
        """
    )

    # Header with a sleek design
    st.markdown(
        """
        <div style="background: linear-gradient(to right, #4a90e2, #50c878); padding: 15px; border-radius: 10px; text-align: center;">
            <h1 style="color: white;">📧 Hiring Assistant Llama</h1>
            <p style="color: #f0fdf4;">Simplify your outreach process with professionally crafted emails.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Input Section
    st.write("### 📝 Enter the Job Posting URL")
    url_input = st.text_input(
        "Enter a URL:", value="https://jobs.nike.com/job/R-33460", help="Paste the job URL to generate an email."
    )

    submit_button = st.button("✨ Generate Email", type="primary")

    # Generate Email Section
    if submit_button:
        try:
            # Load and process data
            st.info("Fetching and processing the job posting... Please wait.")
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)

            # Load portfolio and extract jobs
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)

            if not jobs:
                st.warning("⚠️ No jobs found in the provided URL. Please check and try again.")
                return

            # Process the first job
            job = jobs[0]  # Use the first job as the most relevant
            skills = job.get("skills", [])
            links = portfolio.query_links(skills)
            email = llm.write_mail(job, links)

            # Display results
            st.markdown("### 📧 Your Generated Email")
            st.code(email, language="markdown")

        except Exception as e:
            st.error(f"🚨 An error occurred: {e}")

    # Footer Section
    st.markdown(
        """
        <div style="text-align: center; margin-top: 30px; padding: 10px;">
            <p>💼 Built by <strong>Abdul Ghaffar Ansari</strong> | AI & MLOps Enthusiast</p>
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
