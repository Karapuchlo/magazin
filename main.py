

class Product:
  price_level = 1.0
  products = []

  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity
    self.__class__.products.append(self)

  def get_total_price(self):
    return self.quantity * self.price * self.price_level

  def apply_discount(self):
      return self.price * self.quantity * self.price_level

  @classmethod
  def get_total_inventory_value(self):
     return sum([product.quantity * product.price * self.price_level for product in self.products])

if __name__ == "__main__":
# Создаем экземпляры товаров
    product1 = Product("Телевизор", 30000, 10)
    product2 = Product("Холодильник", 25000, 5)

# Получаем общую стоимость конкретного товара
    print(product1.get_total_price())
    product1.price_level = 0.8
# Применяем скидку

    product1.apply_discount()
# Проверяем, что скидка была применена
    print(product1.get_total_price())

# Получаем общую стоимость всего запаса товаров в магазине
    print(Product.get_total_inventory_value())



