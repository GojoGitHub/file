import os
print("ru eng")
locale = input()
if locale == ("eng"):
    while True:
        print("read for read file ONLY TXT FILES")
        print("write for change file ONLY TXT FILES")
        print("delete for delete file")
        print("dir for print files in directory")
        print("writea for change file without delete previous or create new file text ONLY TXT FILES")
        arg = input("")
        if arg == ("read"):
            print("file path")
            file_path = input()
            print("file name with extension file.txt")
            file = input()
            fileread = os.path.join(file_path, file)
            with open(fileread, 'r', encoding='utf-8') as fil:
                content = fil.read()
                print("file containting:")
                print(content)
        if arg == ("write"):
             print("file path")
             file_path = input()
             print("file name with extension file.txt")
             file = input()
             fileread = os.path.join(file_path, file)
             with open(fileread, 'w', encoding='utf-8') as fil:
                text = input("new text")
                fil.write(text)
                fil.close()
        if arg == ("delete"):
             print("filename with path path/filename.extension")
             filedel = input()
             if os.path.exists(filedel):
                os.remove(filedel)
                print(f"file {filedel} sucesfully deleted.")
                            
        if arg == ("dir"):
            print("path")
            pathf = input()
            print(os.listdir(pathf))
        if arg == ("writea"):
             print("file path")
             file_path = input()
             print("file name with extension file.txt")
             file = input()
             fileread = os.path.join(file_path, file)
             with open(fileread, 'a', encoding='utf-8') as fil:
                print("new text")
                text = input()
                fil.write(text)
                fil.close()
if locale == ("ru"):
    while True:
            print("read для вывода текста из файла ТОЛЬКО TXT ФАЙЛЫ")
            print("write для изменения текста в файле на новый ТОЛЬКО ТХТ ФАЙЛЫ")
            print("delete для удаления файла")
            print("dir для вывода файлов в директории")
            print("writea для добавления текста в файле без удаления предыдущего ТОЛЬКО ТХТ ФАЙЛЫ")
            arg = input("")
            if arg == ("read"):
                print("директория файла")
                file_path = input()
                print("имя файла с расширением напрмиер file.txt")
                file = input()
                fileread = os.path.join(file_path, file)
                with open(fileread, 'r', encoding='utf-8') as fil:
                    content = fil.read()
                    print("файл содержит")
                    print(content)
            if arg == ("write"):
                print("директория файла")
                file_path = input()
                print("имя файла с расширением например file.txt")
                file = input()
                fileread = os.path.join(file_path, file)
                with open(fileread, 'w', encoding='utf-8') as fil:
                    text = input("новый текст")
                    fil.write(text)
                    fil.close()
            if arg == ("delete"):
                print("директория файла с названием и расширением например директория/файл.расширение")
                filedel = input()
                if os.path.exists(filedel):
                    os.remove(filedel)
                    print(f"файл {filedel} успешно удален.")
                                
            if arg == ("dir"):
                print("директория")
                pathf = input()
                print(os.listdir(pathf))
            if arg == ("writea"):
                print("директория файла")
                file_path = input()
                print("имя файла с расширением напрмиер file.txt")
                file = input()
                fileread = os.path.join(file_path, file)
                with open(fileread, 'a', encoding='utf-8') as fil:
                    print("текст")
                    text = input()
                    fil.write(text)
                    fil.close()
else:
    if locale == ("eng"):
        print("error")
    if locale == ("ru"):
        print("ошибка")
    else:
        print("language is not supporting")
