# 07. bloks — eksāmena stratēģija

Šajā blokā nav jaunas vielas. Ir forma, laiks un tas, ko atklāj mēģinājuma eksāmeni.
Eksāmena uzbūve un noteikumi: [`kurss/eksamens.md`](../kurss/eksamens.md).

## §1 Laiks un stratēģija

| Daļa | Punkti | Laiks | Minūtes uz punktu |
| --- | --- | --- | --- |
| 1. Dzīvescikls | 20 | 30 min | 1,5 |
| 2. Datubāzes | 20 | 40 min | 2,0 |
| 3. OOP un bibliotēkas | 38 | 80 min | 2,1 |
| 4. Datu struktūras un programmsaskarnes | 42 | 80 min | 1,9 |

**Ar ko sākt.** Ar to daļu, kurā esi stiprākais — tur punkti nāk ātrāk, un pirmās sekmes
noņem spriedzi. Ja visas ir līdzīgas, ej pēc kārtas.

**Kad iet tālāk.** Ja uzdevums «neiet» un esi pavadījis vairāk nekā divkāršu tam paredzēto
laiku, atzīmē to un ej tālāk. Atgriezies, kad pārējais izdarīts. Punkts 4. daļā ir tikpat
vērts kā punkts 3. daļā — bet tikai tad, ja tiec līdz tam.

**Pirmās piecas minūtes.** Izlasi visu darbu cauri, pirms sāc. Tu uzzināsi, kas tevi gaida,
un smadzenes fonā jau sāks strādāt pie grūtākajiem uzdevumiem.

**Ja programma nestrādā līdz galam** — iesniedz to, kas ir. Daļēji strādājoša programma ar
pareizu struktūru dod punktus; tukša datne nedod nevienu. Komentārā pieraksti, ko biji
iecerējis, — dažreiz arī tas ir vērtējams.

## §2 1. daļa: dzīvescikls

Šeit ir izvērsto atbilžu uzdevumi, ne kods. Pārbauda: problēmas analīzi, izstrādes modeļu
salīdzināšanu, prasību veidus, testēšanas veidus, dzīvescikla posmus.

**Kā izskatās pilna atbilde:**

- atbild uz **uzdoto** jautājumu, ne uz līdzīgu;
- ir konkrēta — ar piemēru vai skaitli, ne tikai vispārīgi;
- ja prasa «nosauc trīs», nosauc tieši trīs, katru atsevišķi;
- ja prasa «pamato», atbildē ir vārds «jo» vai «tāpēc ka».

**Biežākā kļūda:** aprakstīt risinājumu tur, kur prasīta problēma, vai otrādi.

Atceries rīcības vārdu nozīmes: **analizē** (sīki pēta), **atpazīst** (identificē),
**formulē** (izsaka), **pamato** (norāda iemeslu), **salīdzina** (norāda gan kopīgo, gan
atšķirīgo — ne tikai vienu no tiem).

## §3 2. daļa: datubāzes

Divi uzdevumu tipi: **datu modelēšana** (no apraksta uz tabulām) un **vaicājumi**.

Kontrolsaraksts datu modelēšanas uzdevumam:

1. vai katrai tabulai ir `id` ar pamatotu datu tipu?
2. vai visiem laukiem ir norādīts tips?
3. vai cenas un summas ir `DECIMAL` vai `REAL`, ne `INTEGER`?
4. vai ārējās atslēgas norāda uz pareizajām tabulām?
5. vai N:M saistībai ir starptabula?
6. vai lauku nosaukumi ir bez garumzīmēm un atstarpēm?
7. vai ir vismaz dažas testa vērtības, ja tās prasa?

Vaicājumu uzdevumos visbiežāk zaudē punktus par:

- aizmirstu `GROUP BY`, kad lieto agregātfunkciju kopā ar citu lauku;
- `WHERE` tur, kur vajag `HAVING`;
- `INNER JOIN` tur, kur vajag `LEFT JOIN` (rezultāts izskatās pareizs, bet trūkst rindu);
- aizmirstu `ORDER BY`, kad uzdevumā teikts «sakārto».

## §4 3. daļa: objektorientētā programmēšana

Viens liels uzdevums, 38 punkti, 80 minūtes. Parasti: izveido klases pēc apraksta, pievieno
metodes, izmanto bibliotēku, parādi darbību.

**Secība, kas strādā:**

1. izlasi visu uzdevumu līdz galam, pirms sāc rakstīt;
2. izraksti klases un to atribūtus uz melnraksta;
3. uzraksti klašu karkasus ar konstruktoriem — tas jau ir punkti;
4. pievieno metodes pa vienai, pārbaudot katru;
5. tikai tad taisi saskarni vai izvadi.

**Punkti nāk par struktūru, ne tikai par gala rezultātu.** Klase ar pareizu konstruktoru un
divām no četrām metodēm dod ievērojami vairāk nekā tukša datne.

Neaizmirsti labās prakses principus — tie ir atsevišķi punkti un tos vērtē visā darbā.

## §5 4. daļa: datu struktūras un programmsaskarnes

Lielākā daļa: 42 punkti. Četri uzdevumi par datu struktūrām, algoritmiem un API.

Pirms sāc rakstīt, atbildi sev uz diviem jautājumiem:

1. **kura struktūra?** — vai secība ir svarīga, kā meklēšu;
2. **cik tas maksā?** — vai mans risinājums nav O(n²) tur, kur var O(n).

Struktūru izvēles atgādne:

| Ja uzdevumā ir… | Ņem |
| --- | --- |
| «cik reižu parādās», «biežākais» | vārdnīca |
| «unikāls», «vai jau bija» | kopa |
| «pēdējais», «atsaukt», «iekavas» | steks |
| «rindas kārtībā», «pirmais, kas pienāca» | rinda |
| «sakārtots», «meklēt ātri» | binārā meklēšana sakārtotā sarakstā |
| «savienojumi», «ceļš», «kaimiņi» | grafs |
| «hierarhija», «vecāks un bērni» | koks |

API uzdevumos vienmēr pārbaudi atbildes struktūru, pirms lieto datus: statusa kods, vai
gaidītais lauks vispār eksistē.

## §6 Kļūdas, kas maksā punktus bez zināšanu trūkuma

1. **Neizlasīts uzdevums līdz galam** — pēdējā teikumā bieži ir papildu nosacījums.
2. **Atbilde uz citu jautājumu** — prasīts «kāpēc», atbildēts «kā».
3. **Aizmirsts izvades formāts** — uzdevumā teikts «ar diviem cipariem aiz komata».
4. **Robežgadījums** — «no 7 līdz 18 **ieskaitot**».
5. **Nav iesniegts tas, kas ir gatavs** — programma paliek nesaglabāta.
6. **Laiks pavadīts vienā uzdevumā** — 30 minūtes vienam punktam.

Pēc katra mēģinājuma eksāmena sadali zaudētos punktus trīs grupās:

| Grupa | Ko ar to darīt |
| --- | --- |
| **Nezināju** | atkārto tēmu |
| **Zināju, bet kļūdījos** | kontrolsaraksts un uzmanība |
| **Nepaspēju** | laika plāns un lēmums iet tālāk |

Tās prasa trīs pilnīgi dažādus risinājumus. Ja to nesadala, cilvēks atkārto to, kas jau
padodas, jo tas ir patīkamāk.

## §7 Eksāmena diena

- paņem līdzi to, kas atļauts, un atstāj mājās to, kas nav — telefons un pulkstenis nedrīkst
  būt līdzi;
- pirmās piecas minūtes: izlasi visu darbu;
- saglabā darbu regulāri, ne beigās;
- pēdējās desmit minūtes: pārbaudi, ka viss iesniegts, un izlasi pirmās daļas atbildes vēlreiz;
- ja kaut kas tehniski nestrādā, saki uzreiz, ne darba beigās.
