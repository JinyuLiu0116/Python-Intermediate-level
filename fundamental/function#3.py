triangel=int(input("Enter the number of triangles: "))

def dots(triangel):
    return int(triangel*(triangel+1)/2)

print(f"Your triangel has {dots(triangel)} dots.")

def fillInfor(subject, score, num, total):
    for index in range(num):
        subject[index]=(input(f"Enter name of subject {index+1}:"))
        score[index]=(int(input(f"Enter your score for {subject[index]}:")))
        total+=score[index]
def letterGrade(ave):
    if ave >=90 and ave <=100:
        return 'A'
    elif ave >=80 and ave <90:
        return 'B'
    elif ave >=70 and ave <80:
        return 'C'
    elif ave >=60 and ave <70:
        return 'D'
    else:
        return 'F'
def getScore(subject,score,num):
    for index in range(num):
        print(f"{subject[index]:10}: {score[index]}")

numOfSubject=5
subject=[""]*numOfSubject
score=[0]*numOfSubject
total=0

name=input("Please enter your name:")
print(f"Hello {name}, please fill your information:")
fillInfor(subject,score,numOfSubject, total)
average=total/numOfSubject
letter=letterGrade(average)

print("Your information:")
print(f"Name: {name}")
getScore(subject,score,numOfSubject)
print(f"Total: {total}")
print(f"Letter Grade: {letter}")
