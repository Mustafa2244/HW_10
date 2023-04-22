from collections import UserDict


class Field:
    def __init__(self, value=None):
        self.value = value


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)


class Record:
    def __init__(self, name: Name, phones: list[Phone] = []):
        self.name = name
        self.phones = phones

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        for my_phone in self.phones:
            if my_phone.value == phone:
                self.phones.remove(my_phone)

    def update_phone(self, old_phone, new_phone):
        for my_phone in self.phones:
            if my_phone.value == old_phone:
                my_phone.value = new_phone


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record


def input_error(func):
    def decorator_with_arguments(command=""):
        try:
            res = func(command)
            if res is None:
                return "Phone not found"
        except KeyError:
            return "KeyError"
        except ValueError:
            return "Phone not number"
        except IndexError:
            return "Give me name and phone please"
        return res
    return decorator_with_arguments


telephone_book = AddressBook()


def hello():
    return "How can I help you?"


@input_error
def add(command):
    name = command.split(" ")[1]
    phone_number = command.split(" ")[2]
    telephone_book.add_record(Record(Name(name), [Phone(phone_number)]))
    return "Phone was successfully added"


@input_error
def change(command):
    for key in telephone_book.keys():
        if key == command.split(" ")[1]:
            telephone_book[key].update_phone(telephone_book[key].phones[0].value, command.split(" ")[2])
    return "Phone was successfully changed"


@input_error
def phone(command):
    for user in telephone_book.keys():
        if user == command.split(" ")[1]:
            return ", ".join([ph.value for ph in telephone_book[user].phones])


def show_all():
    result = []
    for user in telephone_book:
        result.append(f"{user}: {', '.join([ph.value for ph in telephone_book[user].phones])}")
    return "\n".join(result)


def main():
    while True:
        command = input().lower()
        if command == "hello":
            print(hello())
        elif command.split(" ")[0] == "add":
            print(add(command))
        elif command.split(" ")[0] == "change":
            print(change(command))
        elif command.split(" ")[0] == "phone":
            print(phone(command))
        elif command == "show all":
            print(show_all())
        elif command == "exit" or command == "close" or command == "good bye" or command == ".":
            print("Good bye!")
            return


if __name__ == '__main__':
    main()
