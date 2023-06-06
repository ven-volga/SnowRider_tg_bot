from pymongo import MongoClient
from datetime import datetime

client_db = MongoClient('mongodb://localhost:27017/')
db = client_db.ski_assistant_tg
data = db.resorts_content
log = db.client_requests


def insert_data_to_db():
    data.insert_one({
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
        "resorts_info": {
            'Славське': '<b>Славське</b>\n<i>(укр. Славське, місцеві жителі називають Славсько)</i> — гірськолижний курорт України у Львівській області. Зручно діставатися. Готелі, котеджі, приватний сектор у смт. Славське розкинуте по всьому селищу. Найбільш популярні готелі та приватні садиби біля витягів на Тростян та Високий Верх. Зняти житло у Славському біля витягу взимку буває проблематично.\n\n<b>Гірськолижний відпочинок</b>\nСлавське – популярний лижний курорт у Карпатах. На вихідні багатолюдно, кататися на лижах у Славське приїжджають мешканці Львова та навколишніх курортів Трускавець, Моршин, Східниця. Траси у Славському облаштовані на кількох гірках. На горі Тростян прокладено траси різного рівня складності, зокрема. сертифіковані. На горі Політех смт. Славське є дитячий витяг. Канатна дорога у Славському веде на гору Тростян, у сусідній Волосянці – на гору Високий Верх. На лижному курорті Славське крісельний витяг одномісний, у Волосянці (Славське) - двомісний. Ціни на відпочинок взимку у Славському трохи вищі, ніж улітку. На Новий рік та Різдво у готелях та приватному секторі Славського може бути проблематично зняти житло, ціни у Славському на Новорічні свята найвищі.\n\n<b>Чому обирають Славське</b>\n- Наявність крісельного витягу на Тростян та Високий Верх\n- Гарні краєвиди на Славське з гори Тростян\n- Траси різного рівня, кілька гір для катання\n- Приватний сектор Славське добре розвинений, можна зняти недороге житло\n- Зручно добиратися поїздом та машиною',
            'Драгобрат': '<b>Драгобрат</b>\nВисокогірний гірськолижний курорт України. Готелі Драгобрату знаходяться на полонині біля підніжжя гір Стог та Близниця за 7 км від селища Ясіня. З висоти приблизно 1500 метрів від місця, де розкинувся лижний курорт Драгобрат, добре видно найвищі гірські масиви Карпат Чорнагора, Горгани, гори Говерла, Петрос, Синяк.\n\n<b>Гірськолижний відпочинок</b>\nДрагобрат є популярним серед любителів зимового відпочинку в Карпатах. Найкращий час для гірськолижного відпочинку на Драгобраті — зима. Період із грудня до березня. Сніг на Драгобраті лежить до травня, а готелі знижують ціни на житло, зазвичай, вже після новорічних свят.\nВідпочинок на Драгобраті взимку є унікальним. Гірськолижний курорт - один із найкрасивіших на Закарпатті. У Драгобраті завжди є свої шанувальники зимового відпочинку в Карпатах.\n\n<b>Чому обирають Драгобрат </b>\n- Гірськолижний курорт у Карпатах, помірні ціни на підйомники та житло\n- Зима на Драгобраті довга, сніг лежить з листопада до травня\n- Наявність бугельних та крісельних витягів\n- Літній та зимовий відпочинок на Драгобраті, гарні краєвиди на гори\n- Екстремальний підйом на Драгобрат – сюди складно доїхати самостійно',
            'Буковель': '<b>Буковель</b>\nСучасний гірськолижний курорт України. Ціни 2023 року на житло в Буковелі та відпочинок високі, відповідають рівню сервісу. Буковель (траси та готелі) знаходиться біля села Поляниця Івано-Франківської області на висоті понад 900 метрів над рівнем моря. Курорт оточений високими горами. Унікальне розташування та наявність снігових гармат забезпечують стабільний сніговий покрив з листопада по квітень місяць.\n\n<b>Гірськолижний відпочинок</b>\nБуковель взимку – це відпочинок в Карпатах на популярному лижному курорті України. Розвинена інфраструктура курорту в Карпатах, якісний рівень послуг, можливість поєднати зимовий відпочинок у Буковелі 2023, лікувальні та СПА процедури щороку залучають на курорт сотні тисяч туристів. До послуг гостей курорту Буковель: 62 траси завдовжки від 300 до 2350 м, 15 крісельних та 1 бугельний витяг, спортивні траси, траси для новачків та дітей. Всі траси у Буковелі обладнані сніговими гарматами, деякі освітлені. Приїжджайте на зимовий відпочинок у Карпати — Буковель для цього найкраще місце. Окрім лиж та сноубодів, взимку на Буковелі можна покататися на снігоходах, санях з їздовими собаками, сноубайках, ковзанах, спробувати свої сили у зорбінгу.\n\n<b>Чому обирають Буковель </b>\n- Розвинена інфраструктура: 62 траси, 15 крісельних та 1 бугельний витяг\n- Зимовий сезон на Буковелі триває з листопада до квітня\n- Найбільше штучне озеро в Україні є озеро з підігрівом\n- Лікувальні, бальнеологічні, СПА центри, дитячий табір "Артек-Буковель"\n- 4-, 5-зіркові котеджі та вілли, комфортні номери у готельних комплексах',
            'Пилипець': '<b>Пилипець</b>\nМальовничий гірськолижний курорт України, підйомники та траси в Пилипці відомі багатьом туристам. Село у Закарпатській області розташоване у Міжгірському районі. Пилипець – відомий гірськолижний курорт України. Завдяки наявності лижних трас, готелів біля крісельного витягу та однієї з найкрасивіших візитівок Карпат – водоспаду Шипота до Пилипеця на відпочинок приїжджають цілий рік.\n\n<b>Гірськолижний відпочинок</b>\nПилипець популярний серед гірськолижників, сноубордистів, любителів лиж, санок, глінтвейну, селфі та просто всіх, кому подобається казкова зимова природа Карпат. Тут можна зробити чудові фото під назвою «Я в Карпатах зі снарягою» :)\nНаявність стабільного зимового покриву, гірськолижних спусків різного рівня, крісельних та бугельних витягів у поєднанні з помірними цінами на житло у Пилипці дозволяє недорого відпочити у Карпатах узимку. На гірськолижному курорті Пилипець ціни на підйомники 2023 доступні: ціни на підйомник крісла починаються від 70 грн в обидва боки, ціни на підйомник бугеля починаються від 25 грн за підйом. У Пилипці надаються всі послуги гірськолижних курортів: прокат спорядження, ремонт лиж і сноубордів, лижна школа. Можна скористатися послугами професійного інструктора з катання на гірських лижах та сноуборді.\n\n<b>Чому обирають Пилипець </b>\n- Відповідає всім вимогам гірськолижного курорту\n- Наявність підйомника крісла\n- Можливість цілорічного відпочинку\n- Відвідати водоспад Шипіт, піднятися на Боржавський хребет\n- Великий вибір житла у Пилипці: приватний сектор, готелі, садиби',
            'Плай': '<b>Плай</b>\nГірськолижний курорт України у Львівській області. Розташований лижний курорт Плай у Карпатах с. Плав`я на висоті 600 м над рівнем моря. Готелі та підйомники курорту Плай знаходяться поряд із трасою Київ-Чоп. До комплексу веде зручний під`їзд.\n\n<b>Гірськолижний відпочинок</b>\nПлай популярний серед гірськолижників та сноубордистів. Завдяки вдалому місцерозташуванню та наявності снігових гармат на курорті Плай сніг тримається довше, ніж на сусідніх лижних курортах Славське, Пилипець, Подобовець, Звенів. Покататися на лижах на Плай зручно приїжджати мешканцям Львова та відпочиваючим бальнеологічних курортів Східниця, Трускавець, Моршин. На курорті Плай працює лижна школа, прокат спорядження, медпункт, ресторани, СПА-центр.<b>Чому обирають Плай </b>\n- Найсучасніший гірськолижний курорт у Львівській області\n- На курорті Плай: траси різного рівня, снігові гармати, ратраки\n- Наявність підйомників крісел, мультиліфта, бебі-ліфта\n- СПА-центр, спортивні майданчики, басейни, ресторани, конференц-зали\n- Зручний транспортний під`їзд',
            'Яблуниця': '<b>Яблуниця</b>\nBисокогірний лижний курорт України в Івано-Франківській області. До будівництва комплексу Буковель Яблуниця була найпопулярнішим центром гірськолижного спорту. Однією стороною межує з Яблуницьким перевалом, що відокремлює Закарпаття та Прикарпаття.\n\n<b>Гірськолижний відпочинок</b>\nПісля відкриття лижного курорту Буковель Яблуниця втратила минулу славу гірськолижного курорту. Але, дешеве житло в Яблуниці, смішні ціни на витяги та прокат спорядження приваблюють на відпочинок туристів. Спокійна обстановка, небагатолюдні траси, демократичні ціни на витяги приваблюють туристів. А зручне місце розташування (Яблуниця Буковель відстань становить 12-13 км) дозволяє щодня кататися на схилах сучасного гірськолижного курорту європейського рівня.\n\n<b>Чому обирають Яблуниця</b>\n- Гарні види та гори Говерлу, Петрос, Свидовецький масив\n- Спокійно, небагатолюдно на трасах, помірні ціни на підйомники\n- Можна зняти недорого житло в Яблуниці, а кататися в Буковелі\n- Літній відпочинок: походи в гори, екскурсії, СПА-центри та озера Буковеля\n- Можливий трансфер на гірськолижний курорт Драгобрат',
            'Красія': '<b>Красія</b>\nКурорт Красія розташований у Закарпатській області, а саме – в селі Вишка. Навіть у розпал сезону тут немає великих натовпів туристів, оскільки це місце не так розрекламоване, як багато інших осередків гірськолижного спорту. Тут на вас чекає приємна й спокійна атмосфера. Споглядання закарпатської природи налаштує на релакс. А лижний спорт додасть потрібної динаміки.\n\nЯкщо ви тільки вчитеся кататися на лижах, на курорті Красія вам буде дуже комфортно. Є траси як для професіоналів (можна скористатися послугами інструктора у місцевій лижній школі), так і для початківців.\n\nДовжина трас є різною, а одна з прикметних особливостей Красії полягає в тому, що саме тут знаходиться найдовша лижна траса в Україні. Її протяжність сягає 3 з половиною кілометри. Щодо інфраструктури, то важливими її елементами є 2 крісельні витяги.',
            'Мигове': '<b>Мигове</b>\nГірськолижний курорт Чернівецької області. Снігові вершини, морозне повітря, гарна місцевість, хвойні ліси Карпат. Це – Мигове. Готелі, приватний сектор, котеджі та бази відпочинку розташовані на висоті понад 700 метрів над рівнем моря. Курорт відомий мінеральними джерелами, гірськолижними трасами, гарними краєвидами. Поруч знаходяться лижні курорти Карпат: Лопушна (23 км), Тюдов (34,2 км), Косів (44,9 км).\n\n<b>Гірськолижний відпочинок</b>\nМигове має усі атрибути гірськолижного курорту. Готелі розташовані поруч із підйомниками, траси котуються ратраками, працюють прокати спорядження, кафе, медпункт. Траси обладнані бугельними витягами, на схилах встановлені снігові гармати. Початківцям свої послуги пропонують професійні інструктори. Мигове — один з гірськолижних курортів України, де можна кататися ввечері завдяки нічному освітленню. Інфраструктура є зручною для туристів. У Мигові все поряд. Готелі, витяги, ресторани, приватні котеджі. Відвідувачам пропонується традиційний набір послуг: сауна, прогулянки на конях, сноутюбінг. Додатково: скеледром, тир, стрільба з цибулі, льодова ковзанка. А який же Відпочинок в Україні без смачної карпатської кухні: ресторан, кафе швидкого харчування «Швидко», піцерія не дадуть померти з голоду.\n<b>Чому обирають Мигове </b>\nОсобливості лижного курорту Мігово Чернівецької області: комплекс "Мигове" обладнаний сніговими гарматами, довго тримається сніг, прокладено траси різного рівня складності, поряд є джерело мінеральної води\nВзимку – стати на лижі, підкорити гірські схили.Влітку - викупатися в річці та зловити на вудку форель.\nТут є сноутюбінг, льодова ковзанка та прогулянки на санях.\nЗалишити галасливі Чернівці та відпочити на вихідні.\nВипробувати силу місцевої лікувальної води.\n',
            'Яремче': '<b>Яремче</b>\n<i>(стара назва - Яремча)</i> — гірськолижний та кліматичний курорт України в Івано-Франківській області. Центр туристичного життя Прикарпаття. Розташований у мальовничій долині на березі річки Прут. Через Яремчу проходить основний туристичний маршрут на Говерлу та дорога на популярний лижний курорт Буковель.\n\n<b>Гірськолижний відпочинок</b>\nВ Яремче відпочинок в Карпатах є цікавим та пізнавальним. Унікальні природні умови та місцевий колорит ваблять туристів з різних країн. Зручне розташування, клімат та пам`ятки приваблюють туристів у будь-яку пору року. Розвинений зелений туризм та рафтинг. Взимку у Яремчі популярний відпочинок на гірськолижних курортах. Житло в Яремчі різноманітне за рівнем сервісу та цінами. Його багато: бази відпочинку в Яремчі, готелі, туристичні бази, санаторії, мотелі, табори відпочинку для дітей, котеджі, міні-готелі та приватні пансіонати. Яремче (стара назва Яремча) є одним з найбільш відвідуваних туристичних місць у Карпатах.\n\n<b>Чому обирають Яремче </b>\n- Багато туристичних об`єктів та екскурсійних маршрутів\n- Готелі надають трансфер на Буковель, але є і свої лижні траси\n- Великий вибір житла, готелів, кафе, колиб, ресторанів\n- Унікальний клімат - в Яремчі комфортно будь-якої пори року\n- Відвідати сувенірний ринок, водоспад Пробій, скелі Довбуша',
        },
        # resorts coordinates for weather
        'resorts_weather': {
            'Славське': [48.8473, 23.4459],
            'Драгобрат': [48.2496, 24.2496],
            'Буковель': [48.3653, 24.4004],
            'Пилипець': [48.6677, 23.3519],
            'Плай': [48.9033, 23.2928],
            'Яблуниця': [48.3054, 24.4703],
            'Красія': [48.9379, 22.7074],
            'Мигове': [48.1575, 25.379],
            'Яремче': [48.4583, 24.5519],
        },
        # how to get to resorts
        'how_to_get_info': {
            "Славське": '<b>Славське: як дістатися</b>\nПотяги в сторону Ужгорода, зупинка ст. Славсько. Автобусом Львів - Славське, Стрий-Славське. Власним транспортом по трасі Київ — Чоп до повороту в м. Сколе на Славське. Славське знаходиться за 135 км від Львова та за 25 км від Сколе,680 км від Київа.',
            "Драгобрат": '<b>Драгобрат: як дістатися</b>\nДорога на Драгобрат починається в Ясіні. До села можна добратися автобусами з Івано-Франківська, Яремчі, Рахова, Ужгорода або поїздом Київ-Рахів, Одеса- Рахів, Харків-Рахів, Львів-Рахів. Як варіант - поїздами до Яремчі, Ворохти або до Івано-Франківська. Далі автобусом до Ясіні, або зомовити трансфер до Ясиня.\nЗ смт. Ясіня до курорту Драгобрат можна дібратися тільки на повнопривідному транспорті, який потрібно замовити наперед у місцевих жителів. Їх стоянка знаходиться біля АЗС Sun Oil (вул. Миру 148). На автостоянці поруч можна залишити свої власні авто за помірну ціну, де їх охоронятимуть. Тут ведеться відеоспостереження. Звідси можна піднятися до полонини Драгобрат (12 км) до готелів курорту та гірсько-лижних підйомників. Так само прохідні таксі доставляють туристів у зворотному до Ясіня напрямку.',
            "Буковель": '<b>Буковель: як дістатися</b>\n<b>Поїздом</b>\nЗалізничні вокзали великих міст, що знаходяться недалеко від Буковеля: Івано-Франківськ (110 км) та Львів (245 км). З Києва регулярно ходять поїзди до цих населених пунктів.\nТакож до курорту можна доїхати з Ворохти (21 км) та Яремче (40 км).\n\n<b>Автобусом</b>\nЗ усіх прилеглих міст до Буковеля організовуються трансфери до курорту та ходять регулярні автобуси.На автобусну станцію Поляниця, що є найближчою до Буковеля, регулярно курсують автобуси з Івано-Франківська (до 12 разів на день).\nТакож є рейси зі Львова, Луцька, Кутова та Збаражу.',
            "Пилипець": '<b>Пилипець: як дістатися</b>\n<b>Залізничний транспорт:</b>\nдоїзд до станції Воловець, що знаходиться на лінії Київ-Чоп (Львів-Мукачево). З Воловця в напрямку с. Пилипець (15 км.) курсують маршрутні таксі та рейсові автобуси Воловець-Міжгір’я.\n\n<b>Автомобільний транспорт:</b>\nдоїзд по трасі Київ-Ужгород до с. Нижні Ворота (до КПП ДАІ), де необхідно здійснити поворот на дорогу Нижні Ворота – Воловець – Міжгір’я.',
            "Плай": '<b>Плай: як дістатися</b>\nНа особистому транспорті потрібно виїхати на шосе Київ-Чоп і рухатись у напрямку до Стрия. Потім слід обминути Сколе та Оряву, звідки вже рукою подати до гірськолижного курорту.\nЯкщо сідати на електричку зі Львова, потрібно також дістатися до Сколе. Звідси дуже легко дістатися місця.\nОптимальним варіантом є автобус. Від Львівського вокзалу до ГЛК вирушає будь-який маршрут, що проходить через Плав’є із зупинками до Стрия, Сколе та Оряви.\nТрансфер на таксі є досить дорогим способом поїздки, але за бажання та фінансової можливості користуватися ним дуже зручно.',
            "Яблуниця": '<b>Яблуниця: як дістатися</b>\nЗалізницею до Яблуниці можна доїхати з пересадкою у Ворохті, Лазещині чи Ясінях. Далі — маршруткою чи таксі. Відстань між залізничними станціями цих сіл до Яблуниці невелика: з Ворохти — 17 км, з Ясіні — 12 км, з Лазещини — 10 км.\nАвтобусом можна їхати з Івано-Франківська. Час у дорозі: трохи більше двох годин. Маршрутки у напрямку Яблуниці відправляються щогодини, інколи — навіть частіше.',
            "Красія": '<b>Красія: як дістатися</b>\nПотягом – до м. Ужгород, далі автобусом Ужгород – Красія або маршрутним автобусом Ужгород – Великий Березний, Ужгород – Люта до зупинки с. Вишка. Автомобілем – до Ужгорода по трасі Київ – Чоп, далі до с. Кострино і до с. Вишка.\nВідстані: Від Красії до Ужгороду – 69 км. До Львову – 196 км.',
            "Мигове": '<b>Мигове: як дістатися</b>\nМаршрутним транспортом від центрального автовокзалу №1 міста Чернівців. Або на власному авто.',
            "Яремче": '<b>Яремче: як дістатися</b>\nПрямим поїздом дістатися Яремче (якщо з вашого міста такий є);\nПриїхати до Івано-Франківська (59 км до Яремчі), Чернівців (125 км), Тернополя (188 км), або до Львова (204 км), а потім на маршрутному таксі прямо з залізничного вокзалу дістатися до Яремче;\nПрямим автобусом, що йде до Яремче;\nВласним автомобілем – дорога досить комфортна.\n\nТрансфер з Івано-Франківська та Львова до Яремче – звичайна справа. Як правило, достатньо вийти з поїзда, і вас вже зустрічатимуть водії із пропозицією скористатися їхніми послугами.'
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
        # resort tracks information
        'tracks_info': {
            "Славське": '<b>Славське: підйомники, траси</b>\nГора Тростян – 11 трас різного рівня, у т. ч. 6 спортивних, загальна протяжність 22 км. Підйомник крісла 2750 м, 7 бугельних\n\nГора Погар - 1 траса середнього рівня до 1460 м. Крісельний витяг, бугельний, мультиліфт. Передбачено роботу снігових гармат, ратраку, освітлення\n\nГора Менчіл (Варшава): траса до 2 км середнього рівня для любителів та професіоналів, 2 бугельні витяги\n\nГора Кремінь (Політех): 4 траси до 1 км для новачків та любителів, 2 бугельні витяги, 1 дитячий підйомник мультиліфт\n\nВисокий Верх (Захар Беркут): 9 трас різного рівня складності, крісельний витяг 2800 м, 3 бугельні',
            "Драгобрат": '<b>Драгобрат: підйомники, траси</b>\n20 трас, загальною довжиною понад 10 км, траса для фрірайду – 3 км.\n\nНайдовша траса на Драгобраті - 2 км, найкоротша - 300 м.\n\nКласифікація трас: легка, середня, складна.\n\nПідйомники на Драгобраті: 5 бугельних, 2 крісельні, 5 мультиліфтів.\n\nПідйом на ратраку - довжина траси збільшується до 3 км.',
            "Буковель": '<b>Буковель: підйомники, траси</b>\n62 траси загальною довжиною понад 50 км, сноупарк, сноут`юбінг.\n\nНайдовша траса на Буковелі - 2350 м, найкоротша - 300 м.\n\nКласифікація трас: легка, середня, складна.\n\nПідйомники у Буковелі: 1 бугельний, 15 крісельних, дитячі підйомники.\n\nЛижна школа для дорослих та дітей.',
            "Пилипець": '<b>Пилипець: підйомники, траси</b>\nЗагальна протяжність трас – понад 20 км.\n\nНайдовша траса на Гембі - 6 км, Найдовша на Магурі - 1,5 км.\n\nКласифікація трас: легка, середня, складна.\n\nПідйомники в Пилипці: - 6 бугельних, 1 крісельний.',
            "Плай": '<b>Плай: підйомники, траси</b>\nЗагальна довжина трас на Плаї до 1200 м, навчальна – 350 м, дитяча – 350 м.\n\nПерепад висот - 260 м.\n\nКласифікація трас: легка, середня, складна.\n\nПідйомники в Плав`ї: 2 4-крісельні - 1000 м, бугельний - 350 м, бебі-ліфт - 350 м.',
            "Яблуниця": '<b>Яблуниця: підйомники, траси</b>\nТраса "Корова" - 200-250 м, траса "Коза" - 650 м.\n\nКласифікація трас: легка, середня.\n\nПідйомники в Яблуниці: бугельні.\n\n',
            "Красія": '<b>Красія: підйомники, траси</b>\nМультиліфт (приватний) – 300 метрів. Він зручний для сімей з дітьми.\n\nБугельний підйомник туркомплексу «Новий сезон» – 650 метрів.\n\nБугельний підйомник гірськолижного курорту «Красія» – 470 метрів.\n\nКрісельний чотиримісний підйомник –  1800 метрів.\n\nДвомісний крісельний – 1200 метрів.\n\nОдномісний крісельний – 1980 метрів.',
            "Мигове": '<b>Мигове: підйомники, траси</b>\nЗагальна довжина трас на Мигові 3300 м.\n\nТраса для сноут`юбу - 250 м.\n\nКласифікація: легка 1100 м, середня 1240 м, навчальні - 600 та 200 м.\n\nПідйомники Мигове: бугельний 1100 м, бугельний 600 м, мультиліфт 150 м.',
            "Яремче": '<b>Яремче: підйомники, траси</b>\nДві траси, протяжністю 300 та 200 метрів.\n\nПерепад висот 70 та 30 метрів.\n\nКурорт обслуговує 1 бугельний під`йомник.\n\n',
        },
        # ski-pass information
        'skipass_info': {
            'Славське': '<b>Ціни на підйомники\n<i>(сезон 2022-2023)</i></b>\n\nПогар - 1 підйом (крісло) - 30 грн;\nПогар - денний абонемент (крісло) - 300 грн;\nПогар - абонемент (крісло) – 150 грн;\nПогар, Політех (бугель) - 12/15 грн;\n\nТростян, Динамо (крісло) – 70-75 грн;\nТростян, Динамо (бугель 4 підйоми) – 150 грн;\nТростян, Динамо (бугель абонемент на день) – 330 грн;\n\nЗахар Беркут (крісло) – 80/100 грн (вихідні дні);\nЗахар Беркут (бугель 3 години) – 250/300 грн (вихідні дні);\n\nЗахар Беркут (бугель день) – 350/400 грн (вихідні дні);\n<i>*на курорті Славське ціни на витяги 2023 вказані орієнтовні. Актуальні ціни на витяги можуть відрізнятися від вказаних.</i>',
            'Драгобрат': '<b>Ціни на підйомники\n<i>(сезон 2022-2023)</i></b>\n\n<b><i>Підйомники «Драгобрат» (бугельний):</i></b>\n1 підйом – 30 грн (дитячий – 15 грн);\n5 підйомів – 150 грн (дитячий – 40 грн);\n20 підйомів – 500 грн (дитячий – 150 грн);\n50 підйомів – 1200 грн (дитячий – 300 грн).\n\n<b><i>Підйомники «Карпатська Чайка»:</i></b>\n1 підйом крісельний – 100 грн;\n1 підйом бугельний – 30 грн;\n10 підйомів – 350 грн + 20 грн картка;\n50 підйомів - 1250 грн + 20 грн. картка.\nМультиліфт (200 м): 25 грн - 1 підйом; 70 грн - 6 підйомів.\n\n<b><i>Bитяги «Вершина Карпат»:</i></b>\nкрісельне - 100 грн.\nбугельний - 30 грн;\nбугельний на 1 день - 400 грн;\nмультиліфт-"тарілочка" - 25 грн;\n\n<b><i>Підйомники «Оаза»:</i></b>\n1 підйом – 30 грн.\n2 і більше – по 25 грн;\n\n<b><i>Прокат:</i></b>\n70-120 грн./день, дітям - 60 грн./день, для фрірайду - 300 грн./день.\n\n<i>*на курорті Драгобрат ціни на витяги 2023 вказані орієнтовні. Актуальні ціни на витяги можуть відрізнятися від вказаних.</i>',
            'Буковель': '<b>Буковель, ціни 2022-2023\n<i>(будні/святкові дні):</i></b>\n\n1 підйом – від 105/135 грн;\n3 години – 420/545 грн;\n1 день – 975/1270 грн.;\n5 днів – 3850/5010 грн.;\n10 днів – 6825/8875 грн;\n\n<b>Прокат</b>\n<i>(сноуборд/лижі)</i>\nвід 75-400 грн/120-220 грн за 1 день\n\n<i>*на курорті Буковель ціни на витяги 2023 вказані орієнтовні. Актуальні ціни на витяги можуть відрізнятися від вказаних.</i>',
            'Пилипець': '<b>Ціни на підйомники\n<i>(сезон 2022-2023)</i></b>\n\nPазовий крісельний підйомник (верх, низ) - від 100 грн\n1 підйом вверх - від 60 грн.\n\nОдноденний абонемент крісло від 500 грн., 3 години - від 250 грн.\n\nБугельні витяги - від 30 грн.\n\nПрокат лиж – від 100 грн.\n\n<i>*на курорті Пилипець ціни на витяги 2023 вказані орієнтовні. Актуальні ціни на витяги можуть відрізнятися від вказаних.</i>',
            'Плай': '<b>Ціни на підйомники\n<i>(сезон 2022-2023)</i></b>\n\n1 підйом (бугель) - 90/100 грн;\n1 підйом (крісельний) - 110/130 грн;\n\nАбонемент пів дня (09:00-13:00) – 480/550 грн;\nАбонемент пів дня (13:00-17:00) – 480/550 грн;\n\nАбонемент 1 день – 880/1000 грн;\nАбонемент 2 дні – 1500/1850 грн;\nАбонемент 3 дні – 2250/2800 грн;\nАбонемент 4 дні – 2700/3750 грн;\nАбонемент 5 днів – 3350/4600 грн;\n\n<i>*на курорті Плай ціни на витяги 2023 вказані орієнтовні. Актуальні ціни на витяги можуть відрізнятися від вказаних.</i>',
            'Яблуниця': '<b>Ціни на підйомники\n<i>(сезон 2022-2023)</i></b>\n\n1 підйом (бугель) - 20/30 грн (залежно від сезону);\n\nAбонемент 4 години – 200/300 грн (залежно від сезону);\n\nAбонемент 1 день – 350/450 грн (залежно від сезону).\n\n<i>*на курорті Яблуниця ціни на витяги 2023 вказані орієнтовні. Актуальні ціни на витяги можуть відрізнятися від вказаних.</i>',
            'Красія': '<b>Ціни на підйомники\n<i>(сезон 2022-2023)</i></b>\n\n<i>будні | вихідні </i>1 підйом 200 | 200 грн.\n2 години 450 | 450 грн.\nПоловина дня 600 | 650 грн.\n\n1 день 850 | 950 грн.\n2 дні 1530 | 1710 грн.\n3 дні	2295 | 2565 грн.\n4 дні	3060 | 3420 грн.\n5 днів 3825 | 4275 грн.\n\n<i>*на курорті Красія ціни на витяги 2023 вказані орієнтовні. Актуальні ціни на витяги можуть відрізнятися від вказаних.</i>',
            'Мигове': '<b>Ціни на підйомники\n<i>(сезон 2022-2023)</i></b>\n\n1 підйом - 30/40 грн;\nАбонемент денний (9:00-18:00) – 500/550 грн;\nТариф 3 години – 350/400 грн;\nНа 1 годину – 180/200 грн;\nВечірнє катання (18:00-21:00) – 200 грн;\n\n<i>*для мешканців комплексу передбачена знижка 20%. Актуальні ціни на витяги можуть відрізнятися від вказаних.</i>',
            'Яремче': '<b>Ціни на катання\n<i>(сезон 2022-2023)</i></b>\n\nВитяг (одноразово): 30-50 грн.\nДенний абонемент: від 500 грн.\nАренда гірськолижного спорядження: 200-250 грн.\nПрокат санчат: 100-150 грн.\n\n<i>*на курорті Яремче ціни на витяги 2023 вказані орієнтовні. Актуальні ціни на витяги можуть відрізнятися від вказаних.</i>',
        },
        # resorts cafe and restaurants
        'food_info': {
            'Славське': 'Some information',
            'Драгобрат': 'Some information',
            'Буковель': 'Some information',
            'Пилипець': 'Some information',
            'Плай': 'Some information',
            'Яблуниця': 'Some information',
            'Красія': 'Some information',
            'Мигове': 'Some information',
            'Яремче': 'Some information',
        },
        # resort attractions
        'attractions_info': {
            'Славське': '<b>Славське, що подивитися, розваги, екскурсії</b>\nЩо подивитися у Славську залежить від сезону. Відпочинок у Славському взимку – це традиційне катання на лижах та сноубордах, санчатах та снігоходах. Славське взимку - це екскурсії в Карпатах, сауна та чан на травах, чисте морозне повітря і зимові пейзажі, що зачаровують погляд. Приїжджайте на відпочинок у Славське влітку – у Карпатах завжди є на що подивитися. Екскурсії на Тустань та Кам`янку, на термальні джерела Закарпаття, походи в гори, крісельні витяги на вершини гори.',
            'Драгобрат': '<b>Драгобрат: розваги, екскурсії</b>\nВідпочинок у Драгобраті взимку – це традиційні види гірськолижного спорту, катання на санках, снігоходах, сауна, чан на свіжому зимовому повітрі тощо. Влітку відпочинок у Драгобраті неможливо уявити без піших походів на гірські вершини та хребти, у ліс за грибами, на озера та водоспади. У Драгобрат приїжджають подихати чистим повітрям, за спокоєм та тишею.',
            'Буковель': '<b>Буковель: розваги, екскурсії</b>\nВідпочинок у Буковелі взимку – це традиційні види гірськолижного спорту, катання на санках, снігоходах, сауна, ресторани та дискотеки, фестивалі та конкурси. Буковель влітку: піші походи до Карпат, у ліс за грибами, на гірські хребти, на озера та водоспади. Поніжитися на шезлонгах на березі озера, викупатися в басейні або озері з підігрівом, піднятися на підйомнику на вершини гір, милуючись краєвидами та дихаючи чистим хвойним повітрям – приїжджайте влітку до Буковеля, незабутні враження вам гарантовані. Також можна відвідати тамтешній контактний зоопарк "Гуцул-Ленд", якщо ви відпочиваєте з дітьмя, вони будуть в захваті!',
            'Пилипець': '<b>Пилипець: розваги, що подивитись</b>\nУ Пилипці є що подивитись і взимку, і влітку. Головна пам`ятка – водоспад Шипіт. На курорті Пилипець влітку туристам пропонується здійснити походи в гори, на Боржавські полонини, з`їздити на екскурсію на Синевир, оленячу ферму, у заповідник для ведмедів, відвідати Мукачеве, Ужгород, Хуст, Чинадієво. Користуються популярністю поїздки на термальні та мінеральні джерела. Взимку Пилипець неможливо уявити без гірських лиж, санок, сноубордів. Увечері — сауна, лазня та довгі обговорення "зльотів та падінь". Та й зовсім не обійтися без карпатського чану. Місцеві жителі з радістю зварять вас у чані з настойками з карпатських трав.',
            'Плай': '<b>Плай: розваги та екскурсії</b>\nВідпочинок на Плаї - це традиційне катання на лижах та сноубордах, санках та снігоходах. На комплексі Плай працюють 4 ресторани національної та європейської кухні, бістро, СПА центр, басейни, спортивні майданчики. Для проведення конференцій та семінарів передбачено обладнані конференц-зали.',
            'Яблуниця': '<b>Яблуниця: розваги та екскурсії</b>\nЗимовий відпочинок в Яблуниці — це традиційний відпочинок у Карпатах: катання на лижах, сноубордах та санках. З розваг: сауна, лазня, чан, колиби, екскурсії Карпатами. Влітку в Яблуниці можна піднятися на Чорногорський хребет, гори Синяк, Хом`як, cкупатися в озері на Буковелі, здійснити пішу екскурсію до водоспаду Гук, автомобільний тур Закарпаттям.',
            'Красія': '<b>Красія: розваги та екскурсії</b>\nПоїздки на гірськолижний курорт Красія дозволяє відпочиваючим побачити унікальні і популярні туристичні пам’ятки Закарпаття. Відпочиваючи на Красії, ви запросто зможете відвідати:\n– карстові печери в селі Княгиня і місце падіння найбільшого в Європі метеорита;\n– історичні атракції: Ужоцький перевал та оборонна Лінія Арпада;\n– прекрасна Ужанська долина та унікальні дерев`яні храми, побудовані без єдиного цвяха;\n– букові праліси Ужанського національного парку, що охороняються ЮНЕСКО;\n– старовинні тисячолітні міста Закарпаття: Ужгород, Берегово, Мукачево;\n– легендарні замки Закарпаття: мукачівський «Паланок», «Сент-Міклош», палац графа Шенборна;\n– термальні води Косино, Берегово;\n– високогірне село Лумшори, каскад водоспадів та карпатські джакузі – чани;\n– дегустаційні винні підвали .\n\nУ теплу пору року тут запропонують польоти на повітряних кулях та парапланах, збори ягід і грибів, походи в гори. У будь-який період можна покататися на конях-Гуцулик, квадроциклах, снігоходах, санках, сноутюбах. На території курорту є кафе, ресторани і колиби, де подають страви самобутньої закарпатської кухні.',
            'Мигове': '<b> Мигове: розваги та екскурсії</b>\nЕкскурсії до Чернівців, походи по околицях, тури Закарпаттям, поїздки до національного природного парку «Вижницький». На території парку височіють гори Виженка, Кругла та Кам`яна. Як і на кожному курорті, що поважає себе, тут є своя печера Довбуша. Для туристів цікаві пам`ятки природи: "Протягнуті камені", "Соколине Око", мальовничі водоспади "Гірський трон" і "Гук".',
            'Яремче': '<b>Яремче: розваги та екскурсії</b>\nОкрім традиційних літніх походів та екскурсій, зимового катання на лижах та сноубордах, у Яремчі пропонують піднятися на гірські вершини: Говерла, Петрос, Піп-Іван, здійснити тур на квадроциклах або сплав на річці, поїхати на автомобільну оглядову екскурсію Закарпаттям. Ресторани та кафе Яремче працюють цілий рік, готують страви національної та гуцульської кухні. Взимку, а особливо на Новий рік, у Яремчі користуються популярністю сауни та лазні. І найголовніше – відвідайте сувенірний ринок. Не повертайтесь із Яремчі без подарунків!',
        },
        # resort web-cams url
        'web-cams': {
            'Славське': ['https://snih.info/uk/trostian',
                         'https://snih.info/uk/zakhar-berkut',
                         'https://snih.info/uk/pohar',
                         'https://snih.info/uk/politekhnika'],
            'Драгобрат': 'https://snih.info/uk/drahobrat',
            'Буковель': 'https://snih.info/uk/bukovel',
            'Пилипець': 'https://snih.info/uk/pylypets',
            'Плай': 'https://snih.info/uk/plai',
            'Яблуниця': 'https://snih.info/uk',
            'Красія': 'https://snih.info/uk/krasiia',
            'Мигове': 'https://snih.info/uk/myhovo',
            'Яремче': 'https://snih.info/uk',
        },
    })
    print("Insert data into database successfully complete")


def insert_log_to_db():
    log.insert_one(
        {
            "_id": 1,
            "time_stamp": datetime.now(),
            "Славське": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
            "Драгобрат": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
            "Буковель": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
            "Пилипець": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
            "Плай": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
            "Яблуниця": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
            "Красія": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
            "Мигове": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
            "Яремче": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
        },

    )
    print("Insert log into database successfully complete")


if __name__ == '__main__':
    # insert_data_to_db()
    # insert_log_to_db()
    pass
