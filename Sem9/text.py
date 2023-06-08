main_menu = '''\nГлавное меню:
            1. Открыть файл
            2. Сохранить файл
            3. Показать контакты
            4. Добавить контакт
            5. Найти контакт
            6. Изменить контакт
            7. Удалить контакт
            8. Выход
            \n'''

input_choice = "Выберите пункт меню: "

load_successful = 'Телефонная книга успешно открыта'
save_successful = 'Телефонная книга успешно сохранена'
delete_successful = 'Удаление прошло успешно'
change_successful = 'Изменение прошло успешно'

pb_empty = 'Телефонная книга пуста или не загружена!'

input_new_contact = 'Введите данные нового контакта:'
new_contact = {'name': 'Введите имя: ',
               'phone': 'Введите номер телефона: ',
               'comment': 'Введите комментарий: '}

menu_change_contact = ' Введите новое имя, телефон, комментарий в одну строчку через пробелы:'



def new_contact_successful(name: str):
    return f'Контакт {name} успешно добавлен'


input_search = 'Что нужно найти: '

delete_contact = 'Выберете индекс для удаления записи: '
change_contact = 'Выберете индекс для изменения записи: '
change_contact_settings = 'Выберите что будите изменять: '

def empty_search(word) -> str:
    return f'Контакты содержащие слово "{word}" не найдены'
