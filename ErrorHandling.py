file_name=input("Enter the name of the file:")

try:
    with open(file_name,"r") as file:   #opening the file  using "with" to prevent potential leaks. "r" signifies read mode
        content=file.read()             #.read(): reads the entire file

        modified=content.upper()        #.upper(): modifieds the content to be in uppercase
        modified=modified.replace("HELLO","BONJOUR")     #.replace() modifies the content by replacing the old text with the new one
        modified= modified + "This is the last line"     #Adds a line (text) at the end of the file

        modified_version=f"*==ORIGINAL FILE:{file_name}*\n" + content + "\n\n*MODIFIED FILE*\n" + modified      #Joining both the original and modifications into one

        with open("modified_"+ file_name, "w") as new_file: #opening the modified file in write "w" mode
           new_file.write( modified_version)

        print("Original file (myfile.txt) has been modified successfully and saved as (modified_myfile.txt)")  #success message after successful modification

except FileNotFoundError:
    print("File not found. Please check the filename")
except PermissionError:
    print("Permission denied")


