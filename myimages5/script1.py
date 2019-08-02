import sys

def lineCount(inputFileList, outputFileList):
    # filepath = input('Enter file path: ')
    i = 0
    for files in inputFileList:
        count = len(open(files, 'rb').readlines())
        file = open('/tmp/%s' % outputFileList[i], 'w')
        file.write("Number of lines in the file: " + str(count))
        file.close()
        i += 1


if __name__== "__main__":
    inputFileList = sys.argv[2].strip().split(',')
    outputFileList = sys.argv[3].strip().split(',')
    lineCount(inputFileList, outputFileList)
