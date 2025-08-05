from transformers import pipeline, set_seed

def generate_text(topic, max_length=150, num_return_sequences=1):
    # Load the GPT-2 text generation pipeline
    generator = pipeline('text-generation', model='gpt2')
    set_seed(42)  # Ensures repeatability

    # Generate text
    results = generator(topic, max_length=max_length, num_return_sequences=num_return_sequences)

    # Print the generated text
    for i, result in enumerate(results):
        print(f"\nGenerated Paragraph {i+1}:\n")
        print(result['generated_text'])

# Main tool
if __name__ == "__main__":
    print("Generative Text Tool (GPT-2)")
    user_topic = input("Enter a topic to generate text: ")
    generate_text(user_topic)
    
