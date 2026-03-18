from enum import Enum
from typing import Annotated
from pydantic import StringConstraints
from sqlmodel import Field, CheckConstraint

PhoneNumber = Annotated[
    str,
    StringConstraints(min_length=10, max_length=10, pattern=r"^\d{10}$"),
    Field(sa_column_kwargs={
        "constraints": [CheckConstraint("phone_number ~ '^[0-9]{10}$'")]
    })
]


class PermissionLevel(int, Enum):
    GOD = 1
    COMMANDER = 2
    DORM_MANAGER = 3
    DORM_SOLDIER = 4


class RankCategory(str, Enum):
    ENLISTED = "חוגרים"
    NCO = "נגדים"
    OFFICER = "קצינים"
    ACADEMIC = "קצינים אקדמאים"
    PROFESSIONALS = "מקצועי/אחר"


class Rank(str, Enum):
    # Enlisted (Weight 10-19)
    TURAY = 'טוראי'
    RABAT = 'רב"ט'
    SAMAL = 'סמל'
    SAMAR = 'סמ"ר'

    # NCOs (Weight 20-29)
    RASAL = 'רס"ל'
    RASAR = 'רס"ר'
    RASAM = 'רס"ם'
    RASAB = 'רס"ב'
    RANAG = 'רנ"ג'

    # Officers (Weight 40-49)
    SAGAM = 'סג"ם'
    SEGEN = 'סגן'
    SEREN = 'סרן'
    RASAN = 'רס"ן'
    SAAL = 'סא"ל'
    ALAM = 'אל"ם'
    TAAL = 'תא"ל'
    ALUF = 'אלוף'
    RAAL = 'רא"ל'

    # --- ACADEMIC ---
    KAMA = 'קמ"א'
    KAAB = 'קא"ב'
    KAAM = 'קא"ם'

    # special ranks
    KARAF = 'קר"פ'
    RABATZ = 'רב"ץ'
    KARASH = 'קר"ש'
    KAMASH = 'קמ"ש'
    CITIZEN = 'אזרח'

    @property
    def weight(self) -> int:
        weights = {
            Rank.KAMA: 1, Rank.KAAB: 2, Rank.KAAM: 3,
            Rank.TURAY: 10, Rank.RABAT: 11, Rank.SAMAL: 12, Rank.SAMAR: 13,
            Rank.RASAL: 20, Rank.RASAR: 21, Rank.RASAM: 22, Rank.RASAB: 23, Rank.RANAG: 24,
            Rank.SAGAM: 40, Rank.SEGEN: 41, Rank.SEREN: 42, Rank.RASAN: 43,
            Rank.SAAL: 44, Rank.ALAM: 45, Rank.TAAL: 46, Rank.ALUF: 47, Rank.RAAL: 48,
            Rank.KARAF: 0, Rank.RABATZ: 0, Rank.KARASH: 0, Rank.KAMASH: 0, Rank.CITIZEN: -1
        }

        return weights.get(self, 0)

    @property
    def category(self) -> RankCategory:
        if self.weight <= 0: return RankCategory.PROFESSIONALS
        if 10 <= self.weight < 20: return RankCategory.ENLISTED
        if 20 <= self.weight < 30: return RankCategory.NCO
        return RankCategory.OFFICER

    def is_at_least(self, other: "Rank") -> bool:
        if self.category != other.category and other.category != RankCategory.ENLISTED:
            return False
        if self.category == RankCategory.PROFESSIONALS:
            return self == other
        return self.weight >= other.weight
