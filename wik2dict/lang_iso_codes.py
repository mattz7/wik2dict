# -*- coding: utf-8 -*-
"""
Copyright (c) 2004 Guaka

wik2dict is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
"""

# list from MediaWiki 1.2.6's languages/Language.php:
lang_iso_codes = {
	"aa" : "Afar",			# Afar
	"ab" : "Abkhazian",	# Abkhazian - FIXME
	"af" : "Afrikaans",	# Afrikaans
	"ak" : "Akana",		# Akan
	"als" : "Els&auml;ssisch",	# Alsatian
	"am" : "&#4768;&#4635;&#4653;&#4763;",	# Amharic
	"ar" : "&#1575;&#1604;&#1593;&#1585;&#1576;&#1610;&#1577;",	# Arabic
	"arc" : "&#1813;&#1829;&#1810;&#1834;&#1848;&#1821;&#1819;",	# Aramaic
	"as" : "&#2437;&#2488;&#2478;&#2496;&#2527;&#2494;",	# Assamese
	"av" : "&#1040;&#1074;&#1072;&#1088;",	# Avar
	"ay" : "Aymar",		# Aymara
	"az" : "Az&#601;rbaycan",	# Azerbaijani
	"ba" : "&#1041;&#1072;&#1096;&#1185;&#1086;&#1088;&#1090;",	# Bashkir
	"be" : "&#1041;&#1077;&#1083;&#1072;&#1088;&#1091;&#1089;&#1082;&#1072;&#1103;",	# Belarusian ''or'' Byelarussian
	"bg" : "&#1041;&#1098;&#1083;&#1075;&#1072;&#1088;&#1089;&#1082;&#1080;",	# Bulgarian
	"bh"	: "Bihara",
	"bi" : "Bislama",		# Bislama
	"bn" : "&#2476;&#2494;&#2434;&#2482;&#2494; - (Bangla)",	# Bengali
	"bo" : "Bod skad",		# Tibetan
	"br" : "Brezhoneg",	# Breton 
	"bs" : "Bosanski",		# Bosnian
	"ca" : "Catal&agrave;",	# Catalan
	"ce" : "&#1053;&#1086;&#1093;&#1095;&#1080;&#1081;&#1085;",	# Chechen
	"ch" : "Chamoru",		# Chamorro
	"chy" : "Tsets&ecirc;hest&acirc;hese",	# Cheyenne
	"co" : "Corsu",		# Corsican
	"cr" : "Nehiyaw",		# Cree
	"cs" : "&#268;esky",	# Czech
	"csb" : "Cassubian",	# Cassubian - FIXME
	"cv" : "&#1063;&#1233;&#1074;&#1072;&#1096; - (&#264;&#259;va&#349;)",	# Chuvash 
	"cy" : "Cymraeg",		# Welsh
	"da" : "Dansk",		# Danish
	"de" : "Deutsch",		# German
	"dk" : "Dansk", # 'da' is correct for the language.
	"dv" : "Dhivehi",		# Dhivehi
	"dz" : "(Dzongkha)",	# Bhutani
	"ee" : "Eve",			# Eve
	"el" : "&#917;&#955;&#955;&#951;&#957;&#953;&#954;&#940;",	# Greek
	"en" : "English",		# English
	"eo" : "Esperanto",	# Esperanto
	"es" : "Espa&ntilde;ol",	# Spanish
	"et" : "Eesti",		# Estonian
	"eu" : "Euskara",		# Basque
	"fa" : "&#1601;&#1575;&#1585;&#1587;&#1740;",	# Persian
	"ff" : "Fulfulde",		# Fulfulde
	"fi" : "Suomi",		# Finnish
	"fj" : "Na Vosa Vakaviti",	# Fijian
	"fo" : "F&oslash;royskt",	# Faroese
	"fr" : "Fran&ccedil;ais",	# French
	"fy" : "Frysk",		# Frisian
	"ga" : "Gaeilge",		# Irish
	"gd" : "G&agrave;idhlig",	# Scots Gaelic
	"gl" : "Galego",		# Gallegan
	"gn" : "Ava&ntilde;e'&#7869;",	# Guarani
	"gu" : "&#2711;&#2753;&#2716;&#2736;&#2750;&#2724;&#2752;",	# Gujarati 
	"gv" : "Gaelg",		# Manx
	"ha" : "&#1607;&#1614;&#1608;&#1615;&#1587;&#1614;",	# Hausa
	"haw" : "Hawai`i",		# Hawaiian
	"he" : "&#1506;&#1489;&#1512;&#1497;&#1514;",	# Hebrew
	"hi" : "&#2361;&#2367;&#2344;&#2381;&#2342;&#2368;",	# Hindi
	"hr" : "Hrvatski",		# Croatian
	"hu" : "Magyar",		# Hungarian
	"hy" : "&#1344;&#1377;&#1397;&#1381;&#1408;&#1381;&#1398;",	# Armenian
	"hz" : "Otsiherero",	# Herero
	"ia" : "Interlingua",	# Interlingua (IALA)
	"id" : "Bahasa Indonesia",	# Indonesian
	"ie" : "Interlingue",	# Interlingue (Occidental)
	"ig" : "Igbo",			# Igbo
	"ik" : "I&ntilde;upiak",	# Inupiak
	"io" : "Ido",			# Ido
	"is" : "&Iacute;slensk",	# Icelandic
	"it" : "Italiano",		# Italian
	"iu" : "&#5123;&#5316;&#5251;&#5198;&#5200;&#5222;",	# Inuktitut
	"ja" : "&#26085;&#26412;&#35486;",	# Japanese
	"jv" : "Bahasa Jawa",	# Javanese
	"ka" : "&#4325;&#4304;&#4320;&#4311;&#4323;&#4314;&#4312;",	# Georgian
	"kk" : "&#1179;&#1072;&#1079;&#1072;&#1179;&#1096;&#1072;",	# Kazakh
	"kl" : "Kalaallisut",	# Greenlandic
	"km" : "&#6039;&#6070;&#6047;&#6070;&#6017;&#6098;&#6040;&#6082;&#6042;",	# Cambodian
	"kn" : "&#3221;&#3240;&#3277;&#3240;&#3233;",	# Kannada
	"ko" : "&#54620;&#44397;&#50612;",	# Korean
	"ks" : "&#2325;&#2358;&#2381;&#2350;&#2368;&#2352;&#2368; - (&#1603;&#1588;&#1605;&#1610;&#1585;&#1610;)",	# Kashmiri 
	"ku" : "Kurd&icirc;",	# Kurdish
	"kw" : "Kernewek",		# Cornish
	"ky" : "Kirghiz",
	"la" : "Latina",		# Latin
	"lb" : "L&euml;tzebuergesch",	# Luxemburguish
	"li" : "Limburgs",		# Limburgian
	"ln" : "Lingala",		# Lingala
	"lo" : "(Pha xa lao)",	# Laotian 
	"lt" : "Lietuvi&#371;",	# Lithuanian
	"lv" : "Latvie&scaron;u",	# Latvian
	"mi" : "Malagasy",		# Malagasy - FIXME
	"mh" : "Ebon",			# Marshallese
	"mi" : "M&#257;ori",	# Maori
	"mk" : "&#1052;&#1072;&#1082;&#1077;&#1076;&#1086;&#1085;&#1089;&#1082;&#1080;",	# Macedonian
	"ml" : "&#3374;&#3378;&#3375;&#3390;&#3379;&#3330;",	# Malayalam
	"mn" : "&#1052;&#1086;&#1085;&#1075;&#1086;&#1083;",	# Mongoloian
	"mo" : "Moldoveana",	# Moldovan
	"mr" : "&#2350;&#2352;&#2366;&#2336;&#2368;",	# Marathi
	"ms" : "Bahasa Melayu",	# Malay
	"mt" : "bil-Malti",	# Maltese
	"my" : "(Myanmasa)",	# Burmese
	"na" : "Nauru",		# Nauruan
	"nah" : "Nahuatl",
	"nds" : "Platd&uuml;&uuml;tsch",	# Low German ''or'' Low Saxon
	"ne" : "&#2344;&#2375;&#2346;&#2366;&#2354;&#2368;",	# Nepali
	"nl" : "Nederlands",	# Dutch
	"nb" : "Norsk",		# Norwegian [currently using old '''no''' code]
	"ne" : "&#2344;&#2375;&#2346;&#2366;&#2354;&#2368;",	# Nepali
	"nn" : "Nynorsk"	,	# (Norwegian) Nynorsk
	"no" : "Norsk",
	"nv" : "Din&eacute; bizaad",	# Navajo
	"ny" : "Chi-Chewa",	# Chichewa
	"oc" : "Occitan",		# Occitan
	"om" : "Oromoo", 		# Oromo
	"or" : "Oriya",		# Oriya - FIXME
	"pa" : "&#2346;&#2306;&#2332;&#2366;&#2348;&#2368; / &#2602;&#2588;&#2622;&#2604;&#2624; / &#1662;&#1606;&#1580;&#1575;&#1576;&#1610;",	# Punjabi
	"pi" : "&#2346;&#2366;&#2367;&#2356;",	# Pali
	"pl" : "Polski",		# Polish
	"ps" : "&#1662;&#1690;&#1578;&#1608;",	# Pashto
	"pt" : "Portugu&ecirc;s",	# Portuguese
	"qu" : "Runa Simi",	# Quechua
	"rm" : "Rumantsch",	# Raeto-Romance
	"rn" : "Kirundi",		# Kirundi
	"ro" : "Rom&acirc;n&#259;",	# Romanian
	"ru" : "&#1056;&#1091;&#1089;&#1089;&#1082;&#1080;&#1081;",	# Russian
	"rw" : "Kinyarwanda",
	"sa" : "&#2360;&#2306;&#2360;&#2381;&#2325;&#2371;&#2340;",	# Sanskrit
	"sc" : "Sardu",	# Sardinian
	"sd" : "&#2360;&#2367;&#2344;&#2343;&#2367;",	# Sindhi
	"se" : "S&aacute;megiella",	# (Northern) Sami
	"sg"	: "Sangro",
	"si" : "(Simhala)",	# Sinhalese
	"simple" : "Simple English",
	"sk" : "Sloven&#269;ina",	# Slovak
	"sl" : "Sloven&scaron;&#269;ina",	# Slovenian
	"sm" : "Gagana Samoa",	# Samoan
	"sn" : "chiShona",		# Shona
	"so" : "Soomaaliga",	# Somali
	"sq" : "Shqip",		# Albanian
	"sr" : "&#1057;&#1088;&#1087;&#1089;&#1082;&#1080; / Srpski",	# Serbian
	"ss" : "SiSwati",		# Swati
	"st" : "seSotho",		# (Southern) Sotho
	"su" : "Bahasa Sunda",	# Sundanese
	"sv" : "Svenska",		# Swedish
	"sw" : "Kiswahili",	# Swahili
	"ta" : "&#2980;&#2990;&#3007;&#2996;&#3021;",	# Tamil
	"te" : "&#3108;&#3142;&#3122;&#3137;&#3095;&#3137;",	# Telugu
	"tg" : "&#1058;&#1086;&#1207;&#1080;&#1082;&#1251;",	# Tajik
	"th" : "&#3652;&#3607;&#3618;",	# Thai
	"ti" : "Tigrinya",		# Tigrinya - FIXME
	"tk" : "&#1578;&#1585;&#1603;&#1605;&#1606; / &#1058;&#1091;&#1088;&#1082;&#1084;&#1077;&#1085;",	# Turkmen
	"tl" : "Tagalog",		# Tagalog (Filipino)
	"tn" : "Setswana",		# Setswana
	"to" : "Tonga",		# Tonga - FIXME
	"tpi" : "Tok Pisin",	# Tok Pisin
	"tr" : "T&uuml;rk&ccedil;e",	# Turkish
	"ts" : "Xitsonga",		# Tsonga
	"tt" : "Tatar",		# Tatar
	"tw" : "Twi",			# Twi -- FIXME
	"ty" : "Reo M&#257;`ohi",	# Tahitian
	"ug" : "Oyghurque",	# Uyghur
	"uk" : "&#1059;&#1082;&#1088;&#1072;&#1111;&#1085;&#1089;&#1100;&#1082;&#1072;",	# Ukrainian
	"ur" : "&#1575;&#1585;&#1583;&#1608;",	# Urdu
	"uz" : "&#1038;&#1079;&#1073;&#1077;&#1082;",	# Uzbek
	"ve" : "Venda",		# Venda
	"vi" : "Ti&#7871;ng Vi&#7879;t",	# Vietnamese
	"vo" : "Volap&uuml;k",	# Volapuk
	"wa" : "Walon",		# Walloon
	"wo" : "Wollof",		# Wolof
	"xh" : "isiXhosa",		# Xhosan
	"yi" : "&#1497;&#1497;&#1460;&#1491;&#1497;&#1513;",	# Yiddish
	"yo" : "Yor&ugrave;b&aacute;",	# Yoruba
	"za" : "(Cuengh)",		# Zhuang
	"zh" : "&#20013;&#25991;",	# (Zh&#333;ng W...n) - Chinese
	"zh-cn" : "&#20013;&#25991;(&#31616;&#20307;)",	# Simplified
	"zh-tw" : "&#20013;&#25991;(&#32321;&#20307;)",	# Traditional
	"zu" : "isiZulu",		# Zulu
}

