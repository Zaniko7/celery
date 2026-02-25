from proj.tasks import add, divide
from proj.celery import app

# res= app.AsyncResult('33670808-e05c-43c1-8e5a-52d0f5f606c0')
# print(res.successful())

# result = add.delay(5,2)
# print(result.get())

# result = divide.delay(1000,20)
# print(result.get())

# result = add.apply_async((14,6), countdown=15)
# result.forget()

# result = divide.apply_async((999,3), countdown=5)
# print(result.forget())

result = add.apply_async((14,6), countdown=15)
print(result.state)
print(result.get())
print(result.state)
