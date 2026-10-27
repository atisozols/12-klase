#!/usr/bin/env python3
"""Ģenerē skolēnu darba failu (uzdevumi.py) no bloka README.

Uzdevumu teksts tiek rakstīts tikai vienā vietā — bloka README stundu
kartītēs. Šis skripts no tā izveido failu, kurā skolēns raksta risinājumus.

Bloks var būt jaukts: ja kartītes tagu rindā ir atsauce uz .py failu
(piemēram  `[K]` `prakse` · `teorija.py` §3), šīs stundas uzdevumi nonāk
uzdevumi.py, bet pārējās — bloka noklusētajā darba failā.

Lietošana:
    python3 bin/darbafails.py 05-virknes-un-datnes
    python3 bin/darbafails.py 0*
"""
import re
import sys
from pathlib import Path

STUNDA = re.compile(r"^## (\d{2}-\d{3}) · (.+)$", re.M)
TUKSAS_RINDAS = 4          # cik tukšu rindu atstāt risinājumam

# Darba faila valodu nosaka bloka teorijas fails. Ja tāda nav, uzdevumi
# ir dokumenti, nevis kods, un darba fails ir markdown.
KOMENTARS = {".py": "#", ".js": "//", ".sql": "--"}
FAILS_TAGOS = re.compile(r"`\w+(\.(?:py|js|sql))`")


def stundas(teksts):
    atzimes = [(m.group(1), m.group(2), m.start(), m.end()) for m in STUNDA.finditer(teksts)]
    for i, (nr, nosaukums, sak, beig) in enumerate(atzimes):
        nakama = atzimes[i + 1][2] if i + 1 < len(atzimes) else len(teksts)
        yield nr, nosaukums, teksts[beig:nakama]


def uzdevumi(kartite):
    """Atgriež [(numurs, [rindas]), ...] no kartītes Uzdevumi sadaļas.

    Koda bloki uzdevumu iekšpusē README failā ir atkāpināti (saraksta dēļ).
    Atkāpi noņem, bet koda paša struktūru saglabā.
    """
    rindas = kartite.split("\n")
    iekša = kods = False
    atkape = 0
    pasreizejais = None
    for rinda in rindas:
        if rinda.lstrip().startswith("```"):
            if not kods:
                atkape = len(rinda) - len(rinda.lstrip())
            kods = not kods
            if iekša and pasreizejais is not None:
                pasreizejais[1].append(rinda[atkape:])
            continue
        if not kods:
            if rinda.strip() == "**Uzdevumi**":
                iekša = True
                continue
            if iekša and rinda.startswith("**"):
                if pasreizejais:
                    yield pasreizejais
                    pasreizejais = None
                iekša = False
                continue
        if not iekša:
            continue
        m = None if kods else re.match(r"^(\d+)\. (.*)$", rinda)
        if m:
            if pasreizejais:
                yield pasreizejais
            pasreizejais = (int(m.group(1)), [m.group(2)])
        elif pasreizejais is not None and (kods or rinda.strip()):
            pasreizejais[1].append(rinda[atkape:] if kods else rinda.strip())
    if pasreizejais is not None:
        yield pasreizejais


def bez_markdown(rinda):
    """Noņem markdown noformējumu — .py komentārā tas ir tikai troksnis.

    Teksts `pēdiņās` ir kods, tāpēc tajā apakšsvītras un zvaigznītes paliek:
    `parskaitit_bez_transakcijas` nedrīkst kļūt par parskaititbeztransakcijas.
    """
    gabali = re.split(r"(`[^`]+`)", rinda)
    for i, gabals in enumerate(gabali):
        if i % 2:
            gabali[i] = gabals[1:-1]
        else:
            gabals = re.sub(r"\*\*(.+?)\*\*", r"\1", gabals)
            gabali[i] = re.sub(r"(?<!\w)_([^_]+)_(?!\w)", r"\1", gabals)
    return "".join(gabali)


def valoda(katalogs):
    """Bloka noklusētais darba fails: (paplašinājums, komentāra prefikss).

    Ja blokā ir teorija.md, noklusētais ir markdown — arī tad, ja blakus ir
    teorija.py stundām, kurās raksta kodu.
    """
    if (katalogs / "teorija.md").exists():
        return ".md", None
    for fails in sorted(katalogs.glob("teorija.*")):
        if fails.suffix in KOMENTARS:
            return fails.suffix, KOMENTARS[fails.suffix]
    return ".md", None


def stundas_valoda(kartite, noklusetais):
    """Ja kartītes tagu rindā ir atsauce uz koda failu, stunda iet tā darba failā."""
    tagi = kartite.strip().split("\n", 1)[0] if kartite.strip() else ""
    m = FAILS_TAGOS.search(tagi)
    if m:
        return m.group(1), KOMENTARS[m.group(1)]
    return noklusetais


def galvene(virsraksts, paplasinajums, k, citi):
    """Darba faila sākums. citi — pārējie šī bloka darba faili."""
    if k:
        izvade = [
            f"{k} " + "=" * 58,
            f"{k} {virsraksts.upper()} — DARBA FAILS",
            f"{k} " + "=" * 58,
            f"{k} Šeit raksti savus risinājumus.",
            f"{k} Teorija, piemēri un atgādne: teorija{paplasinajums}",
            f"{k} Uzdevumu numuri iet cauri visam blokam.",
        ]
        for cits in citi:
            izvade.append(f"{k} Pārējo stundu uzdevumi: {cits}")
        return izvade + [f"{k} " + "=" * 58, "", ""]
    izvade = [
        f"# {virsraksts} — darba fails",
        "",
        "Šeit raksti savas atbildes. Uzdevumu numuri iet cauri visam blokam.",
        "",
    ]
    for cits in citi:
        izvade += [f"Programmēšanas stundu uzdevumi ir [`{cits}`]({cits}).", ""]
    return izvade


def stundas_uzdevumi(nr, nosaukums, saraksts, k):
    izvade = []
    if k:
        izvade += [f"{k} " + "-" * 58, f"{k} {nr} · {nosaukums}", f"{k} " + "-" * 58, ""]
    else:
        izvade += [f"## {nr} · {nosaukums}", ""]
    for numurs, rindas in saraksts:
        pirma = rindas[0]
        zvaigzne = pirma.startswith("★")
        teksts_r = pirma[1:].strip() if zvaigzne else pirma
        if k:
            prefikss = f"{k} {numurs}. " + ("★ " if zvaigzne else "")
            izvade.append(prefikss + bez_markdown(teksts_r))
            kods = False
            for papildus in rindas[1:]:
                if papildus.lstrip().startswith("```"):
                    kods = not kods
                    continue
                if not papildus.strip():
                    izvade.append(k)
                elif kods:
                    izvade.append(f"{k}    " + papildus)
                else:
                    izvade.append(f"{k}    " + bez_markdown(papildus))
            izvade += [""] * TUKSAS_RINDAS
        else:
            izvade.append(f"**{numurs}.** " + ("★ " if zvaigzne else "") + teksts_r)
            for papildus in rindas[1:]:
                izvade.append(papildus)
            izvade += ["", "", "---", ""]
    izvade.append("")
    return izvade


def generet(kataloga_vards):
    katalogs = Path(kataloga_vards)
    readme = katalogs / "README.md"
    if not readme.exists():
        return
    noklusetais = valoda(katalogs)
    teksts = readme.read_text(encoding="utf-8")
    virsraksts = teksts.split("\n", 1)[0].lstrip("# ").strip()

    # {paplašinājums: (komentāra prefikss, [rindas], uzdevumu skaits)}
    faili = {}
    for nr, nosaukums, kartite in stundas(teksts):
        saraksts = list(uzdevumi(kartite))
        if not saraksts:
            continue
        paplasinajums, k = stundas_valoda(kartite, noklusetais)
        _, rindas, skaits = faili.get(paplasinajums, (k, [], 0))
        rindas += stundas_uzdevumi(nr, nosaukums, saraksts, k)
        faili[paplasinajums] = (k, rindas, skaits + len(saraksts))

    for paplasinajums, (k, rindas, skaits) in faili.items():
        citi = [f"uzdevumi{p}" for p in faili if p != paplasinajums]
        izvade = galvene(virsraksts, paplasinajums, k, citi) + rindas
        fails = katalogs / f"uzdevumi{paplasinajums}"
        fails.write_text("\n".join(izvade).rstrip() + "\n", encoding="utf-8")
        print(f"  {fails}: {skaits} uzdevumi")


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        generet(arg)
