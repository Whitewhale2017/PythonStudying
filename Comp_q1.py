from __builtin__ import raw_input

i = 0
for q in range(1, 3600 // 130 + 1):
    for d in range(1, 3600 // 104 + 1):
        for j in range(1, 3600 // 78 + 1):
            for l in range(1, 3600 // 170 + 1):
                if (q * 130 + d * 104 + j * 78 + l * 170) == 3600:
                    i += 1
                    print(str(i), "q=" + str(1), "d=" + str(d), "j=" + str(j), "l=" + str(l))
input("Press <enter>")
