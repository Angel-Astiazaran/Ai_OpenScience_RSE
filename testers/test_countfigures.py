import pytest
from src.count_figures import count_figures

def test_count_figures():
    input_pdf = 'testers/sample_with_figures.pdf'
    expected_count = 5
    figure_count = count_figures(input_pdf)
    assert figure_count == expected_count
