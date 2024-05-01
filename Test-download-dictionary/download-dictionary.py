import requests

def get_dictionary_data(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}"
    response = requests.get(url)
    data = response.json()
    return data

word = "word"  # Từ  muốn tra cứu
dictionary_data = get_dictionary_data(word)

# Hiển thị thông tin từ điển
if 'title' in dictionary_data:
    print("Error:", dictionary_data['title'])
else:
    meanings = dictionary_data[0]['meanings']
    for meaning in meanings:
        print("Part of speech:", meaning['partOfSpeech'])
        definitions = meaning['definitions']
        for definition in definitions:
            print("- Definition:", definition['definition'])
            if 'example' in definition:
                print("- Example:", definition['example'])
