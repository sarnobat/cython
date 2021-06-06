from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser

# Path to your `.ged` file
file_path = 'rohidekar2.ged'

# Initialize the parser
gedcom_parser = Parser()

# Parse your file
gedcom_parser.parse_file(file_path)

print("1")

root_child_elements = gedcom_parser.get_root_child_elements()

print("2")
# Iterate through all root child elements
for element in root_child_elements:
    #print("3")

    # Is the `element` an actual `IndividualElement`? (Allows usage of extra functions such as `surname_match` and `get_name`.)
    if isinstance(element, IndividualElement):
        print("4")

        # Get all individuals whose surname matches "Doe"
        if element.surname_match('Rohidekar'):

            # Unpack the name tuple
            (first, last) = element.get_name()

            # Print the first and last name of the found individual
            print(first + " " + last)
