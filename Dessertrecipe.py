!pip install streamlit
import streamlit as st

# Function to generate recipe summary based on ingredients
def generate_recipe_summary(ingredients):
    # Here you would use your language model (e.g., GPT-3) to generate the recipe summary
    # For this example, let's just concatenate the ingredients into a simple summary
    recipe_summary = " ".join(ingredients)
    return recipe_summary

def main():
    st.title("Dessert Recipe Summarizer")

    # Input for ingredients
    ingredients = st.text_area("Enter the ingredients separated by commas (e.g., flour, sugar, eggs):")

    if st.button("Generate Recipe"):
        if ingredients:
            ingredients_list = [ingredient.strip() for ingredient in ingredients.split(",")]
            recipe_summary = generate_recipe_summary(ingredients_list)

            # Display the generated recipe summary in bullet points
            st.write("Recipe Summary:")
            st.markdown(f"- {recipe_summary}")

        else:
            st.warning("Please enter the ingredients.")

if __name__ == "__main__":
    main()
