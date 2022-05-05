# Functions go here

# Puts seriesof symbols at start and end of text (for emphasos)
def statement_generator(text, decoration):
    
    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end the statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# Main Routine goes here
statement_generator("look - stars", "*")