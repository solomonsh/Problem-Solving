
# time complexity N^2
def counting_triangles(arr):
    for i in range(len(arr)):
        arr[i] = sorted(arr[i])
    
    unique_triangle = []
    for triangle in arr:
        if triangle not in unique_triangle:
            unique_triangle.append(triangle)
    return len(unique_triangle)

# time complexity N
def counting_triangles_optimized(arr):
        unique_sets = set() 
        for triangle in arr:
            unique_sets.add(triangle[0]*triangle[1]*triangle[2])
        return len(unique_sets)

 
# Test Cases 

# print(counting_triangles_optimized([[2,2,3],[3,2,2],[2,5,6]]))
# print(counting_triangles_optimized([[8,4,6],[100,101,102],[84,93,173]]))

# print(counting_triangles_optimized([[5,8,9],[5,9,8],[9,5,8],[9,8,5],[8,9,5]]))
 