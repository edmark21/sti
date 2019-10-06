
logo = '''

		  ____________________.___ 
		 /   _____/\__    ___/|   |
		 \_____  \   |    |   |   |
		  /        \  |    |   |   |
	 	/_______  /  |____|   |___|
		        \/                 

		Account Generator
	---------------------------------------
			Created By:
	Edmark Jay Sumampen
	---------------------------------------

'''

print logo
lname = raw_input("Enter Lastname: ")
sid = raw_raw_input("Enter 11 digit Student#: ")
city = raw_raw_input("Enter City: ")
yr = raw_input("Enter Birth Year: ")
mt = raw_input("Enter Birth Month: ")
dt = raw_input("Enter Birth Date: ")
lu = lname.upper(0)
print ("\nUsername: " + lname + "." + sid[5:-1] + sid[10] + "@" + city + ".sti.edu.ph")
print ("Password: " + lname + yr + mt + dt)
