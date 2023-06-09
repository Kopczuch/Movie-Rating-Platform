# Movie Rating Platform
Platform for viewing, rating, commenting and searching movies created using Django framework. Work on the app was divided into several assignments for the laboratory classes of the Advanced Internet Applications subject at Poznan University of Technology.
Movie data was provided in json files by the course instructor and added to the postgresql database via python scripts (load_{name}.py)

## Navbar consists of:
- Three buttons: home, search and one for viewing embedded videos
- Name of the platform
- Logged in username
- User button for viewing external content consisting of:
  - Log out/log in functions
  - Viewing movies rated by logged in user
  - In case of adming user: function for adding a new movie.

![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/add820a0-df61-4431-8a97-42eb8995e89b)

## Main Page consists of three parts:
- Popular lately card - app searches and displayes movies with ratings with highest IDs that have the value greater or equal to 4.
- About us card - currently filled with lorem.
- Recommended movies - app searches for movies with similar genres or same director to the random movie that logged in user rated 4 or higher.

![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/ce7f7d1e-48b1-4968-b5ca-f7469a28919e)

## My ratings page:
![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/496207d8-0b8b-4388-95f1-d4cb2f6151db)

## Search page consits of:
- Three search fields for inputing genres, title or minimal rating
- List of all movies/search results depending on user input. For the clarity of the page paginator has been used (six movies per one page)

![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/389c165e-33fb-405d-a462-58cf294a2f68)

## Movie page consits of:
- Movie details (title, year, director, genres, description)
- Button with hyperlink to imdb's movie page for cross refering
- Average rating
- Button for rating the movie, also in case of admin user buttons for adding images to the movie and editting the movie
- Image carousel displaying images associated with the movie
- Comment section containing:
  - Field for adding a comment (only for logged in users)
  - Cards with all comments displaying comment content and author's username

![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/592bfe08-8d9a-4df6-bbe8-f8fda17e7b91)
![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/c59d1df8-416f-463c-8bc9-e988336a25bd)

### Edit movie page:
![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/e037e5dd-0727-45e7-a108-66ddacc511e7)
![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/72bf120e-dcf5-44e0-90c7-d950891b7f8f)

### Add image to the movie form:
![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/ed09416e-1086-42ad-b9c1-36bce9094ca3)

Front image boolean attribute tells app that this image is supposed to be first on the carousel.

### Add rating page:
![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/81846a72-269d-4c18-a381-84dd2dc0e4b2)

## View embedded videos page:
![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/2e7b2611-8200-41e3-b44e-281bf4f4f28d)

### Embedded video details page:
![image](https://github.com/Kopczuch/Movie-Rating-Platform/assets/55816369/acaea877-6a31-41d4-bf93-c35ccaf6e93a)


