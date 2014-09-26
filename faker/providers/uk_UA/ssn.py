# coding=utf-8
from __future__ import unicode_literals
from ..ssn import Provider as SsnProvider


# Note: as there no SSN in Ukraine
# we get value added tax identification number (VATIN) here.
# It is also called "Ідентифікаційний номер платника податків" (in ukrainian).
# It contains only digits and length if 12.


class Provider(SsnProvider):
    ssn_formats = ("############",)
