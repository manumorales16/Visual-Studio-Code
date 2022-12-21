favoriteBooks = []

def addFavoriteBook (bookName):
  if 'Great' not in bookName:
    favoriteBooks.append(bookName)

def printFavoriteBooks():
  print ("Favorite Books: " + str(len(favoriteBooks)) )


addFavoriteBook('Harry Potter')
addFavoriteBook('Great Monkey')
addFavoriteBook('The witcher')
addFavoriteBook('bla bla')
addFavoriteBook('Great Hola')

printFavoriteBooks()