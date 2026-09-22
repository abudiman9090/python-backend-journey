-- tasks table
DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- users + posts tables
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    title TEXT NOT NULL,
    body TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- sample data
INSERT INTO tasks (title) VALUES ('Buy milk');
INSERT INTO tasks (title, done) VALUES ('Walk dog', TRUE);

INSERT INTO users (name, email) VALUES ('Abdu', 'abduke8987@gmail.com');
INSERT INTO users (name, email) VALUES ('Amar', 'abduke8929@gmail.com');
INSERT INTO users (name, email) VALUES ('Amir', 'abduke8984@gmail.com');

INSERT INTO posts (user_id, title) VALUES (1, 'My first post');
INSERT INTO posts (user_id, title) VALUES (1, 'My second post');
INSERT INTO posts (user_id, title) VALUES (2, 'My third post');
INSERT INTO posts (user_id, title) VALUES (2, 'My fourth post');
INSERT INTO posts (user_id, title) VALUES (3, 'My fifth post');