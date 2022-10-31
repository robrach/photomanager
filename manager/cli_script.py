import requests

if __name__ == '__main__':
    print("\nScript that calls the import from 'external API' https://jsonplaceholder.typicode.com/photos/ + 'id'")
    print("or from 'JSON file' with a similar structure.\n")
    print('Example input url: https://jsonplaceholder.typicode.com/photos/5')
    print('Example input url: manager/example_photos/photo_json.json   (or full system path)')

    url = input('\nInput source url: ')

    data = {
        'url': url
    }
    response = requests.post('http://127.0.0.1:8000/photos', json=data)
    status_code = response.status_code

    print('status_code =', response.status_code)
    if status_code == 201:
        print('CREATED:', response.text)
