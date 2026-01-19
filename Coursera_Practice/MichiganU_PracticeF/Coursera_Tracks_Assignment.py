import sqlite3

def open_file():
    conn = sqlite3.connect('TrackDB.sqlite')
    cur = conn.cursor()

    # create the tables to insert data
    cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;
    DROP TABLE IF EXISTS Genre;
                    
    CREATE TABLE Artist (
                      ID INTEGER PRIMARY KEY NOT NULL UNIQUE,
                      Name TEXT UNIQUE);
                      
    CREATE TABLE Genre (
                      ID INTEGER NOT NULL PRIMARY KEY UNIQUE,
                      Name TEXT UNIQUE);
                    
    CREATE TABLE Album (
                      ID INTEGER PRIMARY KEY NOT NULL UNIQUE,
                      Artist_id INTEGER,
                      Title TEXT UNIQUE);

    CREATE TABLE Track (
                      ID INTEGER PRIMARY KEY NOT NULL UNIQUE,
                      Title TEXT UNIQUE,
                      Album_id INTEGER,
                      Genre_id INTEGER,
                      Leng INTEGER,
                      Rating INTEGER,
                      Cou INTEGER);
    ''')
    return conn, cur

def read_csv():
    handle = open('./tracks/tracks.csv')

    # form
    # Another One Bites The Dust,Queen,Greatest Hits,55,100,217103,Rock
    #           0                   1          2      3  4     5    6

    obj = []
    for line in handle:
        line = line.strip()
        pieces = line.split(',')

        if len(pieces)<7: continue

        name = pieces[0]
        artist = pieces[1]
        album = pieces[2]
        count = pieces[3]
        rating = pieces[4]
        length = pieces[5]
        genre = pieces[6]

        #print(f'{name}, {artist}, {album}, {count}, {rating}, {length}')
        obj.append(f'{name}, {artist}, {album}, {count}, {rating}, {length}, {genre}')
    #print(obj)
    return obj

def create_sql(conn, cur, obj):
    for o in obj:
        line = o.strip()
        pieces = line.split(',')

        name = pieces[0]
        artist = pieces[1]
        album = pieces[2]
        count = pieces[3]
        rating = pieces[4]
        length = pieces[5]
        genre = pieces[6]

        #print(f'{name}, {artist}, {album}, {count}, {rating}, {length}')

        cur.execute('''INSERT OR IGNORE INTO Artist (Name)
                    VALUES (?)''', (artist, ))
        cur.execute('''SELECT ID
                    FROM Artist
                    WHERE Name = ?''', (artist, ))
        artist_id = cur.fetchone()[0]
        #print(artist_id)

        cur.execute('''INSERT OR IGNORE INTO Genre (Name)
                    VALUES (?)''', (genre, ))
        cur.execute('''SELECT ID
                    FROM Genre
                    WHERE Name = ?''', (genre, ))
        genre_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Album (Title, Artist_id)
                    VALUES (?,?)''', (album, artist_id))
        cur.execute('''SELECT ID
                    FROM Album 
                    WHERE Title = ?''', (album, ))
        album_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Track 
                    (Title, Album_id, Genre_id, Leng, Rating, Cou)
                    VALUES (?, ?, ?, ?, ?, ?)''', 
                    (name, album_id, genre_id, length, rating, count))

        conn.commit()
    cur.close()

def main():
    conn, cur = open_file()
    obj = read_csv()
    create_sql(conn, cur, obj)

if __name__ == '__main__':
    main()
