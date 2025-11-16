import numpy as np

def extract_surface_lines_np(brep_str):
    lines = brep_str.strip().split('\n')
    surface_stop = 0
    surface_line = 0

    for i, line in enumerate(lines):
        if line.startswith('Surfaces'):
            surface_line = i
        if line.startswith('Triangulations'):
            surface_stop = i
            break

    surfaces = []

    for i in range(surface_line + 1, surface_stop):
        line = lines[i].strip().split(' ')
        # remove leading integer that indicates surface type
        if len(line) > 1:
            surfaces.append(line[1:])
        else:
            surfaces.append(line)

    surfaces_flat = []
    for i in surfaces:
        for j in i:
            if j != '':
                surfaces_flat.append(float(j))

    return np.array(surfaces_flat, dtype=np.float32)