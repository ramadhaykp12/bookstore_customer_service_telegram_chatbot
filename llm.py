from sqlalchemy import create_engine
from langchain_huggingface import HuggingFaceEndpoint
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

db_user = "username"
db_pass = "password"
db_host = "host"
db_port = "port"
db_name = "database_name"

connection_string = f"mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
engine = create_engine(connection_string)

db = SQLDatabase(engine, include_tables=["buku"])

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    max_new_tokens=100,
    do_sample=False,
    huggingfacehub_api_token="huggingface_api_token"
)


def answer_question(question):
    db_chain = SQLDatabaseChain.from_llm(llm, db, return_intermediate_steps=False, verbose=False)

    # Natural language query
    answer = db_chain.invoke(question)
    return answer['result'].split("\n")[0] 


