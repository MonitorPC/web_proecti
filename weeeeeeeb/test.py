a = {"id": 3, "title": "wyhrjhtfgjgvdas", "picture_path": "static/upload_files/1/3.jpg", "average_mark": 0,
     "users_set_mark": "1;", "user_id": 1}

import requests

print(requests.post('http://127.0.0.1:5000/api/picture', json={
    'id': 3,
    'title': 'fasdf',
    'user_id': 1,
    'picture_path': f'static/upload_files/1/3.jpg',
    'average_mark': 0,
    'users_set_mark': ''
}).json())
