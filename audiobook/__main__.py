import argparse
import os.path

from main import BOOK_DIR, AudioBook

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AudioBook - listen to any PDF book")
    parser.add_argument(
        "-l", "--library", action="store_true", help="get all books in library"
    )
    parser.add_argument(
        "-c",
        "--create-json",
        action="store_true",
        help="create json file from input file",
    )
    parser.add_argument(
        "-s",
        "--save-audio",
        action="store_true",
        help="save audio files from input file",
    )
    parser.add_argument(
        "-r", "--read-book", action="store_true", help="read the book from input file"
    )
    parser.add_argument("path", nargs="?", default=None, help="book file path")

    args = parser.parse_args()

    if args.path and not os.path.isfile(args.path):
        if os.path.isfile(os.path.join(BOOK_DIR, args.path)):
            args.path = os.path.join(BOOK_DIR, args.path)
        else:
            print(f"{args.path} is not a valid file")

    ab = AudioBook()
    if args.library:
        ab.get_library()
    elif args.create_json and args.path:
        ab.create_json_book(args.path)
    elif args.save_audio and args.path:
        ab.save_audio(args.path)
    elif args.path:
        ab.read_book(args.path)
    else:
        ab.get_library()
        print("Use `python audiobook -h` to see all valid options")
