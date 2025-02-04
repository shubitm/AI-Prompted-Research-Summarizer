try:
    import openai
    openai.api_key = "<your-api-key>"

except ModuleNotFoundError:
    print("Error: The 'openai' module is not installed. Please install it using 'pip install openai' and try again.")
    exit()

def summarize_research_paper():
    """
    Uses ChatGPT-4 to retrieve, analyze, and summarize scientific research papers based on user input.
    """
    topic = input("Enter a research topic: ")
    keywords = input("Enter relevant keywords (comma-separated): ").split(',')
    
    prompt = f"""
    Retrieve and summarize key findings from scientific research papers related to "{topic}".
    Focus on {', '.join(keywords)}.
    Provide a clear and concise explanation suitable for a general audience.
    Highlight the main conclusions, methodologies, and implications.
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an expert research summarizer."},
                      {"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"An error occurred while generating the summary: {e}")
        return None

# Example Usage
if __name__ == "__main__":
    summary = summarize_research_paper()
    if summary:
        print("\nResearch Summary:\n", summary)
