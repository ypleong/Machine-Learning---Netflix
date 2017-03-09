import numpy as np
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import matplotlib
from textwrap import wrap


def load_data(moviefile, datafile):
    """
    Load data set

    :param moviefile: path of movie file
    :param datafile: path of data file
    :return: movie data and user data files
    """

    movie_genre = {}
    movie_dict = {}
    with open(moviefile, 'r') as f:
        for line in f.readlines():
            split_lines = line.split('\r')
        for line in split_lines:
            split_line = line.split('\t')
            movie_genre[int(split_line[0])] = [int(item) for item in split_line[2:]]
            movie_dict[int(split_line[0])] = split_line[1]

    user_data = []
    with open(datafile, 'r') as f:
        for line in f.readlines():
            split_lines = line.split('\r')
        for line in split_lines:
            user_data.append([int(item) for item in line.split('\t')])

    return movie_genre, user_data, movie_dict


def most_popular_movie(movie_rating_dict):
    movie_rating_count = {}
    movie_rating_average = {}
    for key, value in movie_ratings_dict.iteritems():
        movie_rating_count[key] = len(value)
        movie_rating_average[key] = np.mean(value)

    d1 = Counter(movie_rating_count)
    d2 = Counter(movie_rating_average)

    return d1.most_common(10), d2.most_common(10)


def create_top10_plot(data, movie_dict, movie_ratings_dict, plot_title):
    fig, ax = plt.subplots(2, 5, sharey=True)
    width = 1.0
    fig.subplots_adjust(hspace=0.5)

    for ind, (movie, _) in enumerate(data):
        a = Counter(movie_ratings_dict[movie])
        x = range(5)
        height = [a[item] for item in range(1, 6)]

        if ind < 5:
            axx = ax[0, ind]
        else:
            axx = ax[1, ind - 5]

        axx.bar(x, height, width)
        axx.set_title("\n".join(wrap(movie_dict[movie], 18)), fontsize=10)
        axx.set_xticks([i + width / 2 for i in x])
        axx.set_xticklabels([item + 1 for item in x])

    matplotlib.rcParams.update({'font.size': 10})
    plt.savefig(plot_title)


movie_genre, user_data, movie_dict = load_data('../project3data/movies.txt', '../project3data/data.txt')

user_data = np.array(user_data)

movie_ratings_dict = defaultdict(list)
for key, rating in user_data[:, 1:]:
    movie_ratings_dict[key].append(rating)

most_popular_movies_10, best_movies_10 = most_popular_movie(movie_ratings_dict)

create_top10_plot(most_popular_movies_10, movie_dict, movie_ratings_dict, '../output/top_10_popular_movie.pdf')
create_top10_plot(best_movies_10, movie_dict, movie_ratings_dict, '../output/top_10_best_movie.pdf')
