import argparse


def superdiff(input, modified):
    """
    This function compares two files. It checks if the lines of input file are
    included in the modified file. If yes, adds 0. If not, adds -. Next, we go
    through rest of the lines in the modified file and add them(with a + sign)
    to the output list.

    Args:
        input: first input file- original file
        modified: second modified file- modified file

    Returns:
        output(array): list of lines with either +,- or 0 in the beginning
    """
    output = input

    for i in input:
        if i in modified:
            # adds 0 in the beginning of the line
            output[input.index(i)] = "0 " + i
            modified[modified.index(i)] = True
        else:
            # if the line is not there add -
            output[input.index(i)] = "- " + i

    for y in modified:
        if not y:
            # adds the line to output with a + sign
            output.insert(modified.index(y), "+ " + y)
    return output


def strip_newline(list):
    """
    Getting rid of "\n" at the end of each element in list since
    list() function adds it automatically.
    """
    array = []
    for elem in list:
        array.append(elem.rstrip())
    return array


def main():
    # just an argparse to have a command line interface
    parser = argparse.ArgumentParser(description="SuperDiff")
    # it is required to have exactly to arguments
    parser.add_argument("-f", "--files",
                        required=True,
                        nargs=2,
                        dest="files_list",
                        help="choose two files for comparison")
    results = parser.parse_args()

    open_if = open(results.files_list[0], "r")
    open_of = open(results.files_list[1], "r")

    # applying superdiff and printing it
    output = superdiff(strip_newline(open_if), strip_newline(open_of))
    for i in output:
        print(i)


if __name__ == "__main__":
    main()
