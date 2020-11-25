# SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS.....................................................
#   ..........................XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX......................
#   ...............................IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII......................
#   .................................JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ.....................
#   LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL....................................................
#   PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
#   !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
#   |                         |    |        |                              |                     |
#  33                        59   64       73                            104                   126
#   0........................26...31.......40
#                            -5....0........9.............................40
#                                  0........9.............................40
#                                     3.....9..............................41
#   0.2......................26...31........41
#   0..................20........30........40........50..........................................93
#  S - Sanger        Phred+33,  raw reads typically (0, 40)
#  X - Solexa        Solexa+64, raw reads typically (-5, 40)
#  I - Illumina 1.3+ Phred+64,  raw reads typically (0, 40)
#  J - Illumina 1.5+ Phred+64,  raw reads typically (3, 41)
#      with 0=unused, 1=unused, 2=Read Segment Quality Control Indicator (bold)
#      (Note: See discussion above).
#  L - Illumina 1.8+ Phred+33,  raw reads typically (0, 41)
# https://en.wikipedia.org/wiki/FASTQ_format
import math
from collections import Counter

RANGES = {
    'Sanger': (33, 73),
    'Illumina-1.8': (33, 74),
    'Solexa': (59, 104),
    'Illumina-1.3': (64, 104),
    'Illumina-1.5': (67, 104)
}


def checkEncoding(encoding, encoding_name):
    value = True
    i = len(unique_ascii_symbols)
    while i > 0:
        if unique_ascii_symbols[i - 1] not in encoding:
            print("Is not encoded in ", encoding_name, " because contains character: ", unique_ascii_symbols[i - 1])
            value = False
            break
        i -= 1
    return value


# Function to convert
def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1


def GCratio(sequence):
    letterC = sequence.count('C')
    letterG = sequence.count('G')
    ratio = (letterC + letterG) / float(len(sequence))
    return round(ratio, 2)


def round(number, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(number * multiplier) / multiplier


if __name__ == "__main__":

    # Read fastQ file
    from bioinfokit.analys import fastq
    from Bio import SeqIO
    from Bio.Blast import NCBIWWW

    fastq_iter = fastq.fastq_reader(
        file='J:/Universitetas/BioInformatika/BioInformatics/2Laboratorinis/reads_for_analysis.fastq')
    # read fastq file
    qual_list = []
    GCRatio_list = []
    for record in fastq_iter:
        # get sequence headers, sequence, and quality values
        header_1, sequence, header_2, qual = record
        # get sequence length
        # sequence_len = len(sequence)
        # count A bases
        # a_base = sequence.count('A')
        # print(sequence, qual, a_base, sequence_len)
        qual_list.append(qual)
        # print(header_1, sequence, header_2, qual)
        GCRatio_list.append(GCratio(sequence))
        if 0.24 <= GCratio(sequence) <= 0.39:
            # Prints sequences that are in the first peak
            print("First peak sequence: ", sequence)
        if 0.47 <= GCratio(sequence) <= 0.58:
            # Prints sequences that are in the second peak
            print("Second peak sequence: ", sequence)
        if 0.64 <= GCratio(sequence) <= 0.76:
            # Prints sequences that are in the third peak
            print("Third peak sequence: ", sequence)

    # convert list to string and count ascii characters

    # print(Counter((listToString(qual_list))))
    unique_ascii_symbols = list(set(listToString(qual_list)))
    print("Unique ASCII symbols that were found", unique_ascii_symbols)
    # print(len(unique_ascii_symbols))

    sanger = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHI"""
    solexa = ";<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefgh"
    illumina_1_3 = "@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefgh"
    illumina_1_5 = "CDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghi"
    illumina_1_8 = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJ"""

    # check what encoding is used
    if checkEncoding(sanger, "sanger"):
        print("The encoding is done in sanger")
    if checkEncoding(solexa, "solexa"):
        print("The encoding is done in solexa")
    if checkEncoding(illumina_1_3, "illumina 1.3+"):
        print("The encoding is done in illumina 1.3+")
    if checkEncoding(illumina_1_5, "illumina 1.5+"):
        print("The encoding is done in illumina 1.5+")
    if checkEncoding(illumina_1_8, "illumina 1.8+"):
        print("The encoding is done in illumina 1.8+")

    counter = Counter(GCRatio_list)
    # Print all the CGRatio's
    print("All CGRatio's")
    print(counter)

