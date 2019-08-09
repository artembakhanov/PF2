from task5 import freq_analysis

file_name = input()
f = open(file_name, 'r')
text = f.read()
f.close()

items = freq_analysis(text)
print(f"{items[0][0]} {items[0][1] / len(text) * 100 : .3f}%")
print(f"{items[1][0]} {items[1][1] / (len(text)) * 100 : .3f}%")
