from http import HTTPStatus
import sys
from stream import Stream

def test_tweet_request(client):
    data = {
        "status": "Mock status"
    }
    url = "/tweet"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_tweet_request_fail(client):
    data = {
        "status": ""
    }
    url = "/tweet"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_retweet_request(client):
    data = {
        "tweet": "1158649787366821888"        
    }
    url = "/retweet"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_retweet_request_fail(client):
    data = {
        "id": ""        
    }
    url = "/retweet"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_follow_user_id_request(client):
    data = {
        "id": "1156862303859429377"
    }
    url = "/follow"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_follow_screen_name_request(client):
    data = {
        "handle": "bhutkar_omkar",
    }
    url = "/follow"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_follow_request_fail(client):
    data = {}
    url = "/follow"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_unfollow_id_request(client):
    data = {
        "id": "1156862303859429377"
    }
    url = "/unfollow"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_unfollow_screen_name_request(client):
    data = {
        "screen_name": "bhutkar_omkar",
    }
    url = "/unfollow"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_unfollow_request_fail(client):
    data = {}
    url = "/unfollow"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_followers_id_request(client):
    data = {
        "user": "1156862303859429377",
    }
    url = "/followers"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_followers_screen_name_request(client):
    data = {
        "screen_name": "bhutkar_omkar",
    }
    url = "/followers"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_followers_request_fail(client):
    data = {}
    url = "/followers"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_subscribe_request(client):
    data = {
        "data":{
            "track":"Article370",
            "isTesting":True
            },
        "id":"307d6a9a-60da-4915-9ee5-bae3c0238874",
        "endpoint":"https://webhook.site/#!/832c4ebb-8b80-4330-bbfb-337aea98a579"
    }
    url = "/stream/subscribe"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_subscribe_request_fail(client):
    data = {
        "data":{
            "isTesting":True
        },
        "id":"307d6a9a-60da-4915-9ee5-bae3c023887f",
        "endpoint":"https://webhook.site/#!/832c4ebb-8b80-4330-bbfb-337aea98a579"
    }
    url = "/stream/subscribe"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST 