import pytest
from main import get_random_cat_image


def test_get_random_cat_image(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{
        "id": "MTY4OTk4OQ",
        "url": "https://cdn2.thecatapi.com/images/MTY4OTk4OQ.jpg", "width": 640, "height": 426
    }]
    assert get_random_cat_image() == "https://cdn2.thecatapi.com/images/MTY4OTk4OQ.jpg"


def test_get_random_cat_image_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404
    assert get_random_cat_image() is None



# [{"id":"MTY4OTk4OQ","url":"https://cdn2.thecatapi.com/images/MTY4OTk4OQ.jpg","width":640,"height":426}]



