from fastapi.testclient import TestClient

from app.create_app import create_app


def test_public_and_customer_and_private() -> None:
    client = TestClient(create_app())

    public_response = client.get("/v1/public")
    assert public_response.status_code == 200

    customer_response = client.get("/v1/customer")
    assert customer_response.status_code == 200
    assert isinstance(customer_response.json(), list)

    login_response = client.get("/v1/auth/login")
    assert login_response.status_code == 200
    auth_header = login_response.headers.get("Authorization")
    assert auth_header is not None

    private_response = client.get(
        "/v1/private",
        headers={"Authorization": auth_header},
    )
    assert private_response.status_code == 200
