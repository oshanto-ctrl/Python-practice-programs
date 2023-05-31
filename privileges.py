class User():
	"""Represent a user"""


	def __init__(self,first_name,last_name,username,email,location):
		"""Initialize the users"""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username
		self.email = email
		self.location = location.title()
		self.login_attemps = 0


	def describe_user(self):
		"""Describe the user"""
		print(f"\n{self.first_name} {self.last_name}")
		print(f"	username: {self.username}")
		print(f"	e-mail: {self.email}")
		print(f"	location: {self.location}")

	def greet_user(self):
		"""Greet a user"""
		print(f"\nWelcome back, {self.username}")


	def increment_login_attempts(self):
		"""Increment user login attempts"""
		self.login_attemps += 1


	def reset_login_attempts(self):
		"""Reset login attempts to 0"""
		self.login_attemps = 0



class Admin(User):
	"""A user with administrative privileges"""


	def __init__(self, first_name, last_name, username, email, location):
		"""Initialize an admin"""
		super().__init__(first_name,last_name,username,email,location)


		# Initialize an empty set of privilege
		self.privileges = Privileges()
		#privileges class theka admin ja ja privilege paibo
		#tar e set



class Privileges():
	"""A class to store admin's privileges"""


	def __init__(self, privileges = []):
		"""Initialize a priviliegs list"""
		self.privileges = privileges


	def show_privileges(self):
		print("\nPrivileges")
		if self.privileges:
			for privilege in self.privileges:
				print(f"- {privilege}")
			else:
				print("- This user has no privileges.")



#Main
print("Main")

eric = Admin('eric', 'matthes', 'eMath', 'emath@hotmail.com', 'Golia')
eric.describe_user()

eric.privileges.show_privileges() #first the privileges class
#then show privilege function
#eric.privileges.show_privileges() #first the privileges class


print("Adding privileges")

eric_privileges = [
	'can reset password',
	'can edit username',
	'can moderate discussion',
	'can suspend accounts',
	'can register accounts',
]

eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()




