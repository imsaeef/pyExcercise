sub_list = ['physics','chemistry','biology','highermath','computer','ICT']
print(sub_list)
dislike = input("whice of these subjects do you dislike: ")
remove = sub_list.index(dislike)
del sub_list[remove]
print(sub_list)
