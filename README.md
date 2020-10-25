# BioInformatika
Šiame dokumente aš aprašysiu laisva forma pirmo laboratorinio darbo analizę bei funkcijas įgyvendintas šiame kode ir ką jos atlieka.

Failas BiopythonTutorial.py buvo naudojamas mokantis BioPython bibliotekos

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

   | b1 | b2 | b3 | b4 | m1 | m2 | m3 | m4 |<br/>
b1 | x  |    |    |    |    |    |    |    |<br/>
b2 |    | x  |    |    |    |    |    |    |<br/>
b3 |    |    | x  |    |    |    |    |    |<br/>
b4 |    |    |    | x  |    |    |    |    |<br/>
m1 |    |    |    |    | x  |    |    |    |<br/>
m2 |    |    |    |    |    | x  |    |    |<br/>
m3 |    |    |    |    |    |    | x  |    |<br/>
m4 |    |    |    |    |    |    |    | x  |<br/>

Nesunku yra konvertuoti ir į philip formatą, kuris atrodytų taip:

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

# 1 Laboratorinio darbo analizė

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