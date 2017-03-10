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

    user_data = np.genfromtxt(datafile)

    return movie_genre, user_data, movie_dict


def most_popular_movie(movie_ratings_dict):
    movie_rating_count = {}
    movie_rating_average = {}
    for key, value in movie_ratings_dict.iteritems():
        movie_rating_count[key] = len(value)
        movie_rating_average[key] = np.mean(value)

    d1 = Counter(movie_rating_count)
    d2 = Counter(movie_rating_average)

    return d1.most_common(), d2.most_common()


def get_movies_from_genre(movie_genre, genre):
    movie_list = []
    for key, value in movie_genre.iteritems():
        if value[genre] == 1:
            movie_list.append(key)

    return movie_list


def create_all_ratings_in_dataset(movie_ratings_dict, plot_title, movie_list=None,
                                  genre_title='All Movies Average Ratings'):
    fig, axx = plt.subplots()

    all_ratings = []
    for item, ratings in movie_ratings_dict.iteritems():
        if movie_list is None:
            all_ratings.append(np.mean(ratings))
        else:
            if item in movie_list:
                all_ratings.append(np.mean(ratings))

    axx.set_title(genre_title)
    axx.hist(all_ratings, bins=[item/2. for item in range(2, 11)])
    plt.xlabel('Average ratings')
    plt.ylabel('Frequency')
    plt.savefig(plot_title)
    plt.close()


def create_top10_plot(data, movie_dict, movie_ratings_dict, plot_title, save_location):
    fig, ax = plt.subplots(2, 5, sharey=True)
    width = 1.0
    fig.subplots_adjust(hspace=0.5, top=0.85)

    for ind, (movie, _) in enumerate(data):
        a = Counter(movie_ratings_dict[movie])
        x = range(5)
        height = [a[item] for item in range(1, 6)]

        if ind < 5:
            axx = ax[0, ind]
        else:
            axx = ax[1, ind - 5]
            axx.set_xlabel('Ratings')

        axx.bar(x, height, width)
        axx.set_title("\n".join(wrap(movie_dict[movie], 18)), fontsize=10)
        axx.set_xticks([i + width / 2 for i in x])
        axx.set_xticklabels([item + 1 for item in x])

        if ind % 5 == 0:
            axx.set_ylabel('Frequency')

    matplotlib.rcParams.update({'font.size': 10})
    plt.suptitle(plot_title, fontsize=16)
    plt.savefig(save_location)
    plt.close()


def create_plots_per_genre(movie_list, movie_dict, movie_ratings_dict, plot_title):
    nn = len(movie_list)
    fig, ax = plt.subplots(int(np.ceil(float(nn)/5)), 5, sharey=True)
    width = 1.0
    fig.subplots_adjust(hspace=0.5)
    count = 0

    for ind, movie in enumerate(movie_list):
        a = Counter(movie_ratings_dict[movie])
        x = range(5)
        height = [a[item] for item in range(1, 6)]

        if ind > 0 and ind % 5 == 0:
            count += 1

        if nn < 5:
            axx = ax[ind]
        else:
            axx = ax[count, ind-5*count]

        axx.bar(x, height, width)
        axx.set_title("\n".join(wrap(movie_dict[movie], 18)), fontsize=10)
        axx.set_xticks([i + width / 2 for i in x])
        axx.set_xticklabels([item + 1 for item in x])

    matplotlib.rcParams.update({'font.size': 10})
    plt.savefig(plot_title)
    plt.close()


movie_genre, user_data, movie_dict = load_data('../project3data/movies.txt', '../project3data/data.txt')

genre_dict = ['Unknown', 'Action', 'Adventure', 'Animation', 'Childrens',
              'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
              'Film-Noir', 'Horror', 'Musical', 'Mystery',
              'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

movie_ratings_dict = defaultdict(list)
for key, rating in user_data[:, 1:]:
    movie_ratings_dict[key].append(rating)

most_popular_movies, best_movies = most_popular_movie(movie_ratings_dict)

for i in range(len(movie_genre[1])):
    movie_genre_one = get_movies_from_genre(movie_genre, i)
    # create_plots_per_genre(movie_genre_1, movie_dict, movie_ratings_dict, '../output/movie_genre_0.pdf')
    create_all_ratings_in_dataset(movie_ratings_dict,
                                  '../output/movie_genre_' + str(i) + '.pdf',
                                  movie_list=movie_genre_one, genre_title=genre_dict[i])

create_all_ratings_in_dataset(movie_ratings_dict, '../output/all_movie_ratings.pdf')
create_top10_plot(most_popular_movies[0:10], movie_dict, movie_ratings_dict,
                  'Top 10 Most Popular Movies', '../output/top_10_popular_movie.pdf')
create_top10_plot(best_movies[0:10], movie_dict, movie_ratings_dict,
                  'Top 10 Best Movies', '../output/top_10_best_movie.pdf')


best_movies = np.array([[item[0], item[1]] for item in best_movies])
most_popular_movies = np.array([[item[0], item[1]] for item in most_popular_movies])

fig, ax1 = plt.subplots()
ax1.stem(most_popular_movies[best_movies[:, 0].astype(int)-1, 1], markerfmt=' ')
ax1.set_ylabel('Total number of ratings')
ax2 = ax1.twinx()
ax2.plot(best_movies[:, 1], 'r', linewidth=2)
ax2.set_ylabel('Average ratings')
ax1.set_xlabel('Movie Sorted By Total Number of Ratings')
plt.xlim([0, len(best_movies[:, 0])])
plt.title('All MovieLens Dataset')
plt.savefig('../output/sorted_ratings.pdf')
plt.close()