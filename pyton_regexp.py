import re
import pprint

# print "Testing regexp\n"

string_search = "This is a best test!!!"
match = re.match('This', string_search)
pprint.pprint(match.group(0))
print match.group(0)


print '\nSubstitution\n'

string_substitute = "Substitution of all tall mall!"
subst = re.sub( '([a-z]all)', '||-||', string_substitute)
print subst
print string_substitute