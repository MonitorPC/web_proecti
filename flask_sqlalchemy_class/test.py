from requests import get, post

print(post('http://localhost:5000/api/jobs', json={
    'id': 1,
    'team_leader': 3,
    'job': 'РАБОТА РАБОТА НИЧЕГО КРОМЕ РАБОТЫ',
    'work_size': 3,
    'collaborators': '1, 2',
    'is_finished': True}).json())
