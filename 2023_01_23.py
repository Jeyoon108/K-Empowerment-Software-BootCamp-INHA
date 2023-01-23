# A to Z reminding

# Ch7 practice # 8 ~ # 9

surprise = ["Groucho", "Chico", "Harpo"]

surprise[-1] = surprise[-1].lower()
harpo_list = list(surprise[-1])
harpo_list.reverse()
surprise[-1] = ''.join(harpo_list).capitalize()
print(surprise)
