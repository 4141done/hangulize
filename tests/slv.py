# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.slv import Slovene


class SloveneTestCase(HangulizeTestCase):

    lang = Slovene()

    def test_people(self):
        self.assert_examples({
            u'Milenko Ačimovič': u'밀렌코 아치모비치',
            u'Anton Aškerc': u'안톤 아슈케르츠',
            u'Armin Bačinovič': u'아르민 바치노비치',
            u'Janez Bleiweis': u'야네스 블레이베이스',
            u'Jože Brumen': u'요제 브루멘',
            u'Ivan Cankar': u'이반 찬카르',
            u'Sebastjan Cimirotič': u'세바스티안 치미로티치',
            u'Zlatko Dedič': u'즐라트코 데디치',
            u'Janez Drnovšek': u'야네스 드르노우셰크',
            u'Gregor Fučka': u'그레고르 푸치카',
            u'Jakob Petelin Gallus': u'야코프 페텔린 갈루스',
            u'Samir Handanovič': u'사미르 한다노비치',
            u'Matevž Irt': u'마테우시 이르트',
            u'Željko Ivanek': u'젤코 이바네크',
            u'Rihard Jakopič': u'리하르트 야코피치',
            u'Janez Janša': u'야네스 얀샤',
            u'Bojan Jokić': u'보얀 요키치',
            u'Srečko Katanec': u'스레치코 카타네츠',
            u'Matjaž Kek': u'마티아시 케크',
            u'Ivana Kobilca': u'이바나 코빌차',
            u'Oskar Kogoj': u'오스카르 코고이',
            u'Anže Kopitar': u'안제 코피타르',
            u'Robert Koren': u'로베르트 코렌',
            u'Milan Kučan': u'밀란 쿠찬',
            u'Fran Levstik': u'프란 레우스티크',
            u'Rudolf Maister': u'루돌프 마이스테르',
            u'Željko Milinovič': u'젤코 밀리노비치',
            u'Radoslav Nesterovič': u'라도슬라우 네스테로비치',
            u'Milivoje Novakovič': u'밀리보예 노바코비치',
            u'Borut Pahor': u'보루트 파호르',
            u'Lojze Peterle': u'로이제 페테를레',
            u'Jože Plečnik': u'요제 플레치니크',
            u'Bojan Prašnikar': u'보얀 프라슈니카르',
            u'Friderik Pregl': u'프리데리크 프레글',
            u'France Prešeren': u'프란체 프레셰렌',
            u'Uroš Slokar': u'우로시 슬로카르',
            u'Anton Martin Slomšek': u'안톤 마르틴 슬롬셰크',
            u'Katarina Srebotnik': u'카타리나 스레보트니크',
            u'Leon Štukelj': u'레온 슈투켈',
            u'Dubravka Tomšič': u'두브라우카 톰시치',
            u'Primož Trubar': u'프리모시 트루바르',
            u'Danilo Türk': u'다닐로 튀르크',
            u'Sašo Udovič': u'사쇼 우도비치',
            u'Beno Udrih': u'베노 우드리흐',
            u'Janez Vajkard Valvasor': u'야네스 바이카르트 발바소르',
            u'Jurij Vega': u'유리 베가',
            u'Zdenko Verdenik': u'즈덴코 베르데니크',
            u'Saša Vujačič': u'사샤 부야치치',
            u'Zlatko Zahovič': u'즐라트코 자호비치',
            u'Slavoj Žižek': u'슬라보이 지제크',
        })

    def test_places(self):
        self.assert_examples({
            u'Bled': u'블레트',
            u'Bohinj': u'보힌',
            u'Celje': u'첼리에',
            u'Domžale': u'돔잘레',
            u'Izola': u'이졸라',
            u'Jesenice': u'예세니체',
            u'Kamnik': u'캄니크',
            u'Koper': u'코페르',
            u'Kranj': u'크란',
            u'Kras': u'크라스',
            u'Ljubljana': u'류블랴나',
            u'Maribor': u'마리보르',
            u'Murska Sobota': u'무르스카 소보타',
            u'Nova Gorica': u'노바 고리차',
            u'Novo mesto': u'노보 메스토',
            u'Piran': u'피란',
            u'Pivka': u'피우카',
            u'Ptuj': u'프투이',
            u'Slovenija': u'슬로베니야',
            u'Škofja Loka': u'슈코피아 로카',
            u'Trbovlje': u'트르보울리에',
            u'Triglav': u'트리글라우',
            u'Velenje': u'벨레니에',
        })