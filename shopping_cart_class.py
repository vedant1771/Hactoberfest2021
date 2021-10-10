class order:
    
    delivery_charges = {
        "prime" : 0,
        "non prime" : 50
    }
    
    def __init__(self,delivery_speed,delivery_add):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_add = delivery_add

    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))
        
    def display_order(self):
        print("-------------------- Products in Cart --------------------")
        for product,quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity : {}".format(quantity))
            print("Delivery Charge : {}".format(order.delivery_charges[self.delivery_speed]))
        
    def get_delivery_charges(self):
        return order.delivery_charges[self.delivery_speed]
        
    def get_total_bill(self):
        total = 0
        for product,quantity in self.items_in_cart:
            total += product.get_deal_price() * quantity
        total += self.get_delivery_charges()
        print("Total Bill : {}".format(total))
        
        
class product:

    def __init__(self, name, price, deal_price, rating):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.rating = rating
        self.you_save = price - deal_price
        
    def display_product_details(self):
        print("Name : {}".format(self.name))
        print("Price : {} Rs".format(self.price))
        print("Deal Price : {} Rs".format(self.deal_price))
        print("Rating : {}/5".format(self.rating))
        print("You Save : {} Rs".format(self.you_save))
        
    def get_deal_price(self):
        return self.deal_price
        

class electronic_item(product):
    
    def __init__(self, name, price, deal_price, rating, warranty, specifications):
        super().__init__(name, price, deal_price, rating)
        self.warranty =warranty
        self.specifications = specifications
    
    def display_product_details(self):
        super().display_product_details()
        print("Warranty : {} Months".format(self.warranty))
        print("Specifications : {}".format(self.specifications))
        
        
class grocery_item(product):
    
    
    def __init__(self, name, price, deal_price, rating, packed_date, expiry_date):
        super().__init__(name,price,deal_price,rating)
        self.packed_date = packed_date
        self.expiry_date = expiry_date
        
    def display_product_details(self):
        super().display_product_details()
        print("Packing Date : {}".format(self.packed_date))
        print("Expiry Date : {}".format(self.expiry_date))
    

class laptop(electronic_item):
    
    
    def __init__(self,name, price, deal_price, rating, warranty, specifications, operating_system, screen_size):
        super().__init__(name, price, deal_price, rating, warranty, specifications)
        self.operating_system = operating_system
        self.screen_size = screen_size
    
    def display_product_details(self):
        super().display_product_details()
        print("Operating System : {}".format(self.operating_system))
        print("Screen Size : {} inch".format(self.screen_size))



if __name__ == '__main__':
    
    tv = electronic_item("Tv",12000,10000,4.5,12,90)
    milk = grocery_item("Milk", 50, 45, 4.8, "12/05/21", "20/05/21")
    msi = laptop("MSI PL627RC",50000, 48000, 4.5, 12, "Laptop", "MS-DOS", 16)
    tv.display_product_details()
    print("--------------------")
    milk.display_product_details()
    print("--------------------")
    msi.display_product_details()
    order_1 = order("non prime" , "hyderabad")
    order_1.add_item(msi,1)
    order_1.add_item(milk,2)
    
    order_1.display_order()
    
    order_1.get_total_bill()
