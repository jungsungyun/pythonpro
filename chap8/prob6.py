import pickle
import random
quiz1 = ["우리나라 최초의 한글 소설로 전해지는 이 고전소설의 이름은?"]
quiz2 = ["오스트레일리아(호주)의 수도는?"]
quiz3 = ["우리나라 국보 1호였던 문하재의 이름은?"]
quiz4 = ["우리나라 수도는?"]
answer1 = ["피리부는사나이","홍길동전","어린왕자","피터팬"]
answer2 = ["오세니아","캔버라","파리","뉴욕"]
answer3 = ["경복궁","승례문","동대문","불국사"]
answer4 = ["부산","서울","대구","인천"]
with open("pickles3.dat", "wb") as pickle_file:
    pickle.dump(quiz1, pickle_file)
    pickle.dump(quiz2, pickle_file)
    pickle.dump(quiz3, pickle_file)
    pickle.dump(quiz4, pickle_file)
with open("pickles4.dat", "wb") as pickle_file:
    pickle.dump(answer1, pickle_file)
    pickle.dump(answer2, pickle_file)
    pickle.dump(answer3, pickle_file)
    pickle.dump(answer4, pickle_file)
with open("pickles3.dat", "rb") as pickle_file:
    loadquiz1 = pickle.load(pickle_file)
    loadquiz2 = pickle.load(pickle_file)
    loadquiz3 = pickle.load(pickle_file)
    loadquiz4 = pickle.load(pickle_file)
with open("pickles4.dat", "rb") as pickle_file:
    loadanswer1 = pickle.load(pickle_file)
    loadanswer2 = pickle.load(pickle_file)
    loadanswer3 = pickle.load(pickle_file)
    loadanswer4 = pickle.load(pickle_file)



print("         Welcome to Trivia Challenge!\n")
print("         An Episode You Can't Refuse\n")

questions = [loadquiz1, loadquiz2, loadquiz3, loadquiz4]
answers = [loadanswer1, loadanswer2, loadanswer3, loadanswer4]

while True:
    randomquestion = random.randint(0, len(questions) - 1)
    c_question = questions[randomquestion]
    c_answer = answers[randomquestion]
    
    print(f"\n{c_question[0]}\n") 
    for i, option in enumerate(c_answer, start = 1):
        print(f"        {i} - {option}")


    user = input("What's your answer?:")
    try:
        user = int(user)
        if 1 <= user <= len(c_answer):
            if c_answer[user -1] == c_answer[1]:
                print("Correct\n")
            
            else:
                print("Wrong\n")
        else:
            print("try to input\n")
    except ValueError:
        print("Invalid input\n")

