from perpus_item import Book
from pengguna import Member, Staff

# A class to manage the borrowing transactions between members and staff
class BorrowTransaction:
    def __init__(self, book, member, staff, borrow_date):
        self.book = book
        self.member = member
        self.staff = staff
        self.borrow_date = borrow_date
        self.returned = False

    def borrow_book(self):
        if self.book.borrow():
            print(f"Berhasil: {self.book.title} dipinjam oleh {self.member.name}")
        else:
            print(f"Gagal: {self.book.title} sedang dipinjam.")

    def return_book(self):
        self.book.return_book()
        self.returned = True

if __name__ == "__main__":
    buku_sejarah = Book("Buku Sejarah", "Penulis A", "ISBN-001")
    member_bilal = Member("M. Bilal", "M-001")
    staff_liza = Staff("Buk Liza", "S-001")

    bukti_pinjam_bilal = BorrowTransaction(buku_sejarah, member_bilal, staff_liza, "20-02-2026")

    bukti_pinjam_bilal.borrow_book()
