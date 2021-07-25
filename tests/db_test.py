from db import DB


def test_db():
    db = DB.instance()

    # Test set and get
    db.set('counter', 10)
    counter = db.get('counter')
    assert counter == 10

    # Test delete
    db.delete('counter')
    counter = db.get('counter')
    assert counter is None

    # Test delete non-existent key
    db.delete('hello')
