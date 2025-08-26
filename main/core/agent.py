from langchain.agents import initialize_agent , AgentType
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class AgentAction:
    def __init__(self , Tools):
        self.Tools = Tools
        llm = ChatOpenAI(
            model="openai/gpt-oss-20b:free",
            temperature=0,
            api_key=os.getenv('OPENAI_API_KEY'),
            base_url="https://openrouter.ai/api/v1"
        )

        memory = ConversationBufferMemory(memory_key="chat history" , return_messages=True)

        self.agent = initialize_agent(
            llm=llm , 
            tools= Tools, 
            memory = memory, 
            agent= AgentType.CONVERSATIONAL_REACT_DESCRIPTION ,
            verbose = True
        )

    
    def runprompt(self , prompt):
        self.agent.run(prompt)



        
