import csv
import sys
import argparse


def print_file(file_name):
    with open(file_name + ".csv") as file_object:
        contents = file_object.read()
        print(contents)

def write_list_to_file(output_file, lst):
    with open(output_file, 'a') as file:
        write = csv.writer(file) 
        for element in lst:
            write.writerow(element)
        print(lst)

def write_arb_to_file(output_file, *names):
    with open(output_file, 'a') as file_object:
        for name in names:
            file_object.write(name + ' ')
            print(name)

def read_csv(input_file):
    with open(input_file) as file_object:
        lines = file_object.readlines()
     
    for line in lines:
        lines.append(line.rstrip())
        print(line)


def write_arb_to_file_cli(output_file, *names):
 
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', action='store_true', help="shows output")
    parser.add_argument('--file')
    parser.add_argument('--names', required=True)
    args = parser.parse_args()

    if args.output:
        print("this is the output")
    if args.file:
        print(args.file)  
        with open(args.file, 'r') as file_object:
            names = args.names
        for name in names:
            file_object.write(name)
    else:
        print(names)          
        
    if __name__ == '__main__':
    # Map command line arguments to function arguments.
        write_arb_to_file_cli(*sys.argv[1:])
