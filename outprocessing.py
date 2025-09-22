from langchain.schema import HumanMessage,AIMessage
text={'messages': [HumanMessage(content='write a simple factorial program in any language')], 'plan': AIMessage(content="Here's a development plan for a simple factorial program:"),'code': AIMessage(content='python code')}

print(text['code'].content)