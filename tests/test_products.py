import requests


class TestFilterCheck:

    url = "https://qa.trado.co.il/api/product/filter"
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }


    def test_post_filter_from_low_to_high(self):
        response = requests.post(self.url, headers=self.headers)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
