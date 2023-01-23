# A to Z reminding

# Ch5 practice # 1

song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""

song = song.replace(' m', ' M')

print(song)

# Ch5 practice # 2
print()

questions = ["We don't serve strings around here. Are you a string?",
             "What is said on Father's Day in the forest?",
             "What makes the sound 'Sis! Boom! Bah!'?"
             ]
answers = ["An exploding sheep.",
           "No, I'm a frayed knot.",
           "'Pop!' goes the weasel."
           ]

for k in range(3):
    print(f'Q : {questions[k]}\nA : {answers[k]}')

# Ch5 practice # 3
print()

a = 'roast beef'
b = 'ham'
c = 'head'
d = 'clam'

print("My kitty cat likes %s, My kitty cat likes %s, My kitty cat fell on his %s \
And now thinks he's a %s." % (a, b, c, d))
