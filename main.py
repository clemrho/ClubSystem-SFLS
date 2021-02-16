#powered by Lucas Lu@SFLS
#finished at 2021.2.16

import core 

def main():
    core.printMenu()

    #好贱！！！
    MostImportantKey=input("here: ")


    if MostImportantKey=='1':
        core.consult()
    elif MostImportantKey=='2':
        #core.alterif()
        print('gun!')
    elif MostImportantKey=='3':
        core.adminAdd()
    elif MostImportantKey=='4':
        core.adminAlterif()
    elif MostImportantKey=='5':
        core.adminKillStalin()
    else:
        print("gun!")

    if MostImportantKey!='6':        
        main()
        
if __name__=='__main__':
    main()