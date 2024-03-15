import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

vertices = np.array([[+1, +1, +1, +1], [+1, +1, +1, -1],
                     [+1, +1, -1, +1], [+1, +1, -1, -1],
                     [+1, -1, +1, +1], [+1, -1, +1, -1],
                     [+1, -1, -1, +1], [+1, -1, -1, -1],
                     [-1, +1, +1, +1], [-1, +1, +1, -1],
                     [-1, +1, -1, +1], [-1, +1, -1, -1],
                     [-1, -1, +1, +1], [-1, -1, +1, -1],
                     [-1, -1, -1, +1], [-1, -1, -1, -1]])

edges = [(0, 1), (0, 2), (0, 4), (1, 3), (1, 5),
         (2, 3), (2, 6), (3, 7), (4, 5), (4, 6),
         (5, 7), (6, 7), (0, 8), (1, 9), (2, 10),
         (3, 11), (4, 12), (5, 13), (6, 14), (7, 15),
         (8, 9), (8, 10), (8, 12), (9, 11), (9, 13),
         (10, 11), (10, 14), (11, 15), (12, 13), (12, 14),
         (13, 15), (14, 15)]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

def animate(frame):
    ax.cla()
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    theta = np.radians(frame)
    cos, sin = np.cos(theta), np.sin(theta)
    rotation_matrix = np.array([[cos, -sin, 0, 0],
                                [sin, cos, 0, 0],
                                [0, 0, cos, -sin],
                                [0, 0, sin, cos]])

    rotated_vertices = np.dot(vertices, rotation_matrix)
    vertices_3d = rotated_vertices[:, :3]

    for edge in edges:
        points = np.array([vertices_3d[edge[0]], vertices_3d[edge[1]]])
        ax.plot3D(points[:, 0], points[:, 1], points[:, 2], 'blue')
