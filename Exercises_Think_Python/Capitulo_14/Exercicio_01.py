import os
def main():
    def walkthrought(d_path):
        direcs=list(os.walk(d_path))
        direcs.sort()
        for actual_directory in direcs:
            print(actual_directory[2])
            bellow_directories=actual_directory[1]
            print("----------------------".center(50))
            print(bellow_directories)
            if bellow_directories != []:
                walkthrought(bellow_directories[0])
            else:
                print(actual_directory[0])
        return 0
    walkthrought('/home/maxssdlinux/Documentos/Books_exercices_repository/Exercises_Think_Python')
if __name__=='__main__':
    main()