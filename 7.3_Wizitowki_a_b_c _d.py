#Wizytowki_7.3_dziedziczenie

#Oba typy wizytówek, powinny oferować metodę contact() oraz label_lenght()

# ==================== K L A S Y ==============

class BaseContact:
    def __init__(self, name, surname,email,phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email
        #self.address = address
       
    def __str__(self):
        return f'Wybieram Prywatny numer {self.phone_number} i dzwonie do {self.name} {self.surname}'#' Dlugosc {len(self.name)}'
        #  jak bym zapisala dlugosc do retuturnu tez by dazialalo, tylko zeby nie bylo zgodnie z zadaniem ze to powinna
        #  byc metoda zerkni do BusinesContact jak to dziala



class BusinessContact(BaseContact):
    def __init__(self, position,company,company_phone, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.position = position
       self.company = company
       self.company_phone = company_phone

    def __str__(self):
        return f'Wybieram Firmowy numer {self.phone_number} i dzwonie do {self.name} {self.surname} Dlugosc {len(self.name)}'
        # Dlugosc tutaj pisze tylko dla mnie ze i tak sie da

# ===================== M E T O D Y ==============


# Zadanie b
def contact():
    #y = input("Podaj imie z duzej litery jesli chcesz kontakt firmowy (z malej litery - kontakt prywatny): ")
    for x in lista:
        if y==x.name:   # !!! to jest KLUCZOWE dla filtra zeby porownac co napisalam z tym co jest w bazie danych
            print(x)    #  wypisze cala zalozme ze c jezeli napisalam franek
           
    for z in liste:     # firmowe kontakty
        if y==z.name:
            print(z)

# ----------------------------------------------------
# zadanie c
def label_lenght():     #to jest ten sam princip jak contact tylko zmienilam wypisiwanie
    for x in lista:
        if y==x.name:
            print('Dlugosc imienia to ',len(x.name),'i  nazwiska to ',len(x.surname),'znakow')

    for z in liste:     # firmowe kontakty
        if y==z.name:
            print('Dlugosc imienia to ',len(z.name),'i  nazwiska to ',len(z.surname),'znakow')


# ----------------------------------------------------
# zadanie d      
def create_contacts():
    c = int(input("Podaj rodzaj wizytowki: 0 - firmowa / 1 - Prywatna): "))
    from faker import Faker
#    print(type(c)) ... to mi pomoglo bo sie zacielam przez to ze input byl "str" i wymaga "int" zeby dzialalo "if" 
    fake = Faker()
    for _ in range(int(input("Podaj ilosc wizytowek: "))):
        if c==0:
            b_contact=BusinessContact(name=fake.name(), email=fake.email(),surname="",phone_number=fake.phone_number(),position="",company="",company_phone="")
#   w razie potrzeby mozna dodac ... company=fake.company(),position=fake.job()
            print("Business Contact: ",b_contact.name,b_contact.phone_number,b_contact.email)      
        if c==1:
            p_contact=BaseContact(name=fake.name(), email=fake.email(),surname="",phone_number=fake.phone_number())
            print("Private Contact: ",p_contact.name,p_contact.phone_number,p_contact.email)

        
# ==================   Poczatek  ======================
a = BaseContact(name="jarek", surname="czaplicki", email="czap.trak",phone_number="683452321")
b = BaseContact(name="maniak", surname="benek", email="ben.bez", phone_number="995561254")
c = BaseContact(name="franek", surname="pagowski", email="pag.toi", phone_number="321468753")
d = BaseContact(name="darek", surname="mruz", email="mruz.chlod",phone_number="856427154")
e = BaseContact(name="marek", surname="galaks", email="gal.sex", phone_number="951852456")

aa = BusinessContact(name="Jarek", surname="czaplicki", company="ursus", position="traktorzysta", email="czap.trak",phone_number="683452321", company_phone="431824967")
bb = BusinessContact(name="Maniak", surname="benek", company="urzad pracy", position="bezrobotny", email="ben.bez", phone_number="995561254", company_phone="167943258")
cc = BusinessContact(name="Franek", surname="pagowski", company="toi-toi", position="sprzatacz", email="pag.toi", phone_number="321468753", company_phone="741258963")
dd = BusinessContact(name="Darek", surname="mruz", company="iglotex", position="lodziarz", email="mruz.chlod",phone_number="856427154", company_phone="753159852")
ee = BusinessContact(name="Marek", surname="galaks", company="sex-shop", position="model", email="gal.sex", phone_number="951852456", company_phone="213645978")

lista=[a,b,c,d,e]

liste=[aa,bb,cc,dd,ee]

# Wazne zeby Y teda input bylo zadefiniowane przed definiciami, wczesznej mialam w ciele definicie zerkni do gory contact()

print('')
print("ZADANIE 7.3_a ... Używając dziedziczenia, rozdzielilam podstawową klasę wizytówki na dwie osobne")
print('')

print('')
print("ZADANIE 7.3_b ... Uzylam imiona: jarek, maniak, franek, darek, marek")
print('')

y = input("Podaj imie z duzej litery jesli chcesz kontakt firmowy (z malej litery - kontakt prywatny): ")

contact()

print('')
print("ZADANIE 7.3_c")
print('')

label_lenght()

print('')
print("ZADANIE 7.3_d")
print('')

create_contacts()


# ... tylko zeby sie nie zamknielo odrazu okno jezeli program urochomie direkt z foldera
"""
k=input("nacisni 0 zeby skonczyc: ")
if k==0:
    pass
"""