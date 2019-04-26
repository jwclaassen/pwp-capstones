#need this to identify isbns between classes, for .set_isbn in Book class interacting with the list of isbns in self.books in TomeRaterr class
isbnlist = []

class User(object):
    def __init__(self, name, email):
		self.name = name
		self.email = email
		self.books = {}
	
	def get_email(self):
		return self.email
	
	def change_email(self, new_email):
		print("User's email has been updated from", self.email, "to", new_email)
		self.email = new_email
	
	def __repr__(self):
		return "User " + self.name + ", email: " + self.email + ", books read: " + str(len(self.books))
	
	def __eq__(self, other):
		if self.name == other.name:
			return self.email == other.email
		return False
	
	def read_book(self, book, rating = None):
		self.books[book] = rating
	
	def get_average_rating(self):
		tempratingboolean = False
		temprates = 0
		for rating in self.books.values():
			if rating != None:
				temprates += rating
				tempratingboolean = True
		if tempratingboolean == False:
			return None
		return temprates / len(ratings)

class Book:
	def __init__(self, title, isbn):
		self.title = title
		self.isbn = isbn
		self.ratings = []
	
	def get_title(self):
		return self.title
	
	def get_isbn(self):
		return self.isbn
	
	def set_isbn(self, new_isbn):
		if not new_isbn in isbnlist:
			print("Book's isbn has been updated from", self.isbn, "to", new_isbn)
			isbn_list.pop(self.isbn)
			self.isbn = new_isbn
	
	def add_rating(self, rating):
		if rating != None:
			if rating <= 4 and rating >= 0:
				self.ratings.append(rating)
			else:
				print("Invalid Rating")
		else:
			print("Invalid Rating")
	
	def __eq__(self, other):
		if self.isbn == other.isbn:
			return self.title == other.title
		return False
	
	def get_average_rating(self):
		tempratingboolean = False
		tempratingsum = 0
		for rating in self.ratings:
			if rating != None:
				tempratingsum += rating
				tempratingboolean = True
		if tempratingboolean == False:
			return None
		return tempratingsum / len(ratings)
	
	def __repr__(self):
		return self.title + ", ISBN: " + str(self.isbn)
	
	def __hash__(self):
		return hash((self.title, self.isbn))

class Fiction(Book):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn)
		self.author = author
	
	def get_author(self):
		return self.author
	
	def __repr__(self):
		return self.title + " by " + self.author

class Non_Fiction(Book):
	def __init__(self, title, subject, level, isbn):
		super().__init__(title, isbn)
		self.level = level
		self.subject = subject
	
	def get_subject(self):
		return self.subject
	
	def get_level(self):
		return self.level
	
	def __repr__(self):
		return self.title + ", a " + self.level + " manual on " + self.subject

class TomeRater:
	def __init__(self):
		self.users = {}
		self.books = {}
	
	def create_book(self, title, isbn):
		booklist = self.books.keys().getisbn()
		for book in booklist:
			isbnlist.append(book.getisbn)
		if not isbn in isbnlist:
			tempbook = Book(title, isbn)
			return tempbook
		else:
			print("That book already exists")
	
	def create_novel(self, title, author, isbn):
		tempfiction = Fiction(title, author, isbn)
		return tempfiction
		
	def create_non_fiction(self, title, subject, level, isbn):
		tempnon_fiction = Non_Fiction(title, subject, level, isbn)
		return tempnon_fiction
	
	def add_book_to_user(self, book, email, rating = None):
		if email in self.users.keys():
			self.users[email].read_book(book, rating)
			book.add_rating(rating)
			if not book in self.books.keys():
				self.books[book] = 0
			self.books[book] += 1
		else:
			print("No user with email " + email + "!")
	
	def add_user(self, name, email, user_books = None):
		self.users[email] = User(name, email)
		if not email in self.users.keys():
			if "@" in email and (".com" in email or ".edu" in email or ".org" in email):
				if user_books != None:
					for book in user_books:
						self.add_book_to_user(book, email)
			else:
				print("That is not a valid email")
		else:
			print("That user already exists")
	def print_catalog(self):
		print("List of Books:")
		for book in self.books.keys():
			print(book)
	
	def print_users(self):
		print("list of Users:")
		for user in self.users.values():
			print(user)
	
	def most_read_book(self):
		high = ["",0]
		for book in self.books.keys():
			if self.books[book] > high[1]:
				high = [book, self.books[book]]
		return high
	
	def highest_rated_book(self):
		high = ["",-1]
		for book in self.books.keys():
			if book.get_average_rating() > high[1]:
				high = [book, book.get_average_rating()]
		return high
	
	def most_positive_user(self):
		high = ["",-1000]
		for user in self.users.values():
			if user.get_average_rating() > high[1]:
				high = [user, user.get_average_rating()]
		return high