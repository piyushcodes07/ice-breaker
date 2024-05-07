import os
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from linkedIn.linkedIn import scrape_linkedIn

if __name__ == "__main__":
    load_dotenv()
    print(os.environ['OPENAI_API_KEY'])

    summary_template = """
    given the LinkedIn information {information} about a person i want you to create 
    1. a short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],template=summary_template
    )

    linkedIn_data= scrape_linkedIn(mock=True)

    llm = ChatOpenAI(temperature=0,model_name="gpt-3.5-turbo")
    chain=LLMChain(llm=llm,prompt=summary_prompt_template)
    res=chain.invoke(input={"information":linkedIn_data})
    print(res)
