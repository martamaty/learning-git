class Film:
    def __init__(self, title, year,types, season,episode, views):
       self.title = title
       self.year = year
       self.types = types
       self.season = season
       self.episode = episode
       self.views = views

        # Variables
       self.current_views = 0

    def play(self, step=1):
       self.current_views += step
       

    def __str__(self):
        return f'{self.title} {self.year} {self.types} {self.views}'

class Series:
    def __init__(self, title, year, types, season,episode, views):
       self.title = title
       self.year = year
       self.types = types
       self.season = season
       self.episode = episode
       self.views = views

    def set_current_views(self, value):
       if value <= self.views:
          self.current_views = value
       
      # Variables
       self._current_views = 0

    def play(self, step=1):
       self.views += step
       return

    def __str__(self):
        return f'{self.title} {self.year} {self.types}  {self.season} {self.episode} {self.views}'

def get_movies():
   for x in Lista:
      if type(x) == Film:
         print(x.title,"  ",x.year)

def get_series():
   for x in Lista:
      S=0
      for s in range (0,int(x.season)):
         S=S+1
         E=0
         for e in range(0,int(x.episode)):
            E=E+1
            print(x.title,"S",str(S).zfill(2),"E",str(E).zfill(3))

def search():
   y = input("Podaj tytul filmu lub serialu: ")
   for x in Lista:
        if y==x.title:   # !!! to jest KLUCZOWE dla filtra zeby porownac co napisalam z tym co jest w bazie danych
            print(x)

def generate_views():
   import random
   print("Losowo wybrany film/serial: ",random.choice(Lista),"ilość odtworzeń",random.choice(range(1, 100)))
#   v=random.choice(range(1, 100))   # to jest alternativa do poprzedniego zapisu
#   print(v)
   
def ten_times():
    for f in range(0,10):
        generate_views()
    pass

def top_titles():
   Views=[]
   for x in Lista:
      Views.append(x.title and int(x.views))
#   print(Views)    

   Views.sort(reverse=True)  
#   print(Views)
   for v in Views:
#      print(v)
      for x in Lista:
         if v==int(x.views):
            print(x.title, x.views)
            
        

dom_z_papieru = Series(title="dom_z_papieru", year= "2019", types= "crimy", season= "2", episode="10", views=15)
na_wspolnej = Series(title="na_wspolnej", year= "2010", types= "familly", season= "5", episode="22", views=30)
policjanci = Series(title="policjanci", year= "2000", types= "crimy", season= "3", episode="8", views=8)
klan = Series(title="klan", year= "1990", types= "drama", season= "8", episode="5", views=20)
barwy_szczescia = Series(title="barwy_szczescia", year= "1980", types= "love", season= "6", episode="10", views=66)

pulp_fiction = Film(title="pulp_fiction", year= "2019", types="",season="0",episode="1",views=3)
milioner_z_slamsu = Film(title="milioner_z_slamsu", year="2015", types="",season="0",episode="0",views=10)
the_beach = Film(title="the_beach",year="1997", types="",season="0",episode="0",views=7)
kogel_mogel = Film(title="kogel_mogel",year="1977", types="",season="0",episode="0",views=4)
the_mask= Film(title="the_mask",year="1995", types="",season="0",episode="0",views=5)

Lista=[dom_z_papieru,na_wspolnej,policjanci,klan,barwy_szczescia,pulp_fiction,milioner_z_slamsu,the_beach,the_mask,kogel_mogel]

print()
print("------------- Film i rok produkcji ---------------- ")
get_movies()

print()
print("------------- Serial S-sezon E-odzinek  ---------------- ")
get_series()

print()
search()

print()
ten_times()

print()
print("------- najpopularniejsze tytuły ----------")
top_titles()