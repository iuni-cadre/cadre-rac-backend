import sys


def line_count(argv):
    input_files = []
    arg_range = range(3, len(argv))
    for i in arg_range:
        input = argv[i]
        input_files.append(input)
    output_count = 0
    for files in input_files:
        count = len(open(files, 'rb').readlines())
        output_file_name = '/tmp/output' + str(output_count)
        file = open(output_file_name, 'w')
        file.write("Number of lines in the file: " + str(count))
        file.close()
        output_count += 1


if __name__ == "__main__":
    argv = sys.argv
    line_count(argv)
