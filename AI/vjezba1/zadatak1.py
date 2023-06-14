solutions = 0

for x in range(-100, 100):
    for y in range(-100, 100):
        for z in range(-100, 100):
            if x + y == 0 or z + x == 0 or z + y == 0:
                pass
            elif ((z / (x + y)) + (y / (z + x)) + (x / (z + y))) == 4:
                solutions += 1
                
                print("x: ", x, "y: ", y, "z: ", z)

print("Broj rjesenja je: ", solutions)
                
                