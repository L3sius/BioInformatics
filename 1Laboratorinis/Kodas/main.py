def findCodonSeq(seq):
    i = 0
    codon_list = []
    while i < len(seq):
        if seq[i] == 'ATG':
            start_pos = i
            j = i
            while j < len(seq):
                if seq[j] == 'TAA' or seq[j] == 'TAG' or seq[j] == 'TGA':
                    end_pos = j
                    codon_list.append(''.join(str(e) for e in seq[start_pos:end_pos + 1]))
                    i = j
                    break
                j += 1
        i += 1
    return codon_list


def printSequenceList(text, seq_list):
    print(text)
    for x in range(len(seq_list)):
        print(seq_list[x])
    print()
    print()


def findLongestCodonSeq(seq_list):
    return max(seq_list, key=len)


def removeUselessCodons(seq):
    return [i for i in seq if len(i) >= 100]


def completeAssignment(file_name, number):
    # Read file
    for seq_record in SeqIO.parse("J:/Universitetas/BioInformatika/1Laboratorinis/viruses/data/" + file_name,
                                  "fasta"):
        seq_record.seq  # Check if list gets parsed

    # 1 užduotis
    split = 3
    listFrame1 = [seq_record.seq[i:i + split] for i in range(0, len(seq_record.seq), split)]
    listFrame2 = [seq_record.seq[i:i + split] for i in range(1, len(seq_record.seq), split)]
    listFrame3 = [seq_record.seq[i:i + split] for i in range(2, len(seq_record.seq), split)]
    listReverseFrame1 = [seq_record.seq.reverse_complement()[i:i + split] for i in range(0, len(seq_record.seq), split)]
    listReverseFrame2 = [seq_record.seq.reverse_complement()[i:i + split] for i in range(1, len(seq_record.seq), split)]
    listReverseFrame3 = [seq_record.seq.reverse_complement()[i:i + split] for i in range(2, len(seq_record.seq), split)]

    # FRAME +1 (CGC TAC GTC)
    # FRAME +2 (C GCT ACG)
    # FRAME +3 (CG CTA CGT)
    # FRAME -1 (TTG TGC AAA) Reverse
    # FRAME -2 (T TGT GCA) Reverse
    # FRAME -3 (TT GTG CAA) Reverse

    # Create one big list
    listFrameCodonSeq = findCodonSeq(listFrame1) + findCodonSeq(listFrame2) + findCodonSeq(listFrame3) + findCodonSeq(
        listReverseFrame1) + findCodonSeq(listReverseFrame2) + findCodonSeq(listReverseFrame3)

    # printSequenceList("All frames combined are as follows:", listFrameCodonSeq)

    # 2 užduotis find longest sequence
    longestCodon = findLongestCodonSeq(listFrameCodonSeq)
    # print(longestCodon)

    # 3 užduotis remove all sequences which are <100 symbols
    listFrameCodonSeq = removeUselessCodons(listFrameCodonSeq)
    # printSequenceList("Longest codons:", listFrameCodonSeq)

    # 4 užduotis find frequencies
    # printSequenceList("Longest codons:", listFrameCodonSeq)
    # print(listFrameCodonSeq)
    sequenceString = ''.join(listFrameCodonSeq)  # Combine all list elements to one big string
    sequenceStringSplit = [sequenceString[i:i + split] for i in range(0, len(sequenceString), split)]
    # print(sequenceStringSplit)
    counts = Counter(sequenceStringSplit)  # Count different triplets
    # print(counts)
    ATG[number] = counts['ATG'] / sum(counts.values())
    TAA[number] = counts['TAA'] / sum(counts.values())
    TAG[number] = counts['TAG'] / sum(counts.values())
    TGA[number] = counts['TGA'] / sum(counts.values())
    print("File name: ", file_name)
    print('Normalized ATG:', ATG[number])
    print('Normalized TAA:', TAA[number])
    print('Normalized TAG:', TAG[number])
    print('Normalized TGA:', TGA[number])


def calculateMatrix():
    # calculate distance matrix
    z1 = 0
    distance = []

    while z1 < number:
        z2 = 0
        distance_row = []
        while z2 < number:
            distance_row.append(
                pow((ATG[z1] - ATG[z2]), 2) + pow((TAA[z1] - TAA[z2]), 2) + pow((TAG[z1] - TAG[z2]), 2) + pow((
                        TGA[z1] - TGA[z2]), 2))
            z2 += 1
        distance.append(distance_row)
        z1 += 1

    print("Matrix")
    # Matrix output
    for elem in distance:
        for value in elem:
            print("%.6f" % value, end=" ")
        print()


if __name__ == '__main__':
    import Bio
    from collections import Counter
    from Bio import SeqIO

    # Create empty lists for future matrix calculation
    number = 0
    ATG = [0] * 8
    TAA = [0] * 8
    TAG = [0] * 8
    TGA = [0] * 8
    completeAssignment("bacterial1.fasta", number)
    number += 1
    completeAssignment("bacterial2.fasta", number)
    number += 1
    completeAssignment("bacterial3.fasta", number)
    number += 1
    completeAssignment("bacterial4.fasta", number)
    number += 1
    completeAssignment("mamalian1.fasta", number)
    number += 1
    completeAssignment("mamalian2.fasta", number)
    number += 1
    completeAssignment("mamalian3.fasta", number)
    number += 1
    completeAssignment("mamalian4.fasta", number)
    number += 1

    # Print all required triplet values
    # print(ATG)
    # print(TAA)
    # print(TAG)
    # print(TGA)

    calculateMatrix()  # Calculate Matrix

    #      | b1 | b2 | b3 | b4 | m1 | m2 | m3 | m4 |
    #   b1 | x  |    |    |    |    |    |    |    |
    #   b2 |    | x  |    |    |    |    |    |    |
    #   b3 |    |    | x  |    |    |    |    |    |
    #   b4 |    |    |    | x  |    |    |    |    |
    #   m1 |    |    |    |    | x  |    |    |    |
    #   m2 |    |    |    |    |    | x  |    |    |
    #   m3 |    |    |    |    |    |    | x  |    |
    #   m4 |    |    |    |    |    |    |    | x  |

    # findCodonSeq(seq_record.seq, listFrame1)
    # findCodonSeq(seq_record.seq.reverse_complement(), listReverse)

    # printSequenceList("Normal sequence codons", findCodonSeq(listFrame1))
    # printSequenceList("Reverse sequence codons", listReverse)

    # longestNormalCodonSeq = findLongestCodonSeq(listNormal)
    # longestReverseCodonSeq = findLongestCodonSeq(listReverse)

    # print("Longest normal sequence codons:", longestNormalCodonSeq)
    # print("Longest reverse sequence codons:", longestReverseCodonSeq)

    # printSequenceList("list frame +1 sequence codons", listFrame1)
    # printSequenceList("list frame +2 sequence codons", listFrame2)

    # string[start: end: step]
    # end_codon_list = (
    #    seq_record.find('TAA', start_pos + 3, len(seq_record.seq) - 1),
    #    seq_record.find('TAG', start_pos + 3, len(seq_record.seq) - 1),
    #    seq_record.find('TGA', start_pos + 3, len(seq_record.seq) - 1))  # Placing variables in a list
    # if codon == 'ATG' -> start writing
    # if codon == 'TAA' or codon == 'TAG' or codon == 'TGA'
    # print(findStopCodons1(seq_record.seq))
    # a(seq_record.seq)
    # einu per ilga stringa, ieskociau A raides, tada jeigu yra T, tada ar yra G -> isprinta ATG
    # findStartStopCodons(seq_record.seq)
    #
    # i = 0
    # while i < len(seq):
    # end_codon_list = []
    # start_pos = seq.find('ATG', i, len(seq_record.seq) - 1)
    # if start_pos != -1:
    # taa = seq.find('TAA', start_pos + 3, len(seq) - 1)
    # tag = seq.find('TAG', start_pos + 3, len(seq) - 1)
    # tga = seq.find('TGA', start_pos + 3, len(seq) - 1)
    # if taa > 0:
    # end_codon_list.append(taa)
    # if tag > 0:
    # end_codon_list.append(tag)
    # if tga > 0:
    # end_codon_list.append(tga)
    # end_pos = min(end_codon_list)  # Find earliest position of stop codon
    # print(start_pos)
    # print(end_pos + 2)
    # print(seq[start_pos:end_pos + 3])
    # final_codon_list.append(seq[start_pos:end_pos + 3])
    # i = end_pos + 3
    # else:
    # break
