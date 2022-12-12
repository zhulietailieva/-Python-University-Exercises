class Phone:
    def __init__(self,phone_brand,phone_model,phone_year,phone_color,phone_price):
        self.phone_brand=phone_brand
        self.phone_model=phone_model
        self.phone_year=phone_year
        self.phone_color=phone_color
        self.phone_price=phone_price

    def info(self):
        return f'{self.phone_brand} - {self.phone_model} - {self.phone_year} - {self.phone_color} - {self.phone_price}'


phone1=Phone('Samsung','S8','2008','black',1500)
phone2=Phone('Iphone','13','2020','red',1200)
phone3=Phone('Sony','A5','2019','white',600)

#print(phone1.info())

phones=[phone1,phone2,phone3]


def sort_by_price(items):
    sorted_phones= sorted(items, key=lambda phone: phone.phone_price)
    return sorted_phones


def sort_by_year(items):
    sorted_phones=sorted(items, key=lambda phone: phone.phone_year)
    return sorted_phones


def print_phones(items):
    res=[]
    for x in items:
        res.append({x.info()})
    return str(res)


def write_results(file_name,items):
    file = open(file_name, "w")
    file.write('Sorted ascending by price:\n')
    file.write(print_phones(sort_by_price(items)))
    file.write('\n')

    file.write('Sorted ascending by year:\n')
    file.write(print_phones(sort_by_year(items)))
    file.write('\n')

    file.close()


print('Sorted ascending by price:')
print(print_phones(sort_by_price(phones)))
print()

print('Sorted ascending by year:')
print(print_phones(sort_by_year(phones)))
print()

write_results('res.txt',phones)

print(print_phones(phones))

