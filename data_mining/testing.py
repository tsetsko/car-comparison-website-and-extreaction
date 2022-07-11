import json
data = [{0: {'General Data': {'Date of production': 'юни 2021г.', 'Type of engine': 'Дизелов', 'Horsepower': '150 к.с.', 'Eurostandard': 'Евро 6', 'Transmission': 'Автоматична', 'Car type': 'Купе', 'Kilometers traveled': '18400 км', 'Colour': 'Син'}}, 'Price': 74400, 'Additional Data': ['Антиблокираща система', 'Въздушни възглавници - Странични', 'Електронна програма за стабилизиране', 'Контрол на налягането на гумите', 'Парктроник', 'Система ISOFIX', 'Система за контрол на дистанцията', 'Система за подпомагане на спирането', 'Лизинг', 'Сервизна книжка', 'Лизинг', 'Сервизна книжка', 'Лети джанти', 'Металик', 'Теглич', 'Аларма', 'Имобилайзер', 'Аларма', 'Имобилайзер', 'Auto Start Stop function', 'Bluetooth \\ handsfree система', 'USB, audio\\video, IN\\AUX изводи', 'Безключово палене', 'Бордкомпютър', 'Ел. Огледала', 'Климатроник', 'Мултифункционален волан', 'Навигация', 'Подгряване на седалките', 'Система за контрол на скоростта (автопилот)', 'Стерео уредба']}, {1: {'General Data': {'Date of production': 'февруари 2022г.', 'Type of engine': 'Бензинов', 'Horsepower': '374 к.с.', 'Eurostandard': 'Евро 6', 'Transmission': 'Автоматична', 'Car type': 'Купе', 'Kilometers traveled': '1000 км', 'Colour': 'Сив'}}, 'Price': 60000, 'Additional Data': []}, {'Price': 19940, 'Additional Data': []}, {3: {'General Data': {'Date of production': 'юли 2021г.', 'Type of engine': 'Бензинов', 'Horsepower': '178 к.с.', 'Eurostandard': 'Евро 6', 'Transmission': 'Автоматична', 'Car type': 'Ван', 'Kilometers traveled': '29500 км', 'Colour': 'Черен'}}, 'Price': 64000, 'Additional Data': ['GPS система за проследяване', 'Автоматичен контрол на стабилността', 'Адаптивни предни светлини', 'Въздушни възглавници - Задни', 'Въздушни възглавници - Предни', 'Въздушни възглавници - Странични', 'Ел. разпределяне на спирачното усилие', 'Електронна програма за стабилизиране', 'Парктроник', 'Система ISOFIX', 'Система за подпомагане на спирането', 'Нов внос', 'Сервизна книжка', '4(5) Врати', 'Лети джанти', 'Централно заключване', '4(5) Врати', 'Лети джанти', 'Централно заключване', 'Централно заключване', 'Auto Start Stop function', 'Steptronic, Tiptronic', 'Бордкомпютър', 'Датчик за светлина', 'Ел. Огледала', 'Ел. Стъкла', 'Ел. регулиране на седалките', 'Климатроник', 'Мултифункционален волан', 'Навигация', 'Подгряване на предното стъкло', 'Регулиране на волана', 'Система за контрол на скоростта (автопилот)']}, {4: {'General Data': {'Date of production': 'септември 2021г.', 'Type of engine': 'Дизелов', 'Horsepower': '116 к.с.', 'Eurostandard': 'Евро 6', 'Transmission': 'Автоматична', 'Car type': 'Седан', 'Kilometers traveled': '6700 км', 'Colour': 'Сив'}}, 'Price': 51990, 'Additional Data': ['Автоматичен контрол на стабилността', 'Адаптивни предни светлини', 'Антиблокираща система', 'Въздушни възглавници - Задни', 'Въздушни възглавници - Предни', 'Въздушни възглавници - Странични', 'Ел. разпределяне на спирачното усилие', 'Електронна програма за стабилизиране', 'Контрол на налягането на гумите', 'Парктроник', 'Система ISOFIX', 'Система за динамична устойчивост', 'Система за защита от пробуксуване', 'Система за изсушаване на накладките', 'Система за контрол на спускането', 'Система за подпомагане на спирането', 'Напълно обслужен', 'Нов внос', 'С регистрация', 'Сервизна книжка', 'Тунинг', 'Напълно обслужен', 'Нов внос', 'С регистрация', 'Сервизна книжка', 'Тунинг', '4(5) Врати', 'LED фарове', 'Ксенонови фарове', 'Лети джанти', 'Металик', 'Отопляеми чистачки', 'Аларма', 'Имобилайзер', 'Каско', 'Централно заключване', 'Аларма', 'Имобилайзер', 'Каско', 'Централно заключване', 'Auto Start Stop function', 'Bluetooth \\ handsfree система', 'DVD, TV', 'Steptronic, Tiptronic', 'USB, audio\\video, IN\\AUX изводи', 'Безключово палене', 'Бордкомпютър', 'Бързи \\ бавни скорости', 'Датчик за светлина', 'Ел. Огледала', 'Ел. Стъкла', 'Ел. усилвател на волана', 'Климатроник', 'Мултифункционален волан', 'Навигация', 'Подгряване на седалките', 'Регулиране на волана', 'Сензор за дъжд', 'Серво усилвател на волана', 'Система за контрол на скоростта (автопилот)', 'Стерео уредба', 'Филтър за твърди частици', 'Хладилна жабка']}, {5: {'General Data': {'Date of production': 'ноември 2020г.', 'Type of engine': 'Дизелов', 'Horsepower': '150 к.с.', 'Eurostandard': 'Евро 6', 'Transmission': 'Автоматична', 'Car type': 'Седан', 'Kilometers traveled': '14600 км', 'Colour': 'Син'}}, 'Price': 65000, 'Additional Data': ['GPS система за проследяване', 'Автоматичен контрол на стабилността', 'Антиблокираща система', 'Въздушни възглавници - Задни', 'Въздушни възглавници - Предни', 'Въздушни възглавници - Странични', 'Ел. разпределяне на спирачното усилие', 'Електронна програма за стабилизиране', 'Контрол на налягането на гумите', 'Парктроник', 'Система ISOFIX', 'Система за динамична устойчивост', 'Система за защита от пробуксуване', 'Система за контрол на спускането', 'Система за подпомагане на спирането', 'Напълно обслужен', 'Нов внос', 'Сервизна книжка', 'Напълно обслужен', 'Нов внос', 'Сервизна книжка', '4(5) Врати', 'LED фарове', 'Металик', 'Аларма', 'Централно заключване', 'Кожен салон', 'Аларма', 'Централно заключване', 'Кожен салон', 'Кожен салон', 'Auto Start Stop function', 'Bluetooth \\ handsfree система', 'Steptronic, Tiptronic', 'USB, audio\\video, IN\\AUX изводи', 'Безключово палене', 'Блокаж на диференциала', 'Бордкомпютър', 'Датчик за светлина', 'Ел. Огледала', 'Ел. Стъкла', 'Ел. усилвател на волана', 'Климатроник', 'Мултифункционален волан', 'Навигация', 'Подгряване на седалките', 'Регулиране на волана', 'Сензор за дъжд', 'Серво усилвател на волана', 'Система за контрол на скоростта (автопилот)', 'Стерео уредба', 'Филтър за твърди частици', 'Хладилна жабка']}, {6: {'General Data': {'Date of production': 'октомври 2020г.', 'Type of engine': 'Дизелов', 'Horsepower': '190 к.с.', 'Eurostandard': 'Евро 6', 'Transmission': 'Автоматична', 'Car type': 'Купе', 'Kilometers traveled': '15000 км', 'Colour': 'Тъмно сив'}}, 'Price': 77000, 'Additional Data': ['GPS система за проследяване', 'Автоматичен контрол на стабилността', 'Адаптивни предни светлини', 'Антиблокираща система', 'Въздушни възглавници - Задни', 'Въздушни възглавници - Предни', 'Въздушни възглавници - Странични', 'Ел. разпределяне на спирачното усилие', 'Електронна програма за стабилизиране', 'Контрол на налягането на гумите', 'Парктроник', 'Система ISOFIX', 'Система за динамична устойчивост', 'Система за защита от пробуксуване', 'Система за контрол на дистанцията', 'Система за подпомагане на спирането', '4x4', 'Напълно обслужен', 'Нов внос', 'С регистрация', 'Сервизна книжка', '4x4', 'Напълно обслужен', 'Нов внос', 'С регистрация', 'Сервизна книжка', '4(5) Врати', 'LED фарове', 'Ксенонови фарове', 'Лети джанти', 'Металик', 'Халогенни фарове', 'Аларма', 'Имобилайзер', 'Каско', 'Централно заключване', 'Велурен салон', 'Кожен салон', 'Аларма', 'Имобилайзер', 'Каско', 'Централно заключване', 'Велурен салон', 'Кожен салон', 'Велурен салон', 'Кожен салон', 'Auto Start Stop function', 'Bluetooth \\ handsfree система', 'Steptronic, Tiptronic', 'USB, audio\\video, IN\\AUX изводи', 'Безключово палене', 'Бордкомпютър', 'Датчик за светлина', 'Ел. Огледала', 'Ел. Стъкла', 'Ел. регулиране на окачването', 'Ел. регулиране на седалките', 'Ел. усилвател на волана', 'Климатроник', 'Мултифункционален волан', 'Навигация', 'Отопление на волана', 'Печка', 'Подгряване на седалките', 'Регулиране на волана', 'Сензор за дъжд', 'Серво усилвател на волана', 'Система за измиване на фаровете', 'Система за контрол на скоростта (автопилот)', 'Стерео уредба', 'Филтър за твърди частици']}, {7: {'General Data': {'Date of production': 'ноември 2020г.', 'Type of engine': 'Дизелов', 'Horsepower': '190 к.с.', 'Eurostandard': 'Евро 6', 'Transmission': 'Автоматична', 'Car type': 'Купе', 'Kilometers traveled': '30376 км', 'Colour': 'Черен'}}, 'Price': 84900, 'Additional Data': ['Автоматичен контрол на стабилността', 'Антиблокираща система', 'Въздушни възглавници - Задни', 'Въздушни възглавници - Предни', 'Въздушни възглавници - Странични', 'Ел. разпределяне на спирачното усилие', 'Електронна програма за стабилизиране', 'Контрол на налягането на гумите', 'Парктроник', 'Система ISOFIX', 'Система за динамична устойчивост', 'Система за защита от пробуксуване', 'Система за контрол на дистанцията', 'Система за подпомагане на спирането', '4x4', 'Buy back', 'Бартер', 'Лизинг', 'Напълно обслужен', 'Сервизна книжка', '4x4', 'Buy back', 'Бартер', 'Лизинг', 'Напълно обслужен', 'Сервизна книжка', '4(5) Врати', 'LED фарове', 'Лети джанти', 'Металик', 'Халогенни фарове', 'Аларма', 'Имобилайзер', 'Централно заключване', 'Кожен салон', 'Аларма', 'Имобилайзер', 'Централно заключване', 'Кожен салон', 'Кожен салон', 'Auto Start Stop function', 'Bluetooth \\ handsfree система', 'Steptronic, Tiptronic', 'USB, audio\\video, IN\\AUX изводи', 'Безключово палене', 'Бордкомпютър', 'Датчик за светлина', 'Ел. Огледала', 'Ел. Стъкла', 'Ел. усилвател на волана', 'Климатроник', 'Мултифункционален волан', 'Навигация', 'Печка', 'Подгряване на седалките', 'Регулиране на волана', 'Сензор за дъжд', 'Серво усилвател на волана', 'Система за контрол на скоростта (автопилот)', 'Стерео уредба', 'Филтър за твърди частици']}, {8: {'General Data': {'Date of production': 'май 2021г.', 'Type of engine': 'Бензинов', 'Horsepower': '306 к.с.', 'Eurostandard': 'Евро 6', 'Transmission': 'Автоматична', 'Car type': 'Седан', 'Kilometers traveled': '7600 км', 'Colour': 'Черен'}}, 'Price': 95000, 'Additional Data': ['Автоматичен контрол на стабилността', 'Антиблокираща система', 'Въздушни възглавници - Задни', 'Въздушни възглавници - Предни', 'Въздушни възглавници - Странични', 'Ел. разпределяне на спирачното усилие', 'Електронна програма за стабилизиране', 'Контрол на налягането на гумите', 'Парктроник', 'Система за динамична устойчивост', 'Система за защита от пробуксуване', 'Система за контрол на дистанцията', 'Система за контрол на спускането', 'Система за подпомагане на спирането', '4x4', 'Лизинг', '4(5) Врати', 'LED фарове', 'Металик', 'Аларма', 'Кожен салон', '4(5) Врати', 'LED фарове', 'Металик', 'Аларма', 'Кожен салон', 'Аларма', 'Кожен салон', 'Кожен салон', 'Auto Start Stop function', 'Bluetooth \\ handsfree система', 'Steptronic, Tiptronic', 'USB, audio\\video, IN\\AUX изводи', 'Безключово палене', 'Бордкомпютър', 'Датчик за светлина', 'Ел. Огледала', 'Ел. Стъкла', 'Ел. усилвател на волана', 'Климатроник', 'Мултифункционален волан', 'Навигация', 'Отопление на волана', 'Сензор за дъжд', 'Серво усилвател на волана', 'Система за контрол на скоростта (автопилот)']}, {9: {'General Data': {'Date of production': 'септември 2020г.', 'Type of engine': 'Бензинов', 'Horsepower': '306 к.с.', 'Eurostandard': 'Евро 6', 'Transmission': 'Автоматична', 'Car type': 'Седан', 'Kilometers traveled': '22000 км', 'Colour': 'Черен'}}, 'Price': 98000, 'Additional Data': ['GPS система за проследяване', 'Автоматичен контрол на стабилността', 'Адаптивни предни светлини', 'Антиблокираща система', 'Въздушни възглавници - Задни', 'Въздушни възглавници - Предни', 'Въздушни възглавници - Странични', 'Ел. разпределяне на спирачното усилие', 'Електронна програма за стабилизиране', 'Контрол на налягането на гумите', 'Парктроник', 'Система ISOFIX', 'Система за динамична устойчивост', 'Система за защита от пробуксуване', 'Система за изсушаване на накладките', 'Система за контрол на дистанцията', 'Система за контрол на спускането', 'Система за подпомагане на спирането', '4x4', 'Лизинг', 'Напълно обслужен', 'С регистрация', 'Сервизна книжка', '4x4', 'Лизинг', 'Напълно обслужен', 'С регистрация', 'Сервизна книжка', '4(5) Врати', 'LED фарове', 'Лети джанти', 'Металик', 'Отопляеми чистачки', 'Спойлери', 'Аларма', 'Каско', 'Централно заключване', 'Велурен салон', 'Аларма', 'Каско', 'Централно заключване', 'Велурен салон', 'Велурен салон', 'Auto Start Stop function', 'Bluetooth \\ handsfree система', 'DVD, TV', 'Steptronic, Tiptronic', 'USB, audio\\video, IN\\AUX изводи', 'Безключово палене', 'Бордкомпютър', 'Датчик за светлина', 'Ел. Огледала', 'Ел. Стъкла', 'Ел. регулиране на окачването', 'Ел. регулиране на седалките', 'Ел. усилвател на волана', 'Климатик', 'Мултифункционален волан', 'Навигация', 'Отопление на волана', 'Печка', 'Подгряване на предното стъкло', 'Подгряване на седалките', 'Регулиране на волана', 'Сензор за дъжд', 'Серво усилвател на волана', 'Система за контрол на скоростта (автопилот)', 'Стерео уредба', 'Филтър за твърди частици']}, {10: {'General Data': {'Date of production': 'февруари 2022г.', 'Type of engine': 'Бензинов', 'Horsepower': '136 к.с.', 'Eurostandard': 'Евро 6', 'Transmission': 'Автоматична', 'Car type': 'Ван', 'Kilometers traveled': '4102 км', 'Colour': 'Бял'}}, 'Price': 73900, 'Additional Data': ['Антиблокираща система', 'Въздушни възглавници - Странични', 'Електронна програма за стабилизиране', 'Контрол на налягането на гумите', 'Парктроник', 'Система ISOFIX', 'Система за контрол на дистанцията', 'Система за подпомагане на спирането', 'Сервизна книжка', 'Сервизна книжка', 'LED фарове', 'Металик', 'Рейлинг на покрива', 'Аларма', 'Имобилайзер', 'Аларма', 'Имобилайзер', 'Auto Start Stop function', 'Bluetooth \\ handsfree система', 'USB, audio\\video, IN\\AUX изводи', 'Безключово палене', 'Бордкомпютър', 'Ел. Огледала', 'Отопление на волана', 'Подгряване на седалките', 'Стерео уредба']}, {11: {'General Data': {'Date of production': 'юни 2021г.', 'Type of engine': 'Бензинов', 'Horsepower': '140 к.с.', 'Eurostandard': 'Евро 6', 'Transmission': 'Автоматична', 'Car type': 'Седан', 'Kilometers traveled': '9000 км', 'Colour': 'Графит'}}, 'Price': 75500, 'Additional Data': ['Автоматичен контрол на стабилността', 'Адаптивни предни светлини', 'Антиблокираща система', 'Въздушни възглавници - Задни', 'Въздушни възглавници - Предни', 'Въздушни възглавници - Странични', 'Ел. разпределяне на спирачното усилие', 'Електронна програма за стабилизиране', 'Контрол на налягането на гумите', 'Парктроник', 'Система ISOFIX', 'Система за динамична устойчивост', 'Система за защита от пробуксуване', 'Система за изсушаване на накладките', 'Система за контрол на дистанцията', 'Система за контрол на спускането', 'Система за подпомагане на спирането', 'Buy back', 'Лизинг', 'Нов внос', 'Сервизна книжка', 'Тунинг', 'Buy back', 'Лизинг', 'Нов внос', 'Сервизна книжка', 'Тунинг', '4(5) Врати', 'LED фарове', 'Лети джанти', 'Металик', 'Отопляеми чистачки', 'Спойлери', 'Теглич', 'Аларма', 'Имобилайзер', 'Централно заключване', 'Кожен салон', 'Аларма', 'Имобилайзер', 'Централно заключване', 'Кожен салон', 'Кожен салон', 'Auto Start Stop function', 'Bluetooth \\ handsfree система', 'Steptronic, Tiptronic', 'USB, audio\\video, IN\\AUX изводи', 'Безключово палене', 'Блокаж на диференциала', 'Бордкомпютър', 'Датчик за светлина', 'Ел. Огледала', 'Ел. Стъкла', 'Ел. регулиране на окачването', 'Ел. регулиране на седалките', 'Ел. усилвател на волана', 'Климатроник', 'Мултифункционален волан', 'Навигация', 'Подгряване на седалките', 'Регулиране на волана', 'Сензор за дъжд', 'Серво усилвател на волана', 'Система за контрол на скоростта (автопилот)', 'Стерео уредба', 'Филтър за твърди частици', 'Хладилна жабка']}, {12: {'General Data': {'Date of production': 'май 2021г.', 'Type of engine': 'Дизелов', 'Horsepower': '150 к.с.', 'Eurostandard': 'Евро 6', 'Transmission': 'Автоматична', 'Car type': 'Купе', 'Kilometers traveled': '25500 км', 'Colour': 'Син'}}, 'Price': 82500, 'Additional Data': ['Антиблокираща система', 'Въздушни възглавници - Странични', 'Електронна програма за стабилизиране', 'Контрол на налягането на гумите', 'Парктроник', 'Система ISOFIX', 'Система за контрол на дистанцията', 'Система за подпомагане на спирането', 'Лизинг', 'Сервизна книжка', 'Лизинг', 'Сервизна книжка', 'Лети джанти', 'Металик', 'Панорамен люк', 'Шибедах', 'Аларма', 'Имобилайзер', 'Аларма', 'Имобилайзер', 'Auto Start Stop function', 'Bluetooth \\ handsfree система', 'USB, audio\\video, IN\\AUX изводи', 'Безключово палене', 'Бордкомпютър', 'Ел. Огледала', 'Климатроник', 'Мултифункционален волан', 'Навигация', 'Подгряване на седалките', 'Система за контрол на скоростта (автопилот)', 'Стерео уредба']}, {13: {'General Data': {'Date of production': 'март 2022г.', 'Type of engine': 'Дизелов', 'Horsepower': '150 к.с.', 'Eurostandard': 'Евро 6', 'Transmission': 'Автоматична', 'Car type': 'Ван', 'Kilometers traveled': '4223 км', 'Colour': 'Зелен'}}, 'Price': 87900, 'Additional Data': ['Антиблокираща система', 'Въздушни възглавници - Странични', 'Електронна програма за стабилизиране', 'Контрол на налягането на гумите', 'Парктроник', 'Система ISOFIX', 'Система за контрол на дистанцията', 'Система за подпомагане на спирането', 'Сервизна книжка', 'Сервизна книжка', 'LED фарове', 'Лети джанти', 'Металик', 'Рейлинг на покрива', 'Аларма', 'Имобилайзер', 'Аларма', 'Имобилайзер', 'Auto Start Stop function', 'Bluetooth \\ handsfree система', 'USB, audio\\video, IN\\AUX изводи', 'Безключово палене', 'Бордкомпютър', 'Ел. Огледала', 'Ел. регулиране на окачването', 'Ел. регулиране на седалките', 'Навигация', 'Отопление на волана', 'Подгряване на седалките', 'Стерео уредба']}, {14: {'General Data': {'Date of production': 'юни 2022г.', 'Type of engine': 'Бензинов', 'Horsepower': '170 к.с.', 'Eurostandard': 'Евро 6', 'Transmission': 'Автоматична', 'Car type': 'Ван', 'Kilometers traveled': '49 км', 'Colour': 'Бял'}}, 'Price': 93500, 'Additional Data': ['Автоматичен контрол на стабилността', 'Адаптивни предни светлини', 'Антиблокираща система', 'Въздушни възглавници - Задни', 'Въздушни възглавници - Предни', 'Въздушни възглавници - Странични', 'Ел. разпределяне на спирачното усилие', 'Електронна програма за стабилизиране', 'Контрол на налягането на гумите', 'Парктроник', 'Система ISOFIX', 'Система за динамична устойчивост', 'Система за защита от пробуксуване', 'Система за изсушаване на накладките', 'Система за контрол на спускането', 'Система за подпомагане на спирането', 'Buy back', 'Лизинг', 'Нов внос', 'С право на дан.к-т', 'Сервизна книжка', 'Buy back', 'Лизинг', 'Нов внос', 'С право на дан.к-т', 'Сервизна книжка', '4(5) Врати', 'LED фарове', 'Лети джанти', 'Металик', 'Отопляеми чистачки', 'Рейлинг на покрива', 'Аларма', 'Имобилайзер', 'Централно заключване', 'Кожен салон', 'Аларма', 'Имобилайзер', 'Централно заключване', 'Кожен салон', 'Кожен салон', 'Auto Start Stop function', 'Bluetooth \\ handsfree система', 'Steptronic, Tiptronic', 'USB, audio\\video, IN\\AUX изводи', 'Безключово палене', 'Блокаж на диференциала', 'Бордкомпютър', 'Датчик за светлина', 'Ел. Огледала', 'Ел. Стъкла', 'Ел. регулиране на окачването', 'Ел. регулиране на седалките', 'Ел. усилвател на волана', 'Климатроник', 'Мултифункционален волан', 'Навигация', 'Подгряване на седалките', 'Регулиране на волана', 'Сензор за дъжд', 'Серво усилвател на волана', 'Система за контрол на скоростта (автопилот)', 'Стерео уредба', 'Филтър за твърди частици', 'Хладилна жабка']}, {15: {'General Data': {'Date of production': 'юни 2022г.', 'Type of engine': 'Бензинов', 'Horsepower': '184 к.с.', 'Eurostandard': 'Евро 6', 'Transmission': 'Автоматична', 'Car type': 'Купе', 'Kilometers traveled': '68 км', 'Colour': 'Бял'}}, 'Price': 98300, 'Additional Data': ['Автоматичен контрол на стабилността', 'Адаптивни предни светлини', 'Антиблокираща система', 'Въздушни възглавници - Задни', 'Въздушни възглавници - Предни', 'Въздушни възглавници - Странични', 'Ел. разпределяне на спирачното усилие', 'Електронна програма за стабилизиране', 'Контрол на налягането на гумите', 'Парктроник', 'Система ISOFIX', 'Система за динамична устойчивост', 'Система за защита от пробуксуване', 'Система за изсушаване на накладките', 'Система за контрол на дистанцията', 'Система за контрол на спускането', 'Система за подпомагане на спирането', 'Buy back', 'Лизинг', 'Нов внос', 'С право на дан.к-т', 'Сервизна книжка', 'Тунинг', '2(3) Врати', 'LED фарове', 'Лети джанти', 'Металик', 'Отопляеми чистачки', 'Спойлери', 'Аларма', 'Имобилайзер', 'Централно заключване', 'Кожен салон', '2(3) Врати', 'LED фарове', 'Лети джанти', 'Металик', 'Отопляеми чистачки', 'Спойлери', 'Аларма', 'Имобилайзер', 'Централно заключване', 'Кожен салон', 'Аларма', 'Имобилайзер', 'Централно заключване', 'Кожен салон', 'Кожен салон', 'Auto Start Stop function', 'Bluetooth \\ handsfree система', 'Steptronic, Tiptronic', 'USB, audio\\video, IN\\AUX изводи', 'Безключово палене', 'Блокаж на диференциала', 'Бордкомпютър', 'Датчик за светлина', 'Ел. Огледала', 'Ел. Стъкла', 'Ел. усилвател на волана', 'Климатроник', 'Мултифункционален волан', 'Навигация', 'Подгряване на седалките', 'Регулиране на волана', 'Сензор за дъжд', 'Серво усилвател на волана', 'Система за контрол на скоростта (автопилот)', 'Стерео уредба', 'Филтър за твърди частици', 'Хладилна жабка']}, {16: {'General Data': {'Date of production': 'януари 2020г.', 'Type of engine': 'Дизелов', 'Horsepower': '190 к.с.', 'Eurostandard': 'Евро 6', 'Transmission': 'Автоматична', 'Car type': 'Купе', 'Kilometers traveled': '22000 км', 'Colour': 'Син'}}, 'Price': 62000, 'Additional Data': ['GPS система за проследяване', 'Автоматичен контрол на стабилността', 'Адаптивни предни светлини', 'Антиблокираща система', 'Въздушни възглавници - Задни', 'Въздушни възглавници - Предни', 'Въздушни възглавници - Странични', 'Ел. разпределяне на спирачното усилие', 'Електронна програма за стабилизиране', 'Контрол на налягането на гумите', 'Парктроник', 'Система ISOFIX', 'Система за динамична устойчивост', 'Система за защита от пробуксуване', 'Система за изсушаване на накладките', 'Система за контрол на дистанцията', 'Система за контрол на спускането', 'Система за подпомагане на спирането', '4x4', 'Бартер', 'Напълно обслужен', 'С регистрация', 'Сервизна книжка', 'Тунинг', '4x4', 'Бартер', 'Напълно обслужен', 'С регистрация', 'Сервизна книжка', 'Тунинг', '2(3) Врати', 'LED фарове', 'Лети джанти', 'Металик', 'Спойлери', 'Халогенни фарове', 'Аларма', 'Имобилайзер', 'Каско', 'Централно заключване', 'Велурен салон', 'Аларма', 'Имобилайзер', 'Каско', 'Централно заключване', 'Велурен салон', 'Велурен салон', 'Auto Start Stop function', 'Bluetooth \\ handsfree система', 'Steptronic, Tiptronic', 'USB, audio\\video, IN\\AUX изводи', 'Безключово палене', 'Блокаж на диференциала', 'Бордкомпютър', 'Датчик за светлина', 'Ел. Огледала', 'Ел. Стъкла', 'Ел. регулиране на седалките', 'Ел. усилвател на волана', 'Климатроник', 'Мултифункционален волан', 'Навигация', 'Подгряване на предното стъкло', 'Подгряване на седалките', 'Регулиране на волана', 'Сензор за дъжд', 'Серво усилвател на волана', 'Система за измиване на фаровете', 'Система за контрол на скоростта (автопилот)', 'Стерео уредба', 'Филтър за твърди частици', 'Хладилна жабка']}, {17: {'General Data': {'Date of production': 'април 2021г.', 'Type of engine': 'Бензинов', 'Horsepower': '306 к.с.', 'Eurostandard': 'Евро 6', 'Transmission': 'Автоматична', 'Car type': 'Купе', 'Kilometers traveled': '21892 км', 'Colour': 'Черен'}}, 'Price': 95000, 'Additional Data': ['Антиблокираща система', 'Въздушни възглавници - Странични', 'Електронна програма за стабилизиране', 'Контрол на налягането на гумите', 'Парктроник', 'Система ISOFIX', 'Система за контрол на дистанцията', 'Система за подпомагане на спирането', '4x4', 'Лизинг', 'Сервизна книжка', '4x4', 'Лизинг', 'Сервизна книжка', 'LED фарове', 'Лети джанти', 'Металик', 'Аларма', 'Имобилайзер', 'Кожен салон', 'Аларма', 'Имобилайзер', 'Кожен салон', 'Кожен салон', 'Auto Start Stop function', 'Bluetooth \\ handsfree система', 'USB, audio\\video, IN\\AUX изводи', 'Безключово палене', 'Бордкомпютър', 'Ел. Огледала', 'Ел. регулиране на седалките', 'Климатроник', 'Мултифункционален волан', 'Навигация', 'Отопление на волана', 'Подгряване на седалките', 'Система за контрол на скоростта (автопилот)', 'Стерео уредба']}]

print(json.dump(data))