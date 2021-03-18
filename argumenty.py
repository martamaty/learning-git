def fun_default(breakfast_english,b='coffee'):
    print(breakfast_english,b)
fun_default('cont',)

def fun_positional(breakfast_english,drink_coffee):
    print('english','tea')
fun_positional('1','2')

def fun_keyword(x,a='english', b='coffee'):
    print(x,a,b)
fun_keyword(0,'conti','tea')

def customized_hello(first_name, last_name):
    print("Hello Mr ",first_name, last_name,"are yoiu ok?")

customized_hello("adi", "sov")

items = [
    "jajka",
    "bułka",
    "ser feta",
    "masło",
    "pomidor"
]
payment='reka'
def shopping(items, payment='card', shop='local', bag='plastic', transport='own'):
    print(items,payment,shop,bag,transport)
shopping(items, shop='supermaket')
shopping(items, payment='cash',transport='delivery')