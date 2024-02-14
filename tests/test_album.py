from lib.album import *

"""
Album constructs with an id, title, release_year, artist_id
"""
def test_album_constructs():
    album = Album(1, "Test Album", 1984, 1)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.release_year == 1984
    assert album.artist_id == 1

"""
Format albums to strings nicely
"""
def test_artists_format_nicely():
    album = Album(1, "Test Album", 1984, 2)
    assert str(album) == "Album(1, Test Album, 1984, 2)"

"""
Compare two identical albums
And have them be equal
"""
def test_artists_are_equal():
    album1 = Album(1, "Test Album", 1984, 2)
    album2 = Album(1, "Test Album", 1984, 2)
    assert album1 == album2

