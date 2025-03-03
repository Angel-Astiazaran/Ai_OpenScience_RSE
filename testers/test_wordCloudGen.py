import pytest
from src.wordCloudGen import generate_wordcloud

def test_generate_wordcloud():
    text= 'sample text for wordcloud'
    output_image = 'output/wordcloud.png'
    generate_wordcloud(text)
    assert os.path.exists(output_image)