import csv
import sys
import argparse

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

