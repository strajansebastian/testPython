import re
import pprint

# print "Testing regexp\n"

string_search = "This is the best test!!!this This THIS tHIS"
match = re.search('This', string_search)
pprint.pprint(match.group(0))
print match.group(0)

string_search = "This is the best test!!!this This THIS tHIS"
match = re.match(r'(?P<THS>This) (is)', string_search)
print match.group(0)
print match.group(1, 2)
print 'Name: ', match.group('THS')

string_search = "This is the best test!!!this This THIS tHIS"
match = re.findall('This', string_search, re.IGNORECASE)
print match


print '\nSubstitution\n'

string_substitute = "Substitution of all tall mall!"
subst = re.sub( '([a-z]all)', '||-||', string_substitute)
print subst
print string_substitute