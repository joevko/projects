import re
import argparse
import highlighter


def main():
    """
    ArgumentParser for the command line interface.
    Then calling scanner function to color the matching syntaxes.
    -f: filename to scan
    -r: regex to detect
    -t: highlight found syntaxes
    """

    parser = argparse.ArgumentParser(description="Grep Utility")
    parser.add_argument("-f", "--file",
                        help="file")
    parser.add_argument("-r", "--regex",
                        required=True,
                        nargs="+",
                        dest="regex_list",
                        help="regex",
                        type=str)
    parser.add_argument("-t", "--highlight",
                        dest='highlight',
                        action='store_true',
                        help="highlight")
    results = parser.parse_args()

    with open(results.file) as file:
        file_content = file.readlines()

    coloured_source_file = scanner(file_content,
                                   results.regex_list,
                                   results.highlight)

    for i in coloured_source_file:
        print(i[:-1])


def scanner(text, syntax_file, highlight):
    """
    Looping through source file(text) to find keywords to color.
    Looping through syntax file to get info on which words to color and then
    using the previously written color_print function to change the colors of
    the found keywords. Used the built-in func replace() to replace the found
    keywords with coloured keywords.

    Args:
        text (str): text to style.
        syntax_file(dict): where key is regex and value a name for it.
        highlight (dict): where key is corresponding name from the syntax file
            and value is a bash color.
    Returns:
        output (list): list  with added attributes
    """

    # highlight = True;
    output = []

    for line in text:
        found_syntaxes = []
        coloured_line = line
        # print(line)
        key_colour = 0
        coloured = False
        for key in syntax_file:
            key_colour += 1
            # print(key)

            found_syntaxes = re.findall(key, line)
            if len(found_syntaxes) > 0:
                # We have found one or more syntaxes!
                for i in found_syntaxes:
                    if highlight:
                        # Color the found syntaxes if the user needs highlights
                        if key_colour > 5:
                            key_colour = 0
                        new_text = highlighter.color_print(
                                i, int(31 + key_colour))
                        coloured_line = coloured_line.replace(i, new_text)
                coloured = True
        if coloured:
            output.append(coloured_line)

    return output


if __name__ == "__main__":
    main()
