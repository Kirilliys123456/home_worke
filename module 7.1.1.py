class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        str_product = f'{self.name}, {self.weight}, {self.category}'
        return  str_product

# Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
# 1 Инкапсулированный атрибут __file_name = 'products.txt'.
# 2 Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его
#   и возвращает единую строку со всеми товарами из файла __file_name.
# 3 Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
#   Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
#   Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .

class Shop: # tuple
    __file_name = 'products.txt'
    def get_product(self):
        file = open(self.__file_name, 'r+')
        prod_str = file.read()
        file.close()
        # pprint(prod_str)
        return prod_str

    def add(self, *products):
        file_get = self.get_product()
        for i in products:
            if self.get_product().find(f'{i.name},') == -1:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()
            else:
                print(f'Продукт {i.name} уже есть в магазине')

shop1 = Shop()
product4 = Product('Apple1', 0.4,'Fruits')
product2 = Product('Apple', 0.3,'Fruits')
product1 = Product('Cucumber', 5.3,'Vegetables')
product3 = Product('Peach', 2, 'Fruits')
print(product2)
shop1.add(product1, product2, product3, product4, product2)
print(f'\n{shop1.get_product()}')