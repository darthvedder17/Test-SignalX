# Test-SignalX

Think of something like an extremely simplified version of Netflix movie recommendation system. You can take whatever assumptions that you think are needed here. 

The attached zip file contains the sample data for this challenge.

--

 challenge-sd-data.zip


What needs to be built?
Your function is supposed to provide a ranked feed of the top 10 movies for any given user. 
The ranking should be done by scoring each of the generated movies for a user on overall relevance which in turn should be calculated from the below-mentioned variables :
Time Delta of the 'release_date' of the movie from today i.e. how old is the movie
Impact of this should follow a Gaussian decay function (the closer the better) ( Ref )
User's preference towards the movie 
based on 'genres' in the movie and preference towards each genre
Preference towards the movie by Related users
Average of each Related user's preference towards this movie, as calculated above.

Already available sample datasets
 User and Related Users Datasets which provides
list of all users
list of all related users to a given user - this can be say friends of a given user)
User is an object with key fields being 'user_id' and 'name' 
Movie Datasets which provides
list of movies (pieces of content) that are generated for a given user
Movie is an object with key fields being 'movie_id', 'genres' and 'release_date'
User Preference Dataset which provides
list of preferences for a given user with various genres the user has interacted with in the past.
preference is object with key fields being 'user_id', 'genre' and 'preference_score'




![Alt text](signal-z.png?raw=true "Output")
