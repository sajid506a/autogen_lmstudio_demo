import autogen
config_list = [
    {
        "base_url": "http://localhost:1234/v1",
        "api_key": "NULL",  # just a placeholder
    }
]

llm_config = {
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
    system_message="You are a code specializing in python"
)
termination_msg = lambda x: isinstance(x, dict) and "TERMINATE" == str(x.get("content", ""))[-9:].upper()


user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=100,
    is_termination_msg=termination_msg,
    code_execution_config={"last_n_messages": 2000,"work_dir": "web"},
    llm_config=llm_config,
    system_message="""
    Reply Terminate if task has been completed Otherwise, reply CONTINUE, or the reason why task is not completed print it
"""
)

task= """
write a python method to print 1 to 100 numbers
"""

user_proxy.initiate_chat(assistant,message = task)