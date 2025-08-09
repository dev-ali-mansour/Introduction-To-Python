import contextlib
import os

import psycopg2 as postgres


@contextlib.contextmanager
def my_context():
    print('hello')
    yield 42
    print('goodbye')

with my_context() as foo:
    print('foo is {}'.format(foo))


@contextlib.contextmanager
def database(url):
    # Setup database connection
    db=postgres.connect(url)

    yield db

    # teardown database connection
    db.disconnect()

url = 'http://datacamp.com/data'
with database(url) as my_db:
    cursor_list = my_db.excute('SELECT * FROM courses')

@contextlib.contextmanager
def in_dir(path):
    # Save the current working directory
    old_dir = os.getcwd()

    # Switch to the new directory
    os.chdir(path)

    yield

    # Change back to previous working directory
    os.chdir(old_dir)

with in_dir('/data/project_1'):
    project_files = os.listdir()

