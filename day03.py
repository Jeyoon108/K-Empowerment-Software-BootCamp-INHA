# practice #1 - m으로 시작하는 단어를 대문자로 만들어보자.
song_1 = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""

print(song_1.replace(' m',' M'))

# or

song_2 = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""

song_list = song_2.split()
song_list[14] = song_list[14].title()
song_string = ' '.join(song_list)
print(song_string.replace(', ',',\n'))