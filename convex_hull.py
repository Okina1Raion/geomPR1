import sys
import math
from tkinter import *


def convex_hull_trick(a, c):
    st = list({-1 * sys.maxsize, -1 * sys.maxsize}) * len(a)
    from_ = list({sys.maxsize, sys.maxsize}) * len(a)
    B = list({-1 * sys.maxsize, -1 * sys.maxsize}) * len(a)
    B[0] = 0
    st[0] = 0
    from_[0] = -1 * sys.maxsize
    sz = 0
    pos = 0
    for i in range(1, len(a)):
        while from_[pos] < a[i]:
            pos = pos + 1
        j = st[pos - 1]
        B[i] = (c[j] * a[i] + B[j])
        print(B[i], a[i], c[i])
        if i < len(a):
            while True:
                j = st[sz]
                x = divide(B[j] - B[i], c[i] - c[j])
                if x > from_[sz]:
                    break
                sz -= 1
            st[sz + 1] = i
            from_[sz + 1] = x
            sz += 1
    return B[len(a) - 1]


def divide(a, b):
    delta = 0
    if a % b != 0:
        delta = 1
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        return a / b + delta
    return -1 * (math.fabs(a) / math.fabs(b))


convex_hull_trick(list((1, 2, 3, 4, 5)), list((5, 4, 3, 2, 1)))
# canvas.pack(fill=BOTH, expand=1)
# # root.geometry("400x250+300+300")
# root.mainloop()
# # root = Tk()
# # btn = Button(root,  # родительское окно
# #              text="Click me",  # надпись на кнопке
# #              width=30, height=5,  # ширина и высота
# #              bg="white", fg="black")  # цвет фона и надписи
# # btn.bind("<Button-1>", hello)  # при нажатии ЛКМ на кнопку вызывается функция Hello
# # btn.pack()  # расположить кнопку на главном окне
# root.mainloop()
