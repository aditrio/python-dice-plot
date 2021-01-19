import matplotlib.pyplot as p
import numpy as np
import random


#program menghitung kemungkinan hasil jumlah lemparan 2 dadu



def dice(n):
    rolls = []
    for i in range(n):
        two_dice = np.random.randint(1, 7) + np.random.randint(1, 7)
        rolls.append(two_dice)
    return rolls


n = input("Berapa kali lemparan ? (rekomendasi > 1000) : ")

result = dice(int(n))

p.ylabel('banyaknya angka hasil jumlah yang keluar')
p.xlabel('hasil jumlah 2 dadu')
p.hist(result)

p.show()