import sqlite3
import pytest
import app
from cs50 import SQL


@pytest.fixture(scope="module")
def db():
    db = app.config["db"]
    db.execute("DROP TABLE IF EXISTS users")
    db.execute("CREATE TABLE users (id INTEGER, username TEXT, hash TEXT)")
    return db


@pytest.fixture()
def client(monkeypatch):
    with open('sql/schema.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    db = sqlite3.connect('test.db')
    db.cursor().executescript(sql_script)
    mock_db = SQL("sqlite:///test.db")
    monkeypatch.setattr(app, "db", mock_db)
    return app.app.test_client()


def test_simple(client):
    response = client.get("/", follow_redirects=True)
    assert response.status_code == 200
    assert len(response.history) == 1
    assert response.request.path == "/login"


def test_register(client):
    response = client.post("/register", data={
        "username": "testuser",
        "password": "testuser",
        "confirm": "testuser",
    }, follow_redirects=True)
    assert response.status_code == 200
