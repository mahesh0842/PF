a=[[1,2],[2,3],[3,4],[4,5]]
b=[[5,6],[6,7],[7,8],[8,9]]
def add_matrices(mat1,mat2):
    result=[]
    for i in range(len(mat1)):
        row=[]
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result
add_matrices(a,b)
print("Matrix addition result:", add_matrices(a, b))