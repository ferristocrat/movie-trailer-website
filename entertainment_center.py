import fresh_tomatoes
import media

#defining each movie using the "Movie" class
dark_knight = media.Movie("The Dark Knight", "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.", "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", "https://www.youtube.com/watch?v=EXeTwQWrcwY", "2008")
inception = media.Movie("Inception", "A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.","https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg","https://www.youtube.com/watch?v=YoHD9XEInc0", "2010")
italian_job = media.Movie("The Italian Job", "After being betrayed and left for dead in Italy, Charlie Croker and his team plan an elaborate gold heist against their former ally.","https://upload.wikimedia.org/wikipedia/en/d/db/Italianjob.jpg","https://www.youtube.com/watch?v=7HZndLdQOPk", "2003")
green_mile = media.Movie("The Green Mile", "The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a mysterious gift.", "https://upload.wikimedia.org/wikipedia/en/c/ce/Green_mile.jpg","https://www.youtube.com/watch?v=Ki4haFrqSrw","1999")
law_abiding_citizen = media.Movie("Law Abiding Citizen", "A frustrated man decides to take justice into his own hands after a plea bargain sets one of his family's killers free. He targets not only the killer but also the district attorney and others involved in the deal.", "https://upload.wikimedia.org/wikipedia/en/9/95/Law_abiding_citizen_ver5.jpg", "https://www.youtube.com/watch?v=LX6kVRsdXW4","2009")

#a list of our movies
movies = [dark_knight, inception, italian_job, green_mile, law_abiding_citizen]

#using code from fresh_tomatoes.py to display our webpage 
fresh_tomatoes.open_movies_page(movies)
