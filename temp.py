import numpy as np

filename = "Marschner41.raw"

dim_x, dim_y, dim_z = 41, 41, 41
v=dim_x*dim_y*dim_z
e =0
A = np.fromfile(filename, dtype='uint8', sep="")
print(len(A))
A = A.reshape((dim_x, dim_y, dim_z))
c=int(input("Enter the c value: "))
a=0
for i in range(0,dim_x):
    for j in range(0,dim_y):
        for k in range(0,dim_z):
            if(A[i][j][k]<=c):
                a+=1
                if(i+1 < dim_x):
                    if(A[i+1][j][k]<=c):
                        e+=1
                        #x=i+j*dim_x+k*dim_x*dim_y+1
                        #y=(i+1)+j*dim_x+k*dim_x*dim_y+1
                        #t=(x-1)*v+y-((x)*(x+1)/2)
                        #arr[x-1][t]=-1
                        #arr[y-1][t]=1

                if(j+1 < dim_y):
                    if(A[i][j+1][k]<=c):
                        e+=1
                        #x=i+(j)*dim_x+k*dim_x*dim_y+1
                        #y=(i)+(j+1)*dim_x+k*dim_x*dim_y+1
                        #t=(x-1)*v+y-((]

                        #arr[x-1][t]=-1
                        #rr[y-1][t]=1
                if(k+1<dim_z):
                    if(A[i][j][k+1]<=c):
                        e+=1
                        #x=i+(j)*dim_x+k*dim_x*dim_y+1
                        #y=(i)+(j)*dim_x+(k+1)*dim_x*dim_y+1
                        #t=(x-1)*v+y-((x)*(x+1)/2)
                        #arr[x-1][t]=-1
                        #arr[y-1][t]=1
print(a)
print(e)

t=0
k=0
arr=[ [0] * int(e) for i in range(int(v))]
#print(len(arr))
for i in range(0,dim_x):
    for j in range(0,dim_y):
        for k in range(0,dim_z):
            if(A[i][j][k]<=c):
                if(i+1 < dim_x):
                    if(A[i+1][j][k]<=c):
                        #e+=1
                        x=i+j*dim_x+k*dim_x*dim_y
                        y=(i+1)+j*dim_x+k*dim_x*dim_y
                        arr[x][t]=-1
                        arr[y][t]=1
                        t+=1
                        #if(k==0):
                            #print(x)
                            #print(y)
                            #k+=1

                if(j+1 < dim_y):
                    if(A[i][j+1][k]<=c):
                        #e+=1
                        x=i+(j)*dim_x+k*dim_x*dim_y
                        y=(i)+(j+1)*dim_x+k*dim_x*dim_y
                        arr[x][t]=-1
                        arr[y][t]=1
                        t+=1
                if(k+1<dim_z):
                    if(A[i][j][k+1]<=c):
                        #e+=1
                        x=i+(j)*dim_x+k*dim_x*dim_y
                        y=(i)+(j)*dim_x+(k+1)*dim_x*dim_y
                        arr[x][t]=-1
                        arr[y][t]=1
                        t+=1
for i in range(0,v):
    if(arr[i][1]==-1):
        print("hello")
    if(arr[i][1]==1):
        print("bye")

rank=np.linalg.matrix_rank(arr)
print("Rank: " + str(rank))
betti_0 = a - rank

print("==========")
print('| \N{GREEK SMALL LETTER BETA}\N{SUBSCRIPT ZERO} =',betti_0,'|')
print("==========")















