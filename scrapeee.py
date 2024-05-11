import os
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from linkedIn.linkedIn import scrape_linkedIn
from agents.linkedIn_lookup_agent import lookup as linkedIn_lookup_aganet
from output_parsers import summary_parser
def ice_break_with(name:str)->str:

    linkedIn_scraped_url_OpenAI = linkedIn_lookup_aganet(name=name)

    summary_template = """
        given the LinkedIn information {information} about a person i want you to create 
        1. a short summary
        2. two interesting facts about them
        \n{format_instructions}
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template,partial_variables={"format_instructions":summary_parser.get_format_instructions()}
    )

    linkedIn_data = scrape_linkedIn(linkedIn_scraped_url_OpenAI,mock=True)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    #chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    chain = summary_prompt_template | llm | summary_parser
    res = chain.invoke(input={"information": linkedIn_data})

    print(res)


if __name__ == "__main__":
    load_dotenv()
    # print(os.environ['OPENAI_API_KEY'])
    ice_break_with(name="car rental bussiness")


