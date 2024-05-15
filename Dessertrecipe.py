import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain import OpenAI
from langchain_core.output_parsers import CommaSeparatedListOutputParser
# USeful to create the Retrieval part
from langchain.chains import create_retrieval_chain

# Set up OpenAI
openai_key = "sk-proj-EH5zKkQqNqLPmrksxJbGT3BlbkFJCiWotwUvgGgkhYvrEqas"
llm = OpenAI(api_key=openai_key, model_name="gpt-3.5-turbo")

def generate_recipe_summary(ingredients):
    # For this example, let's just get the ingredients and concatenate the ingredients into a simple summary
    
    recipe_summary = " ".join(ingredients)
    return recipe_summary

def main():
   st.title("Dessert Recipe Summarizer")

    # Input for ingredients
   ingredients = st.text_area("Enter the ingredients separated by commas (e.g., flour, sugar, eggs):")
   
  
   if st.button("Generate Recipe"):
        if ingredients:
            #ingredients_list = [ingredient.strip() for ingredient in ingredients.split(",")]
            parser = CommaSeparatedListOutputParser()
            chain = ingredients | llm | parser
            #recipe_summary = generate_recipe_summary(ingredients_list)

            # Display the generated recipe summary in bullet points
            st.write("Recipe Summary:")
            chain.invoke({
            "input": ingredients
            })
            st.markdown(f"- {recipe_summary}")

        else:
            st.warning("Please enter the ingredients.")

if __name__ == "__main__":
    main()
