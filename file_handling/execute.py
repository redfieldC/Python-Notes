# #Add new information to the file
# new_info = "This is new information to be added."
# with open("example.txt", 'a') as file:
#     file.write(new_info + '\n')


# add information to a particular line
# file_path = 'example.txt'  # Replace with your file's path
# line_number_to_add_to = 1  # Change this to the line number where you want to add content
# new_content = "This is for itvedant" + '\n'

# with open(file_path, 'r') as file:
#     lines = file.readlines()

# if 1 <= line_number_to_add_to <= len(lines):
#     lines.insert(line_number_to_add_to-1, new_content)

# with open(file_path, 'w') as file:
#     file.writelines(lines)



# Update a specific line in the file
# line_number_to_update = 1  # Change this to the line number you want to update
# new_data = "Below is information on Ameya Potdar"

# with open("example.txt", 'r') as file:
#     lines = file.readlines()

# if 1 <= line_number_to_update <= len(lines):
#     lines[line_number_to_update - 1] = new_data + '\n'

# with open("example.txt", 'w') as file:
#     file.writelines(lines)


# Delete a particular Line
# file_path = 'example.txt'  # Replace with your file's path
# line_number_to_delete = 2  # Change this to the line number you want to delete

# with open(file_path, 'r') as file:
#     lines = file.readlines()

# if 1 <= line_number_to_delete <= len(lines):
#     del lines[line_number_to_delete - 1]

# with open(file_path, 'w') as file:
#     file.writelines(lines)

with open("example.txt", 'r') as file:
    lines = file.readlines()
    print(lines)