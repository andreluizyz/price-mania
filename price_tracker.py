import requests

def buscar_produtos(product):
    url = f"https://dummyjson.com/products/search?q={product}"

    answer = requests.get(url)

    if answer.status_code != 200:
        print("Erro ao buscar dados da API")
        return
    
    data = answer.json()
    return data["products"]


def mostrar_produtos(produtos):
    if not produtos:
        print("No products found.")
        return
    
    print("\n📦 Products found:\n")
    
    for p in produtos:
        print(f"Name: {p['title']}")
        print(f"Price: ${p['price']}")
        print(f"Rating: {p['rating']}")
        print("-" * 30)


def main():
    product = input("Enter the product you want to find: ")
    
    products = buscar_produtos(product)
    mostrar_produtos(products)


if __name__ == "__main__":
    main()