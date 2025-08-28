#!/usr/bin/env -S python3 -B

from time import time
from polyedr.common.tk_drawer import TkDrawer
from noshadow.polyedr import Polyedr


tk = TkDrawer()
try:
    for name in ["ccc", "cube", "test_polyedr", "box", "king", "cow"]:

        if name == "test_polyedr":
            print("=============================================================")
            print(f"Начало работы с полиэдром '{name}'")
            start_time = time()
            Polyedr(f"data/{name}.geom").draw(tk)
            delta_time = time() - start_time
            print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
            print('Площадь есть одна грань и примерно равна 7.79')
            print(f"Площадь граней не содержащих хороших точек = {Polyedr(f"data/{name}.geom").bad_area()}")
            input("Hit 'Return' to continue -> ")
            print('')
        else:
            print("=============================================================")
            print(f"Начало работы с полиэдром '{name}'")
            start_time = time()
            Polyedr(f"data/{name}.geom").draw(tk)
            delta_time = time() - start_time
            print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
            print(f"Площадь граней не содержащих хороших точек = {Polyedr(f"data/{name}.geom").bad_area()}")
            input("Hit 'Return' to continue -> ")
            print('')
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
