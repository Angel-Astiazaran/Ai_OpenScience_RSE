import pytest
from src.extract_links import extract_links

def test_extract_links():
    input_pdf = 'testers/sample_with_links.pdf'
    expected_links = ['http://www.google.com', 'http://www.github.com']
    links = extract_links(input_pdf)
    assert links == expected_links