#-------------------------Homework 2-------------------------#
# isim kaynağı https://www.isimarsivi.com/isim-sihirbazi

#Question 1
CV1 = {'firstname':'Necib','lastname':'Ergül','age': 20,'position': 'CEO'}
CV2 = {'firstname':'Rüstem','lastname':'Tokyay','age': 27,'position': 'HR'}
CV3 = {'firstname':'İpek','lastname':'Tokyay','age': 25,'position': 'Intern'}
CV4 = {'firstname':'Gizem','lastname':'Öztuna','age': 30,'position': 'CFO'}
CV5 = {'firstname':'Alper','lastname':'Koyuncu','age': 22,'position': 'Intern'}

#Question 2
people = [CV1, CV2, CV3, CV4, CV5]	#----combine dictionaries
for i in range(5):	#----"for" loop for selecting dictionary
	CV = people[i]
	print("Employee", i+1,"\b's CV:")
	for k,v in CV.items():	#----print items in dictionary
		print(k,"\b:",v)
	print("\n")	#----seperate employee infos into blocks