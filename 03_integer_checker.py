# checks input is a number more than zero
def num_check(question, low):
    vaild = False 
    while not vaild:

        error = "Please enter a number that is more than"
        "(or equal to) {}".format(low)

        try:

            # asks user to enter a number
            response = int(input(question))
                
            # checks number is more than zero
            if response >= low:
                return response 

            # outputs error if input is invaild
            else: 
                print(error) 
                print()

        except ValueError:
            print(error)