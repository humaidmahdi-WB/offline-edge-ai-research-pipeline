from openai import OpenAI

# Connect to the local LM Studio OpenAI-compatible REST endpoint
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def query_local_llm(prompt: str, temperature: float = 0.2) -> str:
    """Send a technical research query to the offline local model."""
    response = client.chat.completions.create(
        model="local-model",
        messages=[
            {
                "role": "system",
                "content": "You are a precise, analytical STEM and systems-engineering research assistant."
            },
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    sample_prompt = (
        "Analyze the thermal dissipation and memory-bandwidth bottlenecks "
        "when running quantized 3B-parameter LLMs on CPU-bound edge hardware."
    )
    print("Querying offline LM Studio server...\n")
    print(query_local_llm(sample_prompt))
  
