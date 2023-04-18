# Функиця выводин информацию из справочника
def show_data() -> None:
    with open('tel_book/telbook.txt', "r", encoding='utf-8') as f:
        print(f.read())
    print('===== Конец справочника =====\n')


# Функция добавления информации в справочник
def add_data() -> None:
    fio = input("Введите ФИО контакта: ")
    tel_number = input("Введите номер телефона: ")
    with open('tel_book/telbook.txt', "a", encoding='utf-8') as f:
        f.write(f'\n{fio} |  {tel_number}')
    print('Контакт добавлен!\n')


# Функция поиска инфы в справочнике
def find_data() -> None:
    data = input('Введите данные для поиска: ')
    with open('tel_book/telbook.txt', "r", encoding='utf-8') as f:
        tel_book = f.read()
    print('Результаты поиска:')
    print(search(tel_book, data))


# Функция находит в строке записи по определенному криетерию поиска. Используем как подфункцию в функции find_data для вывода инфы
def search(book: str, info: str) -> str:
    book = book.split('\n') #для понимания разделителя данных взяли новую строку \n
    return '\n'.join([post for post in book if info in post]) # выводи инфу по каждому найденному значения в списком с новой строки



'''
Домашнее задание:
Функция изменения записи работает следующим образом:
1. Запросить пользователя ввести данные для поиска (имя или номер телефона).
2. Прочитать телефонный справочник из файла и найти все записи, которые содержат заданные данные для поиска.
3. Если найдена только одна запись, то выбрать ее для изменения. Если найдено несколько записей, то вывести список найденных записей и попросить пользователя выбрать одну для изменения.
4. Предложить пользователю выбрать, какое поле записи он хочет изменить: имя или номер телефона.
5.1. Если пользователь выбирает изменить имя, то запросить новое имя и создать новую запись с новым именем и старым номером телефона.
5.2. Если пользователь выбирает изменить номер телфона, то запросит новый номер телефона и оставит старое имя'''

# Функция изменения информации в справочнике
def edit_data() -> None:
    data = input('Введите данные для поиска: ')
    with open('tel_book/telbook.txt', "r", encoding='utf-8') as f:
        tel_book = f.read()
    
    # Поиск информации для изменения
    found_records = [post for post in tel_book.split('\n') if data in post]
    if len(found_records) == 0:
        print('Ничего не найдено.')
        return
    elif len(found_records) == 1:
        record = found_records[0]
    else:
        # Если найдено несколько записей, показать список и попросить пользователя выбрать
        print('Найдено несколько записей:')
        for i, r in enumerate(found_records):
            print(f'{i+1}. {r}')
        choice = input('Введите номер записи, которую хотите изменить: ')
        try:
            record = found_records[int(choice)-1]
        except (IndexError, ValueError):
            print('Неверный выбор.')
            return
    
    # Предложить изменить имя или номер телефона
    print('Что вы хотите изменить?')
    print(f'1. Имя: {record.split("|")[0].strip()}')
    print(f'2. Номер телефона: {record.split("|")[1].strip()}')
    choice = input('Введите номер поля для изменения: ')
    if choice == '1':
        new_name = input('Введите новое имя: ')
        new_record = new_name + ' | ' + record.split("|")[1].strip()
    elif choice == '2':
        new_number = input('Введите новый номер телефона: ')
        new_record = record.split("|")[0].strip() + ' | ' + new_number
    else:
        print('Неверный выбор.')
        return
    
    # Изменить запись и записать обновленный список в файл
    with open('tel_book/telbook.txt', "w", encoding='utf-8') as f:
        for post in tel_book.split('\n'):
            if post == record:
                f.write(new_record+'\n')
            else:
                f.write(post+'\n')
    print('Запись успешно изменена!\n')



'''
Функция удаления записи работает следующим образом:
1. Прочитать переменную информацию из файла.
2. Организовать поиск в этой информации.
3. Вывести список контактов, соответствующих заданному имени или фамилии.
4. Попросить пользователя выбрать номер контакта для удаления.
5. Удалить выбранный контакт из списка.
6. Перезаписать файл через 'w'
'''
# Функиця удаления инфы в справочнике:
def delete_data() -> None:
    data = input('Введите имя или фамилию контакта для удаления: ')
    with open('tel_book/telbook.txt', "r", encoding='utf-8') as f:
        tel_book = f.read()
    
    contacts = [post for post in tel_book.split('\n') if data in post]
    if not contacts:
        print('Контакты не найдены')
        return
    
    print('Список контактов:')
    for i, contact in enumerate(contacts):
        print(f'{i + 1}. {contact}')
    
    try:
        choice = int(input('Выберите номер контакта для удаления: '))
    except ValueError:
        print('Некорректный ввод')
        return
    
    if not 1 <= choice <= len(contacts):
        print('Некорректный номер контакта')
        return
    
    contacts.pop(choice - 1)
    new_tel_book = '\n'.join(contacts)
    
    with open('tel_book/telbook.txt', "w", encoding='utf-8') as f:
        f.write(new_tel_book)
    print('Контакт удален!\n')
