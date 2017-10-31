CN_mobile = [134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,187,188,147,178,1705]
CN_union = [130,131,132,155,156,185,186,145,178,1709]
CN_telecom = [133,153,180,181,189,177,1700]
def phone_number_check():
    number = input('Enter Your Number :')
    while len(number) < 11:
        print('Invalid length, your number should be in 11 digits')
        number = input('Enter Your Number :')
    num1 = int(number[0 : 3])
    num2 = int(number[0 : 4])
    if num1 in CN_mobile or num2 in CN_mobile:
        print('Operator : {}'.format('CN_mobile'))
        print('We\'re sending verification code via text to your pohone:' + number)
    elif num1 in CN_union or num2 in CN_union:
        print('Operator : {}'.format('CN_union'))
        print('We\'re sending verification code via text to your pohone:' + number)
    elif num1 in CN_telecom or num2 in CN_telecom:
        print('Operator : {}'.format('CN_telecom'))
        print('We\'re sending verification code via text to your pohone:' + number)
    else:
        print('No such an operator')
        phone_number_check()

phone_number_check()
