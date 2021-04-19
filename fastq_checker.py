import argparse
import sys
import gzip
import itertools
import re

class Validator:
    """Class to validate fastq files
    """
    def __init__(self, input_, output_, fail_fast):
        self.input_file = input_
        self.output_file = output_
        self.fail_fast = fail_fast

    @staticmethod
    def file_chunked_into_four_lines(iterable):
        """This is literally so we can read 4 lines at a time
        """
        it = iter(iterable)
        chunk = tuple(itertools.islice(it, 4))
        while chunk:
            yield chunk
            chunk = tuple(itertools.islice(it, 4))

    def is_gz_file(self, filepath):
        with open(filepath, 'rb') as test_f:
            return test_f.read(2) == b'\x1f\x8b'
    
    def check_header(self, string):
        if string.startswith('@'):
            return True
        else:
            raise Exception(f"Header issue: Header does not start with @, but {string[0]}")

    def check_delim(self, string):
        if string == "+\n":
            return True
        else:
            raise Exception(f"Delimiter Issue: Delimiter is not + but {repr(string)}")
    
    def check_sequence_and_quality(self, sequence, quality):
        if not re.match(r'^[CGATNcgatn]*$', sequence):
            raise Exception(f"Sequence Issue: Sequence '{sequence}' has character that isn't in 'CGATNcgatn'")
        if len(sequence) != len(quality):
            diff = abs(len(sequence) - len(quality))
            raise Exception(f"Quality Issue: Sequence and quality differ by {diff}")
        return True
    
    def validate(self):
        if self.is_gz_file(self.input_file):
            print(f"Opening gzipped file {self.input_file}")
            f = gzip.open(self.input_file, "rt")
        else:
            print(f"Opening regular file {self.input_file}")
            f = open(self.input_file, "r")
        try:
            # i = 0
            # header = None
            # sequence = None
            # delim = None
            # quality = None

            # for line in f:
            #     # assign based on 4 line chunks
            #     if i == 0:
            #         header = line
            #     elif i == 1:
            #         sequence = line
            #     elif i == 2:
            #         delim = line
            #     elif i == 3:
            #         quality = line
            #     i+=1
            lineno = 0
            for header, sequence, delim, quality in Validator.file_chunked_into_four_lines(f):
                try:
                    self.check_header(header)
                    self.check_sequence_and_quality(sequence, quality)
                    self.check_delim(delim)
                except Exception as e:
                    lineno_plus_four = lineno + 4
                    print(f"{e} on lines {str(lineno)} to {str(lineno_plus_four)}")
                    if self.fail_fast:
                        sys.exit(1)
                lineno += 4
        except Exception as e:
            print("Exception found")
            print(e)
        finally:
            f.close()
    
    def fix(self):
        pass


def parse_args(args):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i", "--input", type=str, required=True, default=None, help="Input fastq or fastq.gz file to check"
    )

    parser.add_argument(
        "-o", "--output", type=str, default=None, help="Output fastq or fastq.gz file if not just validating"
    )

    parser.add_argument(
        "-f", "--fix", action='store_true', help="Fix fastq file for you, otherwise it will just validate"
    )

    parser.add_argument(
        "-x", "--fail-fast", action='store_true', help="Fails after the first error it encounters. Good for fast check"
    )
    return parser.parse_args()

def main():
    try:
        args = parse_args(sys.argv[1:])
        validator = Validator(args.input, args.output, args.fail_fast)
        validator.validate()
        if args.fix:
            validator.fix()
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()