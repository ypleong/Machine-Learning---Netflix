import numpy as np

#Read in U and V
U = np.genfromtxt('U_matrix.csv',delimiter=',')
V = np.genfromtxt('V_matrix.csv',delimiter=',')


#Mean center V & shift U
for i in range(V.shape[0]):
    mean = np.mean(V[i,:])
    for j in range(V.shape[1]):
        V[i,j] = V[i,j] - mean
    for j in range(U.shape[0]):
        U[j,i] = U[j,i] - mean

#Calculate SVD of V
(Av, Sv, Bv) = np.linalg.svd(V)

V_proj = np.dot(np.transpose(Av[:,0:2]),V)
U_proj = np.dot(np.transpose(Av[:,0:2]),np.transpose(U))

#Rescale each dimension of U & V to have unit variance
for i in range(2):
    var = np.var(V_proj[i,:])
    for j in range(V_proj.shape[1]):
        V_proj[i,j] = V_proj[i,j]/np.sqrt(var)
    var = np.var(U_proj[i,:])
    for j in range(U_proj.shape[1]):
        U_proj[i,j] = U_proj[i,j]/np.sqrt(var)

np.savetxt('U_Proj.csv',U_proj,delimiter=',')
np.savetxt('V_Proj.csv',V_proj,delimiter=',')

