from task1 import kwargsAcceptFun

kwargsAcceptFun(ism0="Humoyun", yosh1=35, joy3="Uchtepa")
kwargsAcceptFun()

from task2 import typeBasedTransformer
information = {
    'a': 13,
    'b': 4.5,
    'c': "Sekin",
    'd': False,
    'e': [6, 4, 3],
    'f': {"hw": 5, "ts": 6},
    'g': None,
    'h': (2, 8, 10)
}

output1 = typeBasedTransformer(information)
print(output1)
from task3 import func,funx
if __name__ == "__main__":
    func()
    funx()
    func()
    funx()
    func()
