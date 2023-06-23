def rotate_layers(matrix, r):
    if not matrix or not matrix[0]:
        return matrix

    m, n = len(matrix), len(matrix[0])
    outer_layer_elements = 2 * (m + n) - 4
    rotations = r % outer_layer_elements

    def rotate_outer_layer(layer_matrix, layer_rotations):
        if not layer_matrix or not layer_matrix[0]:
            return layer_matrix

        m, n = len(layer_matrix), len(layer_matrix[0])
        outer_layer_elements = 2 * (m + n) - 4
        layer_rotations %= outer_layer_elements

        outer_layer = []
        for j in range(n):
            outer_layer.append(layer_matrix[0][j])
        for i in range(1, m):
            outer_layer.append(layer_matrix[i][n - 1])
        for j in range(n - 2, -1, -1):
            outer_layer.append(layer_matrix[m - 1][j])
        for i in range(m - 2, 0, -1):
            outer_layer.append(layer_matrix[i][0])

        rotated_outer_layer = outer_layer[-layer_rotations:] + outer_layer[:-layer_rotations]

        idx = 0
        for j in range(n):
            layer_matrix[0][j] = rotated_outer_layer[idx]
            idx += 1
        for i in range(1, m):
            layer_matrix[i][n - 1] = rotated_outer_layer[idx]
            idx += 1
        for j in range(n - 2, -1, -1):
            layer_matrix[m - 1][j] = rotated_outer_layer[idx]
            idx += 1
        for i in range(m - 2, 0, -1):
            layer_matrix[i][0] = rotated_outer_layer[idx]
            idx += 1

        return layer_matrix

    # Rotate the outer layer
    rotated_matrix = rotate_outer_layer(matrix, rotations)

    # Rotate the internal layers
    if m > 2 and n > 2:
        inner_matrix = []
        for i in range(1, m - 1):
            inner_row = matrix[i][1:n-1]
            inner_matrix.append(inner_row)
        inner_rotations = r % (outer_layer_elements - 8)  # Exclude the outer layer elements
        inner_rotated_matrix = rotate_layers(inner_matrix, inner_rotations)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                rotated_matrix[i][j] = inner_rotated_matrix[i - 1][j - 1]

    return rotated_matrix


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
r = 2

rotated = rotate_layers(matrix, r)
print(f'{rotated}')