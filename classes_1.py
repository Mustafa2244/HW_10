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
