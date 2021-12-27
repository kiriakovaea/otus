class JsonPlaceHolderTests:
    ENDPOINT = "https://jsonplaceholder.typicode.com/"
    GET_ALL_RESOURCES = 'posts/'
    CREATE_RESOURCE = 'posts'
    UPDATE_RESOURCE = 'posts/1'

    def get_all_resources(self, client):
        response = client.get_unauthorized(url=self.ENDPOINT, uri=self.GET_ALL_RESOURCES)
        assert response.status_code == 200
        response_data = response.json()
        return response_data

    def get_filtering_resources(self, client, user_id=None, title=None):
        params = {}
        if user_id is not None:
            params['userId'] = user_id
        if title is not None:
            params['title'] = title
        response = client.get_unauthorized(url=self.ENDPOINT, uri=self.GET_ALL_RESOURCES, params=params)
        assert response.status_code == 200
        response_data = response.json()
        return response_data

    def create_resource(self, client, params: dict):
        response = client.post_unauthorized(url=self.ENDPOINT, uri=self.CREATE_RESOURCE, json=params)
        assert response.status_code == 201
        response_data = response.json()
        return response_data

    def update_resource(self, client,  params: dict):
        response = client.put_unauthorized(url=self.ENDPOINT, uri=self.UPDATE_RESOURCE, data=params)
        assert response.status_code == 200
        response_data = response.json()
        return response_data

    def delete_resource(self, client):
        response = client.delete_unauthorized(url=self.ENDPOINT, uri=self.UPDATE_RESOURCE)
        assert response.status_code == 200
        response_data = response.json()
        return response_data
