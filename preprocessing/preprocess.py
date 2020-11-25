"""
Script for preprocessing graph and solution matrix into correct format
2020.11.25 - Dongju Kim
"""

import numpy as np

incheon_drone = {
    'drone': ['Incheon_matrix_drone.csv', 'Incheon_matrix_drone_required.csv'],
    'truck': ['Incheon_matrix.csv', 'Incheon_matrix_required.csv']}

for vehicle_type, csv_list in incheon_drone.items():
    graph     = np.loadtxt(csv_list[0], delimiter=',', dtype=np.float32)
    solution  = np.loadtxt(csv_list[1], delimiter=',', dtype=np.float32)

    np.fill_diagonal(graph, -1)
    solution  = np.array(solution != 0).astype(int)

    graph     = np.savetxt(csv_list[0].split('.')[0] + '_v2.csv', graph, delimiter=',')
    solution  = np.savetxt(csv_list[1].split('.')[1] + '_v2.csv', solution, delimiter=',')
