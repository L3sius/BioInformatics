#Useful link http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec19
#Always write this!
from Bio.Seq import Seq

#2.4.1 FASTA code that worked for me
from Bio import SeqIO
for seq_record in SeqIO.parse("J:/Universitetas/BioInformatika/ls_orchid.fasta", "fasta"):
	print(seq_record.id)
	print(repr(seq_record.seq))
	print(len(seq_record))
    
#2.4.2 GenBank code that worked for me
from Bio import SeqIO
for seq_record in SeqIO.parse("J:/Universitetas/BioInformatika/ls_orchid.gbk", "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
    
#3.1 This is used for iterating through sequence
    my_seq = Seq("GATCG")
    for index, letter in enumerate(my_seq):
        print("%i %s" % (index, letter))
#Use this to print length of the sequence
    print(len(my_seq))
#Count is used to find the number of letters/words in a sequence
    Seq("AABBCAWAD").count("AA") #Will print 1
    Seq("AABBCAAD").count("AA") #Will print 2
    
#What does GC mean? In molecular biology and genetics, GC-content (or guanine-cytosine content) 
#is the percentage of nitrogenous bases 
#in a DNA or RNA molecule that are either guanine (G) or cytosine (C).
#GC calculation can be done with a function
    from Bio.Seq import Seq
    from Bio.SeqUtils import GC
    my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
    GC(my_seq)
    
#Slicing array: 
    from Bio.Seq import Seq
    my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
    my_seq[4:12] #Outcome Seq('GATGGGCC') (Includes 4, excludes 12)
#Start:Stop:Stride
    my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
    my_seq[0::3] #Outcome Seq('GCTGTAGTAAG') 0 - first letter G, stop is empty, 3 - every third letter starting from 0
    my_seq[1::3] #Outcome Seq('AGGCATGCATC') 1 - second letter A, stop is empty, 3 - every third letter starting from 1
    my_seq[::-1] #Outcome Seq('CGCTAAAAGCTAGGATATATCCGGGTAGCTAG') - reverse the sequence
    
#3.4 Adding sequences together
    protein_seq = Seq("EVRNAK")
    dna_seq = Seq("ACGT")
    protein_seq + dna_seq #Outcome Seq('EVRNAKACGT')
#Quick hack for adding all sequences together with a loop
    list_of_seqs = [Seq("ACGT"), Seq("AACC"), Seq("GGTT")]
    concatenated = Seq("")
    for s in list_of_seqs:
        concatenated += s
    
    concatenated #Outcome Seq('ACGTAACCGGTT')
#We can change sequence to .upper() or .lower() cases
    dna_seq = Seq("acgtACGT")
    dna_seq #Outcome Seq('acgtACGT')
    dna_seq.upper() #Outcome Seq('ACGTACGT')
#3.6 Nucleotide sequences and (reverse) complements
    my_seq = Seq("abcde")
    my_seq.complement() #Outcome Seq('tvghe') ???
    my_seq.reverse_complement() #Outcome Seq('ehgvt') Reverse of complement()
#3.10  Comparing Seq objects
    seq1 = Seq("ACGT")
    "ACGT" == seq1 #Outcome True
    seq1 == "ACGT" #Outcome True
#3.11 By Default Seq is an immutable object, however this can be changed with:
    mutable_seq = my_seq.tomutable()
    mutable_seq #Outcome MutableSeq('GCCATCGTAATGGGCCGCTGAAAGGGTGCCCGA')
    mutable_seq.remove("T")
    mutable_seq #Outcome MutableSeq('GCCACGTAATGGGCCGCTGAAAGGGTGCCCGA') - removes first "T"
#3.12 UnknownSeq objects (For DNA or RNA sequences, unknown nucleotides are commonly denoted by the letter “N”)
    from Bio.Seq import UnknownSeq
    unk_dna = UnknownSeq(20, character="N")
    unk_dna #Outcome UnknownSeq(20, character='N')
    print(unk_dna) #Outcome NNNNNNNNNNNNNNNNNNNN
#Complement A -> T, C -> G, T -> A, G -> C! BUS EGZAMINE!
    from Bio.Seq import Seq
    my_dna = Seq("AGTACACTGGT")
    my_dna #Output Seq('AGTACACTGGT')
    my_dna.complement() #Output Seq('TCATGTGACCA')
    my_dna.reverse_complement() #Output Seq('ACCAGTGTACT') iš my_dna imam iš dešinės į kairę, rašom į my_dna.reverse iš kairės į dešinę.
#Kiek genų gali sutalpiti ORF'as (open reading frame)? Vieną, nes ORF'as turi tik vieną stop'ą
#Egzonas koduoja kažkurią baltymo seką.
#Tarp egzonų yra fragmentas, kuris nieko nekoduoja (beprasmis baltymo aspektas) - Intronas.
#Stop kodonas gali būti tik paskutiniame egzone,kuris reiškia baltymo pabaigą.
#Kodonas (3meras) - paremti modeliai yra ne tokie informatyvūs kaip dikodonais paremti modeliai.
#Trikodonais (9merais) - paremti modeliai nenaudojami, nes jiems riekia daug informacijos.
#Kodėl dikodonas (6meras)? Nes jis susideda iš dviejų kodonų einančių vienas po kito.
#Kodonų yra 4^3 = 64
#Dikodonų yra 4^6 (Dauguma jų bus 0)
#Distant sequence -> Complete -> View Tree -> Laukiam kol susiskaičiuos -> Pasirenkam Radial. Ir pažiūrėt kaip skiriasi dažniai tarp virusų (pvz buvo alpha/beta šalia viens kito ir panašiai).
#Pabandyt transliuoti ir dekoduot į baltymą pirmą laboratorinį?