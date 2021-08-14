amount_polygons = int(input())

for x in range(amount_polygons):
    data = list(map(int, input().split()))
    no_vertex = data[0]
    vertex_coord = []

    i = 0
    while i < no_vertex:
        temp = (data[2*i + 1], data[2*i + 2])
        vertex_coord.append(temp)
        i += 1

    out = 0

    i = 0
    while i < len(vertex_coord):
        out = out + vertex_coord[i][0]*vertex_coord[(i+1)%len(vertex_coord)][1] - vertex_coord[(i+1)%len(vertex_coord)][0]*vertex_coord[i][1]
        i += 1
    print(out/2)

