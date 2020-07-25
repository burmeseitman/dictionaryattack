import hashlib

found = False

passhash = input("Enter SHA-256 password Hash value: ")
dictwords = open("passwordlist.txt", "r")

for word in dictwords:
	encryptword = word.encode("utf-8")
	hashvalue = hashlib.sha256(encryptword.strip()).hexdigest()

	if hashvalue == passhash:
		print("Bingo! Password Found.")
		print("This is Password >> " + word)
		found = True
		break

if found == False:
	print("Password not found in the list")

