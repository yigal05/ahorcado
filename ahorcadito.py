import random 
palabra=random.choice(["a","b","c"])
pudejugar=1
while pudejugar==1:
	letraaintentar=input("que letra desaeas probar:")
	if letraaintentar ==palabra:
		print("ganaste")
	else:
		print("sigue intentando")