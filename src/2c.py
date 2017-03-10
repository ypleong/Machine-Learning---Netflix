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
        
    fig = plt.figure()
    ax = fig.add_subplot(111)
    

    nbest = 10
    
    for idx, (movie,ii) in enumerate(best_movies[0:nbest]):
        print idx, movie, ii, movie_dict[movie] #movie_ratings_dict[movie]
        
        ax.text(V_proj[0,movie]*30, V_proj[1,movie]*30,  movie_dict[movie], style='italic',
        bbox={'facecolor':'blue', 'alpha':0.2, 'pad':5})
    
    
    ax.axis([-60,100,-80,100])
    #plt.plot(proj_best_movies[0,:],proj_best_movies[1,:], 'r', linewidth=2)
    plt.savefig('2c.pdf')
    plt.grid()
    plt.show()
    plt.close()
