def division(x, y):
    try:
        resultOfDivision = x / y
        return(resultOfDivision)
    except ZeroDivisionError:
        return('The division by zero is not allowed')

s = input().split()
operators = {'+', '-', '*', '/'}
while s != ['quit']:
    try:
        x = float(s[0])
        y = float(s[2])
        operator = s[1]
        if operator not in operators:
            print(operator, 'is not a valid operator')
        else:
            match(operator):
                case '+':
                    print(x + y)
                case '-':
                    print(x - y)
                case '*':
                    print(x * y)
                case '/':
                    print(division(x, y))
    except ValueError:
        print('Value error, please, enter numbers')
    except TypeError:
        print('Type error')
    except Exception:
        print('Error')
    finally:
        s = input().split()
