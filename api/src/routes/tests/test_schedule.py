from unittest import mock

import pytest


@pytest.fixture
def stub_de_dado():
    return True

def test_stub(stub_de_dado):
    assert stub_de_dado