import openai;


def main() -> None:
    openai.api_key = "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"

    model_engine = "text-davinci-003"
    prompt = "Write a blog on ChatGPT"
    max_tokens = 1024

    completion = openai.Completion.create(engine = model_engine, prompt = prompt, max_tokens = max_tokens, temperature = 0.5, top_p = 1, frequency_penalty = 0, presence_penalty = 0)

    print(completion.choices[0].text)

if __name__ == "__main__":
    main()