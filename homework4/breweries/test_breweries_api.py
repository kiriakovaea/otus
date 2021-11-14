import pytest

from homework4.breweries.base_test import BreweriesBaseTests


class TestBreweries(BreweriesBaseTests):
    """tests for breweries api"""

    def test_get_all_breweries_list(self, client):
        breweries = self.get_breweries_list(client)
        assert len(breweries) == 20
        expected_first = {'id': '10-56-brewing-company-knox', 'name': '10-56 Brewing Company', 'brewery_type': 'micro',
                          'street': '400 Brown Cir', 'address_2': None, 'address_3': None, 'city': 'Knox',
                          'state': 'Indiana', 'county_province': None, 'postal_code': '46534',
                          'country': 'United States', 'longitude': '-86.627954', 'latitude': '41.289715',
                          'phone': '6308165790', 'website_url': None, 'updated_at': '2021-10-23T02:24:55.243Z',
                          'created_at': '2021-10-23T02:24:55.243Z'}
        assert breweries[0] == expected_first

    @pytest.mark.parametrize('type', ['micro', 'closed'])
    def test_get_all_breweries_list_by_type(self, client, type):
        breweries = self.get_breweries_list(client, by_type=type)
        for item in breweries:
            assert item['brewery_type'] == type

    @pytest.mark.parametrize('brewery_id', ['10-56-brewing-company-knox', '12-acres-brewing-company-killeshin'])
    def test_get_brewery_by_id(self, client, brewery_id):
        brewery = self.get_brewery_by_id(client, brewery_id=brewery_id)
        assert brewery['id'] == brewery_id

    def test_get_brewery_by_search(self, client):
        breweries = self.get_brewery_by_search(client, search='brewing-company-knox')
        for item in breweries:
            assert 'brewing-company-knox' in item['name'] or 'brewing-company-knox' in item['id']

    def test_get_brewery_autocomplete_by_search(self, client):
        breweries = self.get_brewery_autocomplete_by_search(client, search='dog')
        for item in breweries:
            assert 'dog' in item['name'] or 'dog' in item['id']
