import pytest 

def pytest_addoption(parser):
    parser.addoption('--pubmed_id', action='store', dest='pubmed', nargs='*', type=float, default=['24151578.0'])

@pytest.fixture
def pubmed_id(request):
    return request.config.getoption('--pubmed_id')


