# from django.test import TestCase

import pytest
from django.urls import reverse, resolve
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
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
