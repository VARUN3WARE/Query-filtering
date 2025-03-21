import streamlit as st
import ollama

# Function to check content appropriateness
def check_content_appropriateness(user_prompt):
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": "You are my English instructor and content moderation assistant. Don't provide external information, just one word is enough. If the prompt is appropriate, respond with 'true'. If it contains harmful, malicious, or inappropriate content, respond with 'false'."},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.message.content.strip().lower()

# Function to get knowledge-based response
def get_knowledge_response(user_prompt):
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": "You are my all-in-one instructor and knowledge guide. Explain the topic in a blog-like format, as if explaining to a 10-year-old."},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.message.content.strip()

# Streamlit UI
def main():
    st.set_page_config(page_title="Content Moderation",layout="wide") 
    st.title("Knowledge and Content Moderation Assistant")
    hide_default_format = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_default_format, unsafe_allow_html=True)

    # Input prompt
    user_prompt = st.text_area("Enter the topic you want to learn about:", "")
    
    if st.button("Submit"):
        if user_prompt.strip() == "":
            st.warning("Please enter a valid topic.")
        else:
            # Check if the content is appropriate
            filter_result = check_content_appropriateness(user_prompt)
            
            if filter_result == 'false':
                st.error("Your input contains inappropriate content and cannot be processed.")
            else:
                # If content is appropriate, provide the knowledge response
                knowledge_response = get_knowledge_response(user_prompt)
                st.success("Here is the knowledge on your topic:")
                st.write(knowledge_response)

# Run the app
if __name__ == "__main__":
    main()
