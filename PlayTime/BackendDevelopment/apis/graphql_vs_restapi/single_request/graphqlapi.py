"""

In this restapi approach you have to make a separate request to get countries, as it is only one request so you won't see much difference between restapi and graphql

"""


from fastapi import FastAPI
import requests

app = FastAPI()

# GraphQL API endpoint in FastAPI
@app.get("/countries_graphql")
async def get_countries_graphql():
    url = 'https://countries.trevorblades.com/'  # GraphQL API URL
    
    # Define the GraphQL query
    query = """
    {
      countries {
        code
        name
        capital
      }
    }
    """
    
    # Send the POST request to GraphQL API
    response = requests.post(url, json={'query': query})
    
    if response.status_code == 200:
        data = response.json()
        countries = [{"name": country['name'], "capital": country.get('capital', 'N/A')}
                     for country in data['data']['countries']]
        return {"countries": countries}
    else:
        return {"error": f"Failed to fetch data with status code {response.status_code}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
