"""
Testing module for bib.py
"""
import pytest
from bibtextomd.bib import main, reorder


def test_single_author_good():
    names = 'Author, First A.'
    n = reorder(names, 'F.A. Author')
    assert n == '**F.A. Author**'


def test_two_authors_good():
    names = 'Author, First A. and Name, Second N.'
    n = reorder(names, 'F.A. Author')
    assert n == '**F.A. Author** and S.N. Name'


def test_three_authors_good():
    names = 'Author, First A. and Name, Second N. and Name, Unicode C.'
    n = reorder(names, 'F.A. Author')
    assert n == '**F.A. Author**, S.N. Name, and U.C. Name'


def test_unicode_good():
    names = 'Namé, Unicode C.'
    n = reorder(names, 'U.C. Namé')
    assert n == '**U.C. Namé**'


def test_missing_name():
    names = 'Author, First A.'
    with pytest.warns(UserWarning):
        reorder(names, 'Missing Author')


def test_no_highlighted_name():
    names = 'Author, First A.'
    n = reorder(names, None)
    assert n == 'F.A. Author'


def test_hyphenated_name():
    names = 'Name, Hypen-Ated'
    n = reorder(names, None)
    assert n == 'H.A. Name'

