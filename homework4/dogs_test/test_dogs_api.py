import pytest

from homework4.dogs_test.base_test import DogsBaseTests


class TestDogs(DogsBaseTests):
    """tests for dogs api"""

    def test_get_all_dogs_list(self, client):
        all_dogs = self.get_dogs_list(client)
        assert all_dogs['status'] == 'success'
        assert len(all_dogs['message']) == 95

    @pytest.mark.parametrize('breed, expected', [('african', 169), ('beagle', 204)])
    def test_get_dogs_by_breed(self, client, breed, expected):
        images_by_breed = self.get_dogs_by_breed(client, breed=breed)
        assert images_by_breed['status'] == 'success'
        assert len(images_by_breed['message']) == expected

    @pytest.mark.parametrize('breed, expected', [('african', 0), ('bulldog', 3)])
    def test_get_dogs_by_breed(self, client, breed, expected):
        images_by_breed = self.get_subbreeds_by_breed(client, breed=breed)
        assert images_by_breed['status'] == 'success'
        assert len(images_by_breed['message']) == expected

    def test_get_random_image(self, client):
        images_by_breed = self.get_random_image(client)
        assert images_by_breed['status'] == 'success'
        assert len(images_by_breed['message']) != 0

    @pytest.mark.parametrize('breed', ['african', 'beagle'])
    def test_get_random_image_by_breed(self, client, breed):
        images_by_breed = self.get_random_image_by_breed(client, breed=breed)
        assert images_by_breed['status'] == 'success'
        assert len(images_by_breed['message']) != 0
