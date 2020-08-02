# Assignment 5

This is Assignment 5 in IN3110.
The task is divided into folders 5.1-5.6. Each folder contains all needed files
to run each of the subtasks (included highlighter.py).

## 5.1 Syntax highlighting

The first part of the assignment is about colouring keywords found in a sent file
based on given syntax and theme files.

You can run it like so:

```bash
python3 highlighter.py naython.syntax naython.theme hello.ny
```

## 5.2 Python syntax

This task is about writing regular expressions for Python.

Run it like this:

```bash
python3 highlighter.py python.syntax python.theme demo.py
```
or the second theme for python:

```bash
python3 highlighter.py python.syntax python2.theme demo.ny
```
## 5.3 Syntax for Java

This task is about writing regular expressions for Java.

 ```bash
 python3 highlighter.py favorite_language.syntax favorite_language.theme demo.java
 ```
 Code in the demo.java files is copied examples from the internet.
## 5.4 Grep

Grep takes a filename along with arbitrary number of regualar expressions,
and prints out all the lines where the regexes where found.

Use -f flag before a file name and -r flag before your regular expressions.
Add --highlight flag to add colours to matching regexes.

Example:

```bash
python3 grep.py -f demo.py -r print string --highlight
```
## 5.5 Superdiff

This task is about comparing two files. It adds 0 if a line remains unchanged, + if a line is
new, and - if something has been removed.

Run:

```bash
python3 diff.py -f demo1.py demo2.py
```

## 5.6 Colouring  Superdiff
Colouring the output from previous task. Additions are green, deletions are red,
and unchanged lines have just a default color.

Run:

```bash
python3 highlighter.py diff.syntax diff.theme diff_output.txt
```
