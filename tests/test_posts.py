def test_creating_and_retrieving_posts(client, frozen_time):
    url = "/posts"
    test_post = {"title": "Hello", "content": "World"}
    response = client.get(url)
    assert response.status_code == 200
    assert response.get_json() == []
    # Create
    response = client.post(url, json=test_post)
    assert response.status_code == 201
    post = response.get_json()
    assert {k: v for k, v in post.items() if k in test_post} == test_post
    assert post["created_at"] == frozen_time.time_to_freeze.isoformat()
    # Read
    response = client.get(f"{url}/{post['uuid']}")
    assert response.status_code == 200
    individual_post = response.get_json()
    assert individual_post == post
