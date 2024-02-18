class Library:
    def __init__(self, file_path):
        self.file_path = file_path

    def __del__(self):
        pass 

    def list_books(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                lineSerious = line.split(",")
                book_info = {}
                for info in lineSerious:
                    key, value = info.strip().split("=")
                    book_info[key] = value
                for key, value in book_info.items():
                    print(f"{key}: {value}")

    def add_book(self, bookName, author, relaseDate, pages):
        with open(self.file_path, "a") as library:
            library.write(f"bookName={bookName},author={author},relaseDate={relaseDate},pages={pages}\n")

    def remove_book(self, bookValue):
        updated_lines = []

        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            lineSerious = line.split(",")
            book_info = {}
            for info in lineSerious:
                key, value = info.strip().split("=")
                book_info[key] = value

            if 'bookName' in book_info and book_info['bookName'] == bookValue:
                continue

            updated_lines.append(line)

        with open(self.file_path, 'w') as file:
            file.writelines(updated_lines)

        print(f"{bookValue} isimli kitap başarıyla silindi.")


lib = Library("books.txt")

while True:
    print("*** MENU***")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Sil")
    print("4) Çıkış")

    value = input("Yapmak istediğiniz işlemi seçiniz (1-4): ")

    if value == "1":
        lib.list_books()
    elif value == "2":
        bookName = input("Kitap ismi giriniz:")
        author = input("Yazar adı girin:")
        relaseDate = input("Verilme tarihi:")
        pages = input("Sayfa sayısı:")
        lib.add_book(bookName, author, relaseDate, pages)
    elif value == "3":
        bookValue = input("Silmek istediğiniz kitabın adını giriniz: ")
        lib.remove_book(bookValue)
    elif value == "4":
        break
    else:
        print("Geçersiz seçenek. Lütfen tekrar deneyin.")




