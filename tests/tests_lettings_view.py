# from django.test import TestCase
from django.test import Client
from django.urls import reverse, resolve
from lettings.models import Address, Letting

import pytest
# from pytest_django.asserts import assertTemplateUsed

client = Client()


@pytest.fixture()
def one_address():
    address = Address.objects.create(
        number=4,
        street="Bd Talabot",
        city="Nimes",
        state="FR",
        zip_code=30000,
        country_iso_code="FR",
    )
    return address


# class LettingsUrlsTestCase(TestCase):
#     @pytest.fixture(autouse=True)
#     def prepare_fixture(self, one_address):
#         self.one_address = one_address

@pytest.mark.django_db
# @pytest.fixture(autouse=True)
def setUp(one_address):
    """setup an instance of letting and address"""
    address = one_address
    letting = Letting.objects.create(
        title="One letting",
        address=address
    )
    print(letting)


def test_letting_index_url():
    """test index url"""
    path = reverse("lettings:index")
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings:index"


# @pytest.mark.django_db
# def tests_letting_view():
#     """
#         Testing if FavouriteProductListView is properly rendered with 200
#         status code and in second assert,
#         we are making sure it returns the correct template 'favourite_product.html'
#     """
#     # address = Address.objects.create(
#     #     number=4,
#     #     street="Bd Talabot",
#     #     city="Nimes",
#     #     state="FR",
#     #     zip_code=30000,
#     #     country_iso_code="FR",
#     # )
#     response = client.get(reverse('lettings:index'))

#     print(response)
#     assert response.status_code == 200
#     assertTemplateUsed(response, 'lettings/index.html')


# from django.test import TestCase

# import pytest
# # from oc_lettings_site import conftest
# from django.urls import reverse, resolve
# from lettings.models import Letting
# # from lettings.models import Address, Letting
# from django.test import Client
# # from pytest_django.asserts import assertTemplateUsed

# from lettings.models import Address
