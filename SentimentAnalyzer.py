import tkinter as tk
import nltk
import requests
from tkinter import ttk
from PIL import Image, ImageTk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment():
    text = input_field.get("1.0", "end").strip()
    if text and text != "Please enter some text...":
        words = text.split()
        if len(words) <= 20:
            sentiment_score = analyzer.polarity_scores(text)
            compound_score = sentiment_score['compound']
            if compound_score >= 0.05:
                sentiment = "This is a Positive sentiment."
            elif compound_score <= -0.05:
                sentiment = "This is a Negative sentiment."
            else:
                sentiment = "This is a Neutral sentiment."

            explanations = []
            for word in words:
                explanation = get_word_explanation(word)
                explanations.append(explanation)

            output_text = sentiment
            output_text += ' It is because: \n'
            for word, explanation in zip(words, explanations):
                output_text += f'{word}: {explanation}\n'

            output_label.config(text=output_text)
        else:
            output_label.config(text="Please enter no more than 20 words.")
    else:
        output_label.config(text="Please enter some text.")


def create_gradient(width, height):
    base = Image.new('RGB', (width, height), '#2C3E50')
    top = Image.new('RGB', (width, height), '#4CA1AF')
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend(list(int(255 * (x / width)) for x in range(width)))
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base


gradient = create_gradient(900, 700)


def get_word_explanation(word):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 0 and 'meanings' in data[0]:
            meanings = data[0]['meanings']
            if len(meanings) > 0 and 'definitions' in meanings[0]:
                definitions = meanings[0]['definitions']
                if len(definitions) > 0 and 'definition' in definitions[0]:
                    return definitions[0]['definition']
    return 'Explanation Not found'


def reset_output_label():
    output_label.config(background='white', font=('Arial', 11))


window = tk.Tk()
window.title("Sentiment Analyzer")
window.geometry("900x700")

background_image = ImageTk.PhotoImage(gradient)
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

title_label_font = ('Lora', 24, 'bold')
title_label = tk.Label(window, text="Sentiment Analyzer", font=title_label_font, fg='black')
title_label.pack(pady=10)

input_field_font = ('Consolas', 14)
input_field = tk.Text(window, height=10, width=70, font=input_field_font, fg='gray')
input_field.insert("end", "Please enter some text...")


def add_prompt(event):
    if input_field.get("1.0", "end").strip() == "Please enter some text...":
        input_field.delete("1.0", "end")
        input_field.config(fg="black")


input_field.bind("<Button-1>", add_prompt)
input_field.pack(pady=20)

style = ttk.Style()
style.configure('my.TButton', font=('Arial', 16), foreground='black')
analyze_button = ttk.Button(window, text="Analyze", command=analyze_sentiment, style='my.TButton')
analyze_button.pack()

output_label_font = ('Roboto', 14)
output_label = tk.Label(window, text="", wraplength=750, justify='left', font=output_label_font, bg='white', fg='black')
output_label.pack(pady=20, padx=20)

footer_label_font = ('Montserrat', 10)
footer_label = tk.Label(window, text="Copyright © Khandakar Sayeem. All Rights Reserved. 2023", font=footer_label_font)
footer_label.pack(side=tk.BOTTOM, pady=10)

window.mainloop()
