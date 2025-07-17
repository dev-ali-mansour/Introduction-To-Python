student_age = 23
student_gpa = 1.25
is_passed = False
# Update Student GPA
student_gpa = 3.75
is_passed = True

print(student_gpa)
print(is_passed)
print(type(student_age))
print(type(is_passed))

# Multi-line String
review_one = '''The courses have been fantastic, 
and their flexibility makes them perfect for my packed schedule.
The platform has been such a valuable resource.
I only wish I'd discovered it earlier.
I'm definitely going to spread the word to my friends about this great experience'''

review_two = '''This time last year, I felt stuck at a career crossroads.
Fast forward to today, and I've successfully transitioned into a role as a Prompt Engineer.
I'm incredibly grateful for the impact you've had on my professional journey.
You're doing amazing work - please continue!'''

print(review_one)
print(review_two)

current_course = "Basics of Python Programming"
# Update 'Basics' to 'Fundamentals'
current_course = current_course.replace("Basics", "Fundamentals")
print(current_course)