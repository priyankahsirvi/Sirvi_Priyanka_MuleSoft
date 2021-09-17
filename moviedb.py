import sqlite3

conn=sqlite3.connect('moviesdb.sqlite')
cur=conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Movies;

CREATE TABLE Movies(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    actor TEXT,
    actress TEXT,
    director TEXT,
    year_of_release INTEGER
);
''')

cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Parasite', 'Choi Woo Shik', 'Park So Dam', 'Bong Joon Ho', 2019)''')

cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('A Werewolf Boy', 'Song Joong Ki', 'Park Bo Young', 'Jo Sung Hee', 2012)''')

cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Interstellar', 'Matthew McConaugher', 'Anne Hathaway', 'Christopher Nolan', 2014)''')

cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Forest Gump', 'Tom Hanks', 'Robin Wright', 'Robert Zemeckis', 1994)''')

cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Cast Away', 'Tom Hanks', 'Helen Hunt', 'Robert Zemeckis', 2000)''')

cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('The Battleship Island', 'Song Joong Ki', 'Kim su an', 'Ryoo Seung wan', 2017)''')

cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Five Feet Apart', 'Cole Sprouse', 'Helen Lu Richardson', 'Justin Baldoni', 2019)''')

cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Dune', 'Timothee Chalamet', 'Zendaya', 'Denis Villeneuve', 2021)''')

cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Train To Busan', 'Gong Yoo', 'Kim su an', 'Yeon Sang Ho', 2016)''')

cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('La La land', 'Ryan Gosling', 'Emma Stone', 'Damien Chazelle', 2016)''')

cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Titanic', 'Leonardo DiCaprio', 'Kate Winslet', 'James Cameron', 1997)''')


sql_all = 'SELECT * FROM Movies'
print ("\n{:<5} {:<30} {:<25}{:<25} {:<25} {:<20}\n".format('Id','Title','Actor','Actress','Director','Year Of Release'))
for row in cur.execute(sql_all):
    id,title,actor,actress,director,year_of_release=row
    print ("{:<5} {:<30} {:<25}{:<25} {:<25} {:<20}".format(id,title,actor,actress,director,year_of_release))


actor_search=input("\nEnter the actor name: ")
print('\nMovies starring '+actor_search+' are: \n' )
print("{:<30}{:<25}{:<25}{:<20}\n".format('Title','Actress','Director','Year of Release'))
for row in cur.execute('SELECT title,actress,director,year_of_release FROM Movies WHERE actor= ?',(actor_search,)):
    title,actress,director,year_of_release=row
    print("{:<30}{:<25}{:<25}{:<20}".format(title,actress,director,year_of_release))

conn.commit()
