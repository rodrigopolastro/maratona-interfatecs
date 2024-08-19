##Simple Documentation About Our First Attempt at a File Comparator Programming    

CORRECT FILE FORMAT   

A - exercises folder documentation  

1 - The exercises folder needs to contains subfolders for all exercises you want to compare.  
2 - Inside this exercises folder, you need create another folder with the same name as the file you want to compare.  
3 - Inside folder with the name of your exercise, you need another two folders with the name 'in' and the name 'out', meaning 'input requisitions' and 'output expected'  
4 - Inside of this two folders, the files should have the same name in both folders with a '.txt' extension, additionally, the filenames should include a numeric character.  
something like this -> 'exercise_name1.txt'  
PS: The files do not necessarily need to have the prefix 'in' in the filename, the files should simply be located in the 'in' folder for inputs and the 'out' folder for outputs.  


CORRECT FILE FORMAT (file to be compared)  

1 - The file can't include security conditional (guard clause) "if __name__ == '__main__'" , and it MUST execute upon being imported.  
