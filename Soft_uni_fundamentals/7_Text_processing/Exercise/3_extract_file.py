entry = input().split(".")
extension = entry[-1]
name = entry[-2].split('\\')
print(f"File name: {name[-1]}\nFile extension: {extension}")
