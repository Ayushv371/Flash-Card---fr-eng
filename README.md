# Flash Card App
This project is a simple **Flash Card Application** built using Python and Tkinter. It is designed to help users learn and memorize French vocabulary by flipping between French words and their English translations. The application implements a card-based learning approach and allows users to mark cards as learned.

## Features
- **Flash Cards**: Displays a French word and its English translation (flips after a delay).
- **Track Progress**: Cards marked as learned are removed from future sessions.
- **Customizable Data**: Utilize pre-defined vocabulary from CSV files or track your learning progress in real-time.

## How It Works
1. A flashcard displays the French word.
2. After 3 seconds, the card flips to show the English translation.
3. You can:
    - Press the ✅ button to mark the word as **learned** (removing it from the dataset).
    - Press the ❌ button to skip the word and move to the next card.
4. Progress is saved to ensure you only focus on unlearned vocabulary in future sessions.

## File Structure
- **`french_data.csv`**: A CSV file containing the vocabulary to learn.
- **`words_to_learn.csv`** (generated dynamically): Tracks remaining unlearned vocabulary.
- **`images/`**: A folder containing:
    - `card_front.png`: Flashcard front image
    - `card_back.png`: Flashcard back image
    - `right.png`: Image for the ✅ button
    - `wrong.png`: Image for the ❌ button
- **`flash_card.py`**: The main Python script for the application.

## Screenshots
-The application starts by showing a French word on the flashcard with a minimalist UI.
![image](https://github.com/user-attachments/assets/26d45137-2a73-4784-b843-d5c49b004407)

-After 3 seconds, the card automatically flips to show the English translation.
![image](https://github.com/user-attachments/assets/27a974f2-3158-4d9d-8d75-53167703dc2b)


## How to Customize
- **Custom Vocabulary**:
    - Replace `french_data.csv` with a new CSV containing your desired vocabulary. Ensure the columns are:
        - `French`
        - `English`
- **Card Images**:
    - Replace the images in the `images` directory with your own designs (make sure to keep the names consistent).
