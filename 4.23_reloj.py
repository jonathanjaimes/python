import time
for i in range(0, 24):
	if i < 10:
			i = "0" + str(i) 
	for j in range(0, 60):
		if j < 10:
			j = "0" + str(j)
		for k in range(0, 60):
			if k < 10:
				print(str(i) + ":" + str(j) + ":" + "0" + str(k))
			
			else:
				print(str(i) + ":" + str(j) + ":" + str(k))
			time.sleep(1)


"""
elif j < 10:
				print(str(i) + ":" + "0" + str(j) + ":" + str(k))
			elif k < 10:
				print("0" + str(i) + ":" + str(j) + ":" + str(k))
"""