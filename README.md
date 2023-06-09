# Movie Rating Platform
 Platform for viewing, rating, commenting and searching movies created using Django framework. Work on the app was divided into several assignments for the laboratory classes of the Advanced Internet Applications subject.
 
 * Navbar consists of:
 ** Three buttons: home, search and one for viewing embedded videos
 ** Name of the platform
 ** Logged in username
 ** User button for viewing external content consisting of:
 *** Log out/log in functions
 *** Viewing movies rated by logged in user
 *** In case of adming user: function for adding a new movie.

 ![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/add820a0-df61-4431-8a97-42eb8995e89b)
 
 # Main Page consists of three parts:
 ## Popular lately card - app searches and displayes movies with ratings with highest IDs that have the value greater or equal to 4.
 ## About us card - currently filled with lorem.
 ## Recommended movies - app searches for movies with similar genres or same director to the movie that logged in user rated 4 or higher.

 ![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/ce7f7d1e-48b1-4968-b5ca-f7469a28919e)
 
 My ratings page:
 ![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/c9e93275-90b5-4517-85ea-1a12f67bc80c)


 Search page consits of:
 ## Three search fields for inputing genres, title or minimal rating
 ## List of all movies/search results depending on user input. For the clarity of the page paginator has been used (six movies per one page)

 ![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/1a950a36-c5f5-4dbc-8969-7415ca9303a4)

 Movie page consits of:
 ## Movie details (title, year, director, genres, description)
 ## Button with hyperlink to imdb's movie page for cross refering
 ## Average rating
 ## Button for rating the movie, also in case of admin user buttons for adding images to the movie and editting the movie
 ## Image carousel displaying images associated with the movie
 ## Comment section containing:
 ### Field for adding a comment (only for logged in users)
 ### Cards with all comments displaying comment content and author's username
 
 ![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/592bfe08-8d9a-4df6-bbe8-f8fda17e7b91)
 ![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/c59d1df8-416f-463c-8bc9-e988336a25bd)

 Add image to the movie form:
 ![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/d412557e-55f1-46a9-9f42-ada4340310cf)

 Edit movie page:
 ![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/5b7e12b0-0b0b-4242-bf02-a75e32b90578)
 ![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/e12f3496-319c-4234-aae3-988eafb3855a)

 Front image boolean attribute tells app that this image is supposed to be first on the carousel
 
 
