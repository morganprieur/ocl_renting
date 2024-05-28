from django.test import TestCase

import pytest
# from oc_lettings_site import conftest
from django.urls import reverse, resolve
from lettings.models import Letting
# from lettings.models import Address, Letting
# from django.test import Client
# from pytest_django.asserts import assertTemplateUsed

from lettings.models import Address


@pytest.fixture()
def one_address() -> Address:
    address = Address.objects.create(
        number=4,
        street="Bd Talabot",
        city="Nimes",
        state="FR",
        zip_code=30000,
        country_iso_code="FR",
    )
    return address


@pytest.mark.django_db
class LettingsUrlsTestCase(TestCase):
    @pytest.fixture(autouse=True)
    def prepare_fixture(self, one_address):
        self.one_address = one_address

    def setUp(self):
        """setup an instance of letting and address"""
        self.address = self.one_address
        self.letting = Letting.objects.create(title="One letting", address=self.address)

    def test_letting_index_url(self):
        """test index url"""
        path = reverse("lettings:index")
        assert path == "/lettings/"
        assert resolve(path).view_name == "lettings:index"


# def test_favourite_products():

#     """
#     Testing if the 'favourite-products' route is mapping to FavouriteProductListView
#     """

#     url = reverse('favourite-products')
#     assert resolve(url).view_name == 'favourite-products'
#     assert resolve(url).func.view_class == FavouriteProductListView
