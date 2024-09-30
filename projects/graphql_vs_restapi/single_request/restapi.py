"""

In this restapi approach you have to make a separate request to get countries, as it is only one request so you won't see much difference between restapi and graphql

"""

from fastapi import FastAPI
import requests

app = FastAPI()

# REST API endpoint in FastAPI
@app.get("/countries_rest")
async def get_countries_rest():
    url = 'https://restcountries.com/v3.1/all'  # Public REST API for countries
    response = requests.get(url)
    
    if response.status_code == 200:
        countries_data = response.json()
        countries = [{"name": country['name']['common'], "capital": country.get('capital', ['N/A'])[0]}
                     for country in countries_data]
        return {"countries": countries}
    else:
        return {"error": f"Failed to fetch data with status code {response.status_code}"}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
