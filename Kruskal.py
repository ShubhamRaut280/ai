def kruskal(edges, num_vertices):
    edges.sort(key=lambda x: x[2])
    mst = []
    sets = [{i} for i in range(num_vertices)]

    def find_set(vertex):
        for s in sets:
            if vertex in s:
                return s

    for u, v, w in edges:
        u_set = find_set(u)
        v_set = find_set(v)
        if u_set != v_set:
            mst.append([u, v, w])
            sets.remove(u_set)
            sets.remove(v_set)
            sets.append(u_set.union(v_set))

    return mst

def main():
    # Example usage:
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    num_vertices = 4

    print("Edges in the MST:")
    print(kruskal(edges, num_vertices))

if __name__ == "__main__":
    main()
