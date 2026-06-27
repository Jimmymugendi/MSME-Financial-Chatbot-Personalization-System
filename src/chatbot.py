import requests
from src.utils import get_cluster_profile

ollama_url = "http://127.0.0.1:11434/api/generate"
model_name = "llama2"   # Change to "llama2", "mistral", etc. as available

def query_ollama(prompt: str) -> str:
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False,
        "temperature": 0.7,
        "max_tokens": 300
    }
    try:
        response = requests.post(ollama_url, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()["response"].strip()
    except Exception as e:
        return f"❌ Ollama Error: {str(e)}"

def create_personalized_prompt(user_query: str, cluster_id: int, user_data: dict):
    profile = get_cluster_profile(cluster_id)
    
    prompt = f"""You are MESH Money Coach, a friendly and practical financial assistant for MSMEs in Kenya.

User Profile: {profile}

User Details:
- Monthly Income: {user_data.get('monthly_income', 'N/A')} KES
- Digital Literacy: {user_data.get('digital_literacy_score', 'N/A'):.0f}/100
- Engagement Score: {user_data.get('engagement_score', 'N/A'):.2f}

Rules:
- Speak simply and encouragingly.
- Mix English and simple Kiswahili when helpful.
- Give very practical, actionable advice.
- Keep response under 150 words.

Question: {user_query}

Response:"""
    return prompt

def chatbot_response(user_query: str, cluster_id: int, user_data: dict):
    prompt = create_personalized_prompt(user_query, cluster_id, user_data)
    return query_ollama(prompt)