from csv import reader
import json


def get_user_list():
    with open("./files/users.json") as users_fd:
        return json.load(users_fd)


def get_book_list():
    with open("./files/books.csv", newline='') as books_fd:
        readers = reader(books_fd)
        header = next(readers)
        book_list = []
        for row in readers:
            book_list.append((dict(zip(header, row))))

        return book_list


if __name__ == "__main__":

    full_user_list = get_user_list()
    short_user_list = []

    for user in full_user_list:
        short_user_list.append({"name": user["name"], "gender": user["gender"], "address": user["address"],
                                "age": user["age"], "books": []})

    print(short_user_list)

    user_num = 0

    for book in get_book_list():

        short_user_list[user_num]["books"].append(book)

        user_num += 1

        if user_num > len(full_user_list) - 1:
            user_num = 0

    with open("./files/user_list.json", "w") as user_json:
        json.dump(short_user_list, user_json, indent=4)
