#Runs the pip library to generate a credit card number that pass Luhn's algorithm
#It includes a local BIN database to retrieve card details like brand, type, country and bank issuer
#All lookups are performed locally
#This tool was created for educational purposes only

from card_generator import CardGenerator

# Initializes the card generator for Visa cards
visacard_generator = CardGenerator('visa')

# Generates a standard card
card = visacard_generator.generate(count=1)
print(card)

