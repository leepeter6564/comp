Homepage URL: http://localhost:8000/home/
Look at me in the eye and tell me that it's not  beautiful.

URL of articles: http://localhost:8000/home/article/<pk> where pk is basically the article id.

Field added: postscript in the Article model and nick_name in Contributors.
I didn't realize that when there were already stuff in the database, default settings had to be set for the new parameters to go along with the existing columns.
Now I know. I am also wondering if migrate automatically removes unused columns too.
