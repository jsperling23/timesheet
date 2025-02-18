# timesheet

## Design
Following the requirements listed in the repository here:
https://gist.github.com/VinhAccrualify/f681c39fea3a1a4ed95b43b806f1d884,
This application was designed using Flask and Jinja for routing and template rendering. All data was stored in a MySQL server and connections to that were done using the MySQL Python connector. Due to the nature of the queries, I decided to keep it simple and just write out my queries instead of using an ORM like SQLAlchemy. JavaScript was used to make parts of the webpage interactive and Bootstrap was used for styling purposes. The application itself has been containerized in a Docker image deployed on a Digital Ocean droplet which can be found at:
http://24.144.89.213:8000/

The reason for most of these design choices was familiarity. I've used Flask fairly extensively in my own projects so I felt comfortable building something from that. Along with that MySQL, is the database I have the most experience with. I did consider separating the frontend and backend using something like React which I've used in my own website but I decided to keep it simple in that regards since the scope of the project is fairly limited. One new thing I've previously not used here was Bootstrap which was a joy to use and I found simplified styling significantly. As for choosing Digital Ocean as a remote host option, once again I am familiar with their services and I found its quite easy to put an application in a Docker container and just transfer that over to one of their servers to run it.
