from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv

load_dotenv()

def generateNames(animalType, animalColor, animalDetails):
    llm = OpenAI(temperature=0.9)
    # name=llm.invoke("Please suggest 5 names for my new dog")

    namePromptTemplate = PromptTemplate(
        input_variables=['animalType', 'animalColor', 'animalDetails'],
        template = "Please suggest 5 names for my new {animalType} which is {animalColor} in color. Some additional details include {animalDetails}"
    )
    
    nameChain = LLMChain(llm=llm, prompt=namePromptTemplate, output_key="petName")
    response = nameChain.invoke({'animalType': animalType, 'animalColor':animalColor,  'animalDetails': animalDetails})
    return response

def nameAgent():
    llm = OpenAI(temperature=0.9)
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    result = agent.run("What is the average age of a dog? Multiple it by 3")
    print (result)

if __name__=="__main__":
    nameAgent();