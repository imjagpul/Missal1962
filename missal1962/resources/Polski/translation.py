from missal1962 import constants
from ..Latin.translation import titles, paternoster, transformations

titles[constants.SANCTI_03_15PL] = 'Św. Klemensa Marii Dworzaka (Hofbauera)'
titles[constants.SANCTI_04_23PL] = 'Św. Wojciecha, Biskupa i Męczennika'
titles[constants.SANCTI_05_03PL] = 'N. M. P., Królowej Polski, Głównej Patronki Polski'
titles[constants.SANCTI_05_08PL] = 'Św. Stanisława, Biskupa i Męczennika'
titles[constants.SANCTI_05_16PL] = 'Św. Andrzeja Boboli, Męczennika'
titles[constants.SANCTI_05_24PL] = 'N. M. P. Wspomożycielki Wiernych'
titles[constants.SANCTI_06_01PL] = 'Bł. Jakuba Strzemię, Biskupa i Wyznawcy'
titles[constants.SANCTI_06_10PL] = 'Bł. Bogumiła, Biskupa i Wyznawcy'
titles[constants.SANCTI_07_18PL] = 'Bł. Szymona z Lipnicy, Wyznawcy'
titles[constants.SANCTI_07_20PL] = 'Bł. Czesława, Wyznawcy'
titles[constants.SANCTI_07_24PL] = 'Bł. Kingi, Dziewicy'
titles[constants.SANCTI_08_26PL] = 'N. M. P. Jasnogórskiej czyli Częstochowskiej'
titles[constants.SANCTI_09_01PL] = 'Bł. Bronisławy, Dziewicy'
titles[constants.SANCTI_09_07PL] = 'Bł. Melchiora Grodzieckiego, Męczennika'
titles[constants.SANCTI_09_25PL] = 'Bł. Władysława z Gielniowa, Wyznawcy'
titles[constants.SANCTI_10_01PL] = 'Bł. Jana z Dukli'
titles[constants.SANCTI_11_13PL] = 'Św. Stanisława Kostki, Wyznawcy'

section_labels = {
    'Communicantes': 'Communicantes',
    'CommunioP': 'Antyfona na Komunię (Okres Wielkanocny)',
    'Communio': 'Antyfona na Komunię',
    'Evangelium': 'Ewangelia',
    'GradualeP': 'Alleluja Wielkanocne',
    'Graduale': 'Graduał',
    'Introitus': 'Introit',
    'Lectio': 'Lekcja',
    'OffertoriumP': 'Antyfona na Ofiarowanie (Okres Wielkanocny)',
    'Offertorium': 'Antyfona na Ofiarowanie',
    'Oratio': 'Kolekta',
    'Postcommunio': 'Pokomunia',
    'Secreta': 'Sekreta',
    'Sequentia': 'Sekwencja',
    'Super populum': 'Modlitwa nad ludem',
    'Prefatio': 'Prefacja',
    'Tractus': 'Traktus',
    # 02-02, feast of the Purification of the B.V.M.
    'De Benedictione Candelarum': 'Poświęcenie Świec',
    'De Distributione Candelarum': 'Rozdawanie Świec',
    'De Processione': 'Procesja',
    # Quad6-0r, Dominica II Passionis seu in Palmis
    'Benedictio Palmorum': 'Poświęcenie Palm',
    'De distributione ramorum': 'Rozdawanie Gałązek',
    'De lectione Evangelica': 'Czytanie Ewangelii',
    'De processione cum ramis benedictis': 'Procesja z Poświęconymi Palmami',
    'Hymnus ad Christum Regem': 'Hymn ku Czci Chrystusa Króla',
    # Quad6-4r, Feria Quinta in Coena Domini
    'Maundi': 'Mandatum, czyli Umywanie Nóg',
    'Post Missam': 'Uroczyste Przeniesienie i Złożenie Najświętszego Sakramentu',
    'Denudatione altaris': 'Obnażenie Ołtarzy',
    # Quad6-5r, Feria Sexta in Parasceve
    'Lectiones': 'Część Pierwsza: Czytania',
    'Passio': 'Pasja',
    'Oratio Fidelium': 'Część Druga: Uroczyste Modły zwane «Modlitwą Wiernych»',
    'Crucis Adoratione': 'Część Trzecia: Uroczysta Adoracja Krzyża',
    'CommunioQ': 'Część Czwarta: Komunia Święta',
    # Quad6-5r, Sabbato Sancto
    'Benedictio ignis': 'Poświęcenie nowego ognia',
    'De benedictione cerei Paschalis': 'Poświęcenie Paschału',
    'De solemni processione': 'Uroczysta Procesja',
    'De praeconio paschali': 'Orędzie Wielkanocne',
    'De lectionibus': 'Czytania',
    'De prima parte Litaniarum': 'Pierwsza Część Litanii',
    'De benedictione aquae baptismalis': 'Poświęcenie Wody Chrzcielnej',
    'De renovatione promissionum baptismatis': 'Odnowienie Przyrzeczeń Chrztu Świętego',
    'De altera parte Litaniarum': 'Druga Część Litanii',
    'De Missa solemni Vigiliae paschalis': 'Uroczysta Msza Rezurekcyjna',
    'Pro Laudibus': 'Laudes',
    'Conclusio': 'Zakończenie'

}

section_labels_multi = {
    'GradualeL1': '1 Graduał',
    'GradualeL2': '2 Graduał',
    'GradualeL3': '3 Graduał',
    'GradualeL4': '4 Graduał',
    'GradualeL5': '5 Graduał',
    'Graduale': '6 Graduał',
    'LectioL1': '1 Lekcja',
    'LectioL2': '2 Lekcja',
    'LectioL3': '3 Lekcja',
    'LectioL4': '4 Lekcja',
    'LectioL5': '5 Lekcja',
    'Lectio': '6 Lekcja',
    'OratioL1': '2 Kolekta',
    'OratioL2': '3 Kolekta',
    'OratioL3': '4 Kolekta',
    'OratioL4': '5 Kolekta',
    'OratioL5': '6 Kolekta',
    'Oratio': '1 Kolekta'
}