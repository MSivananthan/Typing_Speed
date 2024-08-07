import time
import random

class TypingTest:
    def __init__(self, phrases):
        self.phrases = phrases
        self.current_phrase = None
        self.start_time = None
        self.end_time = None
        self.total_characters = 0
        self.correct_characters = 0

    def display_phrase(self):
        self.current_phrase = random.choice(self.phrases)
        print(self.current_phrase)

    def start_test(self):
        self.start_time = time.time()
        user_input = input("Type the phrase: ")
        self.end_time = time.time()
        return user_input

    def calculate_accuracy(self, user_input):
        self.total_characters = len(self.current_phrase)
        self.correct_characters = sum(1 for char1, char2 in zip(self.current_phrase, user_input) if char1 == char2)
        accuracy = (self.correct_characters / self.total_characters) * 100
        return accuracy

    def calculate_speed(self):
        time_taken = self.end_time - self.start_time
        words = self.current_phrase.split()
        words_per_minute = (len(words) / time_taken) * 60
        return words_per_minute

    def display_results(self, accuracy, speed):
        print(f"Accuracy: {accuracy:.2f}%")
        print(f"Speed: {speed:.2f} words per minute")

def main():
    phrases = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is an interpreted, high-level programming language.",
        "Typing speed and accuracy are important skills.",
        "Consistent practice leads to improvement over time.",
        "Concentration and focus are key for accurate typing."
    ]

    typing_test = TypingTest(phrases)

    while True:
        typing_test.display_phrase()
        user_input = typing_test.start_test()
        accuracy = typing_test.calculate_accuracy(user_input)
        speed = typing_test.calculate_speed()
        typing_test.display_results(accuracy, speed)

        retry = input("Do you want to try again? (yes/no): ")
        if retry.lower() != "yes":
            print("Thank you, goodbye.")
            break

if __name__ == "__main__":
    main()
