import basic_visualization
import matplotlib.pyplot as plt
import numpy as np
import random

#Load in movie data and projection of V
movie_genre, user_data, movie_dict = basic_visualization.load_data('../project3data/movies.txt', '../project3data/data.txt')
V_proj = np.loadtxt('V_Proj.csv',delimiter=',')
N = V_proj.shape[1]

#Initialize variables
M = 10
movies_horror = basic_visualization.get_movies_from_genre(movie_genre,11)
horror_position = np.empty([M,2])
horror_names = []
movies_children = basic_visualization.get_movies_from_genre(movie_genre,4)
children_position = np.empty([M,2])
children_names = []
movies_doc = basic_visualization.get_movies_from_genre(movie_genre,9)
doc_position = np.empty([M,2])
doc_names = []

h_sample = random.sample(range(len(movies_horror)),M)
c_sample = random.sample(range(len(movies_children)),M)
d_sample = random.sample(range(len(movies_doc)),M)

#Pick top 10 movies from each genre, and find their location on the V Projection
for i in range(M):
    index_h = movies_horror[h_sample[i]]
    index_c = movies_children[c_sample[i]]
    index_d = movies_doc[d_sample[i]]
    horror_position[i] = V_proj[:,movies_horror[i]]
    children_position[i] = V_proj[:,movies_children[i]]
    doc_position[i] = V_proj[:,movies_doc[i]]
    horror_names.append(movie_dict.get(index_h))
    children_names.append(movie_dict.get(index_c))
    doc_names.append(movie_dict.get(index_d))

plt.scatter(horror_position[:,0], horror_position[:,1],s=20)
for label, x, y in zip(horror_names,horror_position[:,0],horror_position[:,1]):
    plt.annotate(label, xy=(x,y), xytext=(0,0), textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5',fc='green',alpha=0.5),
                 ha='right',va='bottom')#,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0'))

plt.scatter(children_position[:,0], children_position[:,1],s=20)
for label, x, y in zip(children_names,children_position[:,0],children_position[:,1]):
    plt.annotate(label, xy=(x,y), xytext=(0,0), textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5',fc='yellow',alpha=0.5),
                 ha='right',va='bottom')#,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0'))

plt.scatter(doc_position[:,0], doc_position[:,1],s=20)
for label, x, y in zip(doc_names,doc_position[:,0],doc_position[:,1]):
    plt.annotate(label, xy=(x,y), xytext=(0,0), textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5',fc='blue',alpha=0.5),
                 ha='right',va='bottom')#,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0'))    

plt.show()
