import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

credits = pd.read_csv("credits.csv")
titles = pd.read_csv("titles.csv")

def first_task():
    movie_scores = titles[titles['type'] == 'MOVIE']['imdb_score'].dropna()
    show_scores = titles[titles['type'] == 'SHOW']['imdb_score'].dropna()
    plt.hist(movie_scores, np.arange(0, 10.2, 0.2))
    plt.hist(show_scores, np.arange(0, 10.2, 0.2))
    plt.xlabel('Score')
    plt.ylabel('Titles')
    print(f'Movie average - {movie_scores.mean()}\nShow average - {show_scores.mean()}')
    plt.show()
    
def second_task():
    all_shows = titles[titles['type'] == 'SHOW']['age_certification'].dropna()
    labels, values = np.unique(all_shows, return_counts=True)
    plt.pie(values, labels=labels)
    plt.show()

def third_task():
    titles_2000 = titles[titles['release_year'] >= 2000]
    overall = titles_2000.groupby('release_year')['title'].count().reset_index()
    points_8 = titles_2000[titles_2000['imdb_score'] >= 8.0].groupby('release_year')['id'].count().reset_index()
    final = pd.merge(overall, points_8, how = "outer", on='release_year').fillna(0)
    plt.bar(final['release_year'], final['id'] / final['title'])
    plt.xlabel('Years')
    plt.ylabel('Percent')
    plt.show()

def fourth_task():
    top1000_movies = titles.sort_values('imdb_score', ascending=False).head(1000)
    merged_tables = pd.merge(credits, top1000_movies, on='id')
    top10_actors = merged_tables.groupby(by='name')['title'].nunique().sort_values(ascending=False).head(10)
    print(f'Top 10 actors:\n{top10_actors.to_string()}')

def fifth_task():
    top1000_movies = titles.sort_values('imdb_score', ascending=False).head(1000).reset_index()
    list_of_genres = top1000_movies['genres']
    unique_genres = dict()

    for genres in list_of_genres:
        optimized_genres = genres.replace('[', '').replace("'", '').replace(']', '').split(',')
        for genre in optimized_genres:
            if genre not in unique_genres:
                unique_genres[genre] = 0
            else:
                unique_genres[genre] += 1

    plt.bar(unique_genres.keys(), unique_genres.values())
    plt.xlabel('Genres')
    plt.ylabel('Count')
    plt.show()

def main():
    while True:
        choice = int(input('Enter number of task(0-5, 0 - quit): '))
        match choice:
            case 0:
                quit()
            case 1:
                first_task()
            case 2:
                second_task()
            case 3:
                third_task()
            case 4:
                fourth_task()
            case 5:
                fifth_task()

if __name__ == '__main__':
    main()
