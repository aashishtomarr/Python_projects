import time
import textwrap

def calculate_typing_speed():
    # The original text
    raw_text = (
        "In the busiest street of the city, on the bottom floor of a half-century-old passage, "
        "he ran a small tea house inherited from his father. His customers were usually students "
        "of the training center on the street or other shopkeepers in the passage. One morning, "
        "he saw a photography exhibition being set up at the beginning of the street. Out of pure "
        "curiosity, he wanted to visit it. There, he saw a black and white photograph of his father "
        "standing in front of the tea house, a sight he could never show his children."
    )
    
    # WRAP SETTINGS: Limits the line length to 70 characters for readability
    wrapped_text = textwrap.fill(raw_text, width=70)
    
    print("\n" + "="*40)
    print("      TYPING SPEED TEST (WPM)      ")
    print("="*40)
    
    ready = input("\nType 'go' and press Enter to start: ").strip().lower()
    
    if ready == 'go':
        print("\n--- COPY THE TEXT BELOW ---\n")
        print(wrapped_text) # This will now be neatly formatted
        print("\n" + "-"*40)
        
        start_time = time.time()
        user_input = input("Start typing here:\n> ")
        end_time = time.time()
        
        # Timing logic
        time_seconds = max(end_time - start_time, 1) # Prevent division by zero
        time_minutes = time_seconds / 60
        
        # Word lists
        target_words = raw_text.split()
        user_words = user_input.split()
        
        # Calculation logic
        correct_words = sum(1 for w1, w2 in zip(target_words, user_words) if w1 == w2)
        
        if not user_words:
            print("\nError: No text was entered.")
            return

        # WPM Metrics
        net_wpm = correct_words / time_minutes
        accuracy = (correct_words / len(user_words)) * 100

        print("\n" + "*"*15 + " RESULTS " + "*"*15)
        print(f"Time Taken:    {round(time_seconds, 1)}s")
        print(f"Accuracy:      {round(accuracy, 2)}%")
        print(f"Your Score:    {round(net_wpm, 1)} WPM (Net)")
        print("*" * 39)
        
    else:
        print("Test aborted.")

def main():
    while True:
        calculate_typing_speed()
        if input("\nTry again? (y/n): ").lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
