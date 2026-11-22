class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()     
        for i in range (len(words)):
            word = words[i]

            if len(word)> 1 and word[0] == '$' and word[1:].isdigit():
                price = int(word[1:])
                discounted = price * (100 - discount) / 100
                words[i] = f"${discounted:.2f}"
        return " ".join(words)
