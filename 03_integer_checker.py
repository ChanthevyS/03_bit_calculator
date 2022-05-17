# checks input is a number more than a givin value
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

# Main Rountine goes here

keep_going = ""
while keep_going == "":
    print()
    # Ask user for an integer (must be more than / equal to 0)
    var_integer = num_check("Enter an integer:", 0)
    print()

    # Ask for width of an image
    # (must be more than / equal to 1)
    image_width = num_check ("Image width? ", 1)
    print()
    image_height = num_check ("Image height? ", 1)
