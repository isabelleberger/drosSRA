#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `drosSRA` package."""

import pytest
import requests
from drosSRA import drosSRA

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    return requests.get('https://github.com/isabelleberger/drosSRA')

def test_drosSRA(pubmed_id, capsys):
    #drosSRA.main(pubmed_id)
    test_run = drosSRA.main(['-p','24151578.0'])
    out, err = capsys.readouterr()
    assert out=='https://www.ncbi.nlm.nih.gov/genome/gdv/browser/?context=GEO&acc=DRX013093%2CDRX013094\n'
