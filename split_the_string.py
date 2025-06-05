def split_and_join(line):
    # Split the string into a list using space as the delimiter
    line = line.split(" ")
    # Join the list using '-' as the delimiter
    return "-".join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)