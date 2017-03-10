import basic_visualization
import matplotlib.pyplot as plt
import numpy as np
import random
from textwrap import wrap

#Load in movie data and projection of V
movie_genre, user_data, movie_dict = basic_visualization.load_data('../project3data/movies.txt', '../project3data/data.txt')
V_proj = np.loadtxt('V_Proj.csv',delimiter=',')
N = V_proj.shape[1]

#Initialize variables
M = 10
rand_movies = np.empty([M,2])
movie_names = []
movie_index = np.empty(M)

#Pick 10 random movies, and find their location on the V Projection
for i in range(M):
    index = random.randint(0,N-1)
    rand_movies[i,:] =  V_proj[:,index]
    movie_index[i] = index
    #movie_names[i] = movie_dict.get(index)
    movie_names.append(movie_dict.get(index))
print(movie_names)

plt.scatter(rand_movies[:,0], rand_movies[:,1],s=20)
for label, x, y in zip(movie_names,rand_movies[:,0],rand_movies[:,1]):
    plt.annotate("\n".join(wrap(label, 18)), xy=(x,y), xytext=(0,0), textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5',alpha=0.5),
                 ha='right',va='bottom')#,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0'))

plt.title('Ten Random Movies Projected on Two Principal Components')
plt.show()
