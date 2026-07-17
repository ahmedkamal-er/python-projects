def main():
    print("Hello,Sir!")
    total_price = float(input("Enter the total price: "))
    
    if total_price < 100:
        discount_rate = 0
    elif total_price < 500:
        discount_rate = 0.10
    else:
        discount_rate = 0.20
    discount = total_price * discount_rate
    final_price = total_price - discount
    print(f"discount:{discount:.2f}")
    print(f"final price:{final_price:.2f}") 



if __name__ == "__main__":
    main()
