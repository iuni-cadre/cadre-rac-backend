import sys

def lineCount(fileList):
    # filepath = input('Enter file path: ')
    i = 0
    for files in fileList:
        count = len(open(files, 'rb').readlines())
        file = open('/tmp/output' + str(i) + '.txt', 'w')
        file.write("Number of lines in the file: " + str(count))
        file.close()
        i += 1


if __name__== "__main__":
    fileList = sys.argv[1].strip().split(',')
    lineCount(fileList)

