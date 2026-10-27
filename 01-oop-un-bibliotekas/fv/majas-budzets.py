from abc import ABC, abstractmethod
from datetime import datetime
import json

class IerakstsNavAtrasts(Exception):
    """Kļūda, ko parādīt, kad nevar atrast ierakstu"""

class Ieraksts(ABC):
    def __init__(self,  summa, datums=datetime.now(), piezime=""):
        if datums:
            [y, m, d] = [int(x) for x in datums.split("-")]
            self.datums = datetime(y, m, d)
        else:
            self.datums = datums
            
        self.summa = summa
        self.piezime = piezime

    @abstractmethod
    def ietekme(self):
        """ Ienākumiem pozitīvs, izdevumiem negatīvs ( +312.45 / -34.89 )"""

    @classmethod
    def no_vardnicas(cls, dati):
        return cls(dati["summa"], dati["datums"], dati["piezime"])

    def uz_vardnicu(self):
        return {
            "summa": self.summa,
            "datums": self.datums.isoformat()[:10],
            "piezime": self.piezime,
            "tips": self.ietekme()[0]
        }

class Ienakumi(Ieraksts):
    def ietekme(self):
        return f"+{self.summa}"

class Izdevumi(Ieraksts):
    def ietekme(self):
        return f"-{self.summa}"

class Budzets:
    def __init__(self):
        self.ieraksti = {}
        self.currentId = 0

        try:
            with open("izdevumi.json", "r", encoding="utf-8") as datne:
                saturs = json.load(datne)
        except (FileNotFoundError, json.JSONDecodeError):
            saturs = []

        for d in saturs:
            if d["tips"] == '+':
                a = Ienakumi.no_vardnicas(d)
            else:
                a = Izdevumi.no_vardnicas(d)
            self.ieraksti[self.currentId] = a
            self.currentId += 1

    def pievienot(self, ieraksts):
        self.ieraksti[self.currentId] = ieraksts
        self.currentId += 1

        with open("izdevumi.json", "w", encoding="utf-8") as datne:
            json.dump([i.uz_vardnicu() for key, i in self.ieraksti.items()], datne, ensure_ascii=False, indent=2)

    def atrast(self, id):
        if id in self.ieraksti:
            return self.ieraksti[id]
        else:
            raise IerakstsNavAtrasts(f"Neizdevās atrast ierakstu ar ID {id}")

    def dzest(self, id):
        if id in self.ieraksti:
            self.ieraksti.pop(id)
        else:
            raise IerakstsNavAtrasts(f"Neizdevās atrast ierakstu ar ID {id}")

    def periods(self, no, lidz):
        out = []
        for id, ieraksts in self.ieraksti:
            if ieraksts.datums >= no and ieraksts.datums <= lidz:
                out.append(ieraksts)

        return out

    def bilance(self):
        summa = 0
        for id, ieraksts in self.ieraksti:
            summa += int(ieraksts.ietekme())

    def menesa_kopsavilkums(self, datums):
        ienakumi = 0
        izdevumi = 0
        for id, ieraksts in self.ieraksti:
            if ieraksts.datums.month == datums.month:
                if ieraksts.ietekme()[0] == "+":
                    ienakumi += int(ieraksts.ietekme())
                else:
                    izdevumi += int(ieraksts.ietekme())


b = Budzets()
a = Izdevumi(123.45, "2026-10-06", "test2 input")
c = Ienakumi(12.45, "2026-10-07", "test3 input")
b.pievienot(c)
print(c.datums)

    
