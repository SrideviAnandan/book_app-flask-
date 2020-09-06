from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

# display all books
# create a book
# search a book using book id

def db_connection():
    conn = None
    try:
        conn =sqlite3.connect('book.sqlite')
    except sqlite3.Error as e:
        print(e)
    return conn

@app.route('/books/create', methods = ['POST'])
def create_book():
    conn = db_connection()
    cursor = conn.cursor()
    name = request.form['name']
    genre = request.form['genre']
    publisher = request.form['publisher']
    price = request.form['price']
    cursor.execute(""" INSERT INTO readers (name,genre,publisher, price) VALUES (?, ?, ?, ?)""", (name, genre,publisher,price))
    conn.commit()
    return "Book added succesfullly", 201

@app.route('/books', methods = ['GET'])
def book_index():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM readers """)
    book_sql_result = cursor.fetchall()
    books = []
    for row in book_sql_result:
        books.append(dict({"book_id":row[0], "name":row[1],  "genre":row[2], "publisher":row[3], "price":row[4]}))
    return jsonify(books)

@app.route('/book/id',methods = ['GET'])
def get_book_by_id():
    book_id = request.args.get('book_id')
    conn = db_connection()
    cursor = conn.cursor()
    query = """ SELECT * FROM readers where id = ?"""
    cursor.execute(query,(book_id,))
    row = cursor.fetchone()
    if row:
        data = {"id":row[0], "name":row[1],  "genre":row[2], "publisher":row[3], "price":row[4]}
        return jsonify(data)
    else:
        return 'Not Found',404
@app.route('/book/name',methods = ['GET'])
def get_book_by_name():
    name = request.args.get('name')
    conn = db_connection()
    cursor = conn.cursor()
    query = """ SELECT * FROM readers where name = ?"""
    cursor.execute(query,(name,))
    row = cursor.fetchone()
    if row:
        data = {"book_id":row[0], "name":row[1], "genre":row[2], "publisher":row[3], "price":row[4]}
        return jsonify(data)
    else:
        return 'Not Found',404 
@app.route('/book/publisher',methods = ['GET'])
def get_book_by_publisher():
    publisher = request.args.get('publisher')
    conn = db_connection()
    cursor = conn.cursor()
    query = """ SELECT * FROM readers where publisher = ?"""
    cursor.execute(query,(publisher,))
    row = cursor.fetchone()
    if row:
        data = {"book_id":row[0],"name":row[1],  "genre":row[2], "publisher":row[3], "price":row[4]}
        return jsonify(data)
    else:
        return 'Not Found',404   
              
@app.route('/book/author',methods = ['GET'])
def get_book_by_author_id():
    author_id = request.args.get('author_id')
    conn = db_connection()
    cursor = conn.cursor()
    query = """ SELECT * FROM readers_writers where author_id = ?"""

    cursor.execute(query,(author_id,))
    row = cursor.fetchone()
    if row:
        data = {"book_id":row[0], "author_id":row[1]}
        return jsonify(data)
    else:
        return 'Not Found',404         
@app.route('/book/delete',methods = ['DELETE'])
def remove_name():
    name = request.args.get('name')
    conn = db_connection()
    cursor = conn.cursor()
    name = request.form['name']
    cursor.execute(  """DELETE FROM readers WHERE name = ? """,(name))
    conn.commit()
    return "Book deleted succesfullly", 202


     
