#encoding utf-8
import sys
import glob
import os


#directory = r"/Users/joannakorzeniowska/INF3331-joannaek/assignment3.*"
def readFile():
    wordCount = 0
    charCount = 0
    lineCount = 0
    with open(sys.argv[1], 'r') as f:
        for line in f:
            lineCount += 1
            charCount += len(line)
            for word in line.split():
                wordCount += 1
    print("a: ",lineCount, ", b: ", wordCount, ", c: ", charCount, " ,fn: ",f)

def readAllFiles():
    wordCount = 0
    charCount = 0
    lineCount = 0
    for filename in glob.glob('*'):
        print(str(filename))
        with open(filename, 'r') as f:
            for line in f:
                lineCount += 1
                charCount += len(line)
                for word in line.split():
                    wordCount += 1
    print("a: ",lineCount, ", b: ", wordCount, ", c: ", charCount)

def readPyFiles():
    wordCount = 0
    charCount = 0
    lineCount = 0
    for filename in glob.glob('*.py'):
        print(str(filename))
        with open(filename, 'r') as f:
            for line in f:
                lineCount += 1
                charCount += len(line)
                for word in line.split():
                    wordCount += 1
    print("a: ",lineCount, ", b: ", wordCount, ", c: ", charCount)

if __name__ == "__main__":
    if(sys.argv[1] == "*"):
        readAllFiles()
    elif(sys.argv[1] == "*.py"):
        readPyFiles()
    else:
        readFile()



#'''tried to print out the file name, could not really find a solution..
#I think I was somehow on the right path to solve it... ;) '''
# for path in glob.glob(directory):
#     dn, fn = os.path.split(path)
#     print( "a: ",lineCount, ", b: ", wordCount, ", c: ", charCount, " ,fn: ",fn )
