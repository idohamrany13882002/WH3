# STA
score: int = int(input('enter your grade: '))
match score:
    case score if 0<=score<=40:
        print('try harder next time...')
    case score if 41 <= score <= 60:
        print("you're getting there, need some more work")
    case score if 61 <= score <= 80:
        print("pretty good")
    case score if 81 <= score <= 95:
        print("awesome!")
    case score if 96 <= score <= 100:
        print("excellent!!! you're a star!")
    case score if 0>score>100:
        print("illegal grade")
# END
