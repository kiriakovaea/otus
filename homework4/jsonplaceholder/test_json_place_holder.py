import pytest

from homework4.jsonplaceholder.base_test import JsonPlaceHolderTests


class TestJsonPlaceHolder(JsonPlaceHolderTests):
    """tests for jsonplaceholder api"""

    def test_get_all_resources(self, client):
        """ получаем все ресурсы """
        all_resources = self.get_all_resources(client)
        assert len(all_resources) == 100

    def test_create_resource(self, client):
        """ создаем ресурс """
        params = {
            'title': 'testing',
            'body': 'testing jsonplaceholder',
            'userId': 1,
        }
        resource = self.create_resource(client, params)
        del(resource['id'])
        assert resource == params

    def test_update_resource(self, client):
        """обновляем данные созданного ресурса"""
        params_update = {
            'id': 1,
            'title': 'testing-update-resource',
            'body': 'testing update jsonplaceholder resource',
            'userId': '1',
        }
        resource_update = self.update_resource(client, params_update)
        assert resource_update == params_update

    def test_delete_resource(self, client):
        """удаляем данные созданного ресурса"""
        resource_delete = self.delete_resource(client)
        assert resource_delete == {}

    @pytest.mark.parametrize('user_id', [1, 101])
    def test_filtering_resources_by_user_id(self, client, user_id):
        """ фильтруем ресурсы """
        resources = self.get_filtering_resources(client, user_id=user_id)
        for resource in resources:
            assert resource['userId'] == user_id

    @pytest.mark.parametrize('title', ['sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
                                       'ea molestias quasi exercitationem repellat qui ipsa sit aut'])
    def test_filtering_resources_by_title(self, client, title):
        """ фильтруем ресурсы """
        resources = self.get_filtering_resources(client, title=title)
        for resource in resources:
            assert resource['title'] == title
