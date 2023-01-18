from project import isSpam

while True:
    prediction = isSpam(input('Email Contents: '))
    print(str(prediction[0][0]*100) + '% chance of being spam.')
    print('Follow me at @CompanySynapse!')
