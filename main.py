#PKP57J-LKJRVT8HHV


import requests

def get_solution(question):
    app_id = 'PKP57J-LKJRVT8HHV'  # Ваш идентификатор приложения Wolfram|Alpha
    api_url = f'http://api.wolframalpha.com/v2/query?input={question}&appid={app_id}'

    try:
        response = requests.get(api_url)
        data = response.text
        print(data)
        solution = ''
        while True:
        # Извлекаем решение из ответа
            start_index = data.find('<plaintext>') + len('<plaintext>')
            if data.find('<plaintext>') !=-1:
                end_index = data.find('</plaintext>')
                solution += data[start_index:end_index].strip()+'\n'
                data = data.replace('<plaintext>', '', 1)
                data = data.replace('</plaintext>', '', 1)
            else:
                break

        return solution
    except requests.exceptions.RequestException:
        print('Произошла ошибка при отправке запроса.')
        return None

# Пример использования
question = 'x^2 + x - 9 = 0'

if '+' in question:
    question = question.replace('+', '%2B')
solution = get_solution(question)

print(f'Решение: {solution}')
# else:
#     print('Не удалось получить решение.')
