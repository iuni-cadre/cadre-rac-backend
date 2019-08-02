import sys

def lineCount(file1, file2):
    # filepath = input('Enter file path: ')
    i = 1
    # for files in fileList:
    # count = len(open(files, 'rb').readlines())
    file = open('/tmp/output' + str(i) + '.txt', 'w')
    file.write("Number of lines in the file: " + file1 + ' ' + file_2 )
    file.close()
        # i += 1


if __name__== "__main__":
    file_1 = sys.argv[3]
    file_2 = sys.argv[4]
    # string_split = argument.split[',']
    # argument = ','.join(string_split)
    lineCount(file_1, file_2)

