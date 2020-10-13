import requests

def read_chat():
    r = requests.get('http://localhost:3000/')
    return r.json()

def main():
    print(read_chat())

if __name__ == "__main__":
    main()