# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized.

# Examples
# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
import re
camellCaseTextTable = []

# to_camel_case('the_stealth_warrior') did not return correct value: 'TheStealthWarrior' should equal 'theStealthWarrior'

from re import compile as reCompile

PATTERN = reCompile(r'(?i)[-_]([a-z])')

def to_camel_case(text):
    return PATTERN.sub(lambda m: m.group(1).upper(), text)

print to_camel_case("A-B-C")
