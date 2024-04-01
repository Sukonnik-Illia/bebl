def test_comments(client, frozen_time):
    test_post = {"title": "Hello", "content": "World"}

    response = client.post("/posts", json=test_post)
    assert response.status_code == 201
    post = response.get_json()

    url = f"/posts/{post['uuid']}/comments"

    # check empty comments
    response = client.get(url)
    assert response.status_code == 200
    assert response.get_json() == []

    # create comment
    test_comment = {"content": "Coolest post ever!"}
    response = client.post(url, json=test_comment)
    assert response.status_code == 201
    comment_1 = response.get_json()
    assert comment_1["content"] == test_comment["content"]
    assert comment_1["post_id"] == post["uuid"]
    assert comment_1["created_at"] == frozen_time.time_to_freeze.isoformat()

    # check comments
    response = client.get(url)
    assert response.status_code == 200
    assert response.get_json() == [comment_1]

    # create another comment
    test_comment = {"content": "I agree! That this is boring."}
    response = client.post(url, json=test_comment)
    assert response.status_code == 201
    comment_2 = response.get_json()

    response = client.get(url)
    assert response.status_code == 200
    assert response.get_json() == [comment_1, comment_2]
