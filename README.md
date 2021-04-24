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

`-t, --head`: Prints N lines from the top (head) of the file, rounded up to nearest multiple of 4.

`-l, --print-line`: Prints the 4 lines around line N.

`-k, --kill`: Kills the program on line N of the file. Good in conjunction with the line printing options to view parts of file.

# Example Runs

```
> python fastq_checker.py -i examples/frankenFastq.fastq.gz -x
Opening gzipped file frankenFastq.fastq.gz
Sequence Issue: Sequence '+
' has character that isn't in 'CGATNcgatn' on lines 60 to 64
```

```
> python fastq_checker.py -i examples/frankenFastq.fastq.gz --head=4 --kill=4
Opening gzipped file examples/frankenFastq.fastq.gz
@8bde1231-c851-4a0e-bb5c-73b19660c10c_Basecall_Alignment_template
TCGTGTACTTCGTTCAGTTACGTATTGCTACTTGTCGCTCTATCTTCTTTTTGTTTGCATCCGAAACCGAAGAAATAAAGCGGTGGGAATACAATCTCAGGAACCACCACTCCTTACAATGGCCTGCCTCCCACCGCTTTATTTCTTTCGGTTTCGGATCTCGCTAAAACTTTAAAAATGTAATAAAGGAAAGAACAAATTTCAAAGACTTGGGGTGAAGGCGAAACCTGGTGCAGATGGACGAGGTCTGCAGACGGAGGCAGGAGGTGTGGAAGGGCCGGGGCCTGCAGGCCTCCCTGGAACTGGGACTGGTCTCGGTCTGCTGACGTCAGGGTCAGCTCCCCGCGGAGCTGACTTCAGCAACCAACTGTGGGGCCAGCAGCCACCAGCCCAGCCCAGCCAGCTCTCGATACGTTTGATTTCATGCTGAAAAATAAATAATAAAGCCTGAAGATAAACGACAGGCAAGTAATACGTAATA
+
#"'(#,)3331,3,3+02(,-+(&0,)+,&&&&'($()*.0.0023))566-'433/0.,..-,-++-'((%03//+3*))$,)*+)$%$&((..*,,&()%(*+-1-++))$$%&)-2//+2-*$*)(*5*)+1(*+.*+-5.)46241-45..+,()))""$&%*'$##$&+22.,*('$&$'.++.(/.*-3212//3-.)4*11..)-1,()*0.-++('.%.3332/+2---0//4+((+---...)+)'''&-.++*)$%(''&')&'(''%)%,/.,*)&)&204/*0-(+/2213113333232333522121234111',1#.,%),,+0*/02.#*),+(/0-*,--.*+//())&&,-...(+'(&((-,$,-),*'%.2(-)/3-$//+.$(()(''(*%*,,0/)'12+535434103442/233--3+*51*5&'%('&*.0/,....((-,,+$&('+*,%('%#"

KILLING PROGRAM AT LINE 4
```