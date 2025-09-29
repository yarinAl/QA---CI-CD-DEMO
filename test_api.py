import requests

API_URL = "https://sandbox.meshulam.co.il/api/light/server/1.0/createPaymentProcess"


def test_payment_valid():
    data = {
        "pageCode": "e19e0b687744",
        "userId": "52e95954cd5c1311",
        "sum": 100,
        "paymentNum": 1,
        "description": "ORDER123",
        "pageField[fullName]": "Full Name",
        "pageField[phone]": "0534738605",
        "pageField[email]": "debbie@meshulam.co.il"
    }
    response = requests.post(API_URL, data=data)
    assert response.status_code == 200, "Invalid status code"
    response_json = response.json()
    assert "data" in response_json
    assert "url" in response_json["data"]
    print("Valid payment request - Passed")


def test_payment_missing_field():
    data = {
        "pageCode": "e19e0b687744",
        "sum": 100,
        "paymentNum": 1,
        "description": "ORDER123",
        "pageField[fullName]": "Full Name",
        "pageField[phone]": "0534738605",
        "pageField[email]": "debbie@meshulam.co.il"
    }
    response = requests.post(API_URL, data=data)
    response_json = response.json()
    assert response.status_code != 200
    assert "userId" in response_json.get("err", "")
    print("Missing required field - Passed")


def test_payment_invalid_sum():
    data = {
        "pageCode": "e19e0b687744",
        "userId": "52e95954cd5c1311",
        "sum": 0,
        "paymentNum": 1,
        "description": "ORDER123",
        "pageField[fullName]": "Full Name",
        "pageField[phone]": "0534738605",
        "pageField[email]": "debbie@meshulam.co.il"
    }
    response = requests.post(API_URL, data=data)
    try:
        response_json = response.json()
        assert "sum" in response_json.get("err", "")
    except ValueError:
        assert response.status_code != 200
    print("Invalid sum value - Passed")


if __name__ == "__main__":
    test_payment_valid()
    test_payment_missing_field()
    test_payment_invalid_sum()
