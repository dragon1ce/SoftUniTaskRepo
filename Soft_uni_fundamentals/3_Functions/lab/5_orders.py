mydick = {"coffee": 1.5, "water": 1.00, "coke": 1.4, "snacks": 2.0}
type = input()
quant = int(input())
def calc(t,q):
    price = mydick[t]
    return  f"{price * q:.2f}"
print(calc(type,quant))