"""
File I/O
'w' -> Write-Only Mode
'r' -> Read-Only Mode
'r+' -> Read and Write Mode
'a' -> Append Mode
"""
#
#
# print("*****____ How to Write to a File ____*****")
# my_list = [1, 2, 3]
#
# my_file = open("firstwritefile.txt", "w")
#
# for item in my_list:
#     my_file.write(str(item))
#
# my_file.close()

print("*****____ How to Read a File ____*****")

"""
File I/O
Readinga  file -> .read()
Reading line by line -> .readline()
"""


my_files = open("firstwritefile.txt", 'r')

print(str(my_files.read()))
my_files.close()

my_file_line = open("firstwritefile.txt", 'r')
print(str(my_file_line.readline()))
my_file_line.close()

print("************ File Handling using 'with' and 'as' Keywords *************")
print("With As Write")

with open("withas.txt", "w") as with_as_write:
    with_as_write.write("This is an example of 'with' and 'as' for file handling for write/read")

with open("withas.txt", "r") as with_as_read:
    print(str(with_as_read.read()))



