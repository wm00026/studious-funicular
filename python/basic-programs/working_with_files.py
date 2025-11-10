"""
This is a basic program to work with a file

It reads the contents of a file and counts the lines and vowels of the file.

This program uses several principles of file handling in Python, including:
- Opening and closing files
- Reading file contents
- Handling exceptions related to file operations

@author wm00026
"""


"""
file_reader 
@param file_path: String - path to the file to be read
@return: String - contents of the file
"""
def file_reader(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

    except (FileNotFoundError):
        print("The file was not found")
        return None
    except (IOError):
        print("An error occurred while reading the file")
        return None
    return content


"""
count_lines
@param content: String - the contents of the file
@return: Integer - number of lines in the content
"""
def count_lines(content):
    if content is None:
        return 0
    return len(content.splitlines())

"""
count_vowels
@param content: String - the contents of the file
@return: Integer - number of vowels in the content
"""
def count_vowels(content):
    if content is None:
        return 0
    vowels = 'aeiouAEIOU'
    return sum(1 for char in content if char in vowels)

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    content = file_reader(file_path)
    print("\n", content)

    if content is not None:
        lines = count_lines(content)
        vowels = count_vowels(content)
        print(f"Number of lines: {lines}")
        print(f"Number of vowels: {vowels}")
    else: 
        print("No content to analyze.")

