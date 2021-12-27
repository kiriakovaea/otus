class DogsBaseTests:
    ENDPOINT = "https://dog.ceo/"
    ALL_LIST = "api/breeds/list/all"
    RANDOM_IMAGE = 'api/breeds/image/random'

    @classmethod
    def get_endpoint_by_breed(cls, breed: str):
        return f'api/breed/{breed}/images'

    @classmethod
    def get_endpoint_subbreeds_by_breed(cls, breed: str):
        return f'api/breed/{breed}/list'

    @classmethod
    def get_endpoint_random_image_by_breed(cls, breed: str):
        return f'api/breed/{breed}/images/random'

    def get_dogs_list(self, client):
        response = client.get_unauthorized(url=self.ENDPOINT, uri=self.ALL_LIST)
        assert response.status_code == 200
        response_data = response.json()
        return response_data

    def get_dogs_by_breed(self, client, breed: str):
        response = client.get_unauthorized(url=self.ENDPOINT, uri=self.get_endpoint_by_breed(breed))
        assert response.status_code == 200
        response_data = response.json()
        return response_data

    def get_subbreeds_by_breed(self, client, breed: str):
        response = client.get_unauthorized(url=self.ENDPOINT, uri=self.get_endpoint_subbreeds_by_breed(breed))
        assert response.status_code == 200
        response_data = response.json()
        return response_data

    def get_random_image(self, client):
        response = client.get_unauthorized(url=self.ENDPOINT, uri=self.RANDOM_IMAGE)
        assert response.status_code == 200
        response_data = response.json()
        return response_data

    def get_random_image_by_breed(self, client, breed):
        response = client.get_unauthorized(url=self.ENDPOINT, uri=self.get_endpoint_random_image_by_breed(breed))
        assert response.status_code == 200
        response_data = response.json()
        return response_data
