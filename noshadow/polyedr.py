from math import pi
from common.r3 import R3
from common.tk_drawer import TkDrawer


class Edge:
    """ Ребро полиэдра """
    # Параметры конструктора: начало и конец ребра (точки в R3)

    def __init__(self, beg, fin):
        self.beg, self.fin = beg, fin


class Facet:
    """ Грань полиэдра """
    # Параметры конструктора: список вершин

    def __init__(self, vertexes):
        self.vertexes = vertexes


class Polyedr:
    """ Полиэдр """
    # Параметры конструктора: файл, задающий полиэдр
    def __init__(self, file):

        # списки вершин, рёбер и граней полиэдра
        self.vertexes, self.edges, self.facets = [], [], []
        self.good_vertexes = []
        self.good_facet = []
        self.area = 0

        # список строк файла
        with open(file) as f:
            for i, line in enumerate(f):
                if i == 0:
                    # обрабатываем первую строку; buf - вспомогательный массив
                    buf = line.split()
                    # коэффициент гомотетии
                    c = float(buf.pop(0))
                    # углы Эйлера, определяющие вращение
                    alpha, beta, gamma = (float(x) * pi / 180.0 for x in buf)
                elif i == 1:
                    # во второй строке число вершин, граней и рёбер полиэдра
                    nv, nf, ne = (int(x) for x in line.split())
                elif i < nv + 2:
                    # задание всех вершин полиэдра
                    x, y, z = (float(x) for x in line.split())
                    self.vertexes.append(R3(x, y, z).rz(
                        alpha).ry(beta).rz(gamma) * c)
                    if R3.is_good(R3(x, y, z).rz(
                            alpha).ry(beta).rz(gamma) * c):
                        self.good_vertexes.append(R3.is_good(R3(x, y, z).rz(
                            alpha).ry(beta).rz(gamma) * c))

                else:
                    # вспомогательный массив
                    buf = line.split()
                    # количество вершин очередной грани
                    size = int(buf.pop(0))
                    # массив вершин этой грани
                    vertexes = [self.vertexes[int(n) - 1] for n in buf]
                    # задание рёбер грани
                    for n in range(size):
                        self.edges.append(Edge(vertexes[n - 1], vertexes[n]))
                    isgood = 1
                    for i in vertexes:
                        if R3.is_good(i):
                            isgood = 0
                    if isgood == 1:
                        self.good_facet.append(Facet(vertexes))
                    # задание самой грани
                    self.facets.append(Facet(vertexes))

    def facet_area(self, facet):
        if len(facet.vertexes) < 3:
            return 0
        area = 0
        v0 = facet.vertexes[0]
        for i in range(1, len(facet.vertexes) - 1):
            v1 = facet.vertexes[i]
            v2 = facet.vertexes[i + 1]
            a = v1 - v0
            b = v2 - v0
            c = R3.cross(a, b)
            area += abs(c) / 4
        return area

    def bad_area(self):
        for i in self.good_facet:
            self.area += self.facet_area(i)
        return self.area


    # Метод изображения полиэдра
    def draw(self, tk):
        tk.clean()
        for e in self.edges:
            tk.draw_line(e.beg, e.fin)

