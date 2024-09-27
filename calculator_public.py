# Grades    

labs_completed = int(input("Enter the number of labs completed: "))

quiz_completed = int(input("Enter the number of quizzes completed: "))

assignment_1 = int(input("Enter grade for Assignment 1: "))
assignment_2 = int(input("Enter grade for Assignment 2: "))
assignment_3 = int(input("Enter grade for Assignment 3: "))
assignment_4 = int(input("Enter grade for Assignment 4: "))

midterm_1 = int(input("Enter grade for Midterm 1: "))
midterm_2 = int(input("Enter grade for Midterm 2: "))

final = int(input("Enter grade for Final Exam: "))

midterm_and_final_prep = int(input("Enter grade for Midterms and Final Preparation: "))


#All Grades Weighted

labs_weighted = labs_completed/6 * 20 if labs_completed<= 6 else 20

quiz_weighted = quiz_completed/6 * 15 if quiz_completed<= 6 else 15

assignment_weighted = assignment_1*0.04 + assignment_2*0.04 + assignment_3*0.04 + assignment_4*0.04
midterms_weighted = midterm_1*0.125 + midterm_2*0.125 

final_weighted = final*0.18

midterm_and_final_prep_weighted = midterm_and_final_prep  * 0.06


#Total
total_grade = labs_weighted + quiz_weighted + assignment_weighted + midterms_weighted + final_weighted + midterm_and_final_prep_weighted

total_grade = round(total_grade, 2)

#Output
print("Your grade is: "+str(total_grade))
