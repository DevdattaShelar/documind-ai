import urllib.request
import os

# Create the data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# We use r.jina.ai to instantly convert web documentation into clean Markdown
docs_to_download = {
    "langchain.md": "https://r.jina.ai/https://python.langchain.com/docs/get_started/introduction",
    "chromadb.md": "https://r.jina.ai/https://docs.trychroma.com/docs/overview/getting-started",
    "fastapi.md": "https://r.jina.ai/https://fastapi.tiangolo.com/",
    "groq.md": "https://r.jina.ai/https://console.groq.com/docs/quickstart",
    "huggingface.md": "https://r.jina.ai/https://huggingface.co/docs/hub/index"
}
for filename, url in docs_to_download.items():
    print(f"Downloading {filename}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req) as response:
            markdown_content = response.read().decode('utf-8')
            with open(f"data/{filename}", "w", encoding="utf-8") as f:
                f.write(markdown_content)
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

print("All files downloaded into the data/ folder!")