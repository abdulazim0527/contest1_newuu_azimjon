def kwargsAcceptFun(**event3):
        if not event3:
            print("Malumot kiritilmagan")
        else:
            print("Qabul qilingan parameterlar:")
            for a1, b1 in event3.items():
                print(f"{a1}: {b1}") 

#e.g.
kwargsAcceptFun(ism0="Humoyun", yosh1=35, joy3="Uchtepa")
kwargsAcceptFun()
