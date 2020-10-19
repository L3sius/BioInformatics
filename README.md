# BioInformatics
In this document I will define the functions that I used and how do they work

BiopythonTutorial.py was used during learning of Biopython coding

# Assignment 1
In the code there will be a lot of commented lines, including prints() and other notes I've left
while trying to complete this assignment. Feel free to uncomment prints to see the results and how
they changed between different actions.

Function "findCodonSeq(seq)" is used to find all of the triplet sequences which begin with start codon "ATG" and end
with either "TAA", "TAG" or "TGA" stop codons.

Function "printSequenceList(text, seq_list)" is used to print the sequences and check the results earlier.
First parameter is simple string text and the second one is the sequence itself.

Function "findLongestCodonSeq(seq_list)" is used to find the longest codon sequence as requested in "2 užduotis"

Function "removeUselessCodons(seq)" is used to remove all codon sequences which are less than <100 symbols. This is required
because we want to only work with real DNA sequences.

Function "calculateMatrix()" is used to calculate and print out the Matrix as requested in the final part of the task.
Example of the login of it:
F1 - first file, F2 - second file
(ATG[F1] - ATG[F2])^2 = x1
(TAA[F1] - TAA[F2])^2 = x2
(TAG[F1] - TAG[F2])^2 = x3
(TGA[F1] - TGA[F2])^2 = x4

x1+x2+x3+x4 - sum which we insert into the matrix

Function "completeAssignment(file_name, number)" is used to complete all of the assignments.
It requires file_name in order to parse specific "fasta" document, and a number, which is used as an index
for saving triplets later in the code.

