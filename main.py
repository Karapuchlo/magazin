

class Product:
  price_level = 1.0
  products = []

  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity
    self.__class__.products.append(self)

  def get_total_price(self):
    return self.quantity * self.price * self.__class__.price_level

  def apply_discount(self, discount):
      self.__class__.price_level *= (1 - discount)

  @classmethod
  def get_total_inventory_value(cls):
     return sum([product.quantity * product.price * cls.price_level for product in cls.products])

if __name__ == "__main__":
# Создаем экземпляры товаров
    product1 = Product("Телевизор", 30000, 10)
    product2 = Product("Холодильник", 25000, 5)

# Получаем общую стоимость конкретного товара
    print(product1.get_total_price())

# Применяем скидку
    product1.apply_discount(0.1)

# Проверяем, что скидка была применена
    print(product1.get_total_price())

# Получаем общую стоимость всего запаса товаров в магазине
    print(Product.get_total_inventory_value())



