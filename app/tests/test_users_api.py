from app.tests.test_api_db import client

def test_create_user():
    response = client.post(
        "/graphql",
        json={
            "query": """
                mutation {
                    createUser(name: "Alice", email: "alice@example.com") {
                        id
                        name
                        email
                    }
                }
            """
        }
    )
    data = response.json()["data"]["createUser"]
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"

def test_get_users():
    response = client.post(
        "/graphql",
        json={ "query": "{ users { id name email } }" }
    )
    users = response.json()["data"]["users"]
    assert isinstance(users, list)
    assert users[0]["email"] == "test@example.com"
