import tkinter as tk
from tkinter import filedialog
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

import nltk
nltk.download('stopwords')  
nltk.download('punkt')  

class TextSummarizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Summarizer")

        # Set color variables
        bg_color = "#f0f0f0"  # Light gray
        button_bg = "#4caf50"  # Green
        button_fg = "white"
        text_bg = "white"
        text_fg = "black"
        summary_bg = "#cfe2f3"  # Light blue
        summary_fg = "black"

        self.root.configure(bg=bg_color)

        self.file_label = tk.Label(root, text="Select Text File:", bg=bg_color)
        self.file_label.pack(pady=10)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file, bg=button_bg, fg=button_fg)
        self.browse_button.pack(pady=10)

        self.text = tk.Text(root, height=10, width=50, bg=text_bg, fg=text_fg)
        self.text.pack(pady=10)

        self.summarize_button = tk.Button(root, text="Summarize", command=self.summarize_text, bg=button_bg, fg=button_fg)
        self.summarize_button.pack(pady=10)

        self.summary_label = tk.Label(root, text="Summary:", bg=bg_color)
        self.summary_label.pack(pady=10)

        self.summary_text = tk.Text(root, height=10, width=50, bg=summary_bg, fg=summary_fg)
        self.summary_text.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                text_content = file.read()
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, text_content)

    def summarize_text(self):
        input_text = self.text.get(1.0, tk.END)
        words = word_tokenize(input_text)

        stop_words = set(stopwords.words("english"))
        freq_table = dict()

        for word in words:
            word = word.lower()
            if word not in stop_words:
                freq_table[word] = freq_table.get(word, 0) + 1

        sentences = sent_tokenize(input_text)

        sentence_value = dict()
        for sentence in sentences:
            for word, freq in freq_table.items():
                if word in sentence.lower():
                    sentence_value[sentence] = sentence_value.get(sentence, 0) + freq

        sum_values = sum(sentence_value.values())
        average = int(sum_values / len(sentence_value))

        summary = ''
        for sentence in sentences:
            if (sentence in sentence_value) and (sentence_value[sentence] > (1.225 * average)):
                summary += " " + sentence

        self.summary_text.delete(1.0, tk.END)
        self.summary_text.insert(tk.END, summary)


if __name__ == "__main__":
    root = tk.Tk()
    app = TextSummarizerApp(root)
    root.mainloop()
