import streamlit as st
import openai
#from langchain_community.llms import OpenAI
#from langchain.llms import OpenAI

st.title('🍩🍧🎂 Dessert Recipe Generator')

openai_api_key = st.sidebar.text_input('API Key',type='passoword')

client = openai.OpenAI(
    api_key= api_key,
    base_url="https://api.aimlapi.com/",
)

def generate_response(user_input):
    chat_completion = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "user", "content": user_input},
        ],
        temperature=0.7,
        max_tokens=512,
    )
    chat_completion.choices[0].message.content

with st.form('my_form'):
    system_instructions = st.text_area('Enter Ingredients in a comma separated list:', 'Generate a simple dessert recipe with ingredients with flour, butter, sugar:')
    user_query= st.text_area('Enter user content:')
    submitted = st.form_submit_button('Generate Recipe')
   
    if submitted:
        try:
            generate_response(system_instructions,user_query )
        except Exception as e:
            print('Failed to upload to ftp: %s', repr(e))


#old function and form code
#def generate_response(input_text):
 #llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  #st.info(llm(input_text))

#with st.form('my_form'):
  #text = st.text_area('Enter Ingredients in a comma separated list:', 'Generate a simple dessert recipe with ingredients with flour, butter, sugar')
  #submitted = st.form_submit_button('Submit')
  #if not openai_api_key.startswith('sk-'):
    #st.warning('Please enter your OpenAI API key!', icon='⚠')
  #if submitted and openai_api_key.startswith('sk-'):
    #generate_response('Generate a simple dessert recipe with ingredients '+text)
