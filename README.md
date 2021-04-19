# validateFastQ
Quick validator for fastQ written in Python

# To Use

- Have Python3 installed (check with `python --version`)
- Run `python fastq_checker.py -i your_file_location`

# Options

`-i, --input`: Input file, either the raw fastQ file or the gzipped one.

`-o, --output`: Output file for when fixing is implemented.

`-f, --fix`: Fixing flag. Currently not implemented.

`-x, --fast-fail`: Fail the validator on the first error. Helpful for larger files when you just need to confirm the file is messed up.

# Example Run

```
> python fastq_checker.py -i examples/frankenFastq.fastq.gz -x
Opening gzipped file frankenFastq.fastq.gz
Sequence Issue: Sequence '+
' has character that isn't in 'CGATNcgatn' on lines 60 to 64
```
