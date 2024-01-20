from langchain.llms import OpenAI
#from langchain_core.prompts import ChatPromptTemplate
# from langchain_community.llms import OpenAI
# import warnings

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType


# warnings.filterwarnings("ignore",category=DeprecationWarning)

load_dotenv()

def generate_pet_name(animal_type , pet_color):
    llm=ChatOpenAI(temperature=0.5)
    
    #to repurpose prompts
    prompt_template_name = PromptTemplate(
        #parameters taht can be dynamic
        input_variables=['animal_type','pet_color'],
        template="I have a {animal_type} pet , i want 5 cool names for it. It has {pet_color} color.Suggest me names."
    )
    
    #LLMCHAIN allows us to put these inependent componenets of prompts together
    
    name_chain = LLMChain(llm=llm , prompt= prompt_template_name,output_key="pet_name")
    
    response = name_chain({'animal_type' : animal_type , 'pet_color':pet_color})
    return response
    
    # return name_cahin

def langchain_agent():
    llm= OpenAI(temperature=0.7)
    
    #loading tools
    
    tools=load_tools(["wikipedia","llm-math"], llm=llm)
    
    agent = initialize_agent(
        tools , llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose =True
    )
    
    result=agent.run(
        "What is the average age of a dog? Multiply the age by 3"
    )
    print(result)

if __name__ == "__main__":
    langchain_agent()
    #print(generate_pet_name("cat", "orange"))
    