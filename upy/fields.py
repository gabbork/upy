"""
Contains some fields as utilities.
"""
from django.utils.translation import ugettext as _
from django.db import models
from django.utils.text import capfirst
from upy import forms

class NullTrueFieldBase(models.SubfieldBase):
    def to_python(self, value):
        return value == True

class NullTrueField(models.NullBooleanField):   
    __metaclass__ = NullTrueFieldBase 
    def to_python(self, value):
        if value is True:
            return value
        return False

    def get_prep_value(self, value):
        if value is None or value is False:
            return None
        return True
    
    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.NullTrueField,
            'required': not self.blank,
            'label': capfirst(self.verbose_name),
            'help_text': self.help_text}
        defaults.update(kwargs)
        return super(NullTrueField, self).formfield(**defaults)
    
# ISO 3166-1 country names and codes adapted from http://opencountrycodes.appspot.com/python/
CONTINENTS = [(u'africa',_(u'Africa')),
            (u'antarctica',_(u'Antarctica')),
            (u'asia',_(u'Asia')),
            (u'europe',_(u'Europe')),
            (u'north-america',_(u'North America')),
            (u'oceania',_(u'Oceania')),
            (u'south-america',_(u'South America')),
            ]

COUNTRIES = (
    ('GB', _('United Kingdom')), 
    ('AF', _('Afghanistan')), 
    ('AX', _('Aland Islands')), 
    ('AL', _('Albania')), 
    ('DZ', _('Algeria')), 
    ('AS', _('American Samoa')), 
    ('AD', _('Andorra')), 
    ('AO', _('Angola')), 
    ('AI', _('Anguilla')), 
    ('AQ', _('Antarctica')), 
    ('AG', _('Antigua and Barbuda')), 
    ('AR', _('Argentina')), 
    ('AM', _('Armenia')), 
    ('AW', _('Aruba')), 
    ('AU', _('Australia')), 
    ('AT', _('Austria')), 
    ('AZ', _('Azerbaijan')), 
    ('BS', _('Bahamas')), 
    ('BH', _('Bahrain')), 
    ('BD', _('Bangladesh')), 
    ('BB', _('Barbados')), 
    ('BY', _('Belarus')), 
    ('BE', _('Belgium')), 
    ('BZ', _('Belize')), 
    ('BJ', _('Benin')), 
    ('BM', _('Bermuda')), 
    ('BT', _('Bhutan')), 
    ('BO', _('Bolivia')), 
    ('BA', _('Bosnia and Herzegovina')), 
    ('BW', _('Botswana')), 
    ('BV', _('Bouvet Island')), 
    ('BR', _('Brazil')), 
    ('IO', _('British Indian Ocean Territory')), 
    ('BN', _('Brunei Darussalam')), 
    ('BG', _('Bulgaria')), 
    ('BF', _('Burkina Faso')), 
    ('BI', _('Burundi')), 
    ('KH', _('Cambodia')), 
    ('CM', _('Cameroon')), 
    ('CA', _('Canada')), 
    ('CV', _('Cape Verde')), 
    ('KY', _('Cayman Islands')), 
    ('CF', _('Central African Republic')), 
    ('TD', _('Chad')), 
    ('CL', _('Chile')), 
    ('CN', _('China')), 
    ('CX', _('Christmas Island')), 
    ('CC', _('Cocos (Keeling) Islands')), 
    ('CO', _('Colombia')), 
    ('KM', _('Comoros')), 
    ('CG', _('Congo')), 
    ('CD', _('Congo, The Democratic Republic of the')), 
    ('CK', _('Cook Islands')), 
    ('CR', _('Costa Rica')), 
    ('CI', _('Cote d\'Ivoire')), 
    ('HR', _('Croatia')), 
    ('CU', _('Cuba')), 
    ('CY', _('Cyprus')), 
    ('CZ', _('Czech Republic')), 
    ('DK', _('Denmark')), 
    ('DJ', _('Djibouti')), 
    ('DM', _('Dominica')), 
    ('DO', _('Dominican Republic')), 
    ('EC', _('Ecuador')), 
    ('EG', _('Egypt')), 
    ('SV', _('El Salvador')), 
    ('GQ', _('Equatorial Guinea')), 
    ('ER', _('Eritrea')), 
    ('EE', _('Estonia')), 
    ('ET', _('Ethiopia')), 
    ('FK', _('Falkland Islands (Malvinas)')), 
    ('FO', _('Faroe Islands')), 
    ('FJ', _('Fiji')), 
    ('FI', _('Finland')), 
    ('FR', _('France')), 
    ('GF', _('French Guiana')), 
    ('PF', _('French Polynesia')), 
    ('TF', _('French Southern Territories')), 
    ('GA', _('Gabon')), 
    ('GM', _('Gambia')), 
    ('GE', _('Georgia')), 
    ('DE', _('Germany')), 
    ('GH', _('Ghana')), 
    ('GI', _('Gibraltar')), 
    ('GR', _('Greece')), 
    ('GL', _('Greenland')), 
    ('GD', _('Grenada')), 
    ('GP', _('Guadeloupe')), 
    ('GU', _('Guam')), 
    ('GT', _('Guatemala')), 
    ('GG', _('Guernsey')), 
    ('GN', _('Guinea')), 
    ('GW', _('Guinea-Bissau')), 
    ('GY', _('Guyana')), 
    ('HT', _('Haiti')), 
    ('HM', _('Heard Island and McDonald Islands')), 
    ('VA', _('Holy See (Vatican City State)')), 
    ('HN', _('Honduras')), 
    ('HK', _('Hong Kong')), 
    ('HU', _('Hungary')), 
    ('IS', _('Iceland')), 
    ('IN', _('India')), 
    ('ID', _('Indonesia')), 
    ('IR', _('Iran, Islamic Republic of')), 
    ('IQ', _('Iraq')), 
    ('IE', _('Ireland')), 
    ('IM', _('Isle of Man')), 
    ('IL', _('Israel')), 
    ('IT', _('Italy')), 
    ('JM', _('Jamaica')), 
    ('JP', _('Japan')), 
    ('JE', _('Jersey')), 
    ('JO', _('Jordan')), 
    ('KZ', _('Kazakhstan')), 
    ('KE', _('Kenya')), 
    ('KI', _('Kiribati')), 
    ('KP', _('Korea, Democratic People\'s Republic of')), 
    ('KR', _('Korea, Republic of')), 
    ('KW', _('Kuwait')), 
    ('KG', _('Kyrgyzstan')), 
    ('LA', _('Lao People\'s Democratic Republic')), 
    ('LV', _('Latvia')), 
    ('LB', _('Lebanon')), 
    ('LS', _('Lesotho')), 
    ('LR', _('Liberia')), 
    ('LY', _('Libyan Arab Jamahiriya')), 
    ('LI', _('Liechtenstein')), 
    ('LT', _('Lithuania')), 
    ('LU', _('Luxembourg')), 
    ('MO', _('Macao')), 
    ('MK', _('Macedonia, The Former Yugoslav Republic of')), 
    ('MG', _('Madagascar')), 
    ('MW', _('Malawi')), 
    ('MY', _('Malaysia')), 
    ('MV', _('Maldives')), 
    ('ML', _('Mali')), 
    ('MT', _('Malta')), 
    ('MH', _('Marshall Islands')), 
    ('MQ', _('Martinique')), 
    ('MR', _('Mauritania')), 
    ('MU', _('Mauritius')), 
    ('YT', _('Mayotte')), 
    ('MX', _('Mexico')), 
    ('FM', _('Micronesia, Federated States of')), 
    ('MD', _('Moldova')), 
    ('MC', _('Monaco')), 
    ('MN', _('Mongolia')), 
    ('ME', _('Montenegro')), 
    ('MS', _('Montserrat')), 
    ('MA', _('Morocco')), 
    ('MZ', _('Mozambique')), 
    ('MM', _('Myanmar')), 
    ('NA', _('Namibia')), 
    ('NR', _('Nauru')), 
    ('NP', _('Nepal')), 
    ('NL', _('Netherlands')), 
    ('AN', _('Netherlands Antilles')), 
    ('NC', _('New Caledonia')), 
    ('NZ', _('New Zealand')), 
    ('NI', _('Nicaragua')), 
    ('NE', _('Niger')), 
    ('NG', _('Nigeria')), 
    ('NU', _('Niue')), 
    ('NF', _('Norfolk Island')), 
    ('MP', _('Northern Mariana Islands')), 
    ('NO', _('Norway')), 
    ('OM', _('Oman')), 
    ('PK', _('Pakistan')), 
    ('PW', _('Palau')), 
    ('PS', _('Palestinian Territory, Occupied')), 
    ('PA', _('Panama')), 
    ('PG', _('Papua New Guinea')), 
    ('PY', _('Paraguay')), 
    ('PE', _('Peru')), 
    ('PH', _('Philippines')), 
    ('PN', _('Pitcairn')), 
    ('PL', _('Poland')), 
    ('PT', _('Portugal')), 
    ('PR', _('Puerto Rico')), 
    ('QA', _('Qatar')), 
    ('RE', _('Reunion')), 
    ('RO', _('Romania')), 
    ('RU', _('Russian Federation')), 
    ('RW', _('Rwanda')), 
    ('BL', _('Saint Barthelemy')), 
    ('SH', _('Saint Helena')), 
    ('KN', _('Saint Kitts and Nevis')), 
    ('LC', _('Saint Lucia')), 
    ('MF', _('Saint Martin')), 
    ('PM', _('Saint Pierre and Miquelon')), 
    ('VC', _('Saint Vincent and the Grenadines')), 
    ('WS', _('Samoa')), 
    ('SM', _('San Marino')), 
    ('ST', _('Sao Tome and Principe')), 
    ('SA', _('Saudi Arabia')), 
    ('SN', _('Senegal')), 
    ('RS', _('Serbia')), 
    ('SC', _('Seychelles')), 
    ('SL', _('Sierra Leone')), 
    ('SG', _('Singapore')), 
    ('SK', _('Slovakia')), 
    ('SI', _('Slovenia')), 
    ('SB', _('Solomon Islands')), 
    ('SO', _('Somalia')), 
    ('ZA', _('South Africa')), 
    ('GS', _('South Georgia and the South Sandwich Islands')), 
    ('ES', _('Spain')), 
    ('LK', _('Sri Lanka')), 
    ('SD', _('Sudan')), 
    ('SR', _('Suriname')), 
    ('SJ', _('Svalbard and Jan Mayen')), 
    ('SZ', _('Swaziland')), 
    ('SE', _('Sweden')), 
    ('CH', _('Switzerland')), 
    ('SY', _('Syrian Arab Republic')), 
    ('TW', _('Taiwan, Province of China')), 
    ('TJ', _('Tajikistan')), 
    ('TZ', _('Tanzania, United Republic of')), 
    ('TH', _('Thailand')), 
    ('TL', _('Timor-Leste')), 
    ('TG', _('Togo')), 
    ('TK', _('Tokelau')), 
    ('TO', _('Tonga')), 
    ('TT', _('Trinidad and Tobago')), 
    ('TN', _('Tunisia')), 
    ('TR', _('Turkey')), 
    ('TM', _('Turkmenistan')), 
    ('TC', _('Turks and Caicos Islands')), 
    ('TV', _('Tuvalu')), 
    ('UG', _('Uganda')), 
    ('UA', _('Ukraine')), 
    ('AE', _('United Arab Emirates')), 
    ('US', _('United States')), 
    ('UM', _('United States Minor Outlying Islands')), 
    ('UY', _('Uruguay')), 
    ('UZ', _('Uzbekistan')), 
    ('VU', _('Vanuatu')), 
    ('VE', _('Venezuela')), 
    ('VN', _('Viet Nam')), 
    ('VG', _('Virgin Islands, British')), 
    ('VI', _('Virgin Islands, U.S.')), 
    ('WF', _('Wallis and Futuna')), 
    ('EH', _('Western Sahara')), 
    ('YE', _('Yemen')), 
    ('ZM', _('Zambia')), 
    ('ZW', _('Zimbabwe')), 
)

CONTINENT_COUNTRIES = (
       (_(u'Africa'),(
            ('DZ',_(u'Algeria')),
            ('AO',_(u'Angola')),
            ('BJ',_(u'Benin')),
            ('BW',_(u'Botswana')),
            ('BF',_(u'Burkina Faso')),
            ('BI',_(u'Burundi')),
            ('CM',_(u'Cameroon')),
            ('CV',_(u'Cape Verde')),
            ('CF',_(u'Central African Republic')),
            ('TD',_(u'Chad')),
            ('KM',_(u'Comoros')),
            ('CG',_(u'Congo')),
            ('CD',_(u'Congo, The Democratic Republic of the')),
            ('CI',_(u'Cote d\'Ivoire')),
            ('DJ',_(u'Djibouti')),
            ('EG',_(u'Egypt')),
            ('GQ',_(u'Equatorial Guinea')),
            ('ER',_(u'Eritrea')),
            ('ET',_(u'Ethiopia')),
            ('GA',_(u'Gabon')),
            ('GM',_(u'Gambia')),
            ('GH',_(u'Ghana')),
            ('GN',_(u'Guinea')),
            ('GW',_(u'Guinea-Bissau')),
            ('KE',_(u'Kenya')),
            ('LS',_(u'Lesotho')),
            ('LR',_(u'Liberia')),
            ('LY',_(u'Libyan Arab Jamahiriya')),
            ('MG',_(u'Madagascar')),
            ('YT',_(u'Mayotte')),
            ('MW',_(u'Malawi')),
            ('ML',_(u'Mali')),
            ('MR',_(u'Mauritania')),
            ('MU',_(u'Mauritius')),
            ('MA',_(u'Morocco')),
            ('MZ',_(u'Mozambique')),
            ('NA',_(u'Namibia')),
            ('NE',_(u'Niger')),
            ('NG',_(u'Nigeria')),
            ('RE',_(u'Reunion')),
            ('RW',_(u'Rwanda')),
            ('SH',_(u'Saint Helena')),
            ('ST',_(u'Sao Tome and Principe')),
            ('SN',_(u'Senegal')),
            ('SC',_(u'Seychelles')),
            ('SL',_(u'Sierra Leone')),
            ('SO',_(u'Somalia')),
            ('ZA',_(u'South Africa')),
            ('SD',_(u'Sudan')),
            ('SZ',_(u'Swaziland')),
            ('TZ',_(u'Tanzania, United Republic of')),
            ('TG',_(u'Togo')),
            ('TN',_(u'Tunisia')),
            ('UG',_(u'Uganda')),
            ('EH',_(u'Western Sahara')),
            ('ZM',_(u'Zambia')),
            ('ZW',_(u'Zimbabwe')),
            )),
        (_(u'Antarctica'),(
            ('AQ',_(u'Antarctica')),
            ('BV',_(u'Bouvet Island')),
            ('TF',_(u'French Southern Territories')),
            ('HM',_(u'Heard Island and McDonald Islands')),
            )),
        (_(u'Asia'),(
            ('AF',_(u'Afghanistan')),
            ('BH',_(u'Bahrain')),
            ('BD',_(u'Bangladesh')),
            ('BT',_(u'Bhutan')),
            ('IO',_(u'British Indian Ocean Territory')),
            ('BN',_(u'Brunei Darussalam')),
            ('KH',_(u'Cambodia')),
            ('CN',_(u'China')),
            ('HK',_(u'Hong Kong')),
            ('IR',_(u'Iran, Islamic Republic of')),
            ('IN',_(u'India')),
            ('ID',_(u'Indonesia')),
            ('IQ',_(u'Iraq')),
            ('IL',_(u'Israel')),
            ('JP',_(u'Japan')),
            ('JO',_(u'Jordan')),
            ('KZ',_(u'Kazakhstan')),
            ('KW',_(u'Kuwait')),
            ('KP',_(u'Korea, Democratic People\'s Republic of')),
            ('KR',_(u'Korea, Republic of')),
            ('LA',_(u'Lao People\'s Democratic Republic')),
            ('KG',_(u'Kyrgyzstan')),
            ('LB',_(u'Lebanon')),
            ('MO',_(u'Macao')),
            ('MY',_(u'Malaysia')),
            ('MV',_(u'Maldives')),
            ('MM',_(u'Myanmar')),
            ('MN',_(u'Mongolia')),
            ('NP',_(u'Nepal')),
            ('OM',_(u'Oman')),
            ('PK',_(u'Pakistan')),
            ('PS',_(u'Palestinian Territory, Occupied')),
            ('PH',_(u'Philippines')),
            ('QA',_(u'Qatar')),
            ('RU',_(u'Russian Federation')),
            ('SA',_(u'Saudi Arabia')),
            ('SG',_(u'Singapore')),
            ('SY',_(u'Syrian Arab Republic')),
            ('LK',_(u'Sri Lanka')),
            ('TJ',_(u'Tajikistan')),
            ('TW',_(u'Taiwan, Province of China')),
            ('TH',_(u'Thailand')),
            ('TL',_(u'Timor-Leste')),
            ('TR',_(u'Turkey')),
            ('TM',_(u'Turkmenistan')),
            ('AE',_(u'United Arab Emirates')),
            ('UZ',_(u'Uzbekistan')),
            ('VN',_(u'Vietnam')),
            ('YE',_(u'Yemen')),
            )),
        (_(u'Europe'),(
            ('AX',_(u'Aland Islands')),
            ('AL',_(u'Albania')),
            ('AD',_(u'Andorra')),
            ('AM',_(u'Armenia')),
            ('AT',_(u'Austria')),
            ('AZ',_(u'Azerbaijan')),
            ('BY',_(u'Belarus')),
            ('BE',_(u'Belgium')),
            ('BA',_(u'Bosnia and Herzegovina')),
            ('BG',_(u'Bulgaria')),
            ('HR',_(u'Croatia')),
            ('CY',_(u'Cyprus')),
            ('CZ',_(u'Czech Republic')),
            ('DK',_(u'Denmark')),
            ('EE',_(u'Estonia')),
            ('FO',_(u'Faroe Islands')),
            ('FI',_(u'Finland')),
            ('FR',_(u'France')),
            ('GE',_(u'Georgia')),
            ('DE',_(u'Germany')),
            ('GI',_(u'Gibraltar')),
            ('GR',_(u'Greece')),
            ('GL',_(u'Greenland')),
            ('GG',_(u'Guernsey')),
            ('HU',_(u'Hungary')),
            ('IS',_(u'Iceland')),
            ('IE',_(u'Ireland')),
            ('IM',_(u'Isle of Man')),
            ('IT',_(u'Italy')),
            ('JE',_(u'Jersey')),
            ('LV',_(u'Latvia')),
            ('LI',_(u'Liechtenstein')),
            ('LT',_(u'Lithuania')),
            ('LU',_(u'Luxembourg')),
            ('MK',_(u'Macedonia, The Former Yugoslav Republic of')),
            ('MT',_(u'Malta')),
            ('MD',_(u'Moldova')),
            ('MC',_(u'Monaco')),
            ('ME',_(u'Montenegro')),
            ('NL',_(u'Netherlands')),
            ('NO',_(u'Norway')),
            ('PL',_(u'Poland')),
            ('PT',_(u'Portugal')),
            ('RO',_(u'Romania')),
            ('SM',_(u'San Marino')),
            ('RS',_(u'Serbia')),
            ('SK',_(u'Slovakia')),
            ('SI',_(u'Slovenia')),
            ('ES',_(u'Spain')),
            ('SJ',_(u'Svalbard and Jan Mayen')),
            ('SE',_(u'Sweden')),
            ('CH',_(u'Switzerland')),
            ('UA',_(u'Ukraine')),
            ('GB',_(u'United Kingdom')),
            ('VA',_(u'Holy See (Vatican City State)')),
            )),
        (_(u'North America'),(
            ('AS',_(u'American Samoa')),
            ('AI',_(u'Anguilla')),
            ('AG',_(u'Antigua and Barbuda')),
            ('AW',_(u'Aruba')),
            ('BS',_(u'Bahamas')),
            ('BB',_(u'Barbados')),
            ('BZ',_(u'Belize')),
            ('BM',_(u'Bermuda')),
            ('CA',_(u'Canada')),
            ('KY',_(u'Cayman Islands')),
            ('CR',_(u'Costa Rica')),
            ('CU',_(u'Cuba')),
            ('DM',_(u'Dominica')),
            ('DO',_(u'Dominican Republic')),
            ('SV',_(u'El Salvador')),
            ('GD',_(u'Grenada')),
            ('GP',_(u'Guadeloupe')),
            ('GT',_(u'Guatemala')),
            ('HT',_(u'Haiti')),
            ('HN',_(u'Honduras')),
            ('JM',_(u'Jamaica')),
            ('MX',_(u'Mexico')),
            ('MS',_(u'Montserrat')),
            ('AN',_(u'Netherlands Antilles')),
            ('NI',_(u'Nicaragua')),
            ('PA',_(u'Panama')),
            ('PR',_(u'Puerto Rico')),
            ('BL',_(u'Saint Barthelemy')),
            ('KN',_(u'Saint Kitts and Nevis')),
            ('LC',_(u'Saint Lucia')),
            ('MF',_(u'Saint Martin')),
            ('PM',_(u'Saint Pierre and Miquelon')),
            ('VC',_(u'Saint Vincent and the Grenadines')),
            ('TT',_(u'Trinidad and Tobago')),
            ('TC',_(u'Turks and Caicos Islands')),
            ('US',_(u'United States')),
            ('UM',_(u'United States Minor Outlying Islands')),
            ('VG',_(u'Virgin Islands, British')),
            ('VI',_(u'Virgin Islands, U.S.')),
            )),
        (_(u'Oceania'),(
            ('AU',_(u'Australia')),
            ('CX',_(u'Christmas Island')),
            ('CC',_(u'Cocos (Keeling) Islands')),
            ('CK',_(u'Cook Islands')),
            ('FJ',_(u'Fiji')),
            ('PF',_(u'French Polynesia')),
            ('GU',_(u'Guam')),
            ('KI',_(u'Kiribati')),
            ('MH',_(u'Marshall Islands')),
            ('FM',_(u'Micronesia, Federated States of')),
            ('NR',_(u'Nauru')),
            ('NC',_(u'New Caledonia')),
            ('NZ',_(u'New Zealand')),
            ('NU',_(u'Niue')),
            ('NF',_(u'Norfolk Island')),
            ('MP',_(u'Northern Mariana Islands')),
            ('PW',_(u'Palau')),
            ('PG',_(u'Papua New Guinea')),
            ('PN',_(u'Pitcairn')),
            ('WS',_(u'Samoa')),
            ('SB',_(u'Solomon Islands')),
            ('TK',_(u'Tokelau')),
            ('TO',_(u'Tonga')),
            ('TV',_(u'Tuvalu')),
            ('VU',_(u'Vanuatu')),
            ('WF',_(u'Wallis and Futuna')),
            )),
        (_(u'South America'),(
            ('AR',_(u'Argentina')),
            ('BO',_(u'Bolivia')),
            ('BR',_(u'Brazil')),
            ('CL',_(u'Chile')),
            ('CO',_(u'Colombia')),
            ('EC',_(u'Ecuador')),
            ('FK',_(u'Falkland Islands (Malvinas)')),
            ('GF',_(u'French Guiana')),
            ('GY',_(u'Guyana')),
            ('MQ',_(u'Martinique')),
            ('PY',_(u'Paraguay')),
            ('PE',_(u'Peru')),
            ('GS',_(u'South Georgia and the South Sandwich Islands')),
            ('SR',_(u'Suriname')),
            ('UY',_(u'Uruguay')),
            ('VE',_(u'Venezuela')),
            )),
       )
             
class CountryField(models.CharField):
    """
    Is a CharField with the complete list of countries as choices.
    """
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 2)
        kwargs.setdefault('choices', COUNTRIES)

        super(CountryField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        """
        Returns internal type of this field: CharField as string
        """
        return "CharField"
    
    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.NullTrueField
        }
        defaults.update(kwargs)
        return super(CountryField, self).formfield(**defaults) 
        

class ContinentCountryField(models.CharField):
    """
    Is a CharField with the complete list of countries as choices.
    """
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 2)
        kwargs.setdefault('choices', CONTINENT_COUNTRIES)
        super(ContinentCountryField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        """
        Returns internal type of this field: CharField as string
        """
        return "CharField"     

    
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^upy\.fields\.ContinentCountryField","^upy\.fields\.CountryField","^upy\.fields\.NullTrueField"])
except ImportError:
    pass