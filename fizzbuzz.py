for i in range(51):
    if(i%3==0):
        print(str(i)+"=fizz")
    else:
        if(i%5==0):
            print(str(i)+"= buzz")
        else:
            if(i%3==0 and i%5==0):
                print(str(i)+"= fizzbuzz")
            else:
                print(str(i))
def fizzbuzz(r):
    for i in range(1,r):
        if(i%3==0 and i%5==0):
            print(str(i)+"= fizzbuzz")
        else:
            if(i%3==0):
                print(str(i)+"= fizz")
            else:
                if(i%5==0):
                    print(str(i)+"= buzz")
                else:
                    print(str(i))