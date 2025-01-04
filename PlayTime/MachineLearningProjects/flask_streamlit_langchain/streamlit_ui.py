import requests
import streamlit as st

# Create a text input for the user query
user_query = st.text_input("Enter your query")

# Create a button to trigger the function
if st.button("Run"):
    # Call the function based on the user query
    # For example, if the user query is "update book number 4"
    # You can parse the query and get the book id and the new data
    # Then send a PUT request to the /book/<id> endpoint
    # And display the response as markdown
    # You can use LangChain to handle more complex queries
    # And use OpenAI LLM to generate natural language responses
    # This is just a simple example for illustration
    if user_query.startswith("update book number "):
        try:
            book_id = user_query.split()[-1]
            new_data = {"title": "New Title", "author_id": 1} # You can get this from the user or generate it
            response = requests.put(f"http://localhost:5000/book/{book_id}", json=new_data)
            st.markdown(f"The book with id {book_id} has been updated with the following data: {response.json()}")
        except:
            st.markdown("Please enter a valid query")
    else:
        st.markdown("Please enter a valid query")
