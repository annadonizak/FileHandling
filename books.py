import csv

FILEPATH = 'books.csv'


def read_books(file_path):
    books = []
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append(row)
    return books


def extract_unique_genre(books):
    return set([b['Genre'] for b in books])


def filter_books_by_genre(books, genre):
    return [book for book in books if book['Genre'] == genre]


def save_books_to_file(books, genre):
    genre_lowercased = genre.lower().replace(' ', '-')
    file_path = f'books_{genre_lowercased}.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        for book in books:
            file.write(f"{book['Title']}, {book['Author']}, {book['Genre']}, {book['Year']}\n")
    return file_path


def process_genre(books, genre):
    genre_books = filter_books_by_genre(books, genre)
    file_path = save_books_to_file(genre_books, genre)
    print(f"Saved {len(genre_books)} books to {file_path}")


def main():
    books = read_books(FILEPATH)
    genre = extract_unique_genre(books)

    for g in genre:
        process_genre(books, g)


if __name__ == "__main__":
    main()