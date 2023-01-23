# A to Z reminding

# Ch5 practice # 4

salutation = 'Mr.'
name = 'Kim'
product = 'pen'
verbed = 'broken'
room = 'room'
animals = 'dogs'
amount = 'account'
percent = '100'
spokesman = 'Jason'
job_title = 'CEO'

letter = '''Dear {} {},
    Thank you for your letter. We are sorry that our {} \
{} in your {}. Please note that it should never \
be used in a {}, especially near any {}.

    Send us your receipt and {} for shipping and handling. \
We will send you another {} that, in our tests, \
is {}% less likely to have {}.

    Thank you for your support.
    Sincerely,
    {}
    {}'''.format(salutation, name, product, verbed, room, room, animals, amount, product, percent, verbed, spokesman, job_title)

print(letter)
