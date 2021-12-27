class BreweriesBaseTests:
    ENDPOINT = "https://api.openbrewerydb.org/"
    BREWERIES = 'breweries'

    def get_breweries_list(self, client, by_type=None):
        if by_type:
            response = client.get_unauthorized(url=self.ENDPOINT, uri=self.BREWERIES, params='by_type=' + by_type)
        else:
            response = client.get_unauthorized(url=self.ENDPOINT, uri=self.BREWERIES)
        assert response.status_code == 200
        response_data = response.json()
        return response_data

    def get_brewery_by_id(self, client, brewery_id=None):
        response = client.get_unauthorized(url=self.ENDPOINT, uri=self.BREWERIES + '/' + str(brewery_id))
        assert response.status_code == 200
        response_data = response.json()
        return response_data

    def get_brewery_by_search(self, client, search=None):
        response = client.get_unauthorized(url=self.ENDPOINT, uri=self.BREWERIES + '/search?query=' + str(search))
        assert response.status_code == 200
        response_data = response.json()
        return response_data

    def get_brewery_autocomplete_by_search(self, client, search=None):
        response = client.get_unauthorized(url=self.ENDPOINT, uri=self.BREWERIES + '/autocomplete?query=' + str(search))
        assert response.status_code == 200
        response_data = response.json()
        return response_data
