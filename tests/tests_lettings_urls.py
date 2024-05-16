# from django.test import TestCase

# import pytest
from django.urls import reverse, resolve
# from lettings.models import Address  # , Letting
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

# client.get('/path/', {'key1': 'data1', 'key2': 'data2'})


# @pytest.mark.django_db
def test_lettings_url():
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


# def test_dummy():
#     assert 1

# ==== GeeC33
# import pytest

# from django.urls import reverse, resolve
# from django.test import Client
# from pytest_django.asserts import assertTemplateUsed


# @pytest.fixture
# def client():
#     """Fixture to create a test client."""
#     client = Client()

#     return client


# @pytest.mark.django_db
# class TestOCLettingsSiteUrls:
#     """Class grouping URL tests of the oc_lettings_site application."""
#     def test_index_url(self):
#         """
#         GIVEN a URL path for the index is expected,
#         WHEN the URL path is retrieved and the view name is resolved,
#         THEN it should match the expected path and view name.
#         """
#         path = reverse("index")

#         assert path == "/"
#         assert resolve(path).view_name == "index"

#     def test_admin_url(self):
#         """
#         GIVEN a URL path for the admin index is expected,
#         WHEN the URL path is retrieved and the view name is resolved,
#         THEN it should match the expected path and view name.
#         """
#         path = reverse("admin:index")

#         assert path == "/admin/"
#         assert resolve(path).view_name == "admin:index"


# @pytest.mark.django_db
# class TestOCLettingsSiteViews:
#     """Class grouping view tests of the oc_lettings_site application."""
#     def test_index_view(self, client):
#         """
#         GIVEN a client for the index view,
#         WHEN the view is accessed,
#         THEN it should render with the expected content, status code, and template.
#         """
#         path = reverse("index")
#         response = client.get(path)
#         content = response.content.decode()

#         expected_content = "Orange County Lettings 2023"

#         assert expected_content in content
#         assert response.status_code == 200
#         assertTemplateUsed(response, "index.html")

#     def test_404_view(self, client):
#         """
#         GIVEN a client for an unexisting profile view,
#         WHEN the view is accessed,
#         THEN it should render with the expected content, status code, and template.
#         """
#         path = reverse("profiles:profile", kwargs={"username": "azazeaze"})
#         response = client.get(path)
#         content = response.content.decode()

#         expected_content = "404 - Page not found"

#         assert expected_content in content
#         assert response.status_code == 404
#         assertTemplateUsed(response, "404.html")

# ==== slb59
# """test letting urls"""
# import pytest
# from django.test import TestCase
# from django.urls import resolve, reverse

# from lettings.models import Letting


# class LettingsUrlsTestCase(TestCase):
#     @pytest.fixture(autouse=True)
#     def prepare_fixture(self, myaddress):
#         self.myaddress = myaddress

#     def setUp(self):
#         """setup an instance of letting and address"""
#         self.address = self.myaddress
#         self.letting = Letting.objects.create(title="My letting", address=self.address)

#     def test_letting_index_url(self):
#         """test index url"""
#         path = reverse("lettings:index")
#         assert path == "/lettings/"
#         assert resolve(path).view_name == "lettings:index"

#     def test_letting_url(self):
#         """test first letting url"""
#         path = reverse("lettings:letting", args=[1])
#         assert path == "/lettings/1/"
#         assert resolve(path).view_name == "lettings:letting"
