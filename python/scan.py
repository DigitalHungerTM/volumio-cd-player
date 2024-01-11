import json


def main():
    # all tags should have a unique id
    id = input("Put the tag on the scanner: ")
    album_title = input("What is the title of this album?\n")

    # rfid.write("album_title")

    album = {
        id: album_title
    }

    with open("database/database.json", "w") as outfile:
        json.dump(album, outfile)

if __name__ == "__main__":
    main()
