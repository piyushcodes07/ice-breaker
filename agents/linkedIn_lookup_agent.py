from dotenv import load_dotenv
load_dotenv()
import os
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
create_react_agent,
AgentExecutor
)
from tools.tools import get_profile_url_tavily

from langchain import hub


def lookup(name:str)->str:

    llm=ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
    )

    template="""given the full name {name_of_person} i want you to get me a link to there linkedin profile. Your answer should contain only a URL"""

    prompt_template = PromptTemplate(
        template=template,input_variables=["name_of_person"]
    )

    tools_for_agent=[
        Tool(
            name="Crawl google 4 for linkedIn profile url",
            func=get_profile_url_tavily,
            description="use this when you need to get the linkedIn profile url"
        )
    ]

    react_prompt=hub.pull("hwchase17/react")

    agent=create_react_agent(llm=llm,tools=tools_for_agent,prompt=react_prompt)

    agent_executor= AgentExecutor(agent=agent,tools=tools_for_agent,verbose=True)

    result=agent_executor.invoke(
        input={"input":prompt_template.format_prompt(name_of_person=name)}
    )

    linkedIn_profile_url_final = result["output"]
    return linkedIn_profile_url_final



if __name__=="__main__":
    linkedIn_URL = lookup(name="sundar pichai")
    print(linkedIn_URL)