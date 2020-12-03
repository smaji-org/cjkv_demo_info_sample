#!/usr/bin/env python2
# -*- coding:utf-8 -*-

info= {
    "China": {
        "G0": "GB 2312-80",
        "G1": "GB 12345-90",
        "G3": "GB 7589-87 traditional form",
        "G5": "GB 7590-87 traditional form",
        "G7": "Modern Chinese general character chart (Simplified Chinese: 现代汉语通用字表)",
        "G8": "GB8565-88",
        "GCE": "National Academy for Educational Research",
        "GE": "GB16500-95",
        "GFC": "Modern Chinese Standard Dictionary (现代汉语规范词典)",
        "GGFZ": "General Chinese Standard Dictionary (通用规范汉字字典)",
        "GH": "GB/T 15564-1995",
        "GHZ": "Hanyu Da Zidian",
        "GHZR": "Hanyu Da Zidian(second edition) (汉语大字典（第二版）)",
        "GK": "GB 12052-89",
        "GKJ": "Terms in Sciences and Technologies (科技用字) approved by the China National Committee for Terms in Sciences and Technologies (CNCTST)",
        "GKX": "Kangxi Dictionary",
        "GLK": "龍龕手鑑",
        "GT": "Standard Telegraph Codebook (revised), 1983",
        "GZFY": "Dictionary of Chinese Dialects (汉语方言大辞典)",
        "GS": "Singapore Chinese characters",
        "G4K": "Siku Quanshu",
        "GBK": "Encyclopedia of China",
        "GCH": "Cihai",
        "GCY": "Ciyuan",
        "GFZ": "Founder Press System",
        "GHC": "Hanyu Da Cidian",
        "GHF": "漢文佛典疑難俗字彙釋與研究",
        "GCYY": "Chinese Academy of Surveying and Mapping ideographs",
        "GGH": "Old Chinese Dictionary (古代汉语词典)",
        "GJZ": "Commercial Press ideographs",
        "GXC": "Xiandai Hanyu Cidian",
        "GZJW": "Collections of Bronze Inscriptions from Yin and Zhou Dynasties (殷周金文集成引得)",
        "GIDC": "ID System of the Ministry of Public Security of China",
        "GZH": "Zhonghua Zihai",
        "GDZ": "Geology Press ideographs",
        "GRM": "People's Daily ideographs",
        "GWZ": "Hanyu Da Cidian Press ideographs",
        "GXH": "Xinhua Zidian",
        "GLGYJ": "Zhuang Liao Songs Research (壮族嘹歌研究)",
        "GOCD": "Oxford English-Chinese Chinese-English Dictionary (牛津英汉汉英词典)",
        "GPGLG": "Zhuang Folk Song Culture Series - Pingguo County Liao Songs (壮族民歌文化丛书・平果嘹歌)",
        "GXHZ": "Xinhua Big Dictionary (新华大字典)",
        "GZ": "Ancient Zhuang Character Dictionary (古壮字字典)",
        "GZYS": "Chinese Ancient Ethnic Characters Research (中国民族古文字研究)"
    },
    "Hong Kong": {
        "H": "Hong Kong Supplementary Character Set, 2008",
        "HB0": "Computer Chinese Glyph and Character Code Mapping Table, Technical Report C-26 (電腦用中文字型與字碼對照表, 技術通報C-26)",
        "HB1": "Big-5, Level 1",
        "HB2": "Big-5, Level 2",
        "HD": "Hong Kong Supplementary Character Set, 2016"
    },
    "Japan": {
        "J0": "JIS X 0208-1990",
        "J1": "JIS X 0212-1990",
        "J13": "JIS X 0213:2004 level-3 characters replacing J1 characters",
        "J13A": "JIS X 0213:2004 level-3 character addendum from JIS X 0213:2000 level-3 replacing J1 character",
        "J14": "JIS X 0213:2004 level-4 characters replacing J1 characters",
        "J3": "JIS X 0213:2004 Level 3",
        "J3A": "JIS X 0213:2004 Level 3 addendum",
        "J4": "JIS X 0213:2004 Level 4",
        "JARIB": "ARIB STD-B24",
        "JMJ": "Character Information Development and Maintenance Project for e-Government \"MojiJoho-Kiban Project\" (文字情報基盤整備事業)",
        "JH": "Hanyo-Denshi Program (汎用電子情報交換環境整備プログラム)",
        "JA": "Japanese IT Vendors Contemporary Ideographs, 1993",
        "JA3": "JIS X 0213:2004 level-3 characters replacing JA characters",
        "JA4": "JIS X 0213:2004 level-4 characters replacing JA characters",
        "JK": "Japanese Kokuji Collection"
    },
    "Macau": {
        "MAC": "Macao Information System Character Set (澳門資訊系統字集)"
    },
    "North Korea": {
        "KP0": "KPS 9566-97",
        "KP1": "KPS 10721-2000"
    },
    "South Korea": {
        "K0": "KS C 5601-87 (now KS X 1001:2004)",
        "K1": "KS C 5657-91 (now KS X 1002:2004)",
        "K2": "PKS C 5700-1:1994",
        "K3": "PKS C 5700-2:1994",
        "K4": "PKS 5700-3:1998",
        "K6": "KS X 1027-5:2014",
        "K5": "Korean IRG Hanja Character Set",
        "KC": "Korean History On-Line (한국 역사 정보 통합 시스템)"
    },
    "Taiwan": {
        "T1": "CNS 11643-1992 plane 1",
        "T2": "CNS 11643-1992 plane 2",
        "T3": "CNS 11643-1992 plane 3",
        "T4": "CNS 11643-1992 plane 4",
        "T5": "CNS 11643-1992 plane 5",
        "T6": "CNS 11643-1992 plane 6",
        "T7": "CNS 11643-1992 plane 7",
        "TB": "CNS 11643-1992 plane 11",
        "TC": "CNS 11643-1992 plane 12",
        "TD": "CNS 11643-1992 plane 13",
        "TE": "CNS 11643-1992 plane 14",
        "TF": "CNS 11643-1992 plane 15",
        "TA": "Chemical Nomenclature: 4th Edition (化學命名原則(第四版))",
        "T13": "TCA-CNS 11643 19th plane (pending new version)"
    },
    "Vietnam": {
        "V0": "TCVN 5773-1993",
        "V1": "TCVN 6056:1995",
        "V2": "VHN 01-1998",
        "V3": "VHN 02-1998",
        "V4": "Dictionary on Nom (Từ điển chữ Nôm)\nDictionary on Nom of Tay ethnic (Từ điển chữ Nôm Tày)\nLookup Table for Nom in the South (Bảng tra chữ Nôm miền Nam)",
        "VU": "Vietnamese horizontal extensions"
    },
    "United Kingdom": {
        "UK": "IRG N2107R2"
    },
    "N/A": {
        "UTC": "UTC sources",
        "UCI": "UTC sources",
        "SAT": "SAT Daizōkyō Text Database"
    }
}

rev= {}

for region in info:
    for sub in info[region]:
        rev[sub]= region

