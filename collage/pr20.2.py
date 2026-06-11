class StringReverser:
    def reverse_words(self, text):
        # Split the sentence into words
        words = text.split()
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join back into a string
        return " ".join(reversed_words)


# ---- Example Usage ----
sr = StringReverser()

sentence = "Kunal patil"
print("Original:", sentence)
print("Reversed:", sr.reverse_words(sentence))