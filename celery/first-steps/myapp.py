from tasks import add, divide

r= add.delay(10, 30)
print(r.get())
# add.apply_async([5,85])

r=divide.delay(20,2)
r.forget()

# r= divide.delay(3,0)
# print(r.get(propagate=False))
# print(r.traceback)

print("Finished")