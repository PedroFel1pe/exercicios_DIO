#Crie uma classe Produto que tenha:Atributos: nome, preço, quantidade em estoque.Métodos: alterar preço, vender produto (diminuir estoque), repor estoque.
#estou praticando ingles tambem
#vou fazer uma loja que vende shampoo, um unico produto por enquanto
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def change_price(self,new_price):
        self.price = new_price
    def sell_product(self,quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return f"sold {quantity} units. Stock left: {self.stock}"
        else:
            return f"not enough stock. Available: {self.stock}"
    def replenish_product(self, quantity):
        self.stock += quantity
        return f"Replenished {quantity} units. New stock: {self.stock}"

product = Product("shampoo", 15.00, 100)

information = str(input("Would you like to buy a shampoo? yes or no: ")).lower()
if information == "yes":
    Quantity = int(input("how many do you want? "))
    print(product.sell_product(Quantity))
else:
    restock = str(input("will you like to replenish the stock? yes or no :"))
    if restock == "yes":
        Quantity = int(input("How many units will you add? "))
        print(product.replenish_product(Quantity))
    else:
        print("Goodbye!")
print(f"\nProduct: {product.name}")
print(f"Stock: {product.stock}")
print(f"Price: ${product.price:.2f}")