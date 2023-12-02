import tkinter as tk
from tkinter import filedialog
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from tkinter import messagebox

import nltk
nltk.download('stopwords')  
nltk.download('punkt')  

class TextSummarizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Summarizer")

        # Set color variables
        bg_color = "#f2f2f2"  # Light gray
        button_bg = "#4CAF50"  # Green
        button_fg = "white"
        text_bg = "white"
        text_fg = "black"
        summary_bg = "#e6e6e6"  # Light gray
        summary_fg = "black"
        label_highlight_bg = "#cccccc"  # Light gray

        self.root.configure(bg=bg_color)

        self.file_label = tk.Label(root, text="Select Text File:", bg=bg_color, font=("Helvetica", 12))
        self.file_label.pack(pady=10)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file, bg=button_bg, fg=button_fg, font=("Helvetica", 12))
        self.browse_button.pack(pady=10)

        self.text = tk.Text(root, height=10, width=50, bg=text_bg, fg=text_fg, font=("Helvetica", 12))
        self.text.pack(pady=10)

        self.percent_label = tk.Label(root, text="Enter Percentage of Summary You Need to Print:", bg=bg_color, font=("Helvetica", 12))
        self.percent_label.pack(pady=5)

        self.percent_entry = tk.Entry(root, width=5, bg=text_bg, fg=text_fg, font=("Helvetica", 12))
        self.percent_entry.pack(pady=5)

        self.summarize_button = tk.Button(root, text="Summarize", command=self.summarize_text, bg=button_bg, fg=button_fg, font=("Helvetica", 12))
        self.summarize_button.pack(pady=10)

        self.summary_label = tk.Label(root, text="Summary:", bg=bg_color, font=("Helvetica", 12))
        self.summary_label.pack(pady=10)

        self.summary_text = tk.Text(root, height=10, width=50, bg=summary_bg, fg=summary_fg, font=("Helvetica", 12))
        self.summary_text.pack(pady=10)

        self.input_sentence_label = tk.Label(root, text="", bg=label_highlight_bg, font=("Helvetica", 12))
        self.input_sentence_label.pack(pady=5)

        self.output_sentence_label = tk.Label(root, text="", bg=label_highlight_bg, font=("Helvetica", 12))
        self.output_sentence_label.pack(pady=5)

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

        # Get the desired percentage of the summary from the user input
        try:
            target_percentage = float(self.percent_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid percentage.")
            return

        # Calculate the target number of sentences for the summary
        target_summary_sentences = int((target_percentage / 100) * len(sentences))

        # Sort sentences based on their values
        sorted_sentences = sorted(sentence_value.items(), key=lambda x: x[1], reverse=True)

        summary = ''
        summary_sentences = []

        # Select top sentences for the summary
        for sentence, _ in sorted_sentences[:target_summary_sentences]:
            summary += " " + sentence
            summary_sentences.append(sentences.index(sentence) + 1)

        self.summary_text.delete(1.0, tk.END)
        self.summary_text.insert(tk.END, summary)

        # Set input and output sentence labels
        input_sentence_count = len(sentences)
        output_sentence_count = len(summary_sentences)

        self.input_sentence_label.config(text=f"Total Sentences in Input Text: {input_sentence_count}")
        self.output_sentence_label.config(text=f"Total Sentences in Output Summary: {output_sentence_count}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TextSummarizerApp(root)
    root.mainloop()
