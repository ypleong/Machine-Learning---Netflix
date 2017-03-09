import numpy as np


def load_data(moviefile, datafile):
    """
    Load dataset

    :param moviefile: path of movie file
    :param datafile: path of data file
    :return: movie data and user data files
    """

    movie_genre = {}
    with open(moviefile, 'r') as f:
        for line in f.readlines():
            split_lines = line.split('\r')
        for line in split_lines:
            split_line = line.split('\t')
            movie_genre[int(split_line[0])] = [int(item) for item in split_line[2:]]

    user_data = []
    with open(datafile, 'r') as f:
        for line in f.readlines():
            split_lines = line.split('\r')
        for line in split_lines:
            user_data.append([int(item) for item in line.split('\t')])

    return movie_genre, user_data


movie_genre, user_data = load_data('../project3data/movies.txt', '../project3data/data.txt')

user_data = np.array(user_data)
# movie_genre = np.array(movie_genre)

sorted_user_data = np.sort(user_data[:, 1:], axis=0)

print data

