from unittest.mock import patch, mock_open

from html_pages import HtmlPagesConverter


@patch("builtins.open", new_callable=mock_open,
       read_data="quote: ' ")
def test_convert_quotes(fake_file):
    with HtmlPagesConverter(filename="filename.txt") as converter:
        converted_text = converter.get_html_page(0)
        assert converted_text == "quote: &#x27;<br />"