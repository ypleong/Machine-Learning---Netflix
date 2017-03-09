import trainModel
import numpy as np

data = np.genfromtxt('data.txt')

M = np.amax(data[:,0]).astype(int)
N = np.amax(data[:,1]).astype(int)
K = 20
eta = 2e-3
reg = 0.01


results = trainModel.train_model(M, N, K, eta, reg, data, eps=0.0001, max_epochs=500)

np.savetxt('U_matrix.csv',results[0],delimiter=',')
np.savetxt('V_matrix.csv',results[1],delimiter=',')
np.savetxt('E_in.csv',[results[2]],delimiter=',')

