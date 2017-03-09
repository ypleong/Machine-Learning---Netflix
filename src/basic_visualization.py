

def load_data(moviefile, datafile):
    """
    Load dataset

    :param moviefile: path of movie file
    :param datafile: path of data file
    :return: movie data and user data files
    """

    movie_genre = {}
    with open(moviefile, 'r') as f:
        for line in f:
            split_line = line.split(' ')
            movie_genre[split_line[0]] = split_line[2:]

    user_data = []
    with open(datafile, 'r') as f:
        for line in f:
            user_data.append(line.split(' '))

    return movie_genre, user_data


movie_genre, user_data = load_data('./project3data/movies.txt', './project3data/data.txt')
