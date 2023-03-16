import math
from datetime import datetime
import glob 
import json


# Define decay function for movie age
def gaussian_decay(t, delta=365):
    return math.exp(-0.5 * ((t / delta) ** 2))

# Function to generate personalized feed of movies for a given user
def generate_movie_feed(user, movies,user_preferences,related_users):
    # Get user preferences
    preferences = [{preference['genre']:preference['preference_score']} for user in user_preferences if user['user_id'] == user_id for preference in user['preference']]

    # Get related user preferences
    related_user_preferences = {}
    for related_user in related_users.get(str(user), []):
        related_user_preferences[related_user['user_id']] = {preference['genre']: preference['preference_score'] for user in user_preferences if user['user_id'] == related_user['user_id'] for preference in user['preference']}
    
    # Calculate relevance score for each movie
    movie_scores = {}
    for movie in movies:
        # Calculate relevance based on movie age
        delta = (datetime.now() - datetime.strptime(movie['release_date'], '%m/%d/%Y')).days
        age_score = gaussian_decay(delta)
        
        # Calculate relevance based on user preferences
        genre_score = 0
        for genre in movie['genres']:
            for preference in preferences:
                if genre in preference:
                    genre_score += preference[genre]

        # movie_genres = movie['genres']
        # if any(genre in preference.keys() for preference in preferences for genre in movie_genres):
        #     genre_score += preferences[genre]
        genre_score /= len(movie['genres'])
        
        # Calculate relevance based on related user preferences
        related_user_score = 0
        for genre in movie['genres']:
            genre_scores = [related_user_pref.get(genre, 0) for related_user_pref in related_user_preferences.values()]
            genre_mean = sum(genre_scores) / len(genre_scores) if genre_scores else 0
            related_user_score += genre_mean
 
        related_user_score /= len(related_user_preferences)
        # Calculate overall relevance score
        movie_scores[movie['movie_id']] = age_score * genre_score * related_user_score
    # Rank movies based on relevance score
    ranked_movies = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)[:10]
    
    return generate_table(ranked_movies=ranked_movies)


def generate_table(ranked_movies):
    from prettytable import PrettyTable

    table = PrettyTable()
    table.field_names = ["Rank", "Score"]

    for rank, score in ranked_movies:
        table.add_row([rank, score])

    return table
    

if __name__ == "__main__":
    file_list = glob.glob("*.json")
    data_dict = dict()

    for file_name in file_list:
        with open(file_name,"r") as f:
            data = json.load(f)
            data_dict[file_name] = data   
    users = data_dict["user_data.json"]
    user_id = int(input("Enter the user_id of the user : "))
    all_ids = [ids['user_id'] for ids in users]
    if user_id not in all_ids:
        raise Exception("No ID FOUND")

    print(generate_movie_feed(user=user_id,movies=data_dict["movie_data.json"],user_preferences=data_dict["user_preference.json"],related_users=data_dict["related_users.json"]))
