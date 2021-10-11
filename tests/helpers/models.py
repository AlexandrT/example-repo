from dataclasses import dataclass


@dataclass
class Client:
    name: str


@dataclass
class Contractor:
    full_name: str
    name: str
    inn: str
    date_from: str
    country: str


@dataclass
class Representer:
    first_name: str
    last_name: str
    middle_name: str
    ssn: str
    country: str


@dataclass
class Contract:
    number: int
    name: str
    sign_date: str
    start_date: str
    end_date: str
