# Functions go here

# Puts seriesof symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):
    
    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end the statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# Checks user choice is 'integer', 'text' or 'image'
def user_choice():
    
    # Lists of vaild responses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture", "pic"]

    vaild = False
    while not vaild:
        
        # ask user for choice and change response to lowercase
        response = input("File type (integer / text / image): ").lower()

        # Checks for vaild response and redturns text, integer or image

        if response in text_ok:
            return "text"
        
        elif response in integer_ok:
            return "integer" 
      
        elif response in image_ok:
            return "image"
       
        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for an image: ")
            if want_integer == "":
                return "integer"
            else:
                return "image"
        
        else:
            # if response is not vaild, output an error
            print("Please choose a valid file type!")
            print()


# Main Routine goes here

# Heading
statement_generator("Bit Calculator for Integers, Text & Images", "-")

# Display intructions if user has not used the program before 

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # ask the user for the file type 
    
    # For integers, ask for integer
    # (must be an integer more than / equal to 0)

    # For images, ask for width and height
    #(must be integer more than / equal to 1)