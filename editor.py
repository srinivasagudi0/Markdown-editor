# write your code here
def plain(text):
    return text


def bold(text):
    return f"**{text}**"


def italic(text):
    return f"*{text}*"


def inline_code(text):
    return f"`{text}`"


def link(label, url):
    return f"[{label}]({url})"


def header(level, text):
    return f"{'#' * level} {text}\n"


def new_line():
    return "\n"


def unordered_list(rows, items):
    # items is a list of strings length rows
    result = ""
    for item in items:
        result += f"* {item}\n"
    return result


def ordered_list(rows, items):
    result = ""
    for i, item in enumerate(items, start=1):
        result += f"{i}. {item}\n"
    return result


def main():
    formatters = {
        "plain": plain,
        "bold": bold,
        "italic": italic,
        "inline-code": inline_code,
        "link": link,
        "header": header,
        "new-line": new_line,
        "ordered-list": ordered_list,
        "unordered-list": unordered_list,
    }

    output = ""

    while True:
        command = input("Choose a formatter: ")

        if command == "!help":
            print("Available formatters:", " ".join(formatters.keys()))
            print("Special commands: !help !done")

        elif command == "!done":
            # save the final output to output.md and exit
            try:
                with open('output.md', 'w') as outfile:
                    outfile.write(output)
            except IOError:
                # if writing fails, still exit
                pass
            break

        elif command not in formatters:
            print("Unknown formatting type or command")

        else:
            if command == "header":
                while True:
                    try:
                        level = int(input("Level: "))
                    except ValueError:
                        print("The level should be within the range of 1 to 6")
                        continue
                    if 1 <= level <= 6:
                        break
                    print("The level should be within the range of 1 to 6")
                text = input("Text: ")
                output += header(level, text)

            elif command == "link":
                label = input("Label: ")
                url = input("URL: ")
                output += link(label, url)

            elif command in ("ordered-list", "unordered-list"):
                # validate number of rows > 0
                while True:
                    try:
                        rows = int(input("Number of rows: "))
                    except ValueError:
                        print("The number of rows should be greater than zero")
                        continue
                    if rows > 0:
                        break
                    print("The number of rows should be greater than zero")

                items = []
                for i in range(1, rows + 1):
                    item = input(f"Row #{i}: ")
                    items.append(item)

                if command == "ordered-list":
                    output += ordered_list(rows, items)
                else:
                    output += unordered_list(rows, items)

            elif command == "new-line":
                output += new_line()

            else:
                text = input("Text: ")
                output += formatters[command](text)

            print(output)


if __name__ == "__main__":
    main()
