from proj.tasks import add, divide, average
from proj.celery import app
from celery import group, chain, chord

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

# result = add.apply_async((14,6), countdown=15)
# print(result.state)
# print(result.get())
# print(result.state)

# func = add.signature((2,18), countdown=10)
# res = func.delay()
# res.forget()

# r = group(add.s(i, i) for i in range(10))().get()
# print(r)

# g = group(add.s(i) for i in range(10))

# print(g(10).get())

# ch = chain(add.s(2, 8) | add.s(2) )
# print(ch().get())

# ch = chain(add.s(8) | divide.s(2) )
# print(ch(4).get())

# ch = chord((add.s(i,i)for i in range(10)), average.s())
# print(ch().get())

result = add.delay(2,4)
print(result.get())

result = divide.delay(12, 2)
print(result.get())

result = average.delay([1,2,3])
print(result.get())
