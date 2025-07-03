import requests

def test_generate_endpoint():
    url = "http://127.0.0.1:8080/generate"
    payload = {"prompt": "Explain quantum computing in simple terms."}
    response = requests.post(url, json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    print("Test passed ✅", data["response"])

if __name__ == "__main__":
    test_generate_endpoint()
