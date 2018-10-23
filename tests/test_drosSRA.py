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

def test_single_flag(pubmed_id, capsys):
    #drosSRA.main(pubmed_id)
    test_run = drosSRA.main(['-p','24151578.0'])
    out, err = capsys.readouterr()
    assert out=='https://www.ncbi.nlm.nih.gov/genome/gdv/browser/?context=genome&acc=GCF_000001215.4&context=GEO&acc=DRX013093%2CDRX013094\n'

def test_mult_flags(pubmed_id, capsys):
    test_run = drosSRA.main(['-p', '27172187.0', '-s','female'])
    out, err = capsys.readouterr()
    assert out=='https://www.ncbi.nlm.nih.gov/genome/gdv/browser/?context=genome&acc=GCF_000001215.4&context=GEO&acc=SRX357301%2CSRX357302%2CSRX357303%2CSRX357318%2CSRX357319%2CSRX357320%2CSRX357324%2CSRX357325%2CSRX357326%2CSRX357330%2CSRX357331%2CSRX357332%2CSRX357336%2CSRX357337%2CSRX357338%2CSRX971847%2CSRX971848%2CSRX971849%2CSRX971850%2CSRX971851%2CSRX971852\n'
