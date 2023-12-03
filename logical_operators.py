# available logical operators
#
# < less than
# > greater than
# <= less than or equal
# >= greater than or equal
# == equals
# != not equals

password = input('Do you know the secret password? ')
if password != '--secret':
    print('not correct')
else:
    print('correct password')

# boolean values can have 1 or 2 values True or False, no quotes or it will become a string
# True or False are only variables available in boolean
# REMEMBER "= is signing value" and "== is checking equality"

if 2 == 2:
    print('true')
