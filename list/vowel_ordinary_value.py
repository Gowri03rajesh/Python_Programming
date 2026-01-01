words=input("Enter some words:")
vowels='aeiouAEIOU'
vowels_list=[char for char in words if char in vowels]
print("Vowels in the words:",vowels_list)

ordinal_values=[ord(char) for char in words]
print("Ordinary values of each character:",ordinal_values)