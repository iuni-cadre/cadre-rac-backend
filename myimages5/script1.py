import sys

def line_count(argv):
    input_files = []
    arg_range = range(3, len(argv))
    for i in arg_range:
        input = argv[i]
        input_files.append(input)
    output_count = 0
    shared_volume = '/home/aditya/user_package_run_dir' 
    for files in input_files:
        count = len(open(files, 'rb').readlines())
        output_file_name = shared_volume + '/output' + str(output_count) + '.txt'
        file = open(output_file_name, 'w')
        file.write("Number of lines in the file: " + str(count))
        file.close()
        output_count += 1


if __name__ == "__main__":
    argv = sys.argv
    line_count(argv)
