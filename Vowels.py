class VowelCounter:
    def __init__(self, text):
        self.text = text
        self.vowels = "aeiouAEIOU"
        self.count = 0

    def count_vowels(self):
        for char in self.text:
            if char in self.vowels:
                self.count += 1
        return self.count

    def show_result(self):
        print("The number of vowels in the string is:", self.count)


# --- Program Execution ---

# Get input from the user
user_input = input("Enter a string: ")

# Create a VowelCounter object
vc = VowelCounter(user_input)

# Call methods
vc.count_vowels()
vc.show_result()
