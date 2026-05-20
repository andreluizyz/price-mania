import requests

def buscar_produtos(product="iphone"):
    url = f"https://dummyjson.com/products/search?q={product}"

    answer = requests.get(url)

    if answer.status_code != 200:
        print("Erro ao buscar dados da API")
        return
    
    data = answer.json()
    for product in data:
        print(product)
