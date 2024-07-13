import requests

class restCountry:
    #initialized url input
    def __init__(self,url):
        self.url = url 
    
     # this code returns status code of json request 
    def api_status_code(self):
        response = requests.get(self.url)
        return response.status_code    
    
    # if status code is success(200), then response data is fetched and returned as json data
    def fetch_api_data(self):
        if self.api_status_code() == 200:
            response = requests.get(self.url).json()
            return response
        else:
            return "Error-404"

    # this method returns country names which are having dollar as currency    
    def fetch_usdCountry(self):
        if self.api_status_code()==200:
            for data in self.fetch_api_data():
                currencies = data.get('currencies',{})
                for cc,ci in currencies.items():
                    if 'name' in ci and 'dollar' in ci['name'].lower():
                        name = data.get('name',{}).get('official')
                        print(f"Country which are having dollar as currency: {name}")

if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
     # created object for the class for accessing the functions and assign url with value
    rc = restCountry(url)
    rc.fetch_usdCountry()