import re
import numpy as np
from settings import RED_TEXT, FORMAT_CLEAR
def vertices_from_obj(file):
    try:
        # Open the .obj file in read mode
        with open(file, 'r') as file:
            # Initialize an empty list to store the coordinates
            vertices = []
            # Loop through each line in the file
            for line in file:
                # Check if the line starts with 'v'
                if line.startswith('v '):
                    # Use regular expressions to extract the coordinates
                    coordinates = re.findall(r'[-]?\d+[.]\d+', line)
                    # Convert the coordinates to float and append to the list
                    vertices.append([float(coordinates[0]), -float(coordinates[1]), float(coordinates[2])])
            return vertices
    except FileNotFoundError:
        print(f"{RED_TEXT}File not found!")
        print(f"Returning cube vertices...{FORMAT_CLEAR}")
        return np.array([
            [-1, -1, -1], [-1, 1, -1], [1, 1, -1], [1, -1, -1],
            [-1, -1, 1], [-1, 1, 1], [1, 1, 1], [1, -1, 1]
        ])


def lines_from_obj(file):
    first = True
    try:
        # Open the .obj file in read mode
        with open(file, 'r') as file:
            # Initialize an empty list to store the coordinates
            lines_obj = []
            # Loop through each line in the file
            for line in file:
                # Check if the line starts with 'f '
                if line.startswith('f '):
                    '''f 1/1/1 2/2/2 10/3/3
                    f 2/2/4 3/4/5 11/5/6
                    f 3/4/7 4/6/8 12/7/9'''
                    coordinates = re.findall(r'[ ]+\d', line)
                    coordinates = [c[1:] for c in coordinates]
                    if first:
                        print(coordinates)
                        first = False
                    lines_obj.append([int(coordinates[0]), int(coordinates[1])])
            return lines_obj
    except FileNotFoundError:
        print(f"{RED_TEXT}File not found!")
        print(f"Returning cube lines...{FORMAT_CLEAR}")
        return np.array([
            [0, 1], [1, 2], [2, 3], [3, 0],
            [4, 5], [5, 6], [6, 7], [7, 4],
            [0, 4], [1, 5], [2, 6], [3, 7]
        ])
        
def faces_from_obj(file):
    first = True
    try:
        # Open the .obj file in read mode
        with open(file, 'r') as file:
            # Initialize an empty list to store the coordinates
            faces_obj = []
            # Loop through each line in the file
            for line in file:
                # Check if the line starts with 'f '
                if line.startswith('f '):
                    '''f 1/1/1 2/2/2 10/3/3
                    f 2/2/4 3/4/5 11/5/6
                    f 3/4/7 4/6/8 12/7/9'''
                    coordinates = line.split()[1:]
                    faces_obj.append(list(map(lambda x: int(x)-1, coordinates)))
                    if first:
                        print(faces_obj)
                        first = False
            return faces_obj
    except FileNotFoundError:
        print(f"{RED_TEXT}File not found!")
        print(f"Returning cube faces...{FORMAT_CLEAR}")
        return np.array([
            [0, 1, 2, 3], 
            [4, 5, 6, 7], 
            [0, 4, 5, 1],
            [1, 5, 6, 2],
            [2, 6, 7, 3],
            [3, 7, 8, 4],
        ])