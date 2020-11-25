# BioInformatika
Šiame dokumente aš aprašysiu laisva forma laboratorinių darbų analizes bei funkcijas įgyvendintas kode ir ką jos atlieka.

Failas BiopythonTutorial.py buvo naudojamas mokantis BioPython bibliotekos

# Antras laboratorinis darbas

Šioje skiltyje pateiksiu atsakymus į antro laboratorinio darbo klausimus.

1. Tai pirmiausia svarbu suprasti, kuo jie panašūs yra (fasta ir fastQ formatas): <br/>
	1.1. Abu formatai kaupia sekos duomenis bei sekos metaduomenis (angl. data and metadata). <br/>
	1.2. Abu formatai yra pagrįsti tekstu (angl. text-based). <br/>
	<br/>
Koks skirtumas tarp jų? fastQ formatas buvo sugalvotas išspręsti konkrečią sekos metu kylančią problemą: atsižvelgiant į tai, kaip veikia skirtingos sekvenavimo technologijos, tikimybė, kad teisingai identifikuotas bus nukleotidas labai skiriasi. Fasta formatas neturi standartizuoto būdo tai užkuduoti. Užtat fastQ yra papildomai atsirandanti nukleotido kokybės balų seka. (angl. sequence of quality scores) <br/>
Iš esmės fastQ padeda tiesiog nustatyti papildomai sekos kokybę. <br/>
<br/>
Papildoma informacija, kuri yra pateikiama fastQ formate: <br/>
a) Eilutė, prasidedanti @, kurioje yra sekos ID. <br/>
b) Viena ar daugiau eilučių, kuriose yra seka. <br/>
c) Nauja eilutė, prasidedanti simboliu +, tuščia arba kartojanti sekos ID. <br/>
d) Viena ar daugiau eilučių, kuriose yra kokybės balai. <br/>


2. Prie mėnesio dienos kurią gimiau (8-diena) pridedu 33 ir ASCII simbolis būtų: 8+33=41 ")" <br/>

3. Jei būtų naudojami mažesni negu 33 ASCII simboliai tai sekos galėtų įgauti neigiamą kokybės balą. <br/>

4. a) Nustačiau, jog koduotė naudojama failiuke buvo: arba Sanger Phread+33 arba Illumina 1.8+ Phread+33, nes tik jos praėjo mano parašyta scriptuką. Kitos koduotės netenkina, nes buvo panaudoti ASCII simboliai į jas neįeinantys. (Pavyzdžiui skaičiai). Kodėl programa meta, kad gali būti arba Sanger arba Illumina 1.8? Nes šios dvi koduotės yra panašios ir skiriasi tik per vieną ASCII simbolį "j", o kadangi failiuke nebuvo šito simbolio, negalima pilnai nustatyti, kuri koduotė čia yra naudojama. <br/>

b) Atlikau papildomus skaičiavimus, kad surasti C/G nukleotidų pasiskirstymą reade. Tam naudojau kelias funkcijas, tai būtų: GCratio(sequence), į kurią paduodame DNR seką ir atrandom, o atgal gaunam jau santykį C/G nukleotidų esantį toje sekoje. Taip pat dar naudojau funkciją round(number,decimal=0). Jos dėka aš galiu apvalinti gautus atsakymus iki X.XX (dviejų skaičių po kablelio). Galu gale gautus atsakymus surašiau į excel dokumentą (GCAnalizė.xlsx, jis randasi "2Laboratorinis" aplankale). Iš susidariusios lentelės galima matyti, kad buvo keli "peakai", tai būtų nuo 0.24 iki 0.39, tada nuo 0.47 iki 0.58, bei dar vienas nuo 0.64 iki 0.76. <br/>

c) Šitai užduočiai atlikti naudojau internetinį įrankį https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastSearch&BLAST_SPEC=MicrobialGenomes kuris man padėjo atrasti, kokios bakterijos buvo šitame mėginyje. Paleidus programą, yra atspaudinamos sekos, kurios papuola tarp minėtų aukščiau "peakų". <br/>

Tarkim, iš pirmo "peako" buvo paimtos šios sekos: <br/>
GAAGTTCTAATGATTTATCGACTGCTAGACAGCAGATATGCTTAATTTAAGTACCTTATGCTAATTGGCACCATGGGAGTGGGACAGAAATGATATTTTCGTAAAATTTATTTCGTAGTCCCACCACAAATCGCATTGCCTGTAGAATTTC ir gautas rezultatas buvo, kad tai yra Stafilokokas – patogeninis mikroorganizmas. Papildoma informacija žiūtėti .txt dokumentą esantį aplankale "2Laboratorinis/RastosBakterijos/1Peako1variantas.txt </br>
AACTTCACTCTTTGGTATATTGTTATTAGCAGGAAAACGATAAAACCTTTAATCAGAGATATTGAACTTCGTTTCTTTCTGTTAATAGCCTTAGGGGTGATCATTGTTACCTCTTTCCAGGTCTGGCATATAGGTATGTATGACTTGCATG ir gautas rezultatas buvo, kad tai yra Ešerichija marmotae - gramneigiamų, sporas nesudarančių, lazdelės formos bakterija. Papildoma informacija žiūtėti .txt dokumentą esantį aplankale "2Laboratorinis/RastosBakterijos/1Peako2variantas.txt </br>

Iš antro "peako" buvo paimtos šios sekos: <br/>
TTTGGTTCTTCCCGATAATCCTGGGATACACCGCGGGGAAACGCTTCGGCGGTAATCCATTTACTGCCATGGTGATTGGTGGAGCGTTAGTGCATCCATTAATTCTGACTGCTTTCGAGAACGGGCAAAAAGCGGATGCGCTGGGGCTGG ir gautas rezultatas buvo, kad tai yra Šigella sonnei - gramneigiama, lazdelės pavidalo, nemotorinė, sporą nesukelianti bakterija. Papildoma informacija žiūtėti .txt dokumentą esantį aplankale "2Laboratorinis/RastosBakterijos/2Peako1variantas.txt </br>
GGTGGTTTCGCCGGGCATGGTTGATGCGCACACCCATATTTCTGAACCGGGTCGTAGCCACTGGGAAGGTTATGAAACCGGTACTCGCGCAGCGGCAAAAGGTGGTATCACCACCATGATCGAAATGCCGCTCAACCAGCTGCCTGCAACG ir gautas rezultatas buvo, kad tai yra Ešerichija coli (lietuviškai žarninės lazdelės bakterija). Kaip matoma, jau buvo Ešerichijos šeimos bakterija šitame mėginyje, matyt jų yra dar ir daugiau. Papildoma informacija žiūtėti .txt dokumentą esantį aplankale "2Laboratorinis/RastosBakterijos/2Peako2variantas.txt </br>

Ir iš paskutinio "peako" buvo paimtos šios sekos: <br/>
GACGTCCTGGACTGCGGCAACGCCGGAACCCTCATGCGCCTCCTCCTCGGCCTCCTCGCGGGCCAGGAGGGGCTTTTCGCCGTCCTCACCGGGGACGCCTCCTTGAGGCGCCGCCCCATGGGCCGGGTGGTGGCCCCCTTGAGGGCCATGG ir gautas rezultatas buvo, kad tai yra Thermus thermophilus - yra gramneigiama bakterija, naudojama daugelyje biotechnologinių taikymo sričių, įskaitant kaip pavyzdinį organizmą genetinei manipuliacijai, struktūrinę genomiką ir sistemų biologiją. Termo, šitoje vietoje reiškia, kad bakterija yra ypač atspari karščiui. Papildoma informacija žiūtėti .txt dokumentą esantį aplankale "2Laboratorinis/RastosBakterijos/3Peako1variantas.txt </br>
GTCCACGGCGAAGGCCAGGTCCACCAGGTTGATCAGGAGGACCACCCGCCAGAACGTCTTCGCCGAGGCCTCGGGGAGGGGCTTCCCCTCGGGGTGGTTGCGGAAGTGCCGGACCATGAGGTAGACGAGGTAGAGCCCCCCGAGGACCTGG ir gautas rezultatas buvo, kad tai yra taip pat Thermus thermophilus bakterija. Tai nėra nuostabu, nes šitame "peake" yra labai didelis kiekis C/G nukleotidų. Papildoma informacija žiūtėti .txt dokumentą esantį aplankale "2Laboratorinis/RastosBakterijos/3Peako2variantas.txt </br>

5. Šitame mėginyje buvo, pavyzdžiui, bakterijų su dideliu atspurumu karštai temperatūrai (minėtas aukščiau pavyzdys Thermo Thermophilus), nes buvo nemažai didelių C/G nukleotidų pasiskirstymų. Taip pat bakterijų, kurios randamos šiltakraujuose organizmuose (pavyzdžiui Ešerichija coli). Be abejo, tikrai nepatikrinau visų DNR sekų atitikančių minėtus "peakus", tačiau prabėgau pro dalį jų ir aprašiau būtent tai, ką radau. Pastebėjau, kad bakterijų radimo laikas duomenų bazėje naudojant BLAST buvo vidutiniškai apie 30 sekundžių. <br/>

# Pirmas laboratorinis darbas

Šiame kode bus labai daug užkomentuotų eilučių, dažniausiai tai bus print() funkcijos, kurios leis pasižiūrėti tarpinius atsakymus.
Taip pat stengiausi kuo daugiau palikti komentarų, kurie paaiškina svarbias kodo eilutes.

Funkcija "findCodonSeq(seq)" yra naudojama atrasti visus reikalingus sekų tripletus, 
kurie prasideda pradžios kodonu "ATG" ir baigiasi vienu iš pabaigos kodonų "TAA, "TAG" ar "TGA"


Funkcija "printSequenceList(text, seq_list)" yra naudojama atspausdinti kodonų seką ir pasitikrint tarpinius rezultatus.
Tarp paratmetrų reikia paduoti paprastą tekstą bei norimą kodonų seką.

Funkcija "findLongestCodonSeq(seq_list)" yra naudojama atrasti ilgiausią kodonų seką, kaip buvo prašoma 2 užduotyje

Funkcija "removeUselessCodons(seq)" yra naudojama išmesti visas nereikalingas kodonų sekas, kurių ilgis <100,
nes mums yra įdomūs rezultatai realių DNA sekų, o ne visokių šiukšlių.

Funkcija "calculateCodonMatrix()" yra naudojama apskaičiuoti ir atspausdinti kodonų matricą<br/>
Kokia formulė buvo naudojama apskaičiuoti kodonų matricą?<br/>

F1 - pirmas failas, F2 - antras failas<br/>
(ATG[F1] - ATG[F2])^2 = x1<br/>
(TAA[F1] - TAA[F2])^2 = x2<br/>
(TAG[F1] - TAG[F2])^2 = x3<br/>
(TGA[F1] - TGA[F2])^2 = x4<br/>

x1+x2+x3+x4 - suma, kuria įstatom į matricą.<br/>

Philip formatas (matrica), atrodytų taip:

8<br/>
b1 X, skaičius(b2), skaičius(b3), skaičius(b4), skaičius(m1), skaičius(m2), skaičius(m3), skaičius (m4)<br/>
b2 skaičius(b1), X, skaičius(b3), skaičius(b4), skaičius(m1), skaičius(m2), skaičius(m3), skaičius (m4)<br/>
b3 ...<br/>
b4 ...<br/>
m1 ...<br/>
m2 ...<br/>
m3 ...<br/>
m4 ...<br/>

Atitinkamai funkcija "calculateDiCodonMatrix()" taip pat skaičiuoja dikodonų dažnį. Naudojama tokia pati formulė kaip ir skaičiuojant kodonus.
Tiesa, vienas svarbus momentas: kaip ir prašėt, dėl įdomumo bandžiau dikodonuos skaičiuoti juos transliuojant iš DNA sekos.
Atrastus tripletus aš pavaizduodavau vienu simboliu panaudodamas translate() (BioPython) funkciją.
Tada simbolius sujungdavau po du ir radau visą dažnį tokių simbolio porų.
Po to jau atlikau paprastą skaičiavimą, kur lygiai taip pat kaip skaičiuojant kodonus pasinaudojau formulę:
(XX[F1] - XX[F2])^2

Be abejo, po to viską sudėjau į simbolių matricą.

Funkcija "completeAssignment(file_name, number)" yra naudojama įvygdyti visas užduotis ir atlikti pirmąjį laboratorinį darbą.
Jai reikia būtinai paduoti failo pavadinimą, kad išparsinti reikalingą failą, taip pat reikalingas ir unikalus indeksas, šiuo atveju
"number", kad galima būtų išsaugoti specifiškus kodonus/dikodonus į sąrašus.

# Pirmojo laboratorinio darbo analizė

Kaip skaičiavau atstumų matricą tiek kodonams, tiek dikodonams aprašiau anksčiau (prie funkcijų).

Paleidus programą yra gaunami rezultatai:

Gauname kodonų matricą:

B1 		 B2 	  B3 	   B4       M1       M2       M3       M4<br/>
0.000000 0.000068 0.000022 0.000077 0.000003 0.000011 0.000084 0.000008 <br/>
0.000068 0.000000 0.000014 0.000282 0.000067 0.000031 0.000011 0.000070 <br/>
0.000022 0.000014 0.000000 0.000179 0.000022 0.000006 0.000022 0.000031 <br/>
0.000077 0.000282 0.000179 0.000000 0.000078 0.000129 0.000320 0.000078 <br/>
0.000003 0.000067 0.000022 0.000078 0.000000 0.000009 0.000085 0.000009 <br/>
0.000011 0.000031 0.000006 0.000129 0.000009 0.000000 0.000050 0.000011 <br/>
0.000084 0.000011 0.000022 0.000320 0.000085 0.000050 0.000000 0.000104 <br/>
0.000008 0.000070 0.000031 0.000078 0.000009 0.000011 0.000104 0.000000 <br/>

O konvertavus ją į phylip formatą būtų taip:

8 <br/>
B1 0.000068 0.000022 0.000077 0.000003 0.000011 0.000084 0.000008 <br/>
B2 0.000068 0.000014 0.000282 0.000067 0.000031 0.000011 0.000070 <br/>
B3 0.000022 0.000014 0.000179 0.000022 0.000006 0.000022 0.000031 <br/>
B4 0.000077 0.000282 0.000179 0.000078 0.000129 0.000320 0.000078 <br/>
M1 0.000003 0.000067 0.000022 0.000078 0.000009 0.000085 0.000009 <br/>
M2 0.000011 0.000031 0.000006 0.000129 0.000009 0.000050 0.000011 <br/>
M3 0.000084 0.000011 0.000022 0.000320 0.000085 0.000050 0.000104 <br/>
M4 0.000008 0.000070 0.000031 0.000078 0.000009 0.000011 0.000104<br/>


Taip pat gauname ir dikodonų matricą:

B1 		 B2 	  B3 	   B4       M1       M2       M3       M4<br/>
0.000000 0.001408 0.001426 0.001322 0.001802 0.001979 0.001539 0.002768 <br/>
0.001408 0.000000 0.000347 0.001660 0.000460 0.000387 0.000766 0.000908 <br/>
0.001426 0.000347 0.000000 0.001797 0.000408 0.000722 0.000820 0.001409 <br/>
0.001322 0.001660 0.001797 0.000000 0.002124 0.002151 0.002062 0.002822 <br/>
0.001802 0.000460 0.000408 0.002124 0.000000 0.000594 0.000887 0.001198 <br/>
0.001979 0.000387 0.000722 0.002151 0.000594 0.000000 0.001464 0.000344 <br/>
0.001539 0.000766 0.000820 0.002062 0.000887 0.001464 0.000000 0.002201 <br/>
0.002768 0.000908 0.001409 0.002822 0.001198 0.000344 0.002201 0.000000 <br/>

O konvertavus ją į phylip formatą būtų taip:

8 <br/>
B1 0.001408 0.001426 0.001322 0.001802 0.001979 0.001539 0.002768 <br/>
B2 0.001408 0.000347 0.001660 0.000460 0.000387 0.000766 0.000908 <br/>
B3 0.001426 0.000347 0.001797 0.000408 0.000722 0.000820 0.001409 <br/>
B4 0.001322 0.001660 0.001797 0.002124 0.002151 0.002062 0.002822 <br/>
M1 0.001802 0.000460 0.000408 0.002124 0.000594 0.000887 0.001198 <br/>
M2 0.001979 0.000387 0.000722 0.002151 0.000594 0.001464 0.000344 <br/>
M3 0.001539 0.000766 0.000820 0.002062 0.000887 0.001464 0.002201 <br/>
M4 0.002768 0.000908 0.001409 0.002822 0.001198 0.000344 0.002201 <br/>


Ką mes gauname? (Medžių nuotraukos yra įkeltos į "1Laboratornis" aplanką)

Nagrinėjant rezultatą (DiCodonTree.svg) yra matomi, jog klasterizuoja jis į 4 dalis, o ir pačios dalys yra žymiai didesnio atstumo tarpusavyje, negu kodonų dažnių medžio.
Nagrinėjant rezultatą (CodonTree.svg) yra matoma, jog klasterizuoja jis į 4 dalis, bet pačios atšakos yra minimalaus atstumo tarpusavyje. Tos 4 dalys yra B4 ir B3, B1 ir M4, M1 ir M3, B2 ir M2.

Iškart galima pamatyti ir didelį skirtumą tarp skirtingų medžių - dažnis tarp kodonų ir dikodonų labai skiriasi. Be abejo, tai gali būti dėl to, jog buvo atlikti klaidingi skaičiavimai, arba tai, jog
skaičiuojant dikodonų reikšmes buvo naudojamas translate() ir tolimesni atitinkami veiksmai. Taip pat galima pamatyti iš klasterių, kad kai kur bakterijų ir žinduolių virusų dažnis sutampa. Labiausiai, mano supratimu,
varijuoja B4 virusas tiek kodonų, tiek dikodonų medyje.