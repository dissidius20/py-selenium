
# message = ' little,'
# message2 = ' little indians'

# for x in range(1,11):
#     if x % 3 == 0:
#         print(x, message2)
#     elif x == 10:
#         print(x, ' little indian boys')
#     else:
#         print(x, message)
        
# friends = ['josh', 'jed', 'leo', 'kevin', 'jof']

# for friend in friends:
#     print(f'Hello, {friend}!')
# else:
#     print('Hello everyone!')


# score = input('Enter your score" ')
# score = int(score)


# def ifPassed(number):
#     if number >= 50:
#         print('passed')
#     else:
#         print('failed')

# ifPassed(score)

# sentence = 'dog chased boy'

# print(sentence)

# print(' '.join(sentence.split()[::-1]))


# values = [10, 9, 8, 7, 6, 5, 'hello', 4, 3, 2, 1, 0]

# for value in values:
#     try:
#         print(10 / int(value))
#     except ValueError:
#         print('Value Error')
#     except Exception as e:
#         print(str(e))




from array import *


subjects = 0



# Calculate GWA
def calculate(numberOfSubjects, units, grade):
    print('Hello')

def main():
    try:
        subjects = int(input('Enter number of subjects: '))
        if subjects > 0 and subjects <= 20:
            grade_arr = arr
        else:
            print('Please enter a valid number of subjects per semester.')
            main()
    except ValueError as e:
        print('Invalid input. Please enter only numbers.')
        main()
    except Exception as e:
        print('Unknown error occured.')
        print(e)
        main()

    


main()
    

