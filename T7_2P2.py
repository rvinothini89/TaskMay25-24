import requests

class OpenBrew:
    # Initializing with base URL
    def __init__(self, base_url):
        self.base_url = base_url
    
    # Fetch data from URL with pagination
    def fetch_all_data(self):
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

    # Retrieve and count breweries by type and city
    def count_breweries_by_type_and_city(self, state_list):
        data = self.fetch_all_data()
        city_type_count = {}

        for brewery in data:
            city = brewery.get('city')
            state = brewery.get('state')
            brew_type = brewery.get('brewery_type')
            # storing the value in dictionary for each city and its type as key pair value
            if state in state_list:
                if city and brew_type:
                    key = (city, brew_type)
                    if key not in city_type_count:
                        city_type_count[key] = 0
                    city_type_count[key] += 1

        return city_type_count

if __name__ == "__main__":
    base_url = "https://api.openbrewerydb.org/v1/breweries"
    ob = OpenBrew(base_url)
    state_list = ["Alaska", "Maine", "New York"]
    city_type_counts = ob.count_breweries_by_type_and_city(state_list)
    
    # Traversing through dictionary and printing the values
    for (city, brew_type), count in city_type_counts.items():
        print(f"City: {city}, Brewery Type: {brew_type}, Count: {count}")
