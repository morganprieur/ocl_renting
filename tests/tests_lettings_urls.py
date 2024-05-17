from django.test import TestCase

import pytest
from django.urls import reverse, resolve
from lettings.models import Letting
# from lettings.models import Address, Letting
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


# @pytest.mark.django_db
def test_oc_lettings_url():
    client = Client()
    path = reverse('index')  # , kwargs={'pk':1})
    response = client.get(path)
    content = response.content.decode()

    assert path == "/"
    # assert path == "/1"
    assert resolve(path).view_name == "index"
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")
    title = '''<h1 class="page-header-ui-title mb-3 display-6">
                Welcome to Holiday Homes
            </h1>'''
    assert title in content


def test_admin_url():
    path = reverse("admin:index")
    assert path == "/admin/"
    assert resolve(path).view_name == "admin:index"


class LettingsUrlsTestCase(TestCase):
    @pytest.fixture(autouse=True)
    def prepare_fixture(self, one_address):
        self.one_address = one_address

    def setUp(self):
        """setup an instance of letting and address"""
        self.address = self.one_address
        self.letting = Letting.objects.create(title="My letting", address=self.address)

    def test_letting_index_url(self):
        """test index url"""
        path = reverse("lettings:index")
        assert path == "/lettings/"
        assert resolve(path).view_name == "lettings:index"
