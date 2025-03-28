from fastapi import Body, FastAPI

app = FastAPI()


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/books") # this is a decorector that tells FastAPI that the function below is a GET request
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold(): #casefold for case insensitive
            return book


@app.get("/books/") # we have a extra / at the end of the path
async def read_category_by_query(category: str):
    """
    So as you can see in the path parameter, we are passing in something in the URL that we're converting
    to our parameter in our function with a query parameter.
    Fast API automatically knows that, hey, anything that is passed in after books, that is not a dynamic
    path parameter.
    We want to convert into whatever parameters we have here within our function(category: str).
    """
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# Get all books from a specific author using path or query parameters
# @app.get("/books/byauthor/")
# async def read_books_by_author_path(author: str):
#     books_to_return = []
#     for book in BOOKS:
#         if book.get('author').casefold() == author.casefold():
#             books_to_return.append(book)

#     return books_to_return


@app.get("/books/{book_author}/") #extra / at the end of {book_author} is used to add query parameter along with path parameter
async def read_author_category_by_query(book_author: str, category: str):# here category is a query parameter and book_author is a path parameter
    """
    we can use both path and query parameters in the same function 
    this allow us to filter the books by author and category
    """
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return

#################### POST, PUT, DELETE ####################


@app.post("/books/create_book")
async def create_book(new_book=Body()): # we have to import Body() from fastapi
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

########## assignement ##########

@app.get("/books/xauthor")
async def read_books_by_author_query(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)

    return books_to_return
