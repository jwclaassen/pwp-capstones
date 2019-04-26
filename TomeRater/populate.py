from TomeRater import *

Tome_Rater = TomeRater()

class User:
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
	
	#below is not efficient, come back
	def get_average_rating(self):
		ratings = []
		temp1 = 0
		for rating in self.books.values():
			if rating != None:
				ratings.append(rating)
		if ratings == []:
			return None
		for rating in ratings:
			temp1 += rating
		return temp1 / len(ratings)

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
		print("Book's isbn has been updated from", self.isbn, "to", new_isbn)
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
		ratings = []
		temp1 = 0
		for rating in self.ratings:
			if rating != None:
				ratings.append(rating)
		if ratings == []:
			return None
		for rating in ratings:
			temp1 += rating
		return temp1 / len(ratings)
	
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
		isbnlist = []
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
	
	

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
# Tome_Rater.print_catalog()
# Tome_Rater.print_users()

# print("Most positive user:")
# print(Tome_Rater.most_positive_user())
# print("Highest rated book:")
# print(Tome_Rater.highest_rated_book())
# print("Most read book:")
# print(Tome_Rater.most_read_book())