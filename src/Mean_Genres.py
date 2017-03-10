import basic_visualization
import matplotlib.pyplot as plt
import matplotlib.lines as pltLines
import numpy as np
import random

#Load in movie data and projection of V
movie_genre, user_data, movie_dict = basic_visualization.load_data('../project3data/movies.txt', '../project3data/data.txt')
V_proj = np.loadtxt('V_Proj.csv',delimiter=',')
N = V_proj.shape[1]

#Initialize variables
mean_x = np.empty(19)
mean_y = np.empty(19)
var_x = np.empty(19)
var_y = np.empty(19)

#Pick top 10 movies from each genre, and find their location on the V Projection
for genre in range(19):
    movies = basic_visualization.get_movies_from_genre(movie_genre,genre)
    movie_position = np.empty([len(movies),2])
    for i in range(len(movies)):
        movie_position[i,:] = V_proj[:,movies[i]-1]
        
    mean_x[genre] = np.mean(movie_position[:,0])
    mean_y[genre] = np.mean(movie_position[:,1])
    var_x[genre] = np.var(movie_position[:,0])
    var_y[genre] = np.var(movie_position[:,1])
    
genres = ['Unknown','Action','Adventure','Animation','Childrens','Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western']
plt.scatter(mean_x, mean_y, s=100)
for label, x, y, i in zip(genres,mean_x,mean_y,range(19)):
    plt.annotate(label, xy=(x,y), xytext=(0,0), textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5',alpha=0.5),ha='right',va='bottom')#,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0'))
    x1 = np.linspace(x-var_x[i],x+var_x[i],50)
    y1 = y*np.ones(len(x1))
    #plt.plot(x1,y1,'k')
    y2 = np.linspace(y-var_y[i],y+var_y[i],50)
    x2 = x*np.ones(len(y2))
    #plt.plot(x2,y2,'k')
plt.show()
