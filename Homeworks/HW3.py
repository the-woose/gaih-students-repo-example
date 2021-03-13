#-------------------------Homework 3-------------------------#
s_1 = {'first_name':'','last_name':'','midterm_grade':'','project_grade':'','final_grade':'', 'passing_grade':''}
s_2 = {'first_name':'','last_name':'','midterm_grade':'','project_grade':'','final_grade':'', 'passing_grade':''}
s_3 = {'first_name':'','last_name':'','midterm_grade':'','project_grade':'','final_grade':'', 'passing_grade':''}
s_4 = {'first_name':'','last_name':'','midterm_grade':'','project_grade':'','final_grade':'', 'passing_grade':''}
s_5 = {'first_name':'','last_name':'','midterm_grade':'','project_grade':'','final_grade':'', 'passing_grade':''}
students = [s_1, s_2, s_3, s_4, s_5]
grades = []

for i in range(5):	#----For loop for populating dictionaries----#
	info = students[i]
	for k,v in info.items():
		if k == 'first_name':
			students[i]['first_name'] = input("Please enter student " + str(i+1) + "'s first name: ")
		if k == 'last_name':
			students[i]['last_name'] = input("Please enter student " + str(i+1) + "'s last name: ")
		if k == 'midterm_grade':
			students[i]['midterm_grade'] = float(input("Please enter student " + str(i+1) + "'s midterm grade: "))
		if k == 'project_grade':
			students[i]['project_grade'] = float(input("Please enter student " + str(i+1) + "'s project grade: "))
		if k == 'final_grade':
			students[i]['final_grade'] = float(input("Please enter student " + str(i+1) + "'s final grade: "))
	students[i]['passing_grade'] = students[i]['midterm_grade']*0.3 + students[i]['project_grade']*0.3 + students[i]['final_grade']*0.4 	#----grade formula----#
	grades.append([students[i]['first_name'], students[i]['last_name'],round(students[i]['passing_grade'],2)]) 	#----create list----#
print(sorted(grades,key=lambda x:x[2], reverse=True))	

