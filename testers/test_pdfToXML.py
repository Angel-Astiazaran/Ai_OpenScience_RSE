import pytest
from src.pdfToXML import pdfToXML

def test_pdfToCML():
    input_pdf = 'testers/test.pdf'
    expected_output = '<xml...</xml>'
    output = pdfToXML(input_pdf)
    assert output.strip() == expected_output.strip()