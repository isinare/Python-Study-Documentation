while True:
    try:
        age = int(input('what is your age'))
        10/age
    except ZeroDivisionError:
        print('please enter a higher value')
    except ValueError:
        print('please enter a valid value')
    else:
        print('Welcome to the beta participation')
        break
    finally:
        print('Thank your for your co-operation we hope you have liked our beta project')
        print('LogOut Successful')

stage = str(age)
print('Your age is currently' + ' ' + stage)

if age < 18:
     print('You aren\'t allowed here')
if age > 18:
    print('You are allowed here')
