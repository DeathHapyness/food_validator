# food_validator
🏷️ Product Expiry Date Validator
This code is a product date validator designed to check whether an item is within its expiration period based on the purchase date and expiry date provided by the user.

🔹 How the Code Works:
User Input: The user specifies whether they want to validate a food item or a product. If the item is classified as "personal hygiene," the program displays a message and exits.

Date Format: The user can enter dates in the formats DD/MM/YYYY or DDMMYYYY. If an invalid format is entered, an error message is displayed.

Expiration Date Validation:

If the expiry date is beyond 31/12/2027, the program warns that the product is expired because it has surpassed the limit date.

If the expiry date is earlier than the current date, the program calculates and displays how many days the product has been expired.

Otherwise, it shows how many days remain before the product expires.

Information Display: The program prints a summary including the item type, purchase date, expiry date, and the validation result.

Execution Loop: The program continues running until the user types "exit" to close it.

🎯 Use Cases:
✅ Consumers can check if a product is safe to use before consuming it.
✅ Retailers can validate stock items to prevent selling expired goods.

This program is a simple and practical tool for ensuring food safety and product expiration control! 🛒🔍
