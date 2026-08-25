# Vērtēšanas kārtība — Programmēšana II

## Vērtēšanas veidi

| | Kad | Kā vērtē |
| --- | --- | --- |
| **Diagnosticējošā** | Bloka sākumā | Bez vērtējuma; nosaka, ar ko sākt |
| **Formatīvā (FV)** | Bloka vidū | Atgriezeniskā saite, bez ballēm |
| **Summatīvā (SV)** | Bloka noslēgumā | 10 ballu skala |
| **Mēģinājuma eksāmens** | 07. blokā | Procentos, pēc eksāmena kritērijiem |

## Vērtējuma veidošanās

Īpatsvarus nosaka standarta kursa apguves prasības:

| Darbs | Īpatsvars |
| --- | --- |
| SV1 — programmprodukts objektorientētā vidē | 15 % |
| SV2 — tīkls, serveris, droša datubāze | 15 % |
| SV3 — datu struktūras, API, mašīnmācīšanās | 15 % |
| SV4 — analīze un specifikācija | 10 % |
| SV5 — programmatūras izstrāde | 20 % |
| SV6 — produkts komandā | 25 % |

Mēģinājuma eksāmeni gada vērtējumā neietilpst. To mērķis ir cits: parādīt, kur vēl ir robi,
kamēr tos vēl var aizpildīt.

## Darbu forma

Katrs darbs ir **vai nu papīra, vai datora darbs** — nekad abi vienā. Šajā kursā lielākā
daļa ir datora darbi, jo arī centralizētais eksāmens ir pie datora.

**Datora darbos** atļauta programmēšanas valodas un bibliotēku dokumentācija un
w3schools — tieši tā, kā to nosaka eksāmena programma. **Nav atļauti AI rīki.** Kods
jāsaglabā repozitorijā vismaz reizi 10 minūtēs.

**Papīra darbi** šajā kursā ir formatīvie: jēdzieni, algoritmu izsekošana, sarežģītības
novērtēšana, ER modeļi. Tie ir vieta, kur pārbaudīt izpratni bez rīkiem.

**Biļetes** (SV4) — skolēns aizstāv savu izpēti un specifikāciju. To, ko cilvēks pats
pētījis, viņš var pastāstīt; to, kas ir uzģenerēts, — nevar.

## Aizstāvēšana

SV1, SV3, SV5 un SV6 ietver aizstāvēšanu: skolēns demonstrē risinājumu, atbild uz
jautājumiem par savu kodu un **veic tajā nelielu izmaiņu uz vietas**.

Programmprodukts, kuru skolēns nespēj paskaidrot un mainīt, netiek novērtēts neatkarīgi no
tā, cik labi tas strādā. Standarts prasa kompleksu sasniedzamo rezultātu — spēju rīkoties
jaunā situācijā, nevis gatavu failu.

## Attālinātās stundas

Nedēļas 5. un 6. stunda ir attālinātā darba stundas ar konkrētu nododamo rezultātu. Tās
netiek vērtētas atsevišķi ballēs, bet:

- sprinta rezultāta trūkums tiek fiksēts, un nākamā klātienes stunda sākas ar to;
- commit vēsture ir daļa no SV5 un SV6 vērtējuma;
- trīs neizpildīti sprinti pēc kārtas nozīmē konsultāciju, ne aizrādījumu.

## Programmēšanas labās prakses principi

Vērtē pēc tās pašas skalas, ko centralizētais eksāmens:

| Sācis apgūt | Turpina apgūt | Apguvis | Apguvis padziļināti |
| --- | --- | --- | --- |
| Lieto lielākajā daļā koda, bet nekonsekventi vai daļēji korekti | Lieto kopumā korekti un konsekventi, pieļaujot dažas neprecizitātes | Lieto korekti un konsekventi | Lieto vienmēr korekti un konsekventi, pats piedāvā un izmanto līdzīgus principus |

Principi: katrs priekšraksts jaunā rindā · loģiskās daļas atdalītas ar tukšu rindu ·
atkāpes parāda struktūru · nav garu rindu · jēgpilni nosaukumi · komentāri skaidro loģiskās daļas.

## Kur glabājas darbi

Pārbaudes darbu varianti un kritēriji ir privātajā `sv-fv` repozitorijā:

```
sv-fv/12-klase/fv/   FV1, FV2 …
sv-fv/12-klase/sv/   SV1 … SV6, mēģinājuma eksāmeni
```

## Uzlabošana

Katru SV var uzlabot vienu reizi konsultāciju laikā divu nedēļu laikā. Uzlabotais vērtējums
aizstāj iepriekšējo. SV6 komandas darbu uzlabo visa komanda kopā.
