broker_url = 'redis://localhost:6379'
result_backend = 'mongodb://localhost:27017'

# include = ['proj.tasks']

# task_serializer = 'json'
# result_serializer = 'json'
# accept_content = ['json']
timezone = 'Asia/Tehran'
enable_utc = True

# task_routes = {
    # 'proj.tasks.add' : {'queue':'queue1'},
    # 'proj.tasks.divide' : {'queue':'queue2'},
    # 'proj.tasks.average' : {'queue':'queue3'}
# }