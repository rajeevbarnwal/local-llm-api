import requests

def test_generate_endpoint():
    url = "http://127.0.0.1:8080/generate"
    payload = {"prompt": "Explain quantum computing in simple terms."}
    response = requests.post(url, json=payload)
    
    # basic sanity checks
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
    data = response.json()
    assert "response" in data or "error" in data, f"Neither 'response' nor 'error' found in {data}"
    print("Test passed ✅", list(data.keys()))

if __name__ == "__main__":
    test_generate_endpoint()
