# This function will take in a price and a discount amount and calculate the discounted price.
def calculateDiscount(price, discount):

    # Variables and calculates the discount from the original price entered.
    discount = discount / 100
    discountedPrice = price - (price * discount)
    return discountedPrice

if __name__ == "__main__":

    # User input for the original price and discount amount.
    originalPrice = float(input("Enter the price of an item: "))
    discountAmount = float(input("Enter the discount amount: "))
    finalPrice = calculateDiscount(originalPrice, discountAmount)
    print("Price after discount: ", finalPrice)