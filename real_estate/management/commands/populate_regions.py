from django.core.management.base import BaseCommand
from real_estate.models import Region, District

class Command(BaseCommand):
    help = 'Populate regions and districts with updated data structure'

    def handle(self, *args, **options):
        # Clear existing data
        District.objects.all().delete()
        Region.objects.all().delete()
        
        # Uzbekistan regions with keys
        regions_data = [
    {
        'key': 'tashkent_city',
        'name_uz': 'Toshkent shahri',
        'name_ru': 'Город Ташкент',
        'name_en': 'Tashkent City',
        'districts': [
            ('bektemir', 'Bektemir', 'Бектемир', 'Bektemir'),
            ('chilonzor', 'Chilonzor', 'Чиланзар', 'Chilanzar'),
            ('mirobod', 'Mirobod', 'Мирабад', 'Mirobod'),
            ('mirzo_ulugbek', 'Mirzo Ulug\'bek', 'Мирзо Улугбек', 'Mirzo Ulugbek'),
            ('olmazor', 'Olmazor', 'Алмазар', 'Olmazor'),
            ('sergeli', 'Sergeli', 'Сергели', 'Sergeli'),
            ('shayxontohur', 'Shayxontohur', 'Шайхантахур', 'Shaykhantakhur'),
            ('uchtepa', 'Uchtepa', 'Учтепа', 'Uchtepa'),
            ('yakkasaroy', 'Yakkasaroy', 'Яккасарай', 'Yakkasaray'),
            ('yunusobod', 'Yunusobod', 'Юнусабад', 'Yunusabad'),
            ('yashnobod', 'Yashnobod', 'Яшнабад', 'Yashnabad'),
        ]
    },
    {
        'key': 'tashkent_region',
        'name_uz': 'Toshkent viloyati',
        'name_ru': 'Ташкентская область',
        'name_en': 'Tashkent Region',
        'districts': [
            ('angren', 'Angren', 'Ангрен', 'Angren'),
            ('bekobod', 'Bekobod', 'Бекабад', 'Bekabad'),
            ('bostonliq', 'Bo\'stonliq', 'Бустанлык', 'Bostanlyk'),
            ('chinoz', 'Chinoz', 'Чиназ', 'Chinaz'),
            ('qibray', 'Qibray', 'Кибрай', 'Kibray'),
            ('oqqorgon', 'Oqqo\'rg\'on', 'Аккурган', 'Akkurgan'),
            ('olmaliq', 'Olmaliq', 'Алмалык', 'Almalyk'),
            ('ohangaron', 'Ohangaron', 'Ахангаран', 'Akhangaran'),
            ('parkent', 'Parkent', 'Паркент', 'Parkent'),
            ('piskent', 'Piskent', 'Пскент', 'Piskent'),
            ('yangiyol', 'Yangiyo\'l', 'Янгиюль', 'Yangiyul'),
            ('zangiota', 'Zangiota', 'Зангиота', 'Zangiata'),
        ]
    },
    {
        'key': 'andijan',
        'name_uz': 'Andijon viloyati',
        'name_ru': 'Андижанская область',
        'name_en': 'Andijan Region',
        'districts': [
            ('andijan', 'Andijon', 'Андижан', 'Andijan'),
            ('asaka', 'Asaka', 'Асака', 'Asaka'),
            ('baliqchi', 'Baliqchi', 'Балыкчи', 'Balikchi'),
            ('boz', 'Bo\'z', 'Боз', 'Boz'),
            ('bulakbashi', 'Buloqboshi', 'Булокбаши', 'Bulokbashi'),
            ('izboskan', 'Izboskan', 'Избаскан', 'Izboskan'),
            ('jalakuduk', 'Jalaquduq', 'Джалакудук', 'Jalakuduk'),
            ('khojaabad', 'Xo\'jaobod', 'Ходжаабад', 'Khojaabad'),
            ('kurgontepa', 'Qo\'rg\'ontepa', 'Кургантепа', 'Kurgontepa'),
            ('marhamat', 'Marhamat', 'Мархамат', 'Marhamat'),
            ('oltiariq', 'Oltinko\'l', 'Алтынкуль', 'Altynkul'),
            ('pakhtaabad', 'Paxtaobod', 'Пахтаабад', 'Pakhtaabad'),
            ('shahrixon', 'Shahrixon', 'Шахрихан', 'Shakhrikhan'),
        ]
    },
    {
        'key': 'bukhara',
        'name_uz': 'Buxoro viloyati',
        'name_ru': 'Бухарская область',
        'name_en': 'Bukhara Region',
        'districts': [
            ('bukhara', 'Buxoro', 'Бухара', 'Bukhara'),
            ('gijduvan', 'G\'ijduvon', 'Гиждуван', 'Gijduvan'),
            ('jondor', 'Jondor', 'Жондор', 'Jondor'),
            ('kagan', 'Kogon', 'Каган', 'Kagan'),
            ('karakul', 'Qorako\'l', 'Каракуль', 'Karakul'),
            ('karoulbazar', 'Qorovulbozor', 'Караулбазар', 'Karoulbazar'),
            ('olot', 'Olot', 'Алат', 'Alat'),
            ('peshku', 'Peshku', 'Пешку', 'Peshku'),
            ('romitan', 'Romitan', 'Ромитан', 'Romitan'),
            ('shofirkon', 'Shofirkon', 'Шафиркан', 'Shafirkon'),
            ('vobkent', 'Vobkent', 'Вабкент', 'Vabkent'),
        ]
    },
    {
        'key': 'fergana',
        'name_uz': 'Farg\'ona viloyati',
        'name_ru': 'Ферганская область',
        'name_en': 'Fergana Region',
        'districts': [
            ('fergana', 'Farg\'ona', 'Фергана', 'Fergana'),
            ('altiariq', 'Oltiariq', 'Алтыарык', 'Altyaryk'),
            ('bagdad', 'Bag\'dod', 'Багдат', 'Bagdat'),
            ('beshariq', 'Beshariq', 'Бешарык', 'Besharyk'),
            ('buvayda', 'Buvayda', 'Бувайда', 'Buvayda'),
            ('dangara', 'Dang\'ara', 'Дангара', 'Dangara'),
            ('furqat', 'Furqat', 'Фуркат', 'Furkat'),
            ('qoshtepa', 'Qo\'shtepa', 'Куштепа', 'Kushtepa'),
            ('quva', 'Quva', 'Кува', 'Kuva'),
            ('rishton', 'Rishton', 'Риштан', 'Rishtan'),
            ('sox', 'So\'x', 'Сох', 'Sokh'),
            ('toshloq', 'Toshloq', 'Ташлак', 'Tashlak'),
            ('uzbekistan', 'Uzbekiston', 'Узбекистан', 'Uzbekistan'),
            ('yazyavan', 'Yozyovon', 'Язъяван', 'Yazyavan'),
        ]
    },
    {
        'key': 'jizzakh',
        'name_uz': 'Jizzax viloyati',
        'name_ru': 'Джизакская область',
        'name_en': 'Jizzakh Region',
        'districts': [
            ('jizzakh', 'Jizzax', 'Джизак', 'Jizzakh'),
            ('aral', 'Aral', 'Арал', 'Aral'),
            ('bakhmal', 'Baxmal', 'Бахмал', 'Bakhmal'),
            ('dustlik', 'Do\'stlik', 'Дустлик', 'Dustlik'),
            ('forish', 'Forish', 'Фариш', 'Forish'),
            ('gagarin', 'Gagarin', 'Гагарин', 'Gagarin'),
            ('mirzachul', 'Mirzacho\'l', 'Мирзачуль', 'Mirzachul'),
            ('pakhtakor', 'Paxtakor', 'Пахтакор', 'Pakhtakor'),
            ('yangiabad', 'Yangiobod', 'Янгиабад', 'Yangiabad'),
            ('zaamin', 'Zomin', 'Заамин', 'Zaamin'),
            ('zarbdar', 'Zarbdor', 'Зарбдар', 'Zarbdar'),
        ]
    },
    {
        'key': 'namangan',
        'name_uz': 'Namangan viloyati',
        'name_ru': 'Наманганская область',
        'name_en': 'Namangan Region',
        'districts': [
            ('namangan', 'Namangan', 'Наманган', 'Namangan'),
            ('chortoq', 'Chortoq', 'Чартак', 'Chartak'),
            ('chust', 'Chust', 'Чуст', 'Chust'),
            ('kosonsoy', 'Kosonsoy', 'Касансай', 'Kasansay'),
            ('mingbuloq', 'Mingbuloq', 'Мингбулак', 'Mingbulak'),
            ('norin', 'Norin', 'Нарын', 'Naryn'),
            ('pop', 'Pop', 'Пап', 'Pap'),
            ('toiraqurgon', 'To\'raqo\'rg\'on', 'Туракурган', 'Turakurgan'),
            ('uchqorgon', 'Uchqo\'rg\'on', 'Учкурган', 'Uchkurgan'),
            ('uychi', 'Uychi', 'Уйчи', 'Uychi'),
            ('yangiqorgon', 'Yangiqo\'rg\'on', 'Янгикурган', 'Yangikurgan'),
        ]
    },
    {
        'key': 'navoiy',
        'name_uz': 'Navoiy viloyati',
        'name_ru': 'Навоийская область',
        'name_en': 'Navoiy Region',
        'districts': [
            ('navoiy', 'Navoiy', 'Навои', 'Navoiy'),
            ('karmana', 'Karmana', 'Кармана', 'Karmana'),
            ('konimex', 'Konimex', 'Канимех', 'Kanimekh'),
            ('nurota', 'Nurota', 'Нурата', 'Nurata'),
            ('qiziltepa', 'Qiziltepa', 'Кызылтепа', 'Kyzyltepa'),
            ('tomdi', 'Tomdi', 'Тамды', 'Tamdy'),
            ('uchquduq', 'Uchquduq', 'Учкудук', 'Uchkuduk'),
            ('xatirchi', 'Xatirchi', 'Хатирчи', 'Khatyrchi'),
            ('zafarobod', 'Zafarobod', 'Зафарабад', 'Zafarabad'),
        ]
    },
    {
        'key': 'kashkadarya',
        'name_uz': 'Qashqadaryo viloyati',
        'name_ru': 'Кашкадарьинская область',
        'name_en': 'Kashkadarya Region',
        'districts': [
            ('qarshi', 'Qarshi', 'Карши', 'Karshi'),
            ('chiroqchi', 'Chiroqchi', 'Чиракчи', 'Chirakchi'),
            ('dehqonobod', 'Dehqonobod', 'Дехканабад', 'Dehkanabad'),
            ('guzor', 'G\'uzor', 'Гузар', 'Guzar'),
            ('kamashi', 'Qamashi', 'Камаши', 'Kamashi'),
            ('karshi', 'Karshi', 'Карши', 'Karshi'),
            ('kasbi', 'Kasbi', 'Касби', 'Kasbi'),
            ('kitob', 'Kitob', 'Китаб', 'Kitab'),
            ('koson', 'Koson', 'Касан', 'Kasan'),
            ('mirishkor', 'Mirishkor', 'Миришкор', 'Mirishkor'),
            ('muborak', 'Muborak', 'Мубарек', 'Mubarek'),
            ('nishon', 'Nishon', 'Нишан', 'Nishan'),
            ('shahrisabz', 'Shahrisabz', 'Шахрисабз', 'Shahrisabz'),
            ('yakkabog', 'Yakkabog\'', 'Яккабаг', 'Yakkabag'),
        ]
    },
    {
        'key': 'samarkand',
        'name_uz': 'Samarqand viloyati',
        'name_ru': 'Самаркандская область',
        'name_en': 'Samarkand Region',
        'districts': [
            ('samarkand', 'Samarqand', 'Самарканд', 'Samarkand'),
            ('bulungur', 'Bulung\'ur', 'Булунгур', 'Bulungur'),
            ('ishtixon', 'Ishtixon', 'Иштыхан', 'Ishtykhan'),
            ('jomboy', 'Jomboy', 'Джамбай', 'Jambay'),
            ('kattaqorgon', 'Kattaqo\'rg\'on', 'Каттакурган', 'Kattakurgan'),
            ('narpay', 'Narpay', 'Нарпай', 'Narpay'),
            ('nurobod', 'Nurobod', 'Нурабад', 'Nurabad'),
            ('oqdaryo', 'Oqdaryo', 'Акдарья', 'Akdarya'),
            ('urgut', 'Urgut', 'Ургут', 'Urgut'),
        ]
    },
    {
        'key': 'sirdarya',
        'name_uz': 'Sirdaryo viloyati',
        'name_ru': 'Сырдарьинская область',
        'name_en': 'Sirdarya Region',
        'districts': [
            ('guliston', 'Guliston', 'Гулистан', 'Gulistan'),
            ('akhangaran', 'Ohangaron', 'Ахангаран', 'Akhangaran'),
            ('boyovut', 'Boyovut', 'Баяут', 'Bayaut'),
            ('mirzaobod', 'Mirzaobod', 'Мирзаабад', 'Mirzaabad'),
            ('oyqorgon', 'Oqqo\'rg\'on', 'Аккурган', 'Akkurgan'),
            ('sardoba', 'Sardoba', 'Сардоба', 'Sardoba'),
            ('saykhunobod', 'Sayxunobod', 'Сайхунабад', 'Saykhunabad'),
            ('sirdaryo', 'Sirdaryo', 'Сырдарья', 'Sirdarya'),
            ('xovos', 'Xovos', 'Хавас', 'Khavas'),
        ]
    },
    {
        'key': 'surkhandarya',
        'name_uz': 'Surxondaryo viloyati',
        'name_ru': 'Сурхандарьинская область',
        'name_en': 'Surkhandarya Region',
        'districts': [
            ('termiz', 'Termiz', 'Термез', 'Termez'),
            ('angor', 'Angor', 'Ангор', 'Angor'),
            ('bandixon', 'Bandixon', 'Бандихон', 'Bandikhan'),
            ('boysun', 'Boysun', 'Байсун', 'Baysun'),
            ('denov', 'Denov', 'Денау', 'Denau'),
            ('jarkorgon', 'Jarqo\'rg\'on', 'Джаркурган', 'Jarkurgan'),
            ('muzrabot', 'Muzrabot', 'Музрабад', 'Muzrabad'),
            ('olotin', 'Olotin', 'Алтынсай', 'Altynsay'),
            ('qiziriq', 'Qiziriq', 'Кизирик', 'Kizirik'),
            ('qumqorgon', 'Qumqo\'rg\'on', 'Кумкурган', 'Kumkurgan'),
            ('sariosiyo', 'Sariosiyo', 'Сариасия', 'Sariasiya'),
            ('sherobod', 'Sherobod', 'Шерабад', 'Sherabad'),
            ('shorchi', 'Sho\'rchi', 'Шурчи', 'Shurchi'),
            ('uzun', 'Uzun', 'Узун', 'Uzun'),
        ]
    },
    {
        'key': 'khorezm',
        'name_uz': 'Xorazm viloyati',
        'name_ru': 'Хорезмская область',
        'name_en': 'Khorezm Region',
        'districts': [
            ('urgench', 'Urganch', 'Ургенч', 'Urgench'),
            ('bogot', 'Bog\'ot', 'Багат', 'Bagat'),
            ('gurlan', 'Gurlan', 'Гурлен', 'Gurlen'),
            ('hazorasp', 'Xazorasp', 'Хазарасп', 'Khozarasp'),
            ('hiva', 'Xiva', 'Хива', 'Khiva'),
            ('qoshkopir', 'Qo\'shko\'pir', 'Кошкупыр', 'Koshkupir'),
            ('shovot', 'Shovot', 'Шават', 'Shavat'),
            ('yangiarik', 'Yangiariq', 'Янгиарык', 'Yangiaryk'),
            ('yangibozor', 'Yangibozor', 'Янгибазар', 'Yangibazar'),
        ]
    },
    {
        'key': 'karakalpakstan',
        'name_uz': 'Qoraqalpog\'iston Respublikasi',
        'name_ru': 'Республика Каракалпакстан',
        'name_en': 'Republic of Karakalpakstan',
        'districts': [
            ('nukus', 'Nukus', 'Нукус', 'Nukus'),
            ('amudarya', 'Amudaryo', 'Амударья', 'Amudarya'),
            ('beruniy', 'Beruniy', 'Беруни', 'Beruni'),
            ('chimboy', 'Chimboy', 'Чимбай', 'Chimbay'),
            ('ellikqala', 'Ellikqala', 'Элликкала', 'Ellikkala'),
            ('kegeyli', 'Kegeyli', 'Кегейли', 'Kegeyli'),
            ('moinak', 'Mo\'ynoq', 'Муйнак', 'Muinak'),
            ('qonlikol', 'Qo\'ng\'irot', 'Кунград', 'Kungrad'),
            ('qoraozek', 'Qorao\'zak', 'Караузяк', 'Karaozyak'),
            ('shumanay', 'Shumanay', 'Шуманай', 'Shumanay'),
            ('taxtakupir', 'Taxtako\'pir', 'Тахтакупыр', 'Takhtakupyr'),
            ('turtkul', 'To\'rtko\'l', 'Турткуль', 'Turtkul'),
            ('xojeli', 'Xo\'jayli', 'Ходжейли', 'Khojeyli'),
        ]
    }
]
        
        for region_data in regions_data:
            region = Region.objects.create(
                key=region_data['key'],
                name_uz=region_data['name_uz'],
                name_ru=region_data['name_ru'],
                name_en=region_data['name_en'],
            )
            
            self.stdout.write(f"Created region: {region.name_uz}")
            
            # Create districts
            for district_data in region_data['districts']:
                district = District.objects.create(
                    region=region,
                    key=district_data[0],
                    name_uz=district_data[1],
                    name_ru=district_data[2],
                    name_en=district_data[3],
                )
                
                self.stdout.write(f"  Created district: {district.name_uz}")
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated regions and districts')
        )