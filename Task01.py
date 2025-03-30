marks = {'Alice':85, 'Ram':100, 'Geetha':35}
student = input("Enter the student's name: ")
if student in marks:
    print(f"{student}'s marks: {marks[student]}")
else:
    print('Student not found.')
