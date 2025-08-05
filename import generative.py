
import tkinter as tk
from transformers import pipeline, set_seed

# Load the GPT-2 generator only once
generator = pipeline('text-generation', model='gpt2')
set_seed(42)  # For reproducibility

def generate_text():
    topic = entry.get()
    if not topic.strip():
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter a topic.")
        return

    # Generate text
    results = generator(topic, max_length=150, num_return_sequences=1)

    # Display result
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, results[0]['generated_text'])

# GUI setup
root = tk.Tk()
root.title("GPT-2 Text Generator")
root.geometry("700x500")

# Title Label
title_label = tk.Label(root, text="GPT-2 Text Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Input Entry
entry_label = tk.Label(root, text="Enter a topic:", font=("Arial", 12))
entry_label.pack()

entry = tk.Entry(root, width=70, font=("Arial", 12))
entry.pack(pady=5)

# Generate Button
generate_btn = tk.Button(root, text="Generate Text", font=("Arial", 12), command=generate_text)
generate_btn.pack(pady=10)

# Output Text Box
output_text = tk.Text(root, wrap='word', font=("Arial", 12), height=15, width=80)
output_text.pack(pady=10)

# Run the GUI
root.mainloop()