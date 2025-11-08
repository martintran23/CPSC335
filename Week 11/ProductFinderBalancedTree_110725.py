import bisect

def product_catalog():
    prices = []
    names = []
    
    while True:
        print("\n1. Add Product")
        print("2. Search products in price range")
        print("3. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            name = input("Enter product name: ").strip()
            price = float(input("Enter product price: ").strip())
            pos = bisect.bisect_left(prices, price)
            prices.insert(pos, price)
            names.insert(pos, name)
            
            print(f"Product {name} added at price {price}.")
            
        elif choice == "2":
            if not prices:
                print("No products available.")
                continue
            min_price = float(input("Enter minimum price: ").strip())
            max_price = float(input("Enter maximum price: ").strip())
            
            start = bisect.bisect_left(prices, min_price)
            end = bisect.bisect_left(prices, max_price)
            
            if start >= end:
                print("No products found in this range.")
            else:
                print("Products in this range:")
                for i in range(start, end):
                    print(f"- {names[i]} (${prices[i]})")
                    
        elif choice == "3":
            print("Exiting the catalog.")
            break
        
        else:
            print("Invalid choice, please re-enter the value.")
            
if __name__ == "__main__":
    product_catalog()