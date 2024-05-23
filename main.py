# File Copyright (c) 2024 GojoGitHub, four4tReS
# MIT License


import os
from abc import ABC, abstractmethod

# Default constants

# Be careful, some files aren't utf-8 encoded
ENCODING = "utf-8"


class Language:
    def __init__(self,
                 enter_file_path,
                 content,
                 enter_file_content,
                 file_was_removed,
                 file_does_not_exist,
                 enter_path,
                 help_article,
                 exiting,
                 unknown_command,
                 type_help):
        self.ENTER_FILE_PATH = enter_file_path
        self.CONTENT = content
        self.ENTER_FILE_CONTENT = enter_file_content
        self.FILE_WAS_REMOVED = file_was_removed
        self.FILE_DOES_NOT_EXIST = file_does_not_exist
        self.ENTER_PATH = enter_path
        self.HELP_ARTICLE = help_article
        self.EXITING = exiting
        self.UNKNOWN_COMMAND = unknown_command
        self.TYPE_HELP = type_help


class Command(ABC):
    def __init__(self, language):
        self.language = language

    @abstractmethod
    def exec(self):
        pass


class Read(Command):
    def exec(self):
        file_path = input(f"{self.language.ENTER_FILE_PATH}")

        if os.path.exists(file_path):
            file = os.path.join(file_path)

            # 'r' means read mode
            with open(file, 'r', encoding=ENCODING) as opened_file:
                print(f"{self.language.CONTENT}\n{opened_file.read()}")
        else:
            print(f"{self.language.FILE_DOES_NOT_EXIST}")


class Write(Command):
    def exec(self):
        file_path = input(f"{self.language.ENTER_FILE_PATH}")

        file = os.path.join(file_path)

        # 'w' means write mode
        with open(file, 'w', encoding=ENCODING) as opened_file:
            content = input(f"{self.language.ENTER_FILE_CONTENT}")
            opened_file.write(content)
            opened_file.close()


class Delete(Command):
    def exec(self):
        file_path = input(f"{self.language.ENTER_FILE_PATH}")

        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{self.language.FILE_WAS_REMOVED}")
        else:
            print(f"{self.language.FILE_DOES_NOT_EXIST}")


class Dir(Command):
    def exec(self):
        path = input(f"{self.language.ENTER_PATH}")
        print(os.listdir(path))


class AppendingWriting(Command):
    def exec(self):
        file_path = input(f"{self.language.ENTER_FILE_PATH}")

        file = os.path.join(file_path)

        # 'a' means appending write mode
        with open(file, 'a', encoding=ENCODING) as opened_file:
            content = input(f"{self.language.ENTER_FILE_CONTENT}")
            opened_file.write(content)
            opened_file.close()


class Help(Command):
    def exec(self):
        print(f"{self.language.HELP_ARTICLE}")


class Main:
    def __init__(self):
        self.is_running = True

        self.language = self.get_language()

        self.read = Read(self.language)
        self.write = Write(self.language)
        self.delete = Delete(self.language)
        self.dir = Dir(self.language)
        self.writea = AppendingWriting(self.language)
        self.help = Help(self.language)

        print("File Copyright (c) 2024 GojoGitHub, four4tReS")
        print(f"{self.language.TYPE_HELP}")

        while self.is_running:
            self.handle_commands()

    def get_language(self):
        match input(f"Choose the language [en/ru]: "):
            case "en":
                return Language("Enter file path: ",
                                "Content: ",
                                "Enter file content: ",
                                "File was removed.",
                                "File doesn't exist.",
                                "Enter path: ",
                                "read | cat - Displays the content of the file on the screen.\n" +
                                "write - Replaces the contents of the file.\n" +
                                "delete | remove | del | rm - Removes file.\n" +
                                "dir | ls - Displays a list of files and directories.\n" +
                                "writea | Appends the contents of the file.\n" +
                                "help | Gives this article.\n" +
                                "quit | exit | q - Exits the program.",
                                "Exiting the program...",
                                "Unknown command.",
                                "Type help to get help.")
            case "ru":
                return Language("Введите путь до файла: ",
                                "Содержимое: ",
                                "Введите содержимое файла: ",
                                "Файл был удален.",
                                "Файл не найден.",
                                "Введите путь: ",
                                "read | cat - Выводит на экран содержимое файла.\n" +
                                "write - Заменяет содержимое файла.\n" +
                                "delete | remove | del | rm - Удаляет файл.\n" +
                                "dir | ls - Отображает список файлов и каталогов.\n" +
                                "writea | Добавляет к содержимому файла.\n" +
                                "help | Выдает эту статью.\n" +
                                "quit | exit | q - Выход из программы.",
                                "Выход из программы...",
                                "Неизвестная команда.",
                                "Введите help чтобы получить справку.")
            case _:
                print("This language is not currently supported.")
                self.is_running = False

    def handle_commands(self):
        match input("$ "):
            case "read" | "cat":
                self.read.exec()
            case "write":
                self.write.exec()
            case "delete" | "remove" | "del" | "rm":
                self.delete.exec()
            case "dir" | "ls":
                self.dir.exec()
            case "writea" | "append":
                self.writea.exec()
            case "help":
                self.help.exec()
            case "quit" | "exit" | "q":
                print(f"{self.language.EXITING}")
                self.is_running = False
            case _:
                print(f"{self.language.UNKNOWN_COMMAND} {self.language.TYPE_HELP}")


if __name__ == "__main__":
    Main()
