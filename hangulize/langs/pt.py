# -*- coding: utf-8 -*-
from hangulize import *


class Portuguese(Language):
    """For transcribing Portuguese."""

    vowels = u'aAeEiIoOuUQ'
    cs = u'bcCdfghjklmnpqrRsStvwxz'
    son = u'lmnr' # sonorant
    vl = u'cCfkpqRsSt' # voiceless
    notation = Notation([
        (u'ã', 'A~'),
        (u'á', 'A'),
        (u'â', 'A'),
        (u'sç', 'S'),
        (u'ç', 'S'),
        (u'é', 'E'),
        (u'ê', 'E'),
        (u'õ', 'O~'),
        (u'ó', 'O'),
        (u'ô', 'O'),
        ('dumont$', 'dumon'),
        ('^eduar', 'Eduar'),
        ('^eldorado', 'Eldorado'),
        ('^joA~', 'juA~'),
        ('^mirra$', 'mira'),
        ('bb', 'b'),
        ('cc', 'c'),
        ('dd', 'd'),
        ('ff', 'f'),
        ('gg', 'g'),
        ('hh', 'h'),
        ('jj', 'j'),
        ('kk', 'k'),
        ('ll', 'l'),
        ('mm', 'm'),
        ('nn', 'n'),
        ('pp', 'p'),
        ('qq', 'q'),
        ('tt', 't'),
        ('vv', 'v'),
        ('ww', 'w'),
        ('xx', 'x'),
        ('zz', 'z'),
        ('ch', 'C'),
        ('lh', 'L'),
        ('nh', 'N'),
        ('^ex{@}', 'ez'),
        ('^hex{@}', 'ez'),
        ('~e', '~i'),
        ('A~o', 'A~'),
        ('c{k|q}', None),
        ('sc{e|i}', 'S'),
        ('ssc{e|i}', 'S'),
        ('xc{e|i}', 'S'),
        ('xs', 'S'),
        ('xss', 'S'),
        ('ss', 'S'),
        ('c{e|i}', 'S'),
        ('c', 'k'),
        ('x{@}', 'C'),
        ('x', 'S'),
        ('g{e|i}', 'j'),
        ('{g|q}u{e|i}', None),
        ('^e{a|(<cs>)a|(<cs>)(<cs>)a}$', 'E'),
        ('^e{(<cs>)(<cs>)(<cs>)a}$', 'E'),
        ('^e{am|(<cs>)am|(<cs>)(<cs>)am}$', 'E'),
        ('^e{(<cs>)(<cs>)(<cs>)am}$', 'E'),
        ('^e{ans|(<cs>)ans|(<cs>)(<cs>)ans}$', 'E'),
        ('^e{(<cs>)(<cs>)(<cs>)ans}$', 'E'),
        ('^e{as|(<cs>)as|(<cs>)(<cs>)as}$', 'E'),
        ('^e{(<cs>)(<cs>)(<cs>)as}$', 'E'),
        ('^e{o|(<cs>)o|(<cs>)(<cs>)o}$', 'E'),
        ('^e{(<cs>)(<cs>)(<cs>)o}$', 'E'),
        ('^e{om|(<cs>)om|(<cs>)(<cs>)om}$', 'E'),
        ('^e{(<cs>)(<cs>)(<cs>)om}$', 'E'),
        ('^e{ons|(<cs>)ons|(<cs>)(<cs>)ons}$', 'E'),
        ('^e{(<cs>)(<cs>)(<cs>)ons}$', 'E'),
        ('^e{os|(<cs>)os|(<cs>)(<cs>)os}$', 'E'),
        ('^e{(<cs>)(<cs>)(<cs>)os}$', 'E'),
        ('^e{e|(<cs>)e|(<cs>)(<cs>)e}$', 'E'),
        ('^e{(<cs>)(<cs>)(<cs>)e}$', 'E'),
        ('^e{em|(<cs>)em|(<cs>)(<cs>)em}$', 'E'),
        ('^e{(<cs>)(<cs>)(<cs>)em}$', 'E'),
        ('^e{ens|(<cs>)ens|(<cs>)(<cs>)ens}$', 'E'),
        ('^e{(<cs>)(<cs>)(<cs>)ens}$', 'E'),
        ('^e{es|(<cs>)es|(<cs>)(<cs>)es}$', 'E'),
        ('^e{(<cs>)(<cs>)(<cs>)es}$', 'E'),
        ('^e', 'i'),
        ('{C|L|N}e$', 'i'),
        ('e$', 'Q'),
        ('o$', 'u'),
        ('os$', 'us'),
        ('{p|b|m|f|v|g|q}es$', 'Es'),
        ('{C|L|N}es$', 'is'),
        ('es$', 'Qs'),
        ('q', 'k'),
        ('ou', 'o'),
        ('A', 'a'),
        ('E', 'e'),
        ('I', 'i'),
        ('O', 'o'),
        ('U', 'u'),
        ('aa', 'a'),
        ('ee', 'e'),
        ('oo', 'o'),
        ('uu', 'u'),
        ('yy', 'iy'),
        ('^y{@}', 'Y'),
        ('{@}y{@}', 'Y'),
        ('y', 'i'),
        ('ii', 'i'),
        ('m$', '~'),
        ('n$', '~'),
        ('ns$', '~s'),
        ('n{g|k}', '~'),
        ('^r', 'R'),
        ('{n|l|s}r', 'R'),
        ('rr', 'R'),
        ('^s', 'S'),
        ('{<vl>}s', 'S'),
        ('{@}s{@}', 'z'),
        ('s{@}', 'S'),
        ('s{<vl>}', 'S'),
        ('s$', 'S'),
        ('s', 'Z'),
        ('z{@}', 'Z'),
        ('z{<vl>}', 'S'),
        ('z$', 'S'),
        ('Z', 'z'),
        ('k{<son>}', 'F'),
        ('{@}k{<cs>}', 'k,'),
        ('F', 'k'),
        ('C{@}', 'SY'),
        ('C', 'Si'),
        ('N{@}', 'nY'),
        ('N', 'n'),
        ('L{@}', 'lY'),
        ('L', 'l'),
        ('^l', 'l;'),
        ('^m', 'm;'),
        ('^n', 'n;'),
        ('l$', 'l,'),
        ('m$', 'm,'),
        ('n$', 'n,'),
        ('l{@|Y|m,|n,}', 'l;'),
        ('{,}l', 'l;'),
        ('m{@}', 'm;'),
        ('n{@|Y}', 'n;'),
        ('l', 'l,'),
        ('m', 'm,'),
        ('n', 'n,'),
        ('~', '~,'),
        (',,', ','),
        (',;', None),
        (',l,', 'l,'),
        (',m,', 'm,'),
        (',n,', 'n,'),
        ('l{m;|n;}', 'l,'),
        (';', None),
        ('^w', 'W'),
        ('{@|g|k}w', 'W'),
        ('w', 'QW'),
        ('b', Choseong(B)),
        ('d', Choseong(D)),
        ('f', Choseong(P)),
        ('g', Choseong(G)),
        ('j', Choseong(J)),
        ('j', None),
        ('k,', Jongseong(G)),
        ('k', Choseong(K)),
        ('^l', Choseong(L)),
        ('{,}l', Choseong(L)),
        ('l,', Jongseong(L)),
        ('l', Jongseong(L), Choseong(L)),
        ('m,', Jongseong(M)),
        ('m', Choseong(M)),
        ('n,', Jongseong(N)),
        ('n', Choseong(N)),
        ('~', Jongseong(NG)),
        ('p,', Jongseong(B)),
        ('p', Choseong(P)),
        ('r', Choseong(L)),
        ('R', Choseong(H)),
        ('S', Choseong(S)),
        ('t,', Jongseong(S)),
        ('t', Choseong(T)),
        ('v', Choseong(B)),
        ('z', Choseong(J)),
        ('Ya', Jungseong(YA)),
        ('Ye', Jungseong(YE)),
        ('Yi', Jungseong(I)),
        ('Yo', Jungseong(YO)),
        ('Yu', Jungseong(YU)),
        ('YQ', Jungseong(EU)),
        ('Wa', Jungseong(WA)),
        ('We', Jungseong(WE)),
        ('Wi', Jungseong(WI)),
        ('Wo', Jungseong(WEO)),
        ('Wu', Jungseong(U)),
        ('WQ', Jungseong(E)),
        ('a', Jungseong(A)),
        ('e', Jungseong(E)),
        ('i', Jungseong(I)),
        ('o', Jungseong(O)),
        ('u', Jungseong(U)),
        ('Q', Jungseong(EU)),
    ])

    def normalize(self, string):
        def normalize_only_unsafe(string):
            map = {u'Ã': u'ã',
                   u'Á': u'á',
                   u'Â': u'â',
                   u'Ç': u'ç',
                   u'É': u'é',
                   u'Ê': u'ê',
                   u'ê': u'é',
                   u'Õ': u'õ', 
                   u'Ó': u'ó',
                   u'Ô': u'ô'}
            safe = map.keys() + map.values()
            for c in string:
                if c not in safe:
                    yield normalize_roman(c)
                elif c in map:
                    yield map[c]
                else:
                    yield c
        return ''.join(normalize_only_unsafe(string))


pt = Portuguese