# A Member class to represent a library user
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

class Staff:
    def __init__(self, name, staff_id):
        self.name = name

        self.staff_id = staff_id
