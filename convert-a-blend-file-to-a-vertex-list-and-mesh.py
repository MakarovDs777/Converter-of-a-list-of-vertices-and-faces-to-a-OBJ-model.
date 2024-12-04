import os
import matplotlib.pyplot as plt
import numpy as np

def create_obj_file(vertex, edges, filename):
    """
    Создает OBJ-файл из заданных вершин и граней.

    :param vertex: Массив вершин в формате [(x, y, z),...]
    :param edges: Массив граней в формате [(v1, v2, v3),...], где v1, v2, v3 - индексы вершин
    :param filename: Имя файла OBJ
    """
    with open(filename, 'w') as f:
        # Записать вершины
        for i, v in enumerate(vertex):
            f.write(f"v {v[0]} {v[1]} {v[2]}\n")

        # Записать грани
        for edge in edges:
            f.write(f"f {edge[0] + 1} {edge[1] + 1} {edge[2] + 1}\n")

# Пример использования
vertex = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
edges = [(0, 1, 2), (0, 2, 3)]

# Сохранение модели в OBJ файл
desktop_path = os.path.expanduser("~")
filename = os.path.join(desktop_path, "Desktop", "cube_with_corridor_and_room.obj")
create_obj_file(vertex, edges, filename)
print(f"Model saved as {filename}")

# Визуализация
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(np.array(vertex)[:, 0], np.array(vertex)[:, 1], np.array(vertex)[:, 2], color='r', alpha=0.5)
for edge in edges:
    ax.plot3D(*zip(vertex[edge[0]], vertex[edge[1]], vertex[edge[2]]), c='b')
plt.show()
