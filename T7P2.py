# Here trying to print country name, currencies (name and symbol) from json data

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

    #this method returns country name and its currencies along with name and symbol    
    def fetch_CountryName(self):
        if self.api_status_code() == 200:
            for data in self.fetch_api_data():
                country_Name = data.get('name',{}).get('official')
                currencies = data.get('currencies',{})
                print(f"Country Name:{country_Name}, Currency: {currencies}")

if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
     # created object for the class for accessing the functions and assign url with value
    rc = restCountry(url)
    rc.fetch_CountryName()