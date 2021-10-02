from gedcom.element.individual import IndividualElement
from gedcom.element.root import RootElement
from gedcom.parser import Parser

# Path to your `.ged` file
file_path = 'rohidekar2.ged'

gedcom_parser = Parser()
gedcom_parser.parse_file(file_path)

root_child_elements = gedcom_parser.get_root_child_elements()

for element in root_child_elements:

    if isinstance(element, IndividualElement):

        # Get all individuals whose surname matches "Doe"
        if element.surname_match('Rohidekar'):

            # Unpack the name tuple
            (first, last) = element.get_name()

            # Print the first and last name of the found individual
            print(first + " " + last)

            for familyElement in gedcom_parser.get_families(element):
                print("5")
                
#    if isinstance(element, RootElement):
#        print("6")

root_element = gedcom_parser.get_root_element()
print(type(root_element))
#print(root_element.to_gedcom_string(True))
#print(root_element.get_pointer())
#print(root_element.get_individual())
#print(root_element.get_child_elements())
# (first, last) = root_element.get_name()
# print(first + " " + last)
    
elemDict = gedcom_parser.get_element_dictionary()

rootElem = elemDict.get("@I29@") # Venkat Rao Rohidekar
(first, last) = rootElem.get_name()
print(first + " " + last)
families = gedcom_parser.get_families(rootElem)
print(len(families))
print(families[0])