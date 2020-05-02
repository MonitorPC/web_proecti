from requests import post, delete

print(post('http://127.0.0.1:5000/api/jobs').json())
print(post('http://127.0.0.1:5000/api/jobs',
           json={'title': 'Заголовок'}).json())
print(post('http://127.0.0.1:5000/api/jobs', json={
    'id': 4,
    'team_leader': 3,
    'job': 'РАБОТА РАБОТА НИЧЕГО КРОМЕ РАБОТЫ',
    'work_size': 3,
    'collaborators': '1, 2',
    'is_finished': True}).json())
