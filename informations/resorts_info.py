
def get_resort(service, resort_name):
    resort = resorts_content[service][resort_name]
    return resort


resorts_content = {
    # resorts links on Hotels24.ua
    'hotels_links': {
        'Славське': 'https://hotels24.ua/?lang_code=uk&target=search&event=city&typeLink=hotels24&city_id=18598&order_hotel=15&dateDeparture=&openMap=0&city=%D0%A1%D0%BB%D0%B0%D0%B2%D1%81%D1%8C%D0%BA%D0%B5&guests%5B1%5D%5B0%5D=2&guests%5B1%5D%5B1%5D=0&guests%5B1%5D%5B2%5D=0&FilterForm%5Bgeocode_reverse%5D=null&geoLandingId=',
        'Драгобрат': 'https://hotels24.ua/?target=search&event=hotel&storeDateInCookie=1&typeLink=hotels24&city_id=18600&order_hotel=&lang_code=uk&dateArrival=&dateDeparture=&openMap=0&city=%D0%B4%D1%80%D0%B0%D0%B3%D0%BE%D0%B1%D1%80%D0%B0%D1%82&datePicker=&guests%5B1%5D%5B0%5D=2&guests%5B1%5D%5B1%5D=0&guests%5B1%5D%5B2%5D=0',
        'Буковель': 'https://hotels24.ua/?target=search&event=hotel&storeDateInCookie=1&typeLink=hotels24&city_id=18602&lang_code=uk&dateArrival=&dateDeparture=&openMap=0&city=%D0%91%D1%83%D0%BA%D0%BE%D0%B2%D0%B5%D0%BB%D1%8C%2C+%D0%86%D0%B2%D0%B0%D0%BD%D0%BE-%D0%A4%D1%80%D0%B0%D0%BD%D0%BA%D1%96%D0%B2%D1%81%D1%8C%D0%BA%D0%B0+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%2C+%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B0+&datePicker=&guests%5B1%5D%5B0%5D=2&guests%5B1%5D%5B1%5D=0&guests%5B1%5D%5B2%5D=0',
        'Пилипець': 'https://hotels24.ua/?target=search&event=hotel&storeDateInCookie=1&typeLink=hotels24&city_id=18623&lang_code=uk&dateArrival=&dateDeparture=&openMap=0&city=%D0%9F%D0%B8%D0%BB%D0%B8%D0%BF%D0%B5%D1%86%D1%8C%2C+%D0%97%D0%B0%D0%BA%D0%B0%D1%80%D0%BF%D0%B0%D1%82%D1%81%D1%8C%D0%BA%D0%B0+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%2C+%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B0+&datePicker=&guests%5B1%5D%5B0%5D=2&guests%5B1%5D%5B1%5D=0&guests%5B1%5D%5B2%5D=0',
        'Плай': 'https://hotels24.ua/?target=search&event=hotel&storeDateInCookie=1&typeLink=hotels24&city_id=18696&lang_code=uk&dateArrival=&dateDeparture=&openMap=0&city=%D0%9F%D0%BB%D0%B0%D0%B9%2C+%D0%9B%D1%8C%D0%B2%D1%96%D0%B2%D1%81%D1%8C%D0%BA%D0%B0+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%2C+%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B0+&datePicker=&guests%5B1%5D%5B0%5D=2&guests%5B1%5D%5B1%5D=0&guests%5B1%5D%5B2%5D=0',
        'Яблуниця': 'https://hotels24.ua/?target=search&event=hotel&storeDateInCookie=1&typeLink=hotels24&city_id=18651&lang_code=uk&dateArrival=&dateDeparture=&openMap=0&city=%C2%A0%D1%8F%D0%B1%D0%BB%D1%83%D0%BD%D0%B8%D1%86%D1%8F&datePicker=&guests%5B1%5D%5B0%5D=2&guests%5B1%5D%5B1%5D=0&guests%5B1%5D%5B2%5D=0',
        'Красія': 'https://hotels24.ua/?target=search&event=hotel&storeDateInCookie=1&typeLink=hotels24&city_id=18703&lang_code=uk&dateArrival=&dateDeparture=&openMap=0&city=%D0%9A%D1%80%D0%B0%D1%81%D1%96%D1%8F&datePicker=&guests%5B1%5D%5B0%5D=2&guests%5B1%5D%5B1%5D=0&guests%5B1%5D%5B2%5D=0',
        'Мигове': 'https://hotels24.ua/?target=search&event=hotel&storeDateInCookie=1&typeLink=hotels24&city_id=18657&lang_code=uk&dateArrival=&dateDeparture=&openMap=0&city=%D0%9C%D0%B8%D0%B3%D0%BE%D0%B2%D0%BE&datePicker=&guests%5B1%5D%5B0%5D=2&guests%5B1%5D%5B1%5D=0&guests%5B1%5D%5B2%5D=0',
        'Яремче': 'https://hotels24.ua/?target=search&event=hotel&storeDateInCookie=1&typeLink=hotels24&city_id=18300&lang_code=uk&dateArrival=&dateDeparture=&openMap=0&city=%D0%AF%D1%80%D0%B5%D0%BC%D1%87%D0%B5&datePicker=&guests%5B1%5D%5B0%5D=2&guests%5B1%5D%5B1%5D=0&guests%5B1%5D%5B2%5D=0',
    },
    # information about resorts
    'resorts_info': {
        'Славське': '<b>Славське</b>\nЦей курорт розташований на відстані в 130 кілометрів від Львова. Комплекс досить популярний, сюди щороку вирушає чимало любителів та професіоналів лижного спорту. Загалом тут є 11 трас різного рівня складності. Висота варіюється від 1000 до 1600 метрів над рівнем моря. Саме у Славському функціонує найдовший крісельний витяг України, довжина якого досягає 2700 метрів. Що стосується загальної протяжності спусків, то це 22 кілометри.\n\nСлавське є відомим центром гірськолижного спорту, адже саме тут тренується наша олімпійська збірна. Окрім того, на цьому курорті регулярно проходять різноманітні змагання.\n\nСлавське – курорт із м’яким гірським кліматом. Тут дуже розвинена інфраструктура, що може бути цікавим для любителів ресторанів, барів та вечірок. Навіть якщо ви не бажаєте пробувати себе в гірськолижному спорті, тут є чим зайнятися взимку – від споглядання мальовничої місцевої природи до екскурсій.',
        'Драгобрат': '<b>Драгобрат</b>\nЦей гірськолижний курорт є одним з найвідоміших в Україні. Особливістю гірськолижної бази є те, що вона знаходиться доволі далеко від місцевих населених пунктів. Тому відчути атмосферу місцевої мальовничої карпатської природи тут ви можете у відносному усамітненні. Гірськолижний комплекс знаходиться на висоті 1500 метрів над рівнем моря. Саме тому тут чи не найдовше є сніг – з листопада майже по травень.\n\nДістатися сюди дещо важче, аніж до Буковеля. Потрібно на позашляховику їхати з селища Ясеня (Івано-Франківська область). Драгобрат є найбільш високогірним курортом України, куди їдуть прихильники гірськолижного спорту. Понад 20 трас, які чекають на любителів лижного спорту, мають сумарну протяжність близько 10 кілометрів. Курорт відомий тим, що тут є фрістайл-траси світового значення. Деякі з них прокладені через ліс, тож любителям екстремального лижного спорту тут буде цікаво.',
        'Буковель': '<b>Буковель</b>\nСлавнозвісний Буковель знають навіть ті, хто ні разу в житті не приміряв лижі. Цей курорт асоціюється з мальовничою природою, численними розвагами та висококласним сервісом місцевих готелів. Окрім однойменної вершини, відомими горами також є Чорна Клева і Довга. Населений пункт знаходиться на висоті в 920 метрів над рівнем моря. Сумарна протяжність гірськолижних спусків Буковеля – 50 кілометрів. Усього тут обладнано 62 спуски різного рівня складності. Тому тут буде цікаво як професіоналам, так і початківцям лижного спорту. Траси позначені різними кольорами, аби туристи не сплутали їх між собою. Синя позначка свідчить про легкий рівень, червона – про середній, а чорна – про складний. У Буковелі функціонує 16 гірськолижних витягів. Лише один з них є бугельним, решта – крісельними.\n\nМінеральні джерела Буковеля роблять його не лише гірськолижним, а й бальнеологічним курортом. Попри те, що Буковель у багатьох людей асоціюється з дорогим сервісом, насправді тут можна знайти номери та варіанти харчування різного класу. Фешенебельні готелі чудово співіснують з невеликими котеджами та приватними базами відпочинку, а дорогі ресторани європейської кухні – з закладами більш бюджетного рівня, на зразок корчми. Дістатися до Буковеля можна дуже просто. Варто лише доїхати до Івано-Франківська чи міста Яремче. А далі – туди регулярно курсують маршрутні таксі, тож проблеми не виникне.',
        'Пилипець': '<b>Пилипець</b>\nЦей гірськолижний курорт користується великою популярністю в туристів одразу з кількох причин. Чарівна природа Міжгірського району Закарпатської області дивує тих, хто тут уперше. А тим, хто з року в рік вирушає на відпочинок до Пилипця, вона ніби вкотре нагадує, що в Карпатах є чудове місце, де можна відволіктися від звичної життєвої рутини та провести час цікаво і драйвово. Читаючи відгуки про Пилипець, часто можна зустріти порівняння, де його називають «бюджетною версією Драгобрату».\n\nКурорт має висоту в 700 метрів над рівнем моря. Протяжність місцевих гірськолижних трас сягає близько 20 кілометрів. Переважна більшість з них знаходиться на горі Гимба. На цьому курорті немає штучного засніження. А значить – відпочинок залежить від погодних умов, якщо ви розраховуєте значну частину своєї поїздки присвятити саме на катанню на лижах. Водночас і є гарна новина. У Пилипці функціонує чимало веб-камер, за допомогою яких є можливість відслідковувати стан трас. Це дає змогу переконатися в наявності снігу, перш ніж вирушати у мандрівку.\n\nНайкраще доїхати на курорт Пилипець можна, узявши квиток на потяг до станції Воловець. Далі ви можете скористатися послугами маршрутного таксі.',
        'Плай': '<b>Плай</b>\nКурорт Плай розташований у Львівській області. Це один з популярних гірськолижних курортів України. Він є новим та сучасним, адже про його появу дізналися лише у 2007 році. Курорт відзначається компактністю, він невеликий за площею. Дехто називає Плай «міні-версією Буковелю». Аби сюди доїхати, вам потрібно спочатку дістатися потягом до міста Сколе, а потім – пересісти на маршрутне таксі.\n\nНа курорті Плай функціонує 6 гірськолижних трас. З огляду на наявність якісного обладнання для штучного засніження, сюди можна вирушати, не боячись капризів погоди. Однак варто зважати на один важливий аспект, а саме – місцеві ціни. Курорт новий, в його розбудову вкладені великі кошти. Тому цінова політика на більшість послуг тут дещо відрізняється від середньої по більшості інших українських курортів.',
        'Яблуниця': '<b>Яблуниця</b>\nГірськолижний курорт Яблуниця розташований у затишному однойменному селищі в Івано-Франківській області. Лижники полюбляють Яблуницький перевал, розташований на висоті в 931 метр над рівнем моря. Тут знаходиться багато трас різного рівня складності, котрі приваблюють не лише українських, а й закордонних туристів. Є 10 гірськолижних витягів – 8 у самому селищі, а також 2 – на перевалі.\n\nЯблуницю люблять не лише за красу місцевої природи та можливість зайнятися тут гірськолижним спортом. Цей курорт відзначається дуже лояльними цінами та широкою пропозицією житла для туристів. Можна зняти номер в одному з місцевих готелів, або ж – кімнату в приватному секторі. Відносно недалеко від Яблуниці розташовані Буковель і Драгобрат. Тож якщо ви ретельно сплануєте маршрут своєї поїздки, то зможете за одну подорож завітати одразу на 3 курорти.',
        'Красія': '<b>Красія</b>\nКурорт Красія розташований у Закарпатській області, а саме – в селі Вишка. Навіть у розпал сезону тут немає великих натовпів туристів, оскільки це місце не так розрекламоване, як багато інших осередків гірськолижного спорту. Тут на вас чекає приємна й спокійна атмосфера. Споглядання закарпатської природи налаштує на релакс. А лижний спорт додасть потрібної динаміки.\n\nЯкщо ви тільки вчитеся кататися на лижах, на курорті Красія вам буде дуже комфортно. Є траси як для професіоналів (можна скористатися послугами інструктора у місцевій лижній школі), так і для початківців.\n\nДовжина трас є різною, а одна з прикметних особливостей Красії полягає в тому, що саме тут знаходиться найдовша лижна траса в Україні. Її протяжність сягає 3 з половиною кілометри. Щодо інфраструктури, то важливими її елементами є 2 крісельні витяги.',
        'Мигове': '<b>Мигове</b>\nЯкщо під час відпочинку в Карпатах вас передусім цікавить знайомство з регіоном, який вражає своїм автентичним колоритом, то завітайте до Чернівецької області. Тим більш – саме тут розташований відомий гірськолижний курорт Мигово. Якщо ви вже відпочивали на Закарпатті, Івано-Франківщині чи Львівщині, Буковина відкриє перед вами зовсім інші культурні особливості. Кожна з цих областей цікава та унікальна. Тому, аби говорити, що ви познайомилися з традиціями Карпат в усьому розмаїтті, варто побувати у згаданих областях, не оминаючи жодну з них.\n\nТак ось, вертаючись до Мигово: курорт є відносно молодим. Тут ви побачите 4 гірськолижні траси. Вагомою особливістю є те, що одна з них оснащена спеціально для сноубордистів. Загальна довжина трас – приблизно 3,5 кілометри. Вони дивують більш не протяжністю, а розмаїттям. Тут можна знайти навіть траси міжнародного значення та сертифіковані маршрути для міжнародних змагань.',
        'Яремче': '<b>Яремче</b>\nВідпочинок взимку в Яремче стане відмінним рішенням, якщо ви робите свої перші спроби в лижному спорті. Тут є усього лиш 2 траси, і обидві вони призначені саме для початківців. Є один бугельний витяг.\n\nЯремче – це чудовий варіант для спокійного сімейного відпочинку, якщо на тихий релакс ви налаштовані більше, аніж не екстрим. Цей населений пункт є привабливим для туристів одразу в кількох аспектах. Тут можна відпочити за доволі демократичними цінами. Це стосується як житла, так і харчування у місцевих ресторанах.\n\nСвоєрідними «родзинками» міста Яремче є стежка Довбуша та водоспад Пробій. Також тут знаходиться відомий сувенірний ринок. Одним словом, можливість зайнятися гірськолижним спортом – не єдина з доступних розваг. А ще неподалік від цього міста знаходиться Буковель, куди ви можете дістатися маршрутним таксі.',
    },
    # resorts coordinates for weather
    'resorts_weather': {
        "Славське": [48.8473, 23.4459],
        "Драгобрат": [48.2496, 24.2496],
        "Буковель": [48.3653, 24.4004],
        "Пилипець": [48.6677, 23.3519],
        "Плай": [48.9033, 23.2928],
        "Яблуниця": [48.3054, 24.4703],
        "Красія": [48.9379, 22.7074],
        "Мигове": [48.1575, 25.379],
        "Яремче": [48.4583, 24.5519],
    },
    # how to get to resorts
    'how_to_get_info': {
        "Славське": '<b>Як доїхати до Славського:</b>\nПотяги в сторону Ужгорода, зупинка ст. Славсько. Автобусом Львів - Славське, Стрий-Славське. Власним транспортом по трасі Київ — Чоп до повороту в м. Сколе на Славське. Славське знаходиться за 135 км від Львова та за 25 км від Сколе,680 км від Київа.',
        "Драгобрат": '<b>Як доїхати до Драгобрату:</b>\nДорога на Драгобрат починається в Ясіні. До села можна добратися автобусами з Івано-Франківська, Яремчі, Рахова, Ужгорода або поїздом Київ-Рахів, Одеса- Рахів, Харків-Рахів, Львів-Рахів. Як варіант - поїздами до Яремчі, Ворохти або до Івано-Франківська. Далі автобусом до Ясіні, або зомовити трансфер до Ясиня.\nЗ смт. Ясіня до курорту Драгобрат можна дібратися тільки на повнопривідному транспорті, який потрібно замовити наперед у місцевих жителів. Їх стоянка знаходиться біля АЗС Sun Oil (вул. Миру 148). На автостоянці поруч можна залишити свої власні авто за помірну ціну, де їх охоронятимуть. Тут ведеться відеоспостереження. Звідси можна піднятися до полонини Драгобрат (12 км) до готелів курорту та гірсько-лижних підйомників. Так само прохідні таксі доставляють туристів у зворотному до Ясіня напрямку.',
        "Буковель": '<b>Як доїхати до Буковелю:</b>\n',
        "Пилипець": '<b>Як доїхати до Пилипцю:</b>\n',
        "Плай": '<b>Як доїхати до Плай:</b>\n',
        "Яблуниця": '<b>Як доїхати до Яблуниці:</b>\n',
        "Красія": '<b>Як доїхати до Красії:</b>\n',
        "Мигове": '<b>Як доїхати до Мигове:</b>\n',
        "Яремче": '<b>Як доїхати до Яремче:</b>\n'
    },
    # trains information
    'trains_messages': {
        "Славське": 'Тобі пощастило, поїзд зупиняється прямо на станції <b>Славсько</b>, знайти підходящий потяг можеш за посилання нижче',
        "Драгобрат": 'Отакої, до Драгобрату потягом не доїхати, але найближча залізнична станція це <b>Ясіня</b>, подивитися розклад руху поїздів можна за посиланням нижче',
        "Буковель": 'Отакої, до Буковелю потягом не доїхати, але найближча залізнична станція це <b>Татарів-Буковель</b>, подивитися розклад руху поїздів можна за посиланням нижче',
        "Пилипець": 'Отакої, до Пилипцю потягом не доїхати, але найближча залізнична станція це <b>Воловець</b>, подивитися розклад руху поїздів можна за посиланням нижче',
        "Плай": 'Отакої, до Плаю потягом не доїхати, але найближча залізнична станція це <b>Сколе</b>, подивитися розклад руху поїздів можна за посиланням нижче',
        "Яблуниця": 'Отакої, до Яблуниці потягом не доїхати, але оптимально доїхати до <b>Ворохти</b>, подивитися розклад руху поїздів можна за посиланням нижче',
        "Красія": 'Отакої, до Красії потягом не доїхати, але оптимально доїхати до <b>Ужгорода</b>, подивитися розклад руху поїздів можна за посиланням нижче',
        "Мигове": 'Отакої, в Мигове потягом не доїхати, але оптимально доїхати до <b>Чернівців</b>, подивитися розклад руху поїздів можна за посиланням нижче',
        "Яремче": 'Тобі пощастило, поїзд зупиняється прямо на станції <b>Славсько</b>, знайти підходящий потяг можеш за посилання нижче',
    },
    # traffic by station
    'trains_urls': {
        "Славське": "https://uz.gov.ua/passengers/timetable/?station=23091&by_station=%D0%9F%D0%BE%D1%88%D1%83%D0%BA",
        "Драгобрат": "https://uz.gov.ua/passengers/timetable/?station=23213&by_station=%D0%9F%D0%BE%D1%88%D1%83%D0%BA",
        "Буковель": 'https://uz.gov.ua/passengers/timetable/?station=23218&by_station=%D0%9F%D0%BE%D1%88%D1%83%D0%BA',
        "Пилипець": 'https://uz.gov.ua/passengers/timetable/?station=23145&by_station=%D0%9F%D0%BE%D1%88%D1%83%D0%BA',
        "Плай": 'https://uz.gov.ua/passengers/timetable/?station=23088&by_station=%D0%9F%D0%BE%D1%88%D1%83%D0%BA',
        "Яблуниця": 'https://uz.gov.ua/passengers/timetable/?station=23217&by_station=%D0%9F%D0%BE%D1%88%D1%83%D0%BA',
        "Красія": 'https://uz.gov.ua/passengers/timetable/?station=20095&by_station=%D0%9F%D0%BE%D1%88%D1%83%D0%BA',
        "Мигове": 'https://uz.gov.ua/passengers/timetable/?station=23500&by_station=%D0%9F%D0%BE%D1%88%D1%83%D0%BA',
        "Яремче": 'https://uz.gov.ua/passengers/timetable/?station=23255&by_station=%D0%9F%D0%BE%D1%88%D1%83%D0%BA',
    },
}
