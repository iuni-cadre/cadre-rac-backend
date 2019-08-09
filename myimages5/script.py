import sys

def lineCount(filepath):
    # filepath = input('Enter file path: ')
    count = len(open(filepath, 'rb').readlines())
    file = open('/tmp/output.txt', 'w')
    file.write("Number of lines in the file: " + str(count))
    file.close()


if __name__== "__main__":
    lineCount(sys.argv[1])
