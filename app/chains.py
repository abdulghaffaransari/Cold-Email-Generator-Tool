import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}
            
            ### INSTRUCTION:
            You are Abdul Ghaffar Ansari, a Master's student in Artificial Intelligence at Brandenburgische Technische Universität, Cottbus, Germany, 
            with a strong background in AI, MLOps, and data analytics. You are currently seeking a working student position to leverage your 
            technical expertise and hands-on experience in cloud infrastructure, machine learning, and scalable applications. 
            Your Contact Information: LinkedIn: https://www.linkedin.com/in/abdul-ghaffar-ansari-ai/ , and your GitHub: https://www.github.com/abdulghaffaransari.
            
            
            Use the information provided in your profile to write a professional email expressing your interest in the position mentioned above. 
            Mention relevant skills and experiences that align with the role and describe how you can contribute to the organization.
            Also, highlight your certifications and projects,that are highly relevant to job posting.
            Ensure the email is concise, professional, and tailored to the job description. Include the most relevant links from the portfolio: {link_list}.
            Do not provide a preamble.
            
            ### EMAIL (NO PREAMBLE):
            
            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))