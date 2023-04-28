# by default the open() will open the file in read mode, but to write into a file you have to specify the mode
# 'w' mode will delete old data of file and add new one

with open("my_file.txt", mode="w") as file:
    file.write("New text.")
