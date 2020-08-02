import sys
import re


def main():
    # Read files and starts the program
    syntax_dict = create_dictionary(open(sys.argv[1], "r", encoding="utf8"))
    theme_dict = create_dictionary(open(sys.argv[2], "r", encoding="utf8"))
    source_file = open(sys.argv[3], "r", encoding="utf8")

    coloured_source_file = scanner(source_file, syntax_dict, theme_dict)

    # Prints the coloured file to the terminal
    for i in coloured_source_file:
        print(i[:-1])


def color_print(text, style):
    """
    This functions styles the given source text with a style of a choice.

    Args:
        text (str): text to style
        style (int): int of a choice that corresponds to a desired style

    Returns:
        styled (str): text with added attributes

    """
    # print(" asd  " + text)
    formatting = "\033[{}m".format(style)
    # The “\033[0m” sequence removes all attributes (formatting and colors)
    reset = "\033[0m"
    styled = formatting + text + reset
    # print(styled[:-1])
    return styled


def scanner(text, syntax_file, theme_file):
    """
    Looping through source file(text) to find keywords to color.
    Looping through syntax file to get info on which words to color and then
    using the previously written color_print function to change the colors of
    the found keywords. Used the built-in func replace() to replace the found
    keywords with coloured keywords.

    Args:
        text (str): text to style.
        syntax_file(dict): where key is regex and value a name for it.
        theme_file (dict): where key is corresponding name from the syntax file
            and value is a bash color.
    Returnes:
        output (list): list  with added attributes
    """
    output = []

    for line in text:
        coloured_line = line
        for key in syntax_file:
            # print(key)
            found_syntaxes = re.findall(key[1:-1], line)
            if len(found_syntaxes) > 0:
                # We have found one or more syntaxes!
                for i in found_syntaxes:
                    # Colour all the found syntaxes
                    # print(i)
                    new_text = color_print(
                            i, theme_file.get(syntax_file.get(key))[2:])
                    coloured_line = coloured_line.replace(i, new_text)
                    # print(coloured_line)
        # We are done with this line; adding the line to the output
        output.append(coloured_line)

    return output


def create_dictionary(file):
    """
    Creates a dictionary out of an input file.

    Args:
        file: just a file

    Returns:
        file_dict: input file changed into a dictionary
    """
    file_dict = {}
    with file as f:
        for line in f:
            key, val = line.strip().split(': ')
            file_dict[key.strip()] = val.strip()

    # print (file_dict)
    file.close()
    return file_dict


if __name__ == "__main__":
    main()
