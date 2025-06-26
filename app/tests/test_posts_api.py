from app.tests.test_api_db import client

def test_get_all_posts():
    response = client.post(
        "/graphql",
        json={ "query": "{ posts { id title content author { id name } } }" }
    )
    posts = response.json()["data"]["posts"]
    assert len(posts) >= 1
    assert posts[0]["title"] == "Initial Post"

def test_get_post_by_id():
    response = client.post(
        "/graphql",
        json={ "query": "{ post(postId: 1) { id title content author { id name } } }" }
    )
    data = response.json()["data"]["post"]
    assert data["id"] == "1"
    assert data["title"] == "Initial Post"

def test_create_post():
    response = client.post(
        "/graphql",
        json={
            "query": """
                mutation {
                    createPost(title: "New Post", content: "Content here", authorId: 1) {
                        id
                        title
                        content
                        author {
                            name
                        }
                    }
                }
            """
        }
    )
    data = response.json()["data"]["createPost"]
    assert data["title"] == "New Post"
    assert data["author"]["name"] == "Test User"

def test_update_post():
    response = client.post(
        "/graphql",
        json={
            "query": """
                mutation {
                    updatePost(postId: 1, title: "Updated Title", content: "Updated") {
                        id
                        title
                        content
                    }
                }
            """
        }
    )
    data = response.json()["data"]["updatePost"]
    assert data["title"] == "Updated Title"
    assert data["content"] == "Updated"

def test_delete_post():
    response = client.post(
        "/graphql",
        json={
            "query": """
                mutation {
                    deletePost(postId: 1)
                }
            """
        }
    )
    assert response.json()["data"]["deletePost"] is True

    # Verify it no longer exists
    response = client.post(
        "/graphql",
        json={ "query": "{ post(postId: 1) { id } }" }
    )
    assert "errors" in response.json()
