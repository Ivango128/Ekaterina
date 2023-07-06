#PKP57J-LKJRVT8HHV


import requests

def get_solution(question):
    app_id = 'PKP57J-LKJRVT8HHV'  # Ваш идентификатор приложения Wolfram|Alpha
    api_url = f'http://api.wolframalpha.com/v2/query?input={question}&appid={app_id}'

    try:
        response = requests.get(api_url)
        data = response.text
        print(data)

        # Извлекаем решение из ответа
        data = data.replace('<plaintext>', '',1)
        data = data.replace('</plaintext>', '',1)
        #solution = data[start_index:end_index].strip()

        start_index = data.find('<plaintext>') + len('<plaintext>')
        end_index = data.find('</plaintext>')
        solution = data[start_index:end_index].strip()

        return solution
    except requests.exceptions.RequestException:
        print('Произошла ошибка при отправке запроса.')
        return None

# Пример использования
question = '2 + 2 - 56'
solution = get_solution(question)
if solution:
    print(f'Решение: {solution}')
else:
    print('Не удалось получить решение.')
