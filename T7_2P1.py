# Here as part of this code, trying to fetch breweries present in the list of states
import requests

class openbrew:
    # initializing to base url
    def __init__(self,base_url):
        self.base_url = base_url
    # retrieving status code 
    def api_status_code(self,url):
        response = requests.get(url)
        return response.status_code
    # retrieving response if status code is success(200)
    def fetch_webPage_data(self,url):
        all_data = []
        page = 1
        per_page = 50  # Adjust this based on the maximum allowed per page
        while True:
            url = f"{self.base_url}?per_page={per_page}&page={page}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if not data:
                    break
                all_data.extend(data)
                page += 1
            else:
                print(f"Failed to retrieve data from URL: {url}")
                break
        return all_data
    #retrieving data based on specific condition, here its based on state    
    def fetch_data_state(self,state):
        # here the url changes for each state, so building for every state
        state_url = f"{self.base_url}?by_state={state}"
        print(f"fetching data from this url {state_url}")
        if self.api_status_code(state_url)==200:
            count = 0
            for data in self.fetch_webPage_data(state_url):
                if data['state_province'] == state:
                    name = data.get('name')
                    count += 1
                    #printing name of the brewery present in the state
                    print(f"breweries present in the state {state} :{name}")
            # printing total number of count of breweries
            print(f"Total number of breweries in {state}:{count}")
        
if __name__ == "__main__":
    base_url = "https://api.openbrewerydb.org/v1/breweries"
    ob = openbrew(base_url)
    # as the data needed for more than one state, used list for passing list of states
    state_list = ["Alaska","Maine","New York"]
    for state in state_list:
        ob.fetch_data_state(state)