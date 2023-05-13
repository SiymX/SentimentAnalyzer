# SentimentAnalyzer
This program is a Python-based sentiment analyzer that will determine the sentiment of text input and will give individual explanations 
for each word. This also utilizes the Natural Language Toolkit (NLTK) library for sentiment analysis and the tkinter library for an
interactive Graphical User Interface (GUI).




# Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Dependencies](#dependencies)




# Features
- **Graphical User Interface (GUI)**: The sentiment analyzer provides a user-friendly GUI for input and result the display.
- **Sentiment Analysis**: The program will utilize the VADER (Valence Aware Dictionary and sEntiment Reasoner) lexicon from the NLTK library to 
determine the sentiment of the input text. It will then calculate the score to determine whether the sentiment is positive, negative, or netrual.
- **Word Explanations**: The program will fetch word explanations from the ``dictionaryapi.dev`` API based on the input words. If available, it will
provide the definition of individual words to enhance understanding.
- **Input Validation**: The program will also valdiate the input text and ensure that it will contain no more than 20 words. If the input exceeds the limit, 
an error message will display.





# Installation
Contributions to this sentiment analyzer are welcome. If you encounter any issues then you are welcome to submit a pull request or
open an issue. You can also dowload or clone the repostory to your device by using:
```
git clone https://github.com/SiymX/SentimentAnalyzer.git
```

1. Make sure you have Python installed on your system. You can download the latest version of Python from the official Python Website: https://www.python.org/downloads/.
You can also use PyCharm as the development enviornment for this project, download it here from: https://www.jetbrains.com/pycharm/.
2. Install the required dependcies by running the following command:
```
pip install nltk requests pillow
```
3. Download NLTK lexicon by running the Python interpreter and run the following command:
```
import nltk
nltk.download('vader_lexicon')
```




# Usage
You can either run the program via Terminal or run the `exe` file located in the ```/dist``` folder if you are using an Windows Device. To run it on terminal do the following:
1. Open terminal and navigate to the directory where the program files are located.
2. Run the following command to start the Sentiment Analyzer:
```
python SentimentAnalyzer.py
```
3. The GUI Window of the Sentiment Analayzer will appear.
4. Click the **Analyze** button to perform the analaysis.
5. The sentiment analysis will display the output on the outpyt label with each individual words with their explanation.





# Dependencies
* `tkinter`: For creating the GUI.
* `nltk`: For sentiment analysis using the VADER lexicon.
* `requests`: For making HTTP requests to retrieve word explanations.
* `PIL`: For image processing and displaying the background.
