from lib.album import *

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        return [Album(row["id"],
                      row["title"],
                      row["release_year"],
                      row["artist_id"])
                      for row in rows]
    
    def find(self, album_id):
        rows = self._connection.execute(
            'SELECT * from albums WHERE id = %s', [album_id])
        row = rows[0]
        
        return Album(row["id"],
                     row["title"],
                     row["release_year"],
                     row["artist_id"])