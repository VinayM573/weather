def get_weather(city):
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    print(response.status_code, response.text)  # Debugging
    return response.json() if response.status_code == 200 else None
