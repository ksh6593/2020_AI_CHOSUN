test_a =3
if test_a == 3:
    print("3")
else:
    print("3이 아님.")

for i in range(0, 10):
    print(i)

temp = 0
while True:
    temp = temp + 1
    print(temp)
    if temp > 40:
        break

    temp = 0
    while temp < 40:
        temp += 1
        print(temp)

# y = f(x)
def add_function(x):
    y = x +3
    return y

print(add_function(3))
