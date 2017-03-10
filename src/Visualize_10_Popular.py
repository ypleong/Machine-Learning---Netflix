from basic_visualization import load_data, most_popular_movie
import numpy as np
import prob2utils
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import matplotlib
from textwrap import wrap

if __name__ == '__main__':


    # Get 10 best and most popular movies
    movie_genre, user_data, movie_dict = load_data('../project3data/movies.txt', '../project3data/data.txt')

    genre_dict = ['Unknown', 'Action', 'Adventure', 'Animation', 'Childrens',
                  'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
                  'Film-Noir', 'Horror', 'Musical', 'Mystery',
                  'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

    movie_ratings_dict = defaultdict(list)
    for key, rating in user_data[:, 1:]:
        movie_ratings_dict[key].append(rating)

    most_popular_movies, best_movies = most_popular_movie(movie_ratings_dict)
    
    V_proj = np.loadtxt('V_Proj.csv',delimiter=',')
    N = V_proj.shape[1] 
        
    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    

    nbest = 10

    for idx, (movie,ii) in enumerate(most_popular_movies[0:nbest]):
        print idx, movie, ii, movie_dict[movie] #movie_ratings_dict[movie]
        plt.scatter(V_proj[0,movie],V_proj[1,movie])
        #ax.text(V_proj[0,movie], V_proj[1,movie],  movie_dict[movie], style='italic',
        #bbox={'facecolor':'blue', 'alpha':0.2, 'pad':5})
        plt.annotate("\n".join(wrap(movie_dict[movie], 18)), xy=(V_proj[0,movie],V_proj[1,movie]), xytext=(0,0), textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5',alpha=0.5),
                     ha='right',va='bottom')#,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0'))                  
    plt.axis([-3,3,-3,3])
    plt.title('Most Popular Ten Movies Projected along 2 Principal Components')
    
    #plt.plot(proj_best_movies[0,:],proj_best_movies[1,:], 'r', linewidth=2)
    #plt.savefig('2c.pdf')
    plt.show()
    
