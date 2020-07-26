import copy

from django.core.management import BaseCommand

from apps.common.models import Country, Province, District, City

COUNTRIES = [
    {
        "id": "442",
        "name": "Abkhazia",
        "denonym": [
            "Abkhaz",
            "Abkhazian"
        ],
        "adjectival": [
            "Abkhazian"
        ],
        "nationality": "Abkhaz",
        "relevance": None
    },
    {
        "id": "444",
        "name": "Åland Islands",
        "denonym": [
            "Åland Island"
        ],
        "adjectival": [
            "Åland Islander"
        ],
        "nationality": "Åland Island",
        "relevance": None
    },
    {
        "id": "445",
        "name": "Albania",
        "denonym": [
            "Albanian"
        ],
        "adjectival": [
            "Albanian"
        ],
        "nationality": "Albanian",
        "relevance": None
    },
    {
        "id": "446",
        "name": "Algeria",
        "denonym": [
            "Algerian"
        ],
        "adjectival": [
            "Algerian"
        ],
        "nationality": "Algerian",
        "relevance": None
    },
    {
        "id": "447",
        "name": "American Samoa",
        "denonym": [
            "American Samoan"
        ],
        "adjectival": [
            "American Samoan"
        ],
        "nationality": "American Samoan",
        "relevance": None
    },
    {
        "id": "448",
        "name": "Andorra",
        "denonym": [
            "Andorran"
        ],
        "adjectival": [
            "Andorran"
        ],
        "nationality": "Andorran",
        "relevance": None
    },
    {
        "id": "449",
        "name": "Angola",
        "denonym": [
            "Angolan"
        ],
        "adjectival": [
            "Angolan"
        ],
        "nationality": "Angolan",
        "relevance": None
    },
    {
        "id": "450",
        "name": "Anguilla",
        "denonym": [
            "Anguillan"
        ],
        "adjectival": [
            "Anguillan"
        ],
        "nationality": "Anguillan",
        "relevance": None
    },
    {
        "id": "451",
        "name": "Antarctica",
        "denonym": [
            "Antarctic"
        ],
        "adjectival": [
            "Antarctic resident"
        ],
        "nationality": "Antarctic",
        "relevance": None
    },
    {
        "id": "452",
        "name": "Antigua and Barbuda",
        "denonym": [
            "Antiguan or Barbudan"
        ],
        "adjectival": [
            "Antiguans or Barbudan"
        ],
        "nationality": "Antiguan or Barbudan",
        "relevance": None
    },
    {
        "id": "453",
        "name": "Argentina",
        "denonym": [
            "Argentinian"
        ],
        "adjectival": [
            "Argentine",
            "Argentinians"
        ],
        "nationality": "Argentinian",
        "relevance": None
    },
    {
        "id": "454",
        "name": "Armenia",
        "denonym": [
            "Armenian"
        ],
        "adjectival": [
            "Armenians"
        ],
        "nationality": "Armenian",
        "relevance": None
    },
    {
        "id": "455",
        "name": "Aruba",
        "denonym": [
            "Aruban"
        ],
        "adjectival": [
            "Aruban"
        ],
        "nationality": "Aruban",
        "relevance": None
    },
    {
        "id": "456",
        "name": "Australia",
        "denonym": [
            "Australian"
        ],
        "adjectival": [
            "Australian"
        ],
        "nationality": "Australian",
        "relevance": None
    },
    {
        "id": "457",
        "name": "Austria",
        "denonym": [
            "Austrian"
        ],
        "adjectival": [
            "Austrian"
        ],
        "nationality": "Austrian",
        "relevance": None
    },
    {
        "id": "458",
        "name": "Azerbaijan",
        "denonym": [
            "Azerbaijani",
            "Azeri"
        ],
        "adjectival": [
            "Azerbaijanis",
            "Azeri"
        ],
        "nationality": "Azerbaijani",
        "relevance": None
    },
    {
        "id": "459",
        "name": "The Bahamas",
        "denonym": [
            "Bahamian"
        ],
        "adjectival": [
            "Bahamian"
        ],
        "nationality": "Bahamian",
        "relevance": None
    },
    {
        "id": "460",
        "name": "Bahrain",
        "denonym": [
            "Bahraini"
        ],
        "adjectival": [
            "Bahraini"
        ],
        "nationality": "Bahraini",
        "relevance": None
    },
    {
        "id": "462",
        "name": "Barbados",
        "denonym": [
            "Barbadian"
        ],
        "adjectival": [
            "Barbadian"
        ],
        "nationality": "Barbadian",
        "relevance": None
    },
    {
        "id": "463",
        "name": "Belarus",
        "denonym": [
            "Belarusian"
        ],
        "adjectival": [
            "Belarusian"
        ],
        "nationality": "Belarusian",
        "relevance": None
    },
    {
        "id": "464",
        "name": "Belgium",
        "denonym": [
            "Belgian"
        ],
        "adjectival": [
            "Belgian"
        ],
        "nationality": "Belgian",
        "relevance": None
    },
    {
        "id": "465",
        "name": "Belize",
        "denonym": [
            "Belizean"
        ],
        "adjectival": [
            "Belizean"
        ],
        "nationality": "Belizean",
        "relevance": None
    },
    {
        "id": "466",
        "name": "Benin",
        "denonym": [
            "Beninese",
            "Beninois"
        ],
        "adjectival": [
            "Beninese",
            "Beninois"
        ],
        "nationality": "Beninese",
        "relevance": None
    },
    {
        "id": "467",
        "name": "Bermuda",
        "denonym": [
            "Bermudian",
            "Bermudan"
        ],
        "adjectival": [
            "Bermudian",
            "Bermudan"
        ],
        "nationality": "Bermudian",
        "relevance": None
    },
    {
        "id": "469",
        "name": "Bolivia",
        "denonym": [
            "Bolivian"
        ],
        "adjectival": [
            "Bolivian"
        ],
        "nationality": "Bolivian",
        "relevance": None
    },
    {
        "id": "470",
        "name": "Bonaire",
        "denonym": [
            "Bonaire"
        ],
        "adjectival": [
            "Bonaire Dutch"
        ],
        "nationality": "Bonaire",
        "relevance": None
    },
    {
        "id": "471",
        "name": "Bosnia and Herzegovina",
        "denonym": [
            "Bosnian or Herzegovinian"
        ],
        "adjectival": [
            "Bosnian or Herzegovinian"
        ],
        "nationality": "Bosnian or Herzegovinian",
        "relevance": None
    },
    {
        "id": "472",
        "name": "Botswana",
        "denonym": [
            "Motswana",
            "Botswanan"
        ],
        "adjectival": [
            "Motswana",
            "Batswana",
            "Botswanan"
        ],
        "nationality": "Motswana",
        "relevance": None
    },
    {
        "id": "473",
        "name": "Bouvet Island",
        "denonym": [
            "Bouvet Island"
        ],
        "adjectival": [
            ""
        ],
        "nationality": "Bouvet Island",
        "relevance": None
    },
    {
        "id": "474",
        "name": "Brazil",
        "denonym": [
            "Brazilian"
        ],
        "adjectival": [
            "Brazilian"
        ],
        "nationality": "Brazilian",
        "relevance": None
    },
    {
        "id": "475",
        "name": "British Indian Ocean Territory",
        "denonym": [
            "BIOT"
        ],
        "adjectival": [
            "British"
        ],
        "nationality": "BIOT",
        "relevance": None
    },
    {
        "id": "476",
        "name": "Brunei",
        "denonym": [
            "Bruneian"
        ],
        "adjectival": [
            "Bruneian"
        ],
        "nationality": "Bruneian",
        "relevance": None
    },
    {
        "id": "477",
        "name": "Bulgaria",
        "denonym": [
            "Bulgarian"
        ],
        "adjectival": [
            "Bulgarian"
        ],
        "nationality": "Bulgarian",
        "relevance": None
    },
    {
        "id": "478",
        "name": "Burkina Faso",
        "denonym": [
            "Burkinabé"
        ],
        "adjectival": [
            "Burkinabè/Burkinabé"
        ],
        "nationality": "Burkinabé",
        "relevance": None
    },
    {
        "id": "480",
        "name": "Burundi",
        "denonym": [
            "Burundian"
        ],
        "adjectival": [
            "Burundian",
            "Barundi"
        ],
        "nationality": "Burundian",
        "relevance": None
    },
    {
        "id": "481",
        "name": "Cabo Verde",
        "denonym": [
            "Cabo Verdean"
        ],
        "adjectival": [
            "Cabo Verdean"
        ],
        "nationality": "Cabo Verdean",
        "relevance": None
    },
    {
        "id": "482",
        "name": "Cambodia",
        "denonym": [
            "Cambodian"
        ],
        "adjectival": [
            "Cambodian"
        ],
        "nationality": "Cambodian",
        "relevance": None
    },
    {
        "id": "483",
        "name": "Cameroon",
        "denonym": [
            "Cameroonian"
        ],
        "adjectival": [
            "Cameroonian"
        ],
        "nationality": "Cameroonian",
        "relevance": None
    },
    {
        "id": "484",
        "name": "Canada",
        "denonym": [
            "Canadian"
        ],
        "adjectival": [
            "Canadian"
        ],
        "nationality": "Canadian",
        "relevance": None
    },
    {
        "id": "485",
        "name": "Cayman Islands",
        "denonym": [
            "Caymanian"
        ],
        "adjectival": [
            "Caymanian"
        ],
        "nationality": "Caymanian",
        "relevance": None
    },
    {
        "id": "486",
        "name": "Central African Republic",
        "denonym": [
            "Central African"
        ],
        "adjectival": [
            "Central African"
        ],
        "nationality": "Central African",
        "relevance": None
    },
    {
        "id": "487",
        "name": "Chad",
        "denonym": [
            "Chadian"
        ],
        "adjectival": [
            "Chadian"
        ],
        "nationality": "Chadian",
        "relevance": None
    },
    {
        "id": "488",
        "name": "Chile",
        "denonym": [
            "Chilean"
        ],
        "adjectival": [
            "Chilean"
        ],
        "nationality": "Chilean",
        "relevance": None
    },
    {
        "id": "489",
        "name": "China",
        "denonym": [
            "Chinese"
        ],
        "adjectival": [
            "Chinese"
        ],
        "nationality": "Chinese",
        "relevance": None
    },
    {
        "id": "490",
        "name": "Christmas Island",
        "denonym": [
            "Christmas Island"
        ],
        "adjectival": [
            "Christmas Islander"
        ],
        "nationality": "Christmas Island",
        "relevance": None
    },
    {
        "id": "491",
        "name": "Cocos (Keeling) Islands",
        "denonym": [
            "Cocos Island"
        ],
        "adjectival": [
            "Cocos Islander"
        ],
        "nationality": "Cocos Island",
        "relevance": None
    },
    {
        "id": "492",
        "name": "Colombia",
        "denonym": [
            "Colombian"
        ],
        "adjectival": [
            "Colombian"
        ],
        "nationality": "Colombian",
        "relevance": None
    },
    {
        "id": "493",
        "name": "Comoros",
        "denonym": [
            "Comoran",
            "Comorian"
        ],
        "adjectival": [
            "Comoran",
            "Comorian"
        ],
        "nationality": "Comoran",
        "relevance": None
    },
    {
        "id": "494",
        "name": "Republic of the Congo",
        "denonym": [
            "Congolese"
        ],
        "adjectival": [
            "Congolese"
        ],
        "nationality": "Congolese",
        "relevance": None
    },
    {
        "id": "495",
        "name": "Cook Islands",
        "denonym": [
            "Cook Island"
        ],
        "adjectival": [
            "Cook Islander"
        ],
        "nationality": "Cook Island",
        "relevance": None
    },
    {
        "id": "496",
        "name": "Costa Rica",
        "denonym": [
            "Costa Rican"
        ],
        "adjectival": [
            "Costa Rican"
        ],
        "nationality": "Costa Rican",
        "relevance": None
    },
    {
        "id": "498",
        "name": "Croatia",
        "denonym": [
            "Croatian"
        ],
        "adjectival": [
            "Croatian",
            "Croat"
        ],
        "nationality": "Croatian",
        "relevance": None
    },
    {
        "id": "499",
        "name": "Cuba",
        "denonym": [
            "Cuban"
        ],
        "adjectival": [
            "Cuban"
        ],
        "nationality": "Cuban",
        "relevance": None
    },
    {
        "id": "500",
        "name": "Curaçao",
        "denonym": [
            "Curaçaoan"
        ],
        "adjectival": [
            "Curaçaoan"
        ],
        "nationality": "Curaçaoan",
        "relevance": None
    },
    {
        "id": "501",
        "name": "Cyprus",
        "denonym": [
            "Cypriot"
        ],
        "adjectival": [
            "Cypriot"
        ],
        "nationality": "Cypriot",
        "relevance": None
    },
    {
        "id": "502",
        "name": "Czech Republic",
        "denonym": [
            "Czech"
        ],
        "adjectival": [
            "Czech"
        ],
        "nationality": "Czech",
        "relevance": None
    },
    {
        "id": "503",
        "name": "Denmark",
        "denonym": [
            "Danish"
        ],
        "adjectival": [
            "Dane"
        ],
        "nationality": "Danish",
        "relevance": None
    },
    {
        "id": "504",
        "name": "Djibouti",
        "denonym": [
            "Djiboutian"
        ],
        "adjectival": [
            "Djiboutian"
        ],
        "nationality": "Djiboutian",
        "relevance": None
    },
    {
        "id": "505",
        "name": "Dominica",
        "denonym": [
            "Dominican"
        ],
        "adjectival": [
            "Dominican"
        ],
        "nationality": "Dominicans (Commonwealth)",
        "relevance": None
    },
    {
        "id": "506",
        "name": "Dominican Republic",
        "denonym": [
            "Dominican"
        ],
        "adjectival": [
            "Dominican"
        ],
        "nationality": "Dominicans (Republic)",
        "relevance": None
    },
    {
        "id": "507",
        "name": "East Timor",
        "denonym": [
            "Timorese"
        ],
        "adjectival": [
            "Timoresw"
        ],
        "nationality": "East Timorese",
        "relevance": None
    },
    {
        "id": "508",
        "name": "Ecuador",
        "denonym": [
            "Ecuadorian"
        ],
        "adjectival": [
            "Ecuadorian"
        ],
        "nationality": "Ecuadorian",
        "relevance": None
    },
    {
        "id": "509",
        "name": "Egypt",
        "denonym": [
            "Egyptian"
        ],
        "adjectival": [
            "Egyptian"
        ],
        "nationality": "Egyptian",
        "relevance": None
    },
    {
        "id": "443",
        "name": "Afghanistan",
        "denonym": [
            "Afghan"
        ],
        "adjectival": [
            "Afghan"
        ],
        "nationality": "Afghan",
        "relevance": "4"
    },
    {
        "id": "468",
        "name": "Bhutan",
        "denonym": [
            "Bhutanese"
        ],
        "adjectival": [
            "Bhutanese"
        ],
        "nationality": "Bhutanese",
        "relevance": "6"
    },
    {
        "id": "510",
        "name": "El Salvador",
        "denonym": [
            "Salvadoran"
        ],
        "adjectival": [
            "Salvadoran"
        ],
        "nationality": "Salvadoran",
        "relevance": None
    },
    {
        "id": "511",
        "name": "Equatorial Guinea",
        "denonym": [
            "Equatorial Guinean",
            "Equatoguinean"
        ],
        "adjectival": [
            "Equatorial Guinean",
            "Equatoguinean"
        ],
        "nationality": "Equatorial Guinean",
        "relevance": None
    },
    {
        "id": "512",
        "name": "Eritrea",
        "denonym": [
            "Eritrean"
        ],
        "adjectival": [
            "Eritrean"
        ],
        "nationality": "Eritrean",
        "relevance": None
    },
    {
        "id": "513",
        "name": "Estonia",
        "denonym": [
            "Estonian"
        ],
        "adjectival": [
            "Estonian"
        ],
        "nationality": "Estonian",
        "relevance": None
    },
    {
        "id": "514",
        "name": "Swaziland",
        "denonym": [
            "Swazi",
            "Swati"
        ],
        "adjectival": [
            "Swazi"
        ],
        "nationality": "Swazi",
        "relevance": None
    },
    {
        "id": "515",
        "name": "Ethiopia",
        "denonym": [
            "Ethiopian"
        ],
        "adjectival": [
            "Ethiopian",
            "Habesha"
        ],
        "nationality": "Ethiopian",
        "relevance": None
    },
    {
        "id": "516",
        "name": "European Union",
        "denonym": [
            "European"
        ],
        "adjectival": [
            "European"
        ],
        "nationality": "European",
        "relevance": None
    },
    {
        "id": "517",
        "name": "Falkland Islands",
        "denonym": [
            "Falkland Island"
        ],
        "adjectival": [
            "Falkland Islander"
        ],
        "nationality": "Falkland Island",
        "relevance": None
    },
    {
        "id": "518",
        "name": "Faroe Islands",
        "denonym": [
            "Faroese"
        ],
        "adjectival": [
            "Faroese"
        ],
        "nationality": "Faroese",
        "relevance": None
    },
    {
        "id": "519",
        "name": "Fiji",
        "denonym": [
            "Fijian"
        ],
        "adjectival": [
            "Fijian"
        ],
        "nationality": "Fijian",
        "relevance": None
    },
    {
        "id": "520",
        "name": "Finland",
        "denonym": [
            "Finnish"
        ],
        "adjectival": [
            "Finn"
        ],
        "nationality": "Finnish",
        "relevance": None
    },
    {
        "id": "521",
        "name": "France",
        "denonym": [
            "French"
        ],
        "adjectival": [
            "French"
        ],
        "nationality": "French",
        "relevance": None
    },
    {
        "id": "522",
        "name": "French Guiana",
        "denonym": [
            "French Guianese"
        ],
        "adjectival": [
            "French Guianese"
        ],
        "nationality": "French Guianese",
        "relevance": None
    },
    {
        "id": "523",
        "name": "French Polynesia",
        "denonym": [
            "French Polynesian"
        ],
        "adjectival": [
            "French Polynesian"
        ],
        "nationality": "French Polynesian",
        "relevance": None
    },
    {
        "id": "524",
        "name": "French Southern Territories",
        "denonym": [
            "French Southern Territories"
        ],
        "adjectival": [
            "French"
        ],
        "nationality": "French Southern Territories",
        "relevance": None
    },
    {
        "id": "525",
        "name": "Gabon",
        "denonym": [
            "Gabonese"
        ],
        "adjectival": [
            "Gabonese",
            "Gabonaise"
        ],
        "nationality": "Gabonese",
        "relevance": None
    },
    {
        "id": "526",
        "name": "The Gambia",
        "denonym": [
            "Gambian"
        ],
        "adjectival": [
            "Gambian"
        ],
        "nationality": "Gambian",
        "relevance": None
    },
    {
        "id": "527",
        "name": "Georgia",
        "denonym": [
            "Georgian"
        ],
        "adjectival": [
            "Georgian"
        ],
        "nationality": "Georgian",
        "relevance": None
    },
    {
        "id": "528",
        "name": "Germany",
        "denonym": [
            "German"
        ],
        "adjectival": [
            "German"
        ],
        "nationality": "German",
        "relevance": None
    },
    {
        "id": "529",
        "name": "Ghana",
        "denonym": [
            "Ghanaian"
        ],
        "adjectival": [
            "Ghanaian"
        ],
        "nationality": "Ghanaian",
        "relevance": None
    },
    {
        "id": "530",
        "name": "Gibraltar",
        "denonym": [
            "Gibraltar"
        ],
        "adjectival": [
            "Gibraltarian"
        ],
        "nationality": "Gibraltar",
        "relevance": None
    },
    {
        "id": "531",
        "name": "Greece",
        "denonym": [
            "Greek",
            "Hellenic"
        ],
        "adjectival": [
            "Greek",
            "Hellene"
        ],
        "nationality": "Greek",
        "relevance": None
    },
    {
        "id": "532",
        "name": "Greenland",
        "denonym": [
            "Greenlandic"
        ],
        "adjectival": [
            "Greenlander"
        ],
        "nationality": "Greenlandic",
        "relevance": None
    },
    {
        "id": "533",
        "name": "Grenada",
        "denonym": [
            "Grenadian"
        ],
        "adjectival": [
            "Grenadian"
        ],
        "nationality": "Grenadian",
        "relevance": None
    },
    {
        "id": "534",
        "name": "Guadeloupe",
        "denonym": [
            "Guadeloupe"
        ],
        "adjectival": [
            "Guadeloupian"
        ],
        "nationality": "Guadeloupe",
        "relevance": None
    },
    {
        "id": "535",
        "name": "Guam",
        "denonym": [
            "Guamanian"
        ],
        "adjectival": [
            "Guamanian"
        ],
        "nationality": "Guamanian",
        "relevance": None
    },
    {
        "id": "536",
        "name": "Guatemala",
        "denonym": [
            "Guatemalan"
        ],
        "adjectival": [
            "Guatemalan"
        ],
        "nationality": "Guatemalan",
        "relevance": None
    },
    {
        "id": "537",
        "name": "Guernsey",
        "denonym": [
            "Channel Island"
        ],
        "adjectival": [
            "Channel Islander"
        ],
        "nationality": "Guernsey",
        "relevance": None
    },
    {
        "id": "538",
        "name": "Guinea",
        "denonym": [
            "Guinean"
        ],
        "adjectival": [
            "Guinean"
        ],
        "nationality": "Guinean",
        "relevance": None
    },
    {
        "id": "539",
        "name": "Guinea-Bissau",
        "denonym": [
            "Bissau-Guinean"
        ],
        "adjectival": [
            "Bissau-Guinean"
        ],
        "nationality": "Bissau-Guinean",
        "relevance": None
    },
    {
        "id": "540",
        "name": "Guyana",
        "denonym": [
            "Guyanese"
        ],
        "adjectival": [
            "Guyanese"
        ],
        "nationality": "Guyanese",
        "relevance": None
    },
    {
        "id": "541",
        "name": "Haiti}",
        "denonym": [
            "Haitian"
        ],
        "adjectival": [
            "Haitian"
        ],
        "nationality": "Haitian",
        "relevance": None
    },
    {
        "id": "542",
        "name": "Heard Island and McDonald Islands",
        "denonym": [
            "Heard Island or McDonald Islands"
        ],
        "adjectival": [
            ""
        ],
        "nationality": "Heard Island or McDonald Islands",
        "relevance": None
    },
    {
        "id": "543",
        "name": "Honduras",
        "denonym": [
            "Honduran"
        ],
        "adjectival": [
            "Hondurans"
        ],
        "nationality": "Honduran",
        "relevance": None
    },
    {
        "id": "544",
        "name": "Hong Kong",
        "denonym": [
            "Hong Kong",
            "Hong Kongese"
        ],
        "adjectival": [
            "Hongkonger",
            "Hong Kongese"
        ],
        "nationality": "Hong Kong",
        "relevance": None
    },
    {
        "id": "545",
        "name": "Hungary",
        "denonym": [
            "Hungarian",
            "Magyar"
        ],
        "adjectival": [
            "Hungarian",
            "Magyar"
        ],
        "nationality": "Hungarian",
        "relevance": None
    },
    {
        "id": "546",
        "name": "Iceland",
        "denonym": [
            "Icelandic"
        ],
        "adjectival": [
            "Icelander"
        ],
        "nationality": "Icelandic",
        "relevance": None
    },
    {
        "id": "548",
        "name": "Indonesia",
        "denonym": [
            "Indonesian"
        ],
        "adjectival": [
            "Indonesian"
        ],
        "nationality": "Indonesian",
        "relevance": None
    },
    {
        "id": "550",
        "name": "Iraq",
        "denonym": [
            "Iraqi"
        ],
        "adjectival": [
            "Iraqi"
        ],
        "nationality": "Iraqi",
        "relevance": None
    },
    {
        "id": "551",
        "name": "Ireland",
        "denonym": [
            "Irish"
        ],
        "adjectival": [
            "Irish"
        ],
        "nationality": "Irish",
        "relevance": None
    },
    {
        "id": "552",
        "name": "Isle of Man",
        "denonym": [
            "Manx"
        ],
        "adjectival": [
            "Manx"
        ],
        "nationality": "Manx",
        "relevance": None
    },
    {
        "id": "553",
        "name": "Israel",
        "denonym": [
            "Israeli"
        ],
        "adjectival": [
            "Israeli"
        ],
        "nationality": "Israeli",
        "relevance": None
    },
    {
        "id": "554",
        "name": "Italy",
        "denonym": [
            "Italian"
        ],
        "adjectival": [
            "Italian"
        ],
        "nationality": "Italian",
        "relevance": None
    },
    {
        "id": "555",
        "name": "Ivory Coast",
        "denonym": [
            "Ivorian"
        ],
        "adjectival": [
            "Ivorian"
        ],
        "nationality": "Ivorian",
        "relevance": None
    },
    {
        "id": "556",
        "name": "Jamaica",
        "denonym": [
            "Jamaican"
        ],
        "adjectival": [
            "Jamaican"
        ],
        "nationality": "Jamaican",
        "relevance": None
    },
    {
        "id": "557",
        "name": "Jan Mayen",
        "denonym": [
            "Jan Mayen"
        ],
        "adjectival": [
            ""
        ],
        "nationality": "Jan Mayen",
        "relevance": None
    },
    {
        "id": "558",
        "name": "Japan",
        "denonym": [
            "Japanese"
        ],
        "adjectival": [
            "Japanese"
        ],
        "nationality": "Japanese",
        "relevance": None
    },
    {
        "id": "559",
        "name": "Jersey",
        "denonym": [
            "Channel Island"
        ],
        "adjectival": [
            "Channel Islander"
        ],
        "nationality": "Jersey",
        "relevance": None
    },
    {
        "id": "560",
        "name": "Jordan",
        "denonym": [
            "Jordanian"
        ],
        "adjectival": [
            "Jordanians"
        ],
        "nationality": "Jordanian",
        "relevance": None
    },
    {
        "id": "561",
        "name": "Kazakhstan",
        "denonym": [
            "Kazakhstani",
            "Kazakh"
        ],
        "adjectival": [
            "Kazakhstani",
            "Kazakh"
        ],
        "nationality": "Kazakhstani",
        "relevance": None
    },
    {
        "id": "562",
        "name": "Kenya",
        "denonym": [
            "Kenyan"
        ],
        "adjectival": [
            "Kenyan"
        ],
        "nationality": "Kenyan",
        "relevance": None
    },
    {
        "id": "563",
        "name": "Kiribati",
        "denonym": [
            "I-Kiribati"
        ],
        "adjectival": [
            "I-Kiribati"
        ],
        "nationality": "I-Kiribati",
        "relevance": None
    },
    {
        "id": "564",
        "name": "North Korea",
        "denonym": [
            "North Korean"
        ],
        "adjectival": [
            "Korean"
        ],
        "nationality": "North Korean",
        "relevance": None
    },
    {
        "id": "565",
        "name": "South Korea",
        "denonym": [
            "South Korean"
        ],
        "adjectival": [
            ""
        ],
        "nationality": "South Korean",
        "relevance": None
    },
    {
        "id": "566",
        "name": "Kosovo",
        "denonym": [
            "Kosovar",
            "Kosovan"
        ],
        "adjectival": [
            "Kosovar"
        ],
        "nationality": "Kosovar",
        "relevance": None
    },
    {
        "id": "567",
        "name": "Kuwait",
        "denonym": [
            "Kuwaiti"
        ],
        "adjectival": [
            "Kuwaitis"
        ],
        "nationality": "Kuwaiti",
        "relevance": None
    },
    {
        "id": "568",
        "name": "Kyrgyzstan",
        "denonym": [
            "Kyrgyzstani",
            "Kyrgyz",
            "Kirgiz",
            "Kirghiz"
        ],
        "adjectival": [
            "Kyrgyzstani",
            "Kyrgyz",
            "Kirgiz",
            "Kirghiz"
        ],
        "nationality": "Kyrgyzstani",
        "relevance": None
    },
    {
        "id": "569",
        "name": "Laos",
        "denonym": [
            "Lao",
            "Laotian"
        ],
        "adjectival": [
            "Lao",
            "Laotian"
        ],
        "nationality": "Lao",
        "relevance": None
    },
    {
        "id": "570",
        "name": "Latvia",
        "denonym": [
            "Latvian",
            "Lettish"
        ],
        "adjectival": [
            "Latvian",
            "Lett"
        ],
        "nationality": "Latvian",
        "relevance": None
    },
    {
        "id": "571",
        "name": "Lebanon",
        "denonym": [
            "Lebanese"
        ],
        "adjectival": [
            "Lebanese"
        ],
        "nationality": "Lebanese",
        "relevance": None
    },
    {
        "id": "572",
        "name": "Lesotho",
        "denonym": [
            "Basotho"
        ],
        "adjectival": [
            "Basotho",
            "Mosotho"
        ],
        "nationality": "Basotho",
        "relevance": None
    },
    {
        "id": "573",
        "name": "Liberia",
        "denonym": [
            "Liberian"
        ],
        "adjectival": [
            "Liberian"
        ],
        "nationality": "Liberian",
        "relevance": None
    },
    {
        "id": "574",
        "name": "Libya",
        "denonym": [
            "Libyan"
        ],
        "adjectival": [
            "Libyan"
        ],
        "nationality": "Libyan",
        "relevance": None
    },
    {
        "id": "575",
        "name": "Liechtenstein",
        "denonym": [
            "Liechtensteiner"
        ],
        "adjectival": [
            "Liechtensteiner"
        ],
        "nationality": "Liechtensteiner",
        "relevance": None
    },
    {
        "id": "576",
        "name": "Lithuania",
        "denonym": [
            "Lithuanian"
        ],
        "adjectival": [
            "Lithuanian"
        ],
        "nationality": "Lithuanian",
        "relevance": None
    },
    {
        "id": "577",
        "name": "Luxembourg",
        "denonym": [
            "Luxembourg",
            "Luxembourgish"
        ],
        "adjectival": [
            "Luxembourger"
        ],
        "nationality": "Luxembourg",
        "relevance": None
    },
    {
        "id": "547",
        "name": "India",
        "denonym": [
            "Indian"
        ],
        "adjectival": [
            "Indian"
        ],
        "nationality": "Indian",
        "relevance": "2"
    },
    {
        "id": "578",
        "name": "Macau",
        "denonym": [
            "Macanese",
            "Chinese"
        ],
        "adjectival": [
            "Macanese",
            "Chinese"
        ],
        "nationality": "Macanese",
        "relevance": None
    },
    {
        "id": "579",
        "name": "Republic of North Macedonia",
        "denonym": [
            "Macedonian"
        ],
        "adjectival": [
            "Macedonian"
        ],
        "nationality": "Macedonian",
        "relevance": None
    },
    {
        "id": "580",
        "name": "Madagascar",
        "denonym": [
            "Malagasy"
        ],
        "adjectival": [
            "Malagasy"
        ],
        "nationality": "Malagasy",
        "relevance": None
    },
    {
        "id": "581",
        "name": "Malawi",
        "denonym": [
            "Malawian"
        ],
        "adjectival": [
            "Malawian"
        ],
        "nationality": "Malawian",
        "relevance": None
    },
    {
        "id": "582",
        "name": "Malaysia",
        "denonym": [
            "Malaysian"
        ],
        "adjectival": [
            "Malaysian"
        ],
        "nationality": "Malaysian",
        "relevance": None
    },
    {
        "id": "584",
        "name": "Mali",
        "denonym": [
            "Malian",
            "Malinese"
        ],
        "adjectival": [
            "Malian"
        ],
        "nationality": "Malian",
        "relevance": None
    },
    {
        "id": "585",
        "name": "Malta",
        "denonym": [
            "Maltese"
        ],
        "adjectival": [
            "Maltese"
        ],
        "nationality": "Maltese",
        "relevance": None
    },
    {
        "id": "586",
        "name": "Marshall Islands",
        "denonym": [
            "Marshallese"
        ],
        "adjectival": [
            "Marshallese"
        ],
        "nationality": "Marshallese",
        "relevance": None
    },
    {
        "id": "587",
        "name": "Martinique",
        "denonym": [
            "Martiniquais",
            "Martinican"
        ],
        "adjectival": [
            "Martiniquais/Martiniquaise"
        ],
        "nationality": "Martiniquais",
        "relevance": None
    },
    {
        "id": "588",
        "name": "Mauritania",
        "denonym": [
            "Mauritanian"
        ],
        "adjectival": [
            "Mauritanian"
        ],
        "nationality": "Mauritanian",
        "relevance": None
    },
    {
        "id": "589",
        "name": "Mauritius",
        "denonym": [
            "Mauritian"
        ],
        "adjectival": [
            "Mauritian"
        ],
        "nationality": "Mauritian",
        "relevance": None
    },
    {
        "id": "590",
        "name": "Mayotte",
        "denonym": [
            "Mahoran"
        ],
        "adjectival": [
            "Mahoran"
        ],
        "nationality": "Mahoran",
        "relevance": None
    },
    {
        "id": "591",
        "name": "Mexico",
        "denonym": [
            "Mexican"
        ],
        "adjectival": [
            "Mexican"
        ],
        "nationality": "Mexican",
        "relevance": None
    },
    {
        "id": "592",
        "name": "Federated States of Micronesia",
        "denonym": [
            "Micronesian"
        ],
        "adjectival": [
            "Micronesian"
        ],
        "nationality": "Micronesian",
        "relevance": None
    },
    {
        "id": "593",
        "name": "Moldova",
        "denonym": [
            "Moldovan"
        ],
        "adjectival": [
            "Moldovan"
        ],
        "nationality": "Moldovan",
        "relevance": None
    },
    {
        "id": "594",
        "name": "Monaco",
        "denonym": [
            "Monégasque",
            "Monacan"
        ],
        "adjectival": [
            "Monégasque",
            "Monacan"
        ],
        "nationality": "Monégasque",
        "relevance": None
    },
    {
        "id": "595",
        "name": "Mongolia",
        "denonym": [
            "Mongolian"
        ],
        "adjectival": [
            "Mongolian",
            "Mongol"
        ],
        "nationality": "Mongolian",
        "relevance": None
    },
    {
        "id": "596",
        "name": "Montenegro",
        "denonym": [
            "Montenegrin"
        ],
        "adjectival": [
            "Montenegrin"
        ],
        "nationality": "Montenegrin",
        "relevance": None
    },
    {
        "id": "597",
        "name": "Montserrat",
        "denonym": [
            "Montserratian"
        ],
        "adjectival": [
            "Montserratian"
        ],
        "nationality": "Montserratian",
        "relevance": None
    },
    {
        "id": "598",
        "name": "Morocco",
        "denonym": [
            "Moroccan"
        ],
        "adjectival": [
            "Moroccan"
        ],
        "nationality": "Moroccan",
        "relevance": None
    },
    {
        "id": "599",
        "name": "Mozambique",
        "denonym": [
            "Mozambican"
        ],
        "adjectival": [
            "Mozambican"
        ],
        "nationality": "Mozambican",
        "relevance": None
    },
    {
        "id": "600",
        "name": "Myanmar",
        "denonym": [
            "Burmese"
        ],
        "adjectival": [
            "Burmese",
            "Bamar"
        ],
        "nationality": "Burmese",
        "relevance": None
    },
    {
        "id": "601",
        "name": "Namibia",
        "denonym": [
            "Namibian"
        ],
        "adjectival": [
            "Namibian"
        ],
        "nationality": "Namibian",
        "relevance": None
    },
    {
        "id": "602",
        "name": "Nauru",
        "denonym": [
            "Nauruan"
        ],
        "adjectival": [
            "Nauruan"
        ],
        "nationality": "Nauruan",
        "relevance": None
    },
    {
        "id": "604",
        "name": "Netherlands",
        "denonym": [
            "Dutch",
            "Netherlandic"
        ],
        "adjectival": [
            "Dutch",
            "Netherlander"
        ],
        "nationality": "Dutch",
        "relevance": None
    },
    {
        "id": "605",
        "name": "New Caledonia",
        "denonym": [
            "New Caledonian"
        ],
        "adjectival": [
            "New Caledonian"
        ],
        "nationality": "New Caledonian",
        "relevance": None
    },
    {
        "id": "606",
        "name": "New Zealand",
        "denonym": [
            "New Zealand"
        ],
        "adjectival": [
            "New Zealander"
        ],
        "nationality": "New Zealand",
        "relevance": None
    },
    {
        "id": "607",
        "name": "Nicaragua",
        "denonym": [
            "Nicaraguan"
        ],
        "adjectival": [
            "Nicaraguan"
        ],
        "nationality": "Nicaraguan",
        "relevance": None
    },
    {
        "id": "608",
        "name": "Niger",
        "denonym": [
            "Nigerien"
        ],
        "adjectival": [
            "Nigerien"
        ],
        "nationality": "Nigerien",
        "relevance": None
    },
    {
        "id": "609",
        "name": "Nigeria",
        "denonym": [
            "Nigerian"
        ],
        "adjectival": [
            "Nigerian"
        ],
        "nationality": "Nigerian",
        "relevance": None
    },
    {
        "id": "610",
        "name": "Niue",
        "denonym": [
            "Niuean"
        ],
        "adjectival": [
            "Niuean"
        ],
        "nationality": "Niuean",
        "relevance": None
    },
    {
        "id": "611",
        "name": "Norfolk Island",
        "denonym": [
            "Norfolk Island"
        ],
        "adjectival": [
            "Norfolk Islander"
        ],
        "nationality": "Norfolk Island",
        "relevance": None
    },
    {
        "id": "612",
        "name": "Northern Ireland",
        "denonym": [
            "Northern Irish",
            "British"
        ],
        "adjectival": [
            "Northern Irish",
            "British"
        ],
        "nationality": "Northern Irish",
        "relevance": None
    },
    {
        "id": "613",
        "name": "Northern Mariana Islands",
        "denonym": [
            "Northern Marianan"
        ],
        "adjectival": [
            "Northern Marianan"
        ],
        "nationality": "Northern Marianan",
        "relevance": None
    },
    {
        "id": "614",
        "name": "Norway",
        "denonym": [
            "Norwegian"
        ],
        "adjectival": [
            "Norwegian"
        ],
        "nationality": "Norwegian",
        "relevance": None
    },
    {
        "id": "615",
        "name": "Oman",
        "denonym": [
            "Omani"
        ],
        "adjectival": [
            "Omani"
        ],
        "nationality": "Omani",
        "relevance": None
    },
    {
        "id": "617",
        "name": "Palau",
        "denonym": [
            "Palauan"
        ],
        "adjectival": [
            "Palauan"
        ],
        "nationality": "Palauan",
        "relevance": None
    },
    {
        "id": "618",
        "name": "Palestine",
        "denonym": [
            "Palestinian"
        ],
        "adjectival": [
            "Palestinian"
        ],
        "nationality": "Palestinian",
        "relevance": None
    },
    {
        "id": "619",
        "name": "Panama",
        "denonym": [
            "Panamanian"
        ],
        "adjectival": [
            "Panamanian"
        ],
        "nationality": "Panamanian",
        "relevance": None
    },
    {
        "id": "620",
        "name": "Papua New Guinea",
        "denonym": [
            "Papua New Guinean",
            "Papuan"
        ],
        "adjectival": [
            "Papua New Guinean",
            "Papuan"
        ],
        "nationality": "Papua New Guinean",
        "relevance": None
    },
    {
        "id": "621",
        "name": "Paraguay",
        "denonym": [
            "Paraguayan"
        ],
        "adjectival": [
            "Paraguayan"
        ],
        "nationality": "Paraguayan",
        "relevance": None
    },
    {
        "id": "622",
        "name": "Peru",
        "denonym": [
            "Peruvian"
        ],
        "adjectival": [
            "Peruvian"
        ],
        "nationality": "Peruvian",
        "relevance": None
    },
    {
        "id": "623",
        "name": "Philippines",
        "denonym": [
            "Filipino",
            "Philippine"
        ],
        "adjectival": [
            "Filipino",
            "Filipina"
        ],
        "nationality": "Filipino",
        "relevance": None
    },
    {
        "id": "624",
        "name": "Pitcairn Islands",
        "denonym": [
            "Pitcairn Island"
        ],
        "adjectival": [
            "Pitcairn Islander"
        ],
        "nationality": "Pitcairn Island",
        "relevance": None
    },
    {
        "id": "625",
        "name": "Poland",
        "denonym": [
            "Polish"
        ],
        "adjectival": [
            "Pole"
        ],
        "nationality": "Polish",
        "relevance": None
    },
    {
        "id": "626",
        "name": "Portugal",
        "denonym": [
            "Portuguese"
        ],
        "adjectival": [
            "Portuguese"
        ],
        "nationality": "Portuguese",
        "relevance": None
    },
    {
        "id": "627",
        "name": "Puerto Rico",
        "denonym": [
            "Puerto Rican"
        ],
        "adjectival": [
            "Puerto Rican"
        ],
        "nationality": "Puerto Rican",
        "relevance": None
    },
    {
        "id": "628",
        "name": "Qatar",
        "denonym": [
            "Qatari"
        ],
        "adjectival": [
            "Qatari"
        ],
        "nationality": "Qatari",
        "relevance": None
    },
    {
        "id": "629",
        "name": "Réunion",
        "denonym": [
            "Réunionese",
            "Réunionnais"
        ],
        "adjectival": [
            "Réunionese",
            "Réunionnais/Réunionnaise"
        ],
        "nationality": "Réunionese",
        "relevance": None
    },
    {
        "id": "630",
        "name": "Romania",
        "denonym": [
            "Romanian"
        ],
        "adjectival": [
            "Romanian"
        ],
        "nationality": "Romanian",
        "relevance": None
    },
    {
        "id": "631",
        "name": "Russia",
        "denonym": [
            "Russian"
        ],
        "adjectival": [
            "Russian"
        ],
        "nationality": "Russian",
        "relevance": None
    },
    {
        "id": "632",
        "name": "Rwanda",
        "denonym": [
            "Rwandan"
        ],
        "adjectival": [
            "Rwandan",
            "Banyarwanda"
        ],
        "nationality": "Rwandan",
        "relevance": None
    },
    {
        "id": "633",
        "name": "Saba",
        "denonym": [
            "Saba"
        ],
        "adjectival": [
            "Saba Dutch"
        ],
        "nationality": "Saba",
        "relevance": None
    },
    {
        "id": "634",
        "name": "Saint Barthélemy",
        "denonym": [
            "Barthélemois"
        ],
        "adjectival": [
            "Barthélemois/Barthélemoise"
        ],
        "nationality": "Barthélemois",
        "relevance": None
    },
    {
        "id": "635",
        "name": "Saint Helena, Ascension and Tristan da Cunha}",
        "denonym": [
            "Saint Helenian"
        ],
        "adjectival": [
            "Saint Helenian"
        ],
        "nationality": "Saint Helenian",
        "relevance": None
    },
    {
        "id": "636",
        "name": "Saint Kitts and Nevis",
        "denonym": [
            "Kittitian or Nevisian"
        ],
        "adjectival": [
            "Kittitians or Nevisian"
        ],
        "nationality": "Kittitian or Nevisian",
        "relevance": None
    },
    {
        "id": "637",
        "name": "Saint Lucia",
        "denonym": [
            "Saint Lucian"
        ],
        "adjectival": [
            "Saint Lucian"
        ],
        "nationality": "Saint Lucian",
        "relevance": None
    },
    {
        "id": "638",
        "name": "Saint Martin",
        "denonym": [
            "Saint-Martinoise"
        ],
        "adjectival": [
            "Saint-Martinois/Saint-Martinoise"
        ],
        "nationality": "Saint-Martinoise",
        "relevance": None
    },
    {
        "id": "639",
        "name": "Saint Pierre and Miquelon",
        "denonym": [
            "Saint-Pierrais or Miquelonnais"
        ],
        "adjectival": [
            "Saint-Pierrais/Saint-Pierraises or Miquelonnais/Miquelonnaise"
        ],
        "nationality": "Saint-Pierrais or Miquelonnais",
        "relevance": None
    },
    {
        "id": "640",
        "name": "Saint Vincent and the Grenadines",
        "denonym": [
            "Saint Vincentian",
            "Vincentian"
        ],
        "adjectival": [
            "Saint Vincentian",
            "Vincentian"
        ],
        "nationality": "Saint Vincentian",
        "relevance": None
    },
    {
        "id": "641",
        "name": "Samoa",
        "denonym": [
            "Samoan"
        ],
        "adjectival": [
            "Samoan"
        ],
        "nationality": "Samoan",
        "relevance": None
    },
    {
        "id": "642",
        "name": "San Marino",
        "denonym": [
            "Sammarinese"
        ],
        "adjectival": [
            "Sammarinese"
        ],
        "nationality": "Sammarinese",
        "relevance": None
    },
    {
        "id": "616",
        "name": "Pakistan",
        "denonym": [
            "Pakistani"
        ],
        "adjectival": [
            "Pakistani"
        ],
        "nationality": "Pakistani",
        "relevance": "5"
    },
    {
        "id": "583",
        "name": "Maldives",
        "denonym": [
            "Maldivian"
        ],
        "adjectival": [
            "Maldivian"
        ],
        "nationality": "Maldivian",
        "relevance": "6"
    },
    {
        "id": "643",
        "name": "São Tomé and Príncipe",
        "denonym": [
            "São Toméan"
        ],
        "adjectival": [
            "São Toméan"
        ],
        "nationality": "São Toméan",
        "relevance": None
    },
    {
        "id": "644",
        "name": "Saudi Arabia",
        "denonym": [
            "Saudi",
            "Saudi Arabian"
        ],
        "adjectival": [
            "Saudis",
            "Saudi Arabian"
        ],
        "nationality": "Saudi",
        "relevance": None
    },
    {
        "id": "645",
        "name": "Scotland",
        "denonym": [
            "Scottish",
            "British"
        ],
        "adjectival": [
            "Scot"
        ],
        "nationality": "Scottish",
        "relevance": None
    },
    {
        "id": "646",
        "name": "Senegal",
        "denonym": [
            "Senegalese"
        ],
        "adjectival": [
            "Senegalese"
        ],
        "nationality": "Senegalese",
        "relevance": None
    },
    {
        "id": "647",
        "name": "Serbia",
        "denonym": [
            "Serbian"
        ],
        "adjectival": [
            "Serb",
            "Serbian"
        ],
        "nationality": "Serbian",
        "relevance": None
    },
    {
        "id": "648",
        "name": "Seychelles",
        "denonym": [
            "Seychellois"
        ],
        "adjectival": [
            "Seychellois/Seychelloise"
        ],
        "nationality": "Seychellois",
        "relevance": None
    },
    {
        "id": "649",
        "name": "Sierra Leone",
        "denonym": [
            "Sierra Leonean"
        ],
        "adjectival": [
            "Sierra Leonean"
        ],
        "nationality": "Sierra Leonean",
        "relevance": None
    },
    {
        "id": "650",
        "name": "Singapore",
        "denonym": [
            "Singapore",
            "Singaporean"
        ],
        "adjectival": [
            "Singaporean"
        ],
        "nationality": "Singapore",
        "relevance": None
    },
    {
        "id": "651",
        "name": "Sint Eustatius",
        "denonym": [
            "Sint Eustatius",
            "Statian"
        ],
        "adjectival": [
            "Statian"
        ],
        "nationality": "Sint Eustatius",
        "relevance": None
    },
    {
        "id": "652",
        "name": "Sint Maarten",
        "denonym": [
            "Sint Maarten"
        ],
        "adjectival": [
            "Sint Maartener"
        ],
        "nationality": "Sint Maarten",
        "relevance": None
    },
    {
        "id": "653",
        "name": "Slovakia",
        "denonym": [
            "Slovak"
        ],
        "adjectival": [
            "Slovak",
            "Slovakian"
        ],
        "nationality": "Slovak",
        "relevance": None
    },
    {
        "id": "654",
        "name": "Slovenia",
        "denonym": [
            "Slovenian",
            "Slovene"
        ],
        "adjectival": [
            "Slovene",
            "Slovenian"
        ],
        "nationality": "Slovenian",
        "relevance": None
    },
    {
        "id": "655",
        "name": "Solomon Islands",
        "denonym": [
            "Solomon Island"
        ],
        "adjectival": [
            "Solomon Islander"
        ],
        "nationality": "Solomon Island",
        "relevance": None
    },
    {
        "id": "656",
        "name": "Somalia",
        "denonym": [
            "Somali"
        ],
        "adjectival": [
            "Somali"
        ],
        "nationality": "Somali",
        "relevance": None
    },
    {
        "id": "657",
        "name": "Somaliland",
        "denonym": [
            "Somalilander"
        ],
        "adjectival": [
            "Somalilander"
        ],
        "nationality": "Somalilander",
        "relevance": None
    },
    {
        "id": "658",
        "name": "South Africa",
        "denonym": [
            "South African"
        ],
        "adjectival": [
            "South African"
        ],
        "nationality": "South African",
        "relevance": None
    },
    {
        "id": "659",
        "name": "South Georgia and the South Sandwich Islands",
        "denonym": [
            "South Georgia or South Sandwich Islands"
        ],
        "adjectival": [
            ""
        ],
        "nationality": "South Georgia or South Sandwich Islands",
        "relevance": None
    },
    {
        "id": "660",
        "name": "South Ossetia",
        "denonym": [
            "South Ossetian"
        ],
        "adjectival": [
            "South Ossetian"
        ],
        "nationality": "South Ossetian",
        "relevance": None
    },
    {
        "id": "661",
        "name": "South Sudan",
        "denonym": [
            "South Sudanese"
        ],
        "adjectival": [
            "South Sudanese"
        ],
        "nationality": "South Sudanese",
        "relevance": None
    },
    {
        "id": "662",
        "name": "Spain",
        "denonym": [
            "Spanish"
        ],
        "adjectival": [
            "Spaniard"
        ],
        "nationality": "Spanish",
        "relevance": None
    },
    {
        "id": "664",
        "name": "Sudan",
        "denonym": [
            "Sudanese"
        ],
        "adjectival": [
            "Sudanese"
        ],
        "nationality": "Sudanese",
        "relevance": None
    },
    {
        "id": "665",
        "name": "Suriname",
        "denonym": [
            "Surinamese"
        ],
        "adjectival": [
            "Surinamer"
        ],
        "nationality": "Surinamese",
        "relevance": None
    },
    {
        "id": "666",
        "name": "Svalbard",
        "denonym": [
            "Svalbard"
        ],
        "adjectival": [
            ""
        ],
        "nationality": "Svalbard",
        "relevance": None
    },
    {
        "id": "668",
        "name": "Sweden",
        "denonym": [
            "Swedish"
        ],
        "adjectival": [
            "Swede"
        ],
        "nationality": "Swedish",
        "relevance": None
    },
    {
        "id": "669",
        "name": "Switzerland",
        "denonym": [
            "Swiss"
        ],
        "adjectival": [
            "Swiss"
        ],
        "nationality": "Swiss",
        "relevance": None
    },
    {
        "id": "670",
        "name": "Syria",
        "denonym": [
            "Syrian"
        ],
        "adjectival": [
            "Syrian"
        ],
        "nationality": "Syrian",
        "relevance": None
    },
    {
        "id": "671",
        "name": "Taiwan",
        "denonym": [
            "Taiwanese"
        ],
        "adjectival": [
            "Taiwanese"
        ],
        "nationality": "Taiwanese",
        "relevance": None
    },
    {
        "id": "672",
        "name": "Tajikistan",
        "denonym": [
            "Tajikistani"
        ],
        "adjectival": [
            "Tajikistani",
            "Tajik"
        ],
        "nationality": "Tajikistani",
        "relevance": None
    },
    {
        "id": "673",
        "name": "Tanzania",
        "denonym": [
            "Tanzanian"
        ],
        "adjectival": [
            "Tanzanian"
        ],
        "nationality": "Tanzanian",
        "relevance": None
    },
    {
        "id": "674",
        "name": "Thailand",
        "denonym": [
            "Thai"
        ],
        "adjectival": [
            "Thai"
        ],
        "nationality": "Thai",
        "relevance": None
    },
    {
        "id": "675",
        "name": "Timor-Leste",
        "denonym": [
            "Timorese"
        ],
        "adjectival": [
            "Timorese"
        ],
        "nationality": "Timorese",
        "relevance": None
    },
    {
        "id": "676",
        "name": "Togo",
        "denonym": [
            "Togolese"
        ],
        "adjectival": [
            "Togolese"
        ],
        "nationality": "Togolese",
        "relevance": None
    },
    {
        "id": "677",
        "name": "Tokelau",
        "denonym": [
            "Tokelauan"
        ],
        "adjectival": [
            "Tokelauan"
        ],
        "nationality": "Tokelauan",
        "relevance": None
    },
    {
        "id": "678",
        "name": "Tonga",
        "denonym": [
            "Tongan"
        ],
        "adjectival": [
            "Tongan"
        ],
        "nationality": "Tongan",
        "relevance": None
    },
    {
        "id": "679",
        "name": "Trinidad and Tobago",
        "denonym": [
            "Trinidadian or Tobagonian"
        ],
        "adjectival": [
            "Trinidadian or Tobagonian"
        ],
        "nationality": "Trinidadian or Tobagonian",
        "relevance": None
    },
    {
        "id": "680",
        "name": "Tunisia",
        "denonym": [
            "Tunisian"
        ],
        "adjectival": [
            "Tunisian"
        ],
        "nationality": "Tunisian",
        "relevance": None
    },
    {
        "id": "681",
        "name": "Turkey",
        "denonym": [
            "Turkish"
        ],
        "adjectival": [
            "Turk"
        ],
        "nationality": "Turkish",
        "relevance": None
    },
    {
        "id": "682",
        "name": "Turkmenistan",
        "denonym": [
            "Turkmen"
        ],
        "adjectival": [
            "Turkmen"
        ],
        "nationality": "Turkmen",
        "relevance": None
    },
    {
        "id": "683",
        "name": "Turks and Caicos Islands",
        "denonym": [
            "Turks and Caicos Island"
        ],
        "adjectival": [
            "Turk and Caicos Islander"
        ],
        "nationality": "Turks and Caicos Island",
        "relevance": None
    },
    {
        "id": "684",
        "name": "Tuvalu",
        "denonym": [
            "Tuvaluan"
        ],
        "adjectival": [
            "Tuvaluan"
        ],
        "nationality": "Tuvaluan",
        "relevance": None
    },
    {
        "id": "685",
        "name": "Uganda",
        "denonym": [
            "Ugandan"
        ],
        "adjectival": [
            "Ugandan"
        ],
        "nationality": "Ugandan",
        "relevance": None
    },
    {
        "id": "686",
        "name": "Ukraine",
        "denonym": [
            "Ukrainian"
        ],
        "adjectival": [
            "Ukrainian"
        ],
        "nationality": "Ukrainian",
        "relevance": None
    },
    {
        "id": "687",
        "name": "United Arab Emirates",
        "denonym": [
            "Emirati",
            "Emirian",
            "Emiri"
        ],
        "adjectival": [
            "Emirati",
            "Emirian",
            "Emiri"
        ],
        "nationality": "Emirati",
        "relevance": None
    },
    {
        "id": "688",
        "name": "United Kingdom of Great Britain and Northern Ireland",
        "denonym": [
            "British",
            "UK"
        ],
        "adjectival": [
            "Briton",
            "British",
            "English"
        ],
        "nationality": "British",
        "relevance": None
    },
    {
        "id": "689",
        "name": "United States of America",
        "denonym": [
            "United States",
            "U.S.",
            "American"
        ],
        "adjectival": [
            "American"
        ],
        "nationality": "United States",
        "relevance": None
    },
    {
        "id": "690",
        "name": "Uruguay",
        "denonym": [
            "Uruguayan"
        ],
        "adjectival": [
            "Uruguayan"
        ],
        "nationality": "Uruguayan",
        "relevance": None
    },
    {
        "id": "691",
        "name": "Uzbekistan",
        "denonym": [
            "Uzbekistani",
            "Uzbek"
        ],
        "adjectival": [
            "Uzbekistani",
            "Uzbek"
        ],
        "nationality": "Uzbekistani",
        "relevance": None
    },
    {
        "id": "692",
        "name": "Vanuatu",
        "denonym": [
            "Ni-Vanuatu",
            "Vanuatuan"
        ],
        "adjectival": [
            "Ni-Vanuatu"
        ],
        "nationality": "Ni-Vanuatu",
        "relevance": None
    },
    {
        "id": "693",
        "name": "Vatican City State",
        "denonym": [
            "Vatican"
        ],
        "adjectival": [
            "Vatican citizen"
        ],
        "nationality": "Vatican",
        "relevance": None
    },
    {
        "id": "694",
        "name": "Venezuela",
        "denonym": [
            "Venezuelan"
        ],
        "adjectival": [
            "Venezuelan"
        ],
        "nationality": "Venezuelan",
        "relevance": None
    },
    {
        "id": "695",
        "name": "Vietnam",
        "denonym": [
            "Vietnamese"
        ],
        "adjectival": [
            "Vietnamese"
        ],
        "nationality": "Vietnamese",
        "relevance": None
    },
    {
        "id": "696",
        "name": "British Virgin Islands",
        "denonym": [
            "British Virgin Island"
        ],
        "adjectival": [
            "British Virgin Islander"
        ],
        "nationality": "British Virgin Island",
        "relevance": None
    },
    {
        "id": "697",
        "name": "U.S. Virgin Islands",
        "denonym": [
            "U.S. Virgin Island"
        ],
        "adjectival": [
            "U.S. Virgin Islander"
        ],
        "nationality": "U.S. Virgin Island",
        "relevance": None
    },
    {
        "id": "698",
        "name": "Wallis and Futuna",
        "denonym": [
            "Wallis and Futuna",
            "Wallisian or Futunan"
        ],
        "adjectival": [
            "Wallis and Futuna Islanders",
            "Wallisian or Futunan"
        ],
        "nationality": "Wallis and Futuna",
        "relevance": None
    },
    {
        "id": "699",
        "name": "Western Sahara",
        "denonym": [
            "Sahrawi",
            "Sahrawian",
            "Sahraouian"
        ],
        "adjectival": [
            "Sahrawi",
            "Sahraoui"
        ],
        "nationality": "Sahrawi",
        "relevance": None
    },
    {
        "id": "700",
        "name": "Yemen",
        "denonym": [
            "Yemeni"
        ],
        "adjectival": [
            "Yemeni"
        ],
        "nationality": "Yemeni",
        "relevance": None
    },
    {
        "id": "701",
        "name": "Zambia",
        "denonym": [
            "Zambian"
        ],
        "adjectival": [
            "Zambian"
        ],
        "nationality": "Zambian",
        "relevance": None
    },
    {
        "id": "702",
        "name": "Zimbabwe",
        "denonym": [
            "Zimbabwean"
        ],
        "adjectival": [
            "Zimbabwean"
        ],
        "nationality": "Zimbabwean",
        "relevance": None
    },
    {
        "id": "603",
        "name": "Nepal",
        "denonym": [
            "Nepali",
            "Nepalese"
        ],
        "adjectival": [
            "Nepali",
            "Nepalese"
        ],
        "nationality": "Nepali",
        "relevance": "1"
    },
    {
        "id": "549",
        "name": "Iran",
        "denonym": [
            "Iranian",
            "Persian"
        ],
        "adjectival": [
            "Iranian",
            "Persian"
        ],
        "nationality": "Iranian",
        "relevance": None
    },
    {
        "id": "461",
        "name": "Bangladesh",
        "denonym": [
            "Bangladeshi"
        ],
        "adjectival": [
            "Bangladeshi"
        ],
        "nationality": "Bangladeshi",
        "relevance": "3"
    },
    {
        "id": "663",
        "name": "Sri Lanka",
        "denonym": [
            "Sri Lankan"
        ],
        "adjectival": [
            "Sri Lankan"
        ],
        "nationality": "Sri Lankan",
        "relevance": "6"
    }
]

PROVINCES = [
    {"id": 2, "name": "Province No. 2", "name_ne": "", "alternative_names": [], "alternative_names_ne": []},
    {"id": 3, "name": "Province No. 3", "name_ne": "", "alternative_names": [], "alternative_names_ne": []},
    {"id": 4, "name": "Gandaki Pradesh", "name_ne": "", "alternative_names": [], "alternative_names_ne": []},
    {"id": 5, "name": "Province No. 5", "name_ne": "", "alternative_names": [], "alternative_names_ne": []},
    {"id": 7, "name": "Sudurpashchim Pradesh", "name_ne": "", "alternative_names": [], "alternative_names_ne": []},
    {"id": 6, "name": "Karnali", "name_ne": "", "alternative_names": [], "alternative_names_ne": []},
    {"id": 1, "name": "Province No. 1", "name_ne": "", "alternative_names": [], "alternative_names_ne": []},

]

DISTRICTS = [
    {"id": 52, "province_id": 5, "name": "KAPILVASTU", "alternative_names": ["KAPILBASTU"]},
    {"id": 53, "province_id": 5, "name": "PARASI", "alternative_names": ["NAWALPARASI (BARDAGHAT WEST)"]},
    {"id": 43, "province_id": 4, "name": "NAWALPUR", "alternative_names": ["NAWALPARASI (BARDAGHAT EAST)"]},
    {"id": 3, "province_id": 1, "name": "ILAM", "alternative_names": ["ILLAM"]},
    {"id": 1, "province_id": 1, "name": "BHOJPUR"},
    {"id": 2, "province_id": 1, "name": "DHANKUTA"},
    {"id": 4, "province_id": 1, "name": "JHAPA"},
    {"id": 5, "province_id": 1, "name": "KHOTANG"},
    {"id": 6, "province_id": 1, "name": "MORANG"},
    {"id": 7, "province_id": 1, "name": "OKHALDHUNGA"},
    {"id": 8, "province_id": 1, "name": "PANCHTHAR"},
    {"id": 9, "province_id": 1, "name": "SANKHUWASABHA"},
    {"id": 10, "province_id": 1, "name": "SOLUKHUMBU"},
    {"id": 11, "province_id": 1, "name": "SUNSARI"},
    {"id": 12, "province_id": 1, "name": "TAPLEJUNG"},
    {"id": 14, "province_id": 1, "name": "UDAYAPUR"},
    {"id": 15, "province_id": 2, "name": "BARA"},
    {"id": 17, "province_id": 2, "name": "MAHOTTARI"},
    {"id": 18, "province_id": 2, "name": "PARSA"},
    {"id": 19, "province_id": 2, "name": "RAUTAHAT"},
    {"id": 20, "province_id": 2, "name": "SAPTARI"},
    {"id": 21, "province_id": 2, "name": "SARLAHI"},
    {"id": 22, "province_id": 2, "name": "SIRAHA"},
    {"id": 24, "province_id": 3, "name": "CHITWAN"},
    {"id": 25, "province_id": 3, "name": "DHADING"},
    {"id": 26, "province_id": 3, "name": "DOLAKHA"},
    {"id": 27, "province_id": 3, "name": "KATHMANDU"},
    {"id": 29, "province_id": 3, "name": "LALITPUR"},
    {"id": 31, "province_id": 3, "name": "NUWAKOT"},
    {"id": 32, "province_id": 3, "name": "RAMECHHAP"},
    {"id": 33, "province_id": 3, "name": "RASUWA"},
    {"id": 34, "province_id": 3, "name": "SINDHULI"},
    {"id": 36, "province_id": 4, "name": "BAGLUNG"},
    {"id": 37, "province_id": 4, "name": "GORKHA"},
    {"id": 38, "province_id": 4, "name": "KASKI"},
    {"id": 39, "province_id": 4, "name": "LAMJUNG"},
    {"id": 40, "province_id": 4, "name": "MANANG"},
    {"id": 41, "province_id": 4, "name": "MUSTANG"},
    {"id": 42, "province_id": 4, "name": "MYAGDI"},
    {"id": 44, "province_id": 4, "name": "PARBAT"},
    {"id": 45, "province_id": 4, "name": "SYANGJA"},
    {"id": 46, "province_id": 4, "name": "TANAHUN"},
    {"id": 47, "province_id": 5, "name": "ARGHAKHANCHI"},
    {"id": 48, "province_id": 5, "name": "BANKE"},
    {"id": 49, "province_id": 5, "name": "BARDIYA"},
    {"id": 50, "province_id": 5, "name": "DANG"},
    {"id": 51, "province_id": 5, "name": "GULMI"},
    {"id": 54, "province_id": 5, "name": "PALPA"},
    {"id": 55, "province_id": 5, "name": "PYUTHAN"},
    {"id": 56, "province_id": 5, "name": "ROLPA"},
    {"id": 57, "province_id": 5, "name": "RUPANDEHI"},
    {"id": 58, "province_id": 6, "name": "DAILEKH"},
    {"id": 59, "province_id": 6, "name": "DOLPA"},
    {"id": 60, "province_id": 6, "name": "HUMLA"},
    {"id": 61, "province_id": 6, "name": "JAJARKOT"},
    {"id": 62, "province_id": 6, "name": "JUMLA"},
    {"id": 63, "province_id": 6, "name": "KALIKOT"},
    {"id": 64, "province_id": 6, "name": "MUGU"},
    {"id": 66, "province_id": 6, "name": "SALYAN"},
    {"id": 67, "province_id": 6, "name": "SURKHET"},
    {"id": 68, "province_id": 7, "name": "ACHHAM"},
    {"id": 69, "province_id": 7, "name": "BAITADI"},
    {"id": 70, "province_id": 7, "name": "BAJHANG"},
    {"id": 71, "province_id": 7, "name": "BAJURA"},
    {"id": 72, "province_id": 7, "name": "DADELDHURA"},
    {"id": 73, "province_id": 7, "name": "DARCHULA"},
    {"id": 74, "province_id": 7, "name": "DOTI"},
    {"id": 75, "province_id": 7, "name": "KAILALI"},
    {"id": 76, "province_id": 7, "name": "KANCHANPUR"},
    {"id": 77, "province_id": 5, "name": "EASTERN RUKUM", "alternative_names": ["RUKUM EAST"]},
    {"id": 28, "province_id": 3, "name": "KAVREPALANCHOK", "alternative_names": ["KAVREPALANCHOWK"]},
    {"id": 35, "province_id": 3, "name": "SINDHUPALCHOK", "alternative_names": ["SINDHUPALCHOWK"]},
    {"id": 65, "province_id": 6, "name": "WESTERN RUKUM", "alternative_names": ["RUKUM WEST"]},
    {"id": 30, "province_id": 3, "name": "MAKWANPUR", "alternative_names": ["MAKAWANPUR"]},
    {"id": 23, "province_id": 3, "name": "BHAKTAPUR", "alternative_names": ["BHAKTPUR"]},
    {"id": 13, "province_id": 1, "name": "TERHATHUM", "alternative_names": ["TERATHUM"]},
    {"id": 16, "province_id": 2, "name": "DHANUSHA", "alternative_names": ["DHANUSA"]}

]

CITIES = [
    {"id": "414", "name": "Arjundhara", "name_ne": "\u0905\u0930\u094d\u091c\u0941\u0928\u0927\u093e\u0930\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "4"},
    {"id": "415", "name": "Aurahi", "name_ne": "\u0914\u0930\u0939\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "17"},
    {"id": "418", "name": "Baglung", "name_ne": "\u092c\u093e\u0917\u0932\u0941\u0919 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "36"},
    {"id": "420", "name": "Bahudarmai", "name_ne": "\u092c\u0939\u0941\u0926\u0930\u092e\u093e\u0908 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "18"},
    {"id": "422", "name": "Balawa", "name_ne": "\u092c\u0932\u0935\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "17"},
    {"id": "423", "name": "Banepa", "name_ne": "\u092c\u0928\u0947\u092a\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "28"},
    {"id": "425", "name": "Banganga", "name_ne": "\u092c\u093e\u0923\u0917\u0902\u0917\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "52"},
    {"id": "426", "name": "Bansgadhi", "name_ne": "\u092c\u093e\u0938\u0917\u0922\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "49"},
    {"id": "427", "name": "Barahachhetra",
     "name_ne": "\u092c\u0930\u093e\u0939\u0915\u094d\u0937\u0947\u0924\u094d\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "11"},
    {"id": "428", "name": "Barahathawa", "name_ne": "\u092c\u0930\u0939\u0925\u0935\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "21"},
    {"id": "429", "name": "Barbardiya", "name_ne": "\u092c\u093e\u0930\u092c\u0930\u094d\u0926\u093f\u092f\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "49"},
    {"id": "430", "name": "Bardghat", "name_ne": "\u092c\u0930\u094d\u0926\u0918\u093e\u091f ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "53"},
    {"id": "431", "name": "Bardibas", "name_ne": "\u092c\u0930\u094d\u0926\u093f\u092c\u093e\u0938 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "17"},
    {"id": "433", "name": "Baudhimai", "name_ne": "\u092c\u094c\u0927\u0940\u092e\u093e\u0908 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "19"},
    {"id": "436", "name": "Belauri", "name_ne": "\u092c\u0947\u0932\u094c\u0930\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "76"},
    {"id": "437", "name": "Belbaari", "name_ne": "\u092c\u0947\u0932\u0935\u093e\u0930\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "6"},
    {"id": "441", "name": "Bhadrapur", "name_ne": "\u092d\u0926\u094d\u0930\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "4"},
    {"id": "442", "name": "Bhajani", "name_ne": "\u092d\u091c\u0928\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "75"},
    {"id": "443", "name": "Bhaktapur", "name_ne": "\u092d\u0915\u094d\u0924\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "23"},
    {"id": "444", "name": "Bhangaha", "name_ne": "\u092d\u0901\u0917\u093e\u0939\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "17"},
    {"id": "446", "name": "Bharatpur", "name_ne": "\u092d\u0930\u0924\u092a\u0941\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "24"},
    {"id": "447", "name": "Bheemdatta", "name_ne": "\u092d\u0940\u092e\u0926\u0924\u094d\u0924 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "76"},
    {"id": "455", "name": "Bideha", "name_ne": "\u0935\u093f\u0926\u0947\u0939 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "16"},
    {"id": "456", "name": "Bidur", "name_ne": "\u0935\u093f\u0926\u0941\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "31"},
    {"id": "457", "name": "Biratnagar", "name_ne": "\u0935\u093f\u0930\u093e\u091f\u0928\u0917\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "6"},
    {"id": "458", "name": "Birendranagar",
     "name_ne": "\u092c\u0940\u0930\u0947\u0928\u094d\u0926\u094d\u0930\u0928\u0917\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "67"},
    {"id": "459", "name": "Birgunj", "name_ne": "\u092c\u093f\u0930\u0917\u0902\u091c ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "18"},
    {"id": "460", "name": "Birtamod", "name_ne": "\u0935\u093f\u0930\u094d\u0924\u093e\u092e\u094b\u0921 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "4"},
    {"id": "461", "name": "Bode Barsain", "name_ne": "\u092c\u094b\u0926\u0947\u092c\u0930\u0938\u093e\u0908\u0928 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "20"},
    {"id": "462", "name": "Brindaban", "name_ne": "\u092c\u0943\u0928\u094d\u0926\u093e\u0935\u0928 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "19"},
    {"id": "463", "name": "Buddhabhumi", "name_ne": "\u092c\u0941\u0926\u094d\u0927\u092d\u0942\u092e\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "52"},
    {"id": "464", "name": "Budhanilkantha",
     "name_ne": "\u092c\u0941\u0922\u093e\u0928\u093f\u0932\u0915\u0923\u094d\u0920 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "27"},
    {"id": "468", "name": "Butwal", "name_ne": "\u092c\u0941\u091f\u0935\u0932 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "57"}, {"id": "472", "name": "Chandragiri",
                                                                                    "name_ne": "\u091a\u0928\u094d\u0926\u094d\u0930\u093e\u0917\u093f\u0930\u0940 ",
                                                                                    "alternative_names": [],
                                                                                    "alternative_names_ne": [],
                                                                                    "category": "Municipality",
                                                                                    "district_id": "27"},
    {"id": "473", "name": "Chandrapur", "name_ne": "\u091a\u0928\u094d\u0926\u094d\u0930\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "19"},
    {"id": "474", "name": "Changunarayan",
     "name_ne": "\u091a\u093e\u0901\u0917\u0941\u0928\u093e\u0930\u093e\u092f\u0923 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "23"},
    {"id": "482", "name": "Damak", "name_ne": "\u0926\u092e\u0915 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "4"},
    {"id": "487", "name": "Devdaha", "name_ne": "\u0926\u0947\u0935\u0926\u0939 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "57"},
    {"id": "488", "name": "Dewahi Gonahi",
     "name_ne": "\u0926\u0947\u0935\u093e\u0939\u0940 \u0917\u094b\u0928\u093e\u0939\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "19"},
    {"id": "489", "name": "Dhangadhi", "name_ne": "\u0927\u0928\u0917\u0922\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "75"},
    {"id": "493", "name": "Dharan", "name_ne": "\u0927\u0930\u093e\u0928 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "11"},
    {"id": "411", "name": "Aamargadhi", "name_ne": "\u0905\u092e\u0930\u0917\u0922\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "72"},
    {"id": "509", "name": "Gaur", "name_ne": "\u0917\u094c\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "19"},
    {"id": "591", "name": "Maharajgunj", "name_ne": "\u092e\u0939\u093e\u0930\u093e\u091c\u0917\u0902\u091c ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "52"},
    {"id": "594", "name": "Manara Shisawa", "name_ne": "\u092e\u0928\u0930\u093e \u0936\u093f\u0938\u0935\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "17"},
    {"id": "598", "name": "Matihani", "name_ne": "\u092e\u091f\u093f\u0939\u093e\u0928\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "17"},
    {"id": "599", "name": "Maulapur", "name_ne": "\u092e\u094c\u0932\u093e\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "19"},
    {"id": "600", "name": "Mechinagar", "name_ne": "\u092e\u0947\u091a\u0940 \u0928\u0917\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "4"},
    {"id": "572", "name": "Lalitpur", "name_ne": "\u0932\u0932\u093f\u0924\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "29"},
    {"id": "574", "name": "Lamki Chuha", "name_ne": "\u0932\u092e\u094d\u0915\u0940 \u091a\u0941\u0939\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "75"},
    {"id": "577", "name": "Loharpatti", "name_ne": "\u0932\u094b\u0939\u0930\u092a\u091f\u094d\u091f\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "17"},
    {"id": "578", "name": "Lumbini Sanskritik",
     "name_ne": "\u0932\u0941\u092e\u094d\u092c\u093f\u0928\u0940 \u0938\u093e\u0902\u0938\u094d\u0915\u0943\u0924\u093f\u0915 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "57"},
    {"id": "811", "name": "Mahottari", "name_ne": "\u092e\u0939\u094b\u0924\u094d\u0924\u0930\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "17"},
    {"id": "579", "name": "Madhav Narayan",
     "name_ne": "\u092e\u093e\u0927\u0935 \u0928\u093e\u0930\u093e\u092f\u0923 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "19"},
    {"id": "500", "name": "Dudhauli", "name_ne": "\u0926\u0941\u0927\u094c\u0932\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "34"},
    {"id": "501", "name": "Duhabi", "name_ne": "\u0926\u0941\u0939\u0935\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "11"},
    {"id": "503", "name": "Gadhimai", "name_ne": "\u0917\u0922\u0940\u092e\u093e\u0908 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "19"},
    {"id": "504", "name": "Gaindakot", "name_ne": "\u0917\u0948\u0921\u093e\u0915\u094b\u091f ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "43"},
    {"id": "508", "name": "Garuda", "name_ne": "\u0917\u0930\u0941\u0921\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "19"},
    {"id": "510", "name": "Gauradaha", "name_ne": "\u0917\u094c\u0930\u093e\u0926\u0939 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "4"},
    {"id": "511", "name": "Gauriganga", "name_ne": "\u0917\u094c\u0930\u0940\u0917\u0902\u0917\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "75"},
    {"id": "512", "name": "Gaushala", "name_ne": "\u0917\u094c\u0936\u093e\u0932\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "17"},
    {"id": "513", "name": "Ghodaghodi", "name_ne": "\u0918\u094b\u0921\u093e\u0918\u094b\u0921\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "75"},
    {"id": "514", "name": "Ghorahi", "name_ne": "\u0918\u094b\u0930\u093e\u0939\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "50"},
    {"id": "516", "name": "Godawari", "name_ne": "\u0917\u094b\u0926\u093e\u0935\u0930\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "29"},
    {"id": "517", "name": "Godawari, Seti", "name_ne": "\u0917\u094b\u0926\u093e\u0935\u0930\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "75"},
    {"id": "518", "name": "Gokarneshwor",
     "name_ne": "\u0917\u094b\u0915\u0930\u094d\u0923\u0947\u0936\u094d\u0935\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "27"},
    {"id": "519", "name": "Golbazar", "name_ne": "\u0917\u094b\u0932\u092c\u091c\u093e\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "22"},
    {"id": "521", "name": "Gujara", "name_ne": "\u0917\u0941\u091c\u0930\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "19"},
    {"id": "522", "name": "Gulariya", "name_ne": "\u0917\u0941\u0932\u0930\u093f\u092f\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "49"},
    {"id": "527", "name": "Haripur", "name_ne": "\u0939\u0930\u093f\u092a\u0941\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "21"},
    {"id": "528", "name": "Haripurwa", "name_ne": "\u0939\u0930\u093f\u092a\u0941\u0930\u094d\u0935\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "21"},
    {"id": "530", "name": "Hetauda", "name_ne": "\u0939\u0947\u091f\u094c\u0921\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "30"},
    {"id": "532", "name": "Inaruwa", "name_ne": "\u0908\u0928\u0930\u0941\u0935\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "11"},
    {"id": "533", "name": "Ishnath", "name_ne": "\u0908\u0936\u0928\u093e\u0925 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "19"},
    {"id": "534", "name": "Ishworpur", "name_ne": "\u0908\u0936\u094d\u0935\u0930\u092a\u0942\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "21"},
    {"id": "535", "name": "Itahari", "name_ne": "\u0908\u091f\u0939\u0930\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "11"},
    {"id": "537", "name": "Jaleshwar", "name_ne": "\u091c\u0932\u0947\u0936\u094d\u0935\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "17"},
    {"id": "538", "name": "Janakpur", "name_ne": "\u091c\u0928\u0915\u092a\u0941\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "16"},
    {"id": "541", "name": "Jitpur Simara",
     "name_ne": "\u091c\u0940\u0924\u092a\u0941\u0930\u0938\u093f\u092e\u0930\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "15"},
    {"id": "542", "name": "Kabilasi", "name_ne": "\u0915\u0935\u093f\u0932\u093e\u0938\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "21"},
    {"id": "543", "name": "Kageshwori Manohara",
     "name_ne": "\u0915\u093e\u0917\u0947\u0936\u094d\u0935\u0930\u0940 \u092e\u0928\u094b\u0939\u0930\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "27"},
    {"id": "544", "name": "Kalaiya", "name_ne": "\u0915\u0932\u0948\u092f\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "15"},
    {"id": "547", "name": "Kamala", "name_ne": "\u0915\u092e\u0932\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "16"},
    {"id": "548", "name": "Kamalamai", "name_ne": "\u0915\u092e\u0932\u093e\u092e\u093e\u0908 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "34"},
    {"id": "552", "name": "Kapilvastu", "name_ne": "\u0915\u092a\u093f\u0932\u0935\u0938\u094d\u0924\u0941 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "52"},
    {"id": "553", "name": "Karjanha", "name_ne": "\u0915\u0930\u094d\u091c\u0928\u094d\u0939\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "22"},
    {"id": "555", "name": "Katari", "name_ne": "\u0915\u091f\u093e\u0930\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "14"},
    {"id": "582", "name": "Madhyabindu", "name_ne": "\u092e\u0927\u094d\u092f\u0935\u093f\u0928\u094d\u0926\u0941 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "43"},
    {"id": "583", "name": "Madhyapur Thimi",
     "name_ne": "\u092e\u0927\u094d\u092f\u092a\u0941\u0930 \u0925\u093f\u092e\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "23"},
    {"id": "586", "name": "Mahagadhimai", "name_ne": "\u092e\u0939\u093e\u0917\u0922\u0940\u092e\u093e\u0908 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "15"},
    {"id": "700", "name": "Tulsipur", "name_ne": "\u0924\u0941\u0932\u094d\u0938\u093f\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "50"},
    {"id": "701", "name": "Urlabari", "name_ne": "\u0909\u0930\u094d\u0932\u093e\u0935\u093e\u0930\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "6"},
    {"id": "702", "name": "Vyas", "name_ne": "\u0935\u094d\u092f\u093e\u0938 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "46"},
    {"id": "703", "name": "Waling", "name_ne": "\u0935\u093e\u0932\u093f\u0919 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "45"},
    {"id": "412", "name": "Aathabis", "name_ne": "\u0906\u0920\u092c\u0940\u0938 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "58"},
    {"id": "413", "name": "Aathabiskot", "name_ne": "\u0905\u093e\u0920\u092c\u093f\u0938\u0915\u093e\u0947\u091f ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "65"},
    {"id": "416", "name": "Badimalika", "name_ne": "\u092c\u0921\u0940\u092e\u093e\u0932\u093f\u0915\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "71"},
    {"id": "417", "name": "Bagchaur", "name_ne": "\u092c\u093e\u0917\u091a\u094c\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "66"},
    {"id": "419", "name": "Bagmati", "name_ne": "\u092c\u093e\u0917\u092e\u0924\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "21"},
    {"id": "421", "name": "Balara", "name_ne": "\u092c\u0932\u0930\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "21"},
    {"id": "424", "name": "Bangad Kupinde",
     "name_ne": "\u092c\u0928\u0917\u093e\u0921 \u0915\u0941\u092a\u093f\u0923\u094d\u0921\u0947 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "66"},
    {"id": "432", "name": "Barhabise", "name_ne": "\u092c\u093e\u0939\u094d\u0930\u0935\u093f\u0938\u0947 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "35"},
    {"id": "434", "name": "Bedkot", "name_ne": "\u0935\u0947\u0926\u0915\u094b\u091f ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "76"},
    {"id": "435", "name": "Belaka", "name_ne": "\u0935\u0947\u0932\u0915\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "14"},
    {"id": "438", "name": "Belkotgadhi", "name_ne": "\u092c\u0947\u0932\u0915\u094b\u091f\u0917\u0922\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "31"},
    {"id": "439", "name": "Beni", "name_ne": "\u092c\u0947\u0928\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "42"},
    {"id": "440", "name": "Besishahar", "name_ne": "\u092c\u0947\u0938\u0940\u0936\u0939\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "39"},
    {"id": "445", "name": "Bhanu", "name_ne": "\u092d\u093e\u0928\u0941 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "46"},
    {"id": "448", "name": "Bheerkot", "name_ne": "\u092d\u093f\u0930\u0915\u094b\u091f ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "45"},
    {"id": "603", "name": "Mirchaiya", "name_ne": "\u092e\u093f\u0930\u094d\u091a\u0948\u092f\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "22"},
    {"id": "604", "name": "Mithila", "name_ne": "\u092e\u093f\u0925\u093f\u0932\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "16"},
    {"id": "605", "name": "Mithila Bihari",
     "name_ne": "\u092e\u093f\u0925\u093f\u0932\u093e \u092c\u093f\u0939\u093e\u0930\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "16"},
    {"id": "609", "name": "Nagarain", "name_ne": "\u0928\u0917\u0930\u093e\u0908\u0928 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "16"},
    {"id": "610", "name": "Nagarjun", "name_ne": "\u0928\u093e\u0917\u093e\u0930\u094d\u091c\u0941\u0928 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "27"},
    {"id": "614", "name": "Nepalgunj", "name_ne": "\u0928\u0947\u092a\u093e\u0932\u0917\u0902\u091c ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "48"},
    {"id": "616", "name": "Nilkantha", "name_ne": "\u0928\u093f\u0932\u0915\u0923\u094d\u0920 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "25"},
    {"id": "617", "name": "Pachrauta", "name_ne": "\u092a\u091a\u0930\u094c\u0924\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "15"},
    {"id": "625", "name": "Paroha", "name_ne": "\u092a\u0930\u094b\u0939\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "19"},
    {"id": "626", "name": "Parsagadhi", "name_ne": "\u092a\u0930\u094d\u0938\u093e\u0917\u0922\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "18"},
    {"id": "628", "name": "Pathari Shanischare",
     "name_ne": "\u092a\u0925\u0930\u0940 \u0936\u0928\u093f\u0936\u094d\u091a\u0930\u0947 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "6"},
    {"id": "631", "name": "Phatuwa Bijayapur",
     "name_ne": "\u092b\u0924\u0941\u0935\u093e\u092c\u093f\u091c\u092f\u092a\u0941\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "19"},
    {"id": "634", "name": "Pokhara", "name_ne": "\u092a\u094b\u0916\u0930\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "38"},
    {"id": "635", "name": "Pokhariya", "name_ne": "\u092a\u094b\u0916\u0930\u093f\u092f\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "18"},
    {"id": "636", "name": "Punarbas", "name_ne": "\u092a\u0941\u0928\u0930\u094d\u0935\u093e\u0938 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "76"},
    {"id": "641", "name": "Rajapur", "name_ne": "\u0930\u093e\u091c\u093e\u092a\u0941\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "49"},
    {"id": "642", "name": "Rajbiraj", "name_ne": "\u0930\u093e\u091c\u0935\u093f\u0930\u093e\u091c ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "20"},
    {"id": "643", "name": "Rajdevi", "name_ne": "\u0930\u093e\u091c\u0926\u0947\u0935\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "19"},
    {"id": "644", "name": "Rajpur", "name_ne": "\u0930\u093e\u091c\u092a\u0941\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "19"},
    {"id": "645", "name": "Ramdhuni", "name_ne": "\u0930\u093e\u092e\u0927\u0941\u0928\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "11"},
    {"id": "647", "name": "Ramgopalpur",
     "name_ne": "\u0930\u093e\u092e\u0917\u094b\u092a\u093e\u0932\u092a\u0941\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "17"},
    {"id": "648", "name": "Ramgram", "name_ne": "\u0930\u093e\u092e\u0917\u094d\u0930\u093e\u092e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "53"},
    {"id": "650", "name": "Rangeli", "name_ne": "\u0930\u0902\u0917\u0947\u0932\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "6"},
    {"id": "651", "name": "Rapti", "name_ne": "\u0930\u093e\u092a\u094d\u0924\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "24"},
    {"id": "653", "name": "Ratnanagar", "name_ne": "\u0930\u0924\u094d\u0928\u0928\u0917\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "24"},
    {"id": "654", "name": "Ratuwamai", "name_ne": "\u0930\u0924\u0941\u0935\u093e\u092e\u093e\u0908 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "6"},
    {"id": "588", "name": "Mahakali", "name_ne": "\u092e\u0939\u093e\u0915\u093e\u0932\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "76"},
    {"id": "592", "name": "Mai", "name_ne": "\u092e\u093e\u0908 ", "alternative_names": [], "alternative_names_ne": [],
     "category": "Municipality", "district_id": "3"},
    {"id": "658", "name": "Sainamaina", "name_ne": "\u0938\u0948\u0928\u093e\u092e\u0948\u0928\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "57"},
    {"id": "661", "name": "Saptakoshi", "name_ne": "\u0938\u092a\u094d\u0924\u0915\u094b\u0936\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "20"},
    {"id": "669", "name": "Shiva Sataxi", "name_ne": "\u0936\u093f\u0935\u0938\u0924\u093e\u0915\u094d\u0937\u093f ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "4"},
    {"id": "670", "name": "Shivaraj", "name_ne": "\u0936\u093f\u0935\u0930\u093e\u091c ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "52"},
    {"id": "673", "name": "Siddharthanagar",
     "name_ne": "\u0938\u093f\u0926\u094d\u0927\u093e\u0930\u094d\u0925\u0928\u0917\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "57"},
    {"id": "676", "name": "Siraha", "name_ne": "\u0938\u093f\u0930\u0939\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "22"},
    {"id": "449", "name": "Bheri", "name_ne": "\u092d\u0947\u0930\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "61"},
    {"id": "450", "name": "Bheriganga", "name_ne": "\u092d\u0947\u0930\u0940\u0917\u0902\u0917\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "67"},
    {"id": "451", "name": "Bhimad", "name_ne": "\u092d\u093f\u092e\u093e\u0926 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "46"},
    {"id": "452", "name": "Bhimeshwar", "name_ne": "\u092d\u0940\u092e\u0947\u0936\u094d\u0935\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "26"},
    {"id": "453", "name": "Bhojpur", "name_ne": "\u092d\u094b\u091c\u092a\u0941\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "1"}, {"id": "454", "name": "Bhumikasthan",
                                                                                   "name_ne": "\u092d\u0942\u092e\u093f\u0915\u093e\u0938\u094d\u0925\u093e\u0928 ",
                                                                                   "alternative_names": [],
                                                                                   "alternative_names_ne": [],
                                                                                   "category": "Municipality",
                                                                                   "district_id": "47"},
    {"id": "465", "name": "Budhiganga", "name_ne": "\u092c\u0941\u0922\u0940\u0917\u0902\u0917\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "71"},
    {"id": "589", "name": "Mahalaxmi", "name_ne": "\u092e\u0939\u093e\u0932\u0915\u094d\u0937\u094d\u092e\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "29"},
    {"id": "590", "name": "Mahalaxmi", "name_ne": "\u092e\u0939\u093e\u0932\u0915\u094d\u0937\u094d\u092e\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "2"},
    {"id": "606", "name": "Musikot", "name_ne": "\u092e\u0941\u0938\u093f\u0915\u094b\u091f ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "65"},
    {"id": "607", "name": "Musikot", "name_ne": "\u092e\u0941\u0938\u093f\u0915\u094b\u091f ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "51"},
    {"id": "968", "name": "Painyu", "name_ne": "\u092a\u0948\u092f\u0942\u0902", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "44"},
    {"id": "679", "name": "Sukhipur", "name_ne": "\u0938\u0941\u0916\u0940\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "22"},
    {"id": "680", "name": "Sunawarshi", "name_ne": "\u0938\u0941\u0928\u0935\u0930\u094d\u0937\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "6"},
    {"id": "681", "name": "Sundar Haraincha",
     "name_ne": "\u0938\u0941\u0928\u094d\u0926\u0930\u0939\u0930\u0948\u0902\u091a\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "6"},
    {"id": "683", "name": "Sunwal", "name_ne": "\u0938\u0941\u0928\u0935\u0932 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "53"},
    {"id": "685", "name": "Suryabinayak",
     "name_ne": "\u0938\u0942\u0930\u094d\u092f\u0935\u093f\u0928\u093e\u092f\u0915 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "23"},
    {"id": "686", "name": "Suryodaya", "name_ne": "\u0938\u0942\u0930\u094d\u092f\u094b\u0926\u092f ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "3"},
    {"id": "688", "name": "Tansen", "name_ne": "\u0924\u093e\u0928\u0938\u0947\u0928 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "54"},
    {"id": "689", "name": "Tarakeshor", "name_ne": "\u0924\u093e\u0930\u0915\u0947\u0936\u094d\u0935\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "27"},
    {"id": "693", "name": "Tikapur", "name_ne": "\u091f\u093f\u0915\u093e\u092a\u0941\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "75"},
    {"id": "584", "name": "Madi", "name_ne": "\u092e\u093e\u0921\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "9"},
    {"id": "585", "name": "Madi", "name_ne": "\u092e\u093e\u0926\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "24"},
    {"id": "695", "name": "Tilottama", "name_ne": "\u0924\u093f\u0932\u094b\u0924\u094d\u0924\u092e\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "57"},
    {"id": "696", "name": "Tokha", "name_ne": "\u091f\u094b\u0916\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "27"},
    {"id": "699", "name": "Triyuga", "name_ne": "\u0924\u094d\u0930\u093f\u092f\u0941\u0917\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "14"},
    {"id": "466", "name": "Budhinanda", "name_ne": "\u092c\u0941\u0922\u0940\u0928\u0928\u094d\u0926\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "71"},
    {"id": "467", "name": "Bungal", "name_ne": "\u092c\u0941\u0902\u0917\u0932 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "70"},
    {"id": "469", "name": "Chainpur", "name_ne": "\u091a\u0948\u0928\u092a\u0941\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "9"},
    {"id": "470", "name": "Chamunda Bindrasaini",
     "name_ne": "\u091a\u093e\u092e\u0941\u0923\u094d\u0921\u093e \u0935\u093f\u0928\u094d\u0926\u094d\u0930\u093e\u0938\u0948\u0928\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "58"},
    {"id": "471", "name": "Chandannath", "name_ne": "\u091a\u0928\u094d\u0926\u0928\u0928\u093e\u0925 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "62"},
    {"id": "475", "name": "Chapakot", "name_ne": "\u091a\u093e\u092a\u093e\u0915\u094b\u091f ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "45"},
    {"id": "476", "name": "Chaudandigadhi", "name_ne": "\u091a\u094c\u0926\u0923\u094d\u0921\u0940\u0917\u0922\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "14"},
    {"id": "477", "name": "Chaurjahari", "name_ne": "\u091a\u094c\u0930\u091c\u0939\u093e\u0930\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "65"},
    {"id": "478", "name": "Chautara Sangachowkgadhi",
     "name_ne": "\u091a\u094c\u0924\u093e\u0930\u093e \u0938\u093e\u0901\u0917\u093e\u091a\u094b\u0915\u0917\u0922\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "35"},
    {"id": "479", "name": "Chhayanath Rara",
     "name_ne": "\u091b\u093e\u092f\u093e\u0901\u0928\u093e\u0925 \u0930\u093e\u0930\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "64"},
    {"id": "480", "name": "Chhedagad", "name_ne": "\u091b\u0947\u0921\u093e\u0917\u093e\u0921 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "61"},
    {"id": "481", "name": "Dakneshwari",
     "name_ne": "\u0926\u0915\u094d\u0928\u0947\u0936\u094d\u0935\u093e\u0930\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "20"},
    {"id": "483", "name": "Dasharath Chand", "name_ne": "\u0926\u0936\u0930\u0925\u091a\u0928\u094d\u0926 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "69"},
    {"id": "484", "name": "Daxinkaali", "name_ne": "\u0926\u0915\u094d\u0937\u093f\u0923\u0915\u093e\u0932\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "27"},
    {"id": "485", "name": "Deumai", "name_ne": "\u0926\u0947\u0909\u092e\u093e\u0908 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "3"},
    {"id": "486", "name": "Devchuli", "name_ne": "\u0926\u0947\u0935\u091a\u0941\u0932\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "43"},
    {"id": "490", "name": "Dhangadimai", "name_ne": "\u0927\u0928\u0917\u0922\u0940\u092e\u093e\u0908 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "22"},
    {"id": "491", "name": "Dhankuta", "name_ne": "\u0927\u0928\u0915\u0941\u091f\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "2"},
    {"id": "492", "name": "Dhanushadham", "name_ne": "\u0927\u0928\u0941\u0937\u093e\u0927\u093e\u092e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "16"},
    {"id": "494", "name": "Dharmadevi", "name_ne": "\u0927\u0930\u094d\u092e\u0926\u0947\u0935\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "9"},
    {"id": "495", "name": "Dhorpatan", "name_ne": "\u0922\u094b\u0930\u092a\u093e\u091f\u0928 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "36"},
    {"id": "496", "name": "Dhulikhel", "name_ne": "\u0927\u0941\u0932\u093f\u0916\u0947\u0932 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "28"},
    {"id": "520", "name": "Gorkha", "name_ne": "\u0917\u094b\u0930\u0916\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "37"},
    {"id": "523", "name": "Gurbhakot", "name_ne": "\u0917\u0941\u0930\u094d\u092d\u093e\u0915\u094b\u091f ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "67"},
    {"id": "677", "name": "Sitganga", "name_ne": "\u0938\u093f\u0924\u0917\u0902\u0917\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "47"},
    {"id": "678", "name": "Solu Dudhkunda",
     "name_ne": "\u0938\u094b\u0932\u0941\u0926\u0941\u0927\u0915\u0941\u0923\u094d\u0921 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "10"},
    {"id": "682", "name": "Sundarbazar", "name_ne": "\u0938\u0941\u0928\u094d\u0926\u0930\u092c\u091c\u093e\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "39"},
    {"id": "536", "name": "Jaimini", "name_ne": "\u091c\u0948\u092e\u093f\u0928\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "36"},
    {"id": "539", "name": "Jaya Prithvi", "name_ne": "\u091c\u092f\u092a\u0943\u0925\u094d\u0935\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "70"},
    {"id": "545", "name": "Kalika", "name_ne": "\u0915\u093e\u0932\u093f\u0915\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "24"},
    {"id": "546", "name": "Kalyanpur", "name_ne": "\u0915\u0932\u094d\u092f\u093e\u0923\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "22"},
    {"id": "549", "name": "Kamalbazar", "name_ne": "\u0915\u092e\u0932\u092c\u091c\u093e\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "68"},
    {"id": "550", "name": "Kanchanrup", "name_ne": "\u0915\u091e\u094d\u091a\u0928\u0930\u0942\u092a ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "20"},
    {"id": "652", "name": "Raskot", "name_ne": "\u0930\u093e\u0938\u094d\u0915\u094b\u091f ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "63"},
    {"id": "655", "name": "Resunga", "name_ne": "\u0930\u0947\u0938\u0941\u0919\u094d\u0917\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "51"},
    {"id": "657", "name": "Sabaila", "name_ne": "\u0938\u0935\u0948\u0932\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "16"},
    {"id": "659", "name": "Sandhikharka", "name_ne": "\u0938\u0928\u094d\u0927\u093f\u0916\u0930\u094d\u0915 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "47"},
    {"id": "660", "name": "Saphebagar", "name_ne": "\u0938\u093e\u092b\u0947\u092c\u0917\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "68"},
    {"id": "662", "name": "Shaarda", "name_ne": "\u0936\u093e\u0930\u0926\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "66"},
    {"id": "663", "name": "Shadanand", "name_ne": "\u0937\u0921\u093e\u0928\u0928\u094d\u0926 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "1"},
    {"id": "664", "name": "Shahidnagar", "name_ne": "\u0936\u0939\u093f\u0926 \u0928\u0917\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "16"},
    {"id": "665", "name": "Shailyashikhar", "name_ne": "\u0936\u0948\u0932\u094d\u092f\u0936\u093f\u0916\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "73"},
    {"id": "666", "name": "Shambhunath", "name_ne": "\u0936\u092e\u094d\u092d\u0941\u0928\u093e\u0925 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "20"},
    {"id": "667", "name": "Shankharapur", "name_ne": "\u0936\u0919\u094d\u0916\u0930\u093e\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "27"},
    {"id": "524", "name": "Halesi Tuwachung",
     "name_ne": "\u0939\u0932\u0947\u0938\u0940 \u0924\u0941\u0935\u093e\u091a\u0941\u0919 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "5"},
    {"id": "525", "name": "Hansapur", "name_ne": "\u0939\u0902\u0938\u092a\u0941\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "16"},
    {"id": "526", "name": "Hanumannagar Kankalini",
     "name_ne": "\u0939\u0928\u0941\u092e\u093e\u0928\u0928\u0917\u0930 \u0915\u0902\u0915\u093e\u0932\u093f\u0928\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "20"},
    {"id": "529", "name": "Hariwan", "name_ne": "\u0939\u0930\u093f\u0935\u0928 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "21"},
    {"id": "804", "name": "Aaurahi", "name_ne": "\u0914\u0930\u0939\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "16"},
    {"id": "844", "name": "Aaurahi", "name_ne": "\u0914\u0930\u0939\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "22"},
    {"id": "831", "name": "Bishnupur", "name_ne": "\u092c\u093f\u0937\u094d\u0923\u0941\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "20"},
    {"id": "850", "name": "Bishnupur", "name_ne": "\u0935\u093f\u0937\u094d\u0923\u0941\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "22"},
    {"id": "858", "name": "Tripura Sundari",
     "name_ne": "\u0924\u094d\u0930\u093f\u092a\u0941\u0930\u093e\u0938\u0941\u0928\u094d\u0926\u0930\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "25"},
    {"id": "587", "name": "Mahakali", "name_ne": "\u092e\u093e\u0939\u093e\u0915\u093e\u0932\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "73"},
    {"id": "554", "name": "Katahariya", "name_ne": "\u0915\u091f\u0939\u0930\u0940\u092f\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "19"},
    {"id": "556", "name": "Kathmandu", "name_ne": "\u0915\u093e\u0920\u092e\u093e\u0923\u094d\u0921\u094c ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "27"},
    {"id": "557", "name": "Kawasoti", "name_ne": "\u0915\u093e\u0935\u093e\u0938\u094b\u0924\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "43"},
    {"id": "559", "name": "Khairhani", "name_ne": "\u0916\u0948\u0930\u0939\u0928\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "24"},
    {"id": "562", "name": "Kirtipur", "name_ne": "\u0915\u093f\u0930\u094d\u0924\u093f\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "27"},
    {"id": "563", "name": "Kohalpur", "name_ne": "\u0915\u094b\u0939\u0932\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "48"},
    {"id": "565", "name": "Krishnanagar", "name_ne": "\u0915\u0943\u0937\u094d\u0923\u0928\u0917\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "52"},
    {"id": "566", "name": "Krishnapur", "name_ne": "\u0915\u0943\u0937\u094d\u0923\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "76"},
    {"id": "569", "name": "Lahan", "name_ne": "\u0932\u0939\u093e\u0928 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "22"},
    {"id": "570", "name": "Lalbandi", "name_ne": "\u0932\u093e\u0932\u092c\u0928\u094d\u0926\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "21"},
    {"id": "531", "name": "Ilam", "name_ne": "\u0907\u0932\u093e\u092e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "3"},
    {"id": "750", "name": "Likhu", "name_ne": "\u0932\u093f\u0916\u0941", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "31"},
    {"id": "743", "name": "Miklajung", "name_ne": "\u092e\u093f\u0915\u094d\u0932\u093e\u091c\u0941\u0919",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "6"},
    {"id": "751", "name": "Miklajung", "name_ne": "\u092e\u093f\u0915\u094d\u0932\u093e\u091c\u0941\u0919",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "8"},
    {"id": "746", "name": "Sunkoshi", "name_ne": "\u0938\u0941\u0928\u0915\u094b\u0936\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "35"},
    {"id": "940", "name": "Annapurna", "name_ne": "\u0905\u0928\u094d\u0928\u092a\u0941\u0930\u094d\u0923",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "38"},
    {"id": "961", "name": "Annapurna", "name_ne": "\u0905\u0928\u094d\u0928\u092a\u0941\u0930\u094d\u0923",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "42"},
    {"id": "877", "name": "Bagmati", "name_ne": "\u092c\u093e\u0917\u094d\u092e\u0924\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "29"},
    {"id": "882", "name": "Bagmati", "name_ne": "\u092c\u093e\u0917\u094d\u092e\u0924\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "30"},
    {"id": "892", "name": "Likhu", "name_ne": "\u0932\u093f\u0916\u0941", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "7"},
    {"id": "942", "name": "Madi", "name_ne": "\u092e\u093e\u0926\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "38"},
    {"id": "957", "name": "Malika", "name_ne": "\u092e\u093e\u0932\u093f\u0915\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "51"},
    {"id": "922", "name": "Sunkoshi", "name_ne": "\u0938\u0941\u0928\u0915\u094b\u0936\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "7"},
    {"id": "912", "name": "Sunkoshi", "name_ne": "\u0938\u0941\u0928\u0915\u094b\u0936\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "34"},
    {"id": "497", "name": "Dhunibeshi", "name_ne": "\u0927\u0941\u0928\u0940\u092c\u0947\u0902\u0936\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "25"},
    {"id": "498", "name": "Diktel Rupakot Majuwagadhi",
     "name_ne": "\u0926\u093f\u0915\u094d\u0924\u0947\u0932 \u0930\u0941\u092a\u093e\u0915\u094b\u091f \u092e\u091c\u0941\u0935\u093e\u0917\u0922\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "5"},
    {"id": "499", "name": "Dipayal Silgadhi",
     "name_ne": "\u0926\u093f\u092a\u093e\u092f\u0932 \u0938\u093f\u0932\u0917\u0922\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "74"},
    {"id": "502", "name": "Dullu", "name_ne": "\u0926\u0941\u0932\u094d\u0932\u0941 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "58"},
    {"id": "505", "name": "Galkot", "name_ne": "\u0917\u0932\u094d\u0915\u094b\u091f ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "36"},
    {"id": "506", "name": "Galyang", "name_ne": "\u0917\u0932\u094d\u092f\u093e\u0919 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "45"},
    {"id": "708", "name": "Arun", "name_ne": "\u0905\u0930\u0941\u0923", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "1"},
    {"id": "507", "name": "Ganeshman Charnath",
     "name_ne": "\u0917\u0923\u0947\u0936\u092e\u093e\u0928 \u091a\u093e\u0930\u0928\u093e\u0925 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "16"},
    {"id": "515", "name": "Godaita", "name_ne": "\u0917\u094b\u0921\u0948\u0924\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "21"},
    {"id": "540", "name": "Jiri", "name_ne": "\u091c\u093f\u0930\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "26"},
    {"id": "989", "name": "Janaki", "name_ne": "\u091c\u093e\u0928\u0915\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "75"},
    {"id": "1009", "name": "Kaligandaki", "name_ne": "\u0915\u093e\u0932\u0940\u0917\u0923\u094d\u0921\u0915\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "45"},
    {"id": "971", "name": "Kaligandaki", "name_ne": "\u0915\u093e\u0932\u0940\u0917\u0923\u094d\u0921\u0915\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "51"},
    {"id": "1040", "name": "Madi", "name_ne": "\u092e\u093e\u0921\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "56"},
    {"id": "1006", "name": "Malika", "name_ne": "\u092e\u093e\u0932\u093f\u0915\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "42"},
    {"id": "1047", "name": "Mayadevi", "name_ne": "\u092e\u093e\u092f\u093e\u0926\u0947\u0935\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "52"},
    {"id": "1011", "name": "Mayadevi", "name_ne": "\u092e\u093e\u092f\u093e\u0926\u0947\u0935\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "57"},
    {"id": "1012", "name": "Shuddhodhan", "name_ne": "\u0936\u0941\u0926\u094d\u0927\u094b\u0927\u0928",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "52"},
    {"id": "1053", "name": "Shuddhodhan", "name_ne": "\u0936\u0941\u0926\u094d\u0927\u094b\u0927\u0928",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "57"},
    {"id": "1037", "name": "Triveni", "name_ne": "\u0924\u094d\u0930\u093f\u0935\u0947\u0923\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "56"},
    {"id": "784", "name": "Aathrai", "name_ne": "\u0906\u0920\u0930\u093e\u0908", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "13"},
    {"id": "924", "name": "Tripura Sundari",
     "name_ne": "\u0924\u094d\u0930\u093f\u092a\u0941\u0930\u093e\u0938\u0941\u0928\u094d\u0926\u0930\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "35"},
    {"id": "1156", "name": "Janaki", "name_ne": "\u091c\u093e\u0928\u0915\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "48"},
    {"id": "1097", "name": "Triveni", "name_ne": "\u0924\u094d\u0930\u093f\u0935\u0947\u0923\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "65"},
    {"id": "1104", "name": "Triveni", "name_ne": "\u0924\u094d\u0930\u093f\u0935\u0947\u0923\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "66"},
    {"id": "1154", "name": "Bogatan", "name_ne": "\u092c\u094b\u0917\u091f\u093e\u0928", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "74"},
    {"id": "1149", "name": "Aadarsha", "name_ne": "\u0906\u0926\u0930\u094d\u0936", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "74"},
    {"id": "828", "name": "Aagnisaira Krishnasawaran",
     "name_ne": "\u0905\u0917\u094d\u0928\u093f\u0938\u093e\u0907\u0930 \u0915\u0943\u0937\u094d\u0923\u093e\u0938\u0935\u0930\u0928 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "20"},
    {"id": "1138", "name": "Aalitaal", "name_ne": "\u0906\u0932\u093f\u0924\u093e\u0932", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "72"},
    {"id": "908", "name": "Aamachodingmo", "name_ne": "\u0906\u092e\u093e\u091b\u094b\u0926\u093f\u0919\u092e\u094b",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "33"},
    {"id": "706", "name": "Aamchok", "name_ne": "\u0906\u092e\u091a\u094b\u0915", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "1"},
    {"id": "979", "name": "Aanbu Khaireni", "name_ne": "\u0906\u0901\u092c\u0941\u0916\u0948\u0930\u0947\u0928\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "46"},
    {"id": "974", "name": "Aandhikhola", "name_ne": "\u0906\u0901\u0927\u0940\u0916\u094b\u0932\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "45"},
    {"id": "777", "name": "Aathrai Triveni",
     "name_ne": "\u0906\u0920\u0930\u093e\u0908 \u0924\u094d\u0930\u093f\u0935\u0947\u0923\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "12"},
    {"id": "1071", "name": "Adanchuli", "name_ne": "\u0905\u0926\u093e\u0928\u091a\u0941\u0932\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "60"},
    {"id": "793", "name": "Adarsha Kotwal",
     "name_ne": "\u0906\u0926\u0930\u094d\u0936 \u0915\u094b\u0924\u0935\u093e\u0932 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "15"},
    {"id": "1030", "name": "Airawati", "name_ne": "\u0910\u0930\u093e\u0935\u0924\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "55"},
    {"id": "730", "name": "Aiselukharka", "name_ne": "\u0910\u0938\u0947\u0932\u0941\u0916\u0930\u094d\u0915",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "5"},
    {"id": "1141", "name": "Ajaymeru", "name_ne": "\u0905\u091c\u092f\u092e\u0947\u0930\u0941",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "72"},
    {"id": "937", "name": "Ajirkot", "name_ne": "\u0905\u091c\u093f\u0930\u0915\u094b\u091f", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "37"},
    {"id": "1148", "name": "Api Himal", "name_ne": "\u0905\u092a\u093f \u0939\u093f\u092e\u093e\u0932",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "73"},
    {"id": "975", "name": "Arjun Chaupari",
     "name_ne": "\u0905\u0930\u094d\u091c\u0941\u0928 \u091a\u094c\u092a\u093e\u0930\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "45"},
    {"id": "845", "name": "Arnama", "name_ne": "\u0905\u0930\u094d\u0928\u092e\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "22"},
    {"id": "996", "name": "Babai", "name_ne": "\u092c\u092c\u0908", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "50"},
    {"id": "992", "name": "Badhaiyatal", "name_ne": "\u092c\u0922\u0948\u092f\u093e\u0924\u093e\u0932",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "49"},
    {"id": "925", "name": "Badigad", "name_ne": "\u0935\u0921\u093f\u0917\u093e\u0921", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "36"},
    {"id": "1155", "name": "Badikedar", "name_ne": "\u092c\u0921\u094d\u0921\u0940 \u0915\u0947\u0926\u093e\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "74"},
    {"id": "1022", "name": "Bagnaskali", "name_ne": "\u0935\u0917\u0928\u093e\u0938\u0915\u093e\u0932\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "54"},
    {"id": "987", "name": "Baijnath", "name_ne": "\u0935\u0948\u091c\u0928\u093e\u0925", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "48"},
    {"id": "866", "name": "Baiteshwar", "name_ne": "\u0935\u0948\u0924\u0947\u0936\u094d\u0935\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "26"},
    {"id": "880", "name": "Bakaiya", "name_ne": "\u092c\u0915\u0948\u092f\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "30"},
    {"id": "830", "name": "Balan-Bihul", "name_ne": "\u092c\u0932\u093e\u0928-\u092c\u093f\u0939\u0941\u0932 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "20"},
    {"id": "919", "name": "Balephi", "name_ne": "\u092c\u0932\u0947\u092b\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "35"},
    {"id": "980", "name": "Bandipur", "name_ne": "\u092c\u0928\u094d\u0926\u093f\u092a\u0941\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "46"},
    {"id": "999", "name": "Banglachuli", "name_ne": "\u0935\u0902\u0917\u0932\u093e\u091a\u0941\u0932\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "50"},
    {"id": "1115", "name": "Bannigadi Jayagad",
     "name_ne": "\u092c\u093e\u0928\u094d\u0928\u0940\u0917\u0921\u0940\u091c\u0948\u0917\u0921",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "68"},
    {"id": "1098", "name": "Banphikot", "name_ne": "\u092c\u093e\u0901\u092b\u093f\u0915\u094b\u091f",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "65"},
    {"id": "794", "name": "Baragadhi", "name_ne": "\u092c\u093e\u0930\u093e\u0917\u0922\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "15"},
    {"id": "954", "name": "Baragung Muktichhetra",
     "name_ne": "\u092c\u093e\u0930\u093e\u0917\u0941\u0919 \u092e\u0941\u0915\u094d\u0924\u093f\u0915\u094d\u0937\u0947\u0924\u094d\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "41"},
    {"id": "1106", "name": "Barahatal", "name_ne": "\u092c\u0930\u093e\u0939\u0924\u093e\u0932",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "67"},
    {"id": "733", "name": "Barahpokhari", "name_ne": "\u092c\u0930\u093e\u0939\u092a\u094b\u0916\u0930\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "5"},
    {"id": "1078", "name": "Barekot", "name_ne": "\u092c\u093e\u0930\u0947\u0915\u094b\u091f", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "61"},
    {"id": "928", "name": "Bareng", "name_ne": "\u0935\u0930\u0947\u0919", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "36"},
    {"id": "1159", "name": "Bargagoriya", "name_ne": "\u092c\u0930\u094d\u0917\u0917\u094b\u0930\u093f\u092f\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "75"},
    {"id": "725", "name": "Barhadashi", "name_ne": "\u092c\u093e\u0939\u094d\u0930\u0926\u0936\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "4"},
    {"id": "843", "name": "Bariyarpatti",
     "name_ne": "\u092c\u0930\u093f\u092f\u093e\u0930\u092a\u091f\u094d\u091f\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "22"},
    {"id": "775", "name": "Barju", "name_ne": "\u092c\u0930\u094d\u091c\u0941", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "11"},
    {"id": "932", "name": "Barpak Sulikot",
     "name_ne": "\u092c\u093e\u0930\u092a\u093e\u0915 \u0938\u0941\u0932\u0940\u0915\u094b\u091f",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "37"},
    {"id": "840", "name": "Basbariya", "name_ne": "\u092c\u0938\u092c\u0930\u093f\u092f\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "21"},
    {"id": "805", "name": "Bateshwar", "name_ne": "\u092c\u091f\u0947\u0936\u094d\u0935\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "16"},
    {"id": "965", "name": "Baudikali", "name_ne": "\u092c\u094c\u0926\u0940\u0915\u093e\u0932\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "43"},
    {"id": "1163", "name": "Beldandi", "name_ne": "\u092c\u0947\u0932\u0921\u093e\u0901\u0921\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "76"},
    {"id": "825", "name": "Belhi Chapena",
     "name_ne": "\u092c\u0947\u0932\u094d\u0939\u0940 \u091a\u092a\u0947\u0928\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "20"},
    {"id": "853", "name": "Benighat Rorang",
     "name_ne": "\u092c\u0947\u0928\u0940\u0918\u093e\u091f \u0930\u094b\u0930\u093e\u0919\u094d\u0917",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "25"},
    {"id": "875", "name": "Bethanchok", "name_ne": "\u092c\u0947\u0925\u093e\u0928\u091a\u094b\u0915",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "28"},
    {"id": "846", "name": "Bhagawanpur", "name_ne": "\u092d\u0917\u0935\u093e\u0928\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "22"},
    {"id": "1061", "name": "Bhagawatimai", "name_ne": "\u092d\u0917\u0935\u0924\u0940\u092e\u093e\u0908",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "58"},
    {"id": "1140", "name": "Bhageshwar", "name_ne": "\u092d\u093e\u0917\u0947\u0936\u094d\u0935\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "72"},
    {"id": "1057", "name": "Bhairabi", "name_ne": "\u092d\u0948\u0930\u0935\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "58"},
    {"id": "886", "name": "Bhimphedi", "name_ne": "\u092d\u0940\u092e\u092b\u0947\u0926\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "30"},
    {"id": "936", "name": "Bhimsen Thapa", "name_ne": "\u092d\u093f\u092e\u0938\u0947\u0928\u0925\u093e\u092a\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "37"},
    {"id": "772", "name": "Bhokraha", "name_ne": "\u092d\u094b\u0915\u094d\u0930\u093e\u0939\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "11"},
    {"id": "668", "name": "Shikhar", "name_ne": "\u0936\u093f\u0916\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "74"},
    {"id": "671", "name": "Shuklagandaki",
     "name_ne": "\u0936\u0941\u0915\u094d\u0932\u093e\u0917\u0923\u094d\u0921\u0915\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "46"},
    {"id": "672", "name": "Shuklaphanta",
     "name_ne": "\u0936\u0941\u0915\u094d\u0932\u093e\u092b\u093e\u0901\u091f\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "76"},
    {"id": "674", "name": "Siddhicharan", "name_ne": "\u0938\u093f\u0926\u094d\u0926\u093f\u091a\u0930\u0923 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "7"},
    {"id": "656", "name": "Rolpa", "name_ne": "\u0930\u094b\u0932\u094d\u092a\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "56"},
    {"id": "675", "name": "Simraungadh", "name_ne": "\u0938\u093f\u092e\u094d\u0930\u094b\u0928\u0917\u0922 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "15"},
    {"id": "684", "name": "Surunga", "name_ne": "\u0938\u0941\u0930\u0941\u0919\u094d\u200d\u0917\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "20"},
    {"id": "687", "name": "Swargadwari",
     "name_ne": "\u0938\u094d\u0935\u0930\u094d\u0917\u0926\u094d\u0935\u093e\u0930\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "55"},
    {"id": "690", "name": "Thaha", "name_ne": "\u0925\u093e\u0939\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "30"},
    {"id": "691", "name": "Thakurbaba", "name_ne": "\u0920\u093e\u0915\u0941\u0930\u092c\u093e\u092c\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "49"},
    {"id": "692", "name": "Thuli Bheri", "name_ne": "\u0920\u0942\u0932\u0940 \u092d\u0947\u0930\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "59"},
    {"id": "694", "name": "Tilagufa", "name_ne": "\u0924\u093f\u0932\u093e\u0917\u0941\u092b\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "63"},
    {"id": "697", "name": "Tribeni", "name_ne": "\u0924\u094d\u0930\u093f\u0935\u0947\u0923\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "71"},
    {"id": "698", "name": "Tripura Sundari",
     "name_ne": "\u0924\u094d\u0930\u093f\u092a\u0941\u0930\u093e\u0938\u0941\u0928\u094d\u0926\u0930\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "59"},
    {"id": "933", "name": "Aarughat", "name_ne": "\u0906\u0930\u0942\u0918\u093e\u091f", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "37"},
    {"id": "833", "name": "Chandranagar", "name_ne": "\u091a\u0928\u094d\u0926\u094d\u0930\u0928\u0917\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "21"},
    {"id": "1074", "name": "Chankheli", "name_ne": "\u091a\u0902\u0916\u0947\u0932\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "60"},
    {"id": "712", "name": "Chaubise", "name_ne": "\u091a\u094c\u0935\u093f\u0938\u0947", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "2"},
    {"id": "1108", "name": "Chaukune", "name_ne": "\u091a\u094c\u0915\u0941\u0928\u0947", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "67"},
    {"id": "872", "name": "Chaunri Deurali",
     "name_ne": "\u091a\u094c\u0902\u0930\u0940 \u0926\u0947\u0909\u0930\u093e\u0932\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "28"},
    {"id": "1111", "name": "Chaurpati", "name_ne": "\u091a\u094c\u0930\u092a\u093e\u091f\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "68"},
    {"id": "1125", "name": "Chhabis Pathibhera",
     "name_ne": "\u091b\u092c\u094d\u092c\u0940\u0938\u092a\u093e\u0925\u093f\u092d\u0947\u0930\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "70"},
    {"id": "1126", "name": "Chhanna", "name_ne": "\u091b\u093e\u0928\u094d\u0928\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "70"},
    {"id": "1068", "name": "Chharka Tangsong",
     "name_ne": "\u091b\u093e\u0930\u094d\u0915\u093e \u0924\u093e\u0919\u0938\u094b\u0919", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "59"},
    {"id": "786", "name": "Chhathar", "name_ne": "\u091b\u0925\u0930", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "13"},
    {"id": "714", "name": "Chhathar Jorpati",
     "name_ne": "\u091b\u0925\u0930 \u091c\u094b\u0930\u092a\u093e\u091f\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "2"},
    {"id": "985", "name": "Chhatradev", "name_ne": "\u091b\u0924\u094d\u0930\u0926\u0947\u0935",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "47"},
    {"id": "1007", "name": "Chhatrakot", "name_ne": "\u091b\u0924\u094d\u0930\u0915\u094b\u091f",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "51"},
    {"id": "1101", "name": "Chhatreshwari", "name_ne": "\u091b\u0924\u094d\u0930\u0947\u0936\u094d\u0935\u0930\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "66"},
    {"id": "826", "name": "Chhinnamasta", "name_ne": "\u091b\u093f\u0928\u094d\u0928\u092e\u0938\u094d\u0924\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "20"},
    {"id": "814", "name": "Chhipaharmai", "name_ne": "\u091b\u093f\u092a\u0939\u0930\u092e\u093e\u0908 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "18"},
    {"id": "761", "name": "Chichila", "name_ne": "\u091a\u093f\u091a\u093f\u0932\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "9"},
    {"id": "1021", "name": "Nisdi", "name_ne": "\u0928\u093f\u0938\u094d\u0926\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "54"},
    {"id": "1109", "name": "Chingad", "name_ne": "\u091a\u093f\u0919\u094d\u0917\u093e\u0921", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "67"},
    {"id": "748", "name": "Chisankhugadhi", "name_ne": "\u091a\u093f\u0938\u0902\u0916\u0941\u0917\u0922\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "7"},
    {"id": "717", "name": "Chulachuli", "name_ne": "\u091a\u0941\u0932\u093e\u091a\u0941\u0932\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "3"},
    {"id": "939", "name": "Chum Nubri", "name_ne": "\u091a\u0941\u092e \u0928\u0941\u0935\u094d\u0930\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "37"},
    {"id": "1161", "name": "Chure", "name_ne": "\u091a\u0941\u0930\u0947", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "75"},
    {"id": "1000", "name": "Dangisharan", "name_ne": "\u0926\u0902\u0917\u0940\u0936\u0930\u0923",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "50"},
    {"id": "1102", "name": "Darma", "name_ne": "\u0926\u093e\u0930\u094d\u092e\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "66"},
    {"id": "982", "name": "Devghat", "name_ne": "\u0926\u0947\u0935\u0918\u093e\u091f", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "46"},
    {"id": "799", "name": "Devtal", "name_ne": "\u0926\u0947\u0935\u0924\u093e\u0932 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "15"},
    {"id": "773", "name": "Dewangunj", "name_ne": "\u0926\u0947\u0935\u093e\u0928\u0917\u0928\u094d\u091c",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "11"},
    {"id": "806", "name": "Dhanauji", "name_ne": "\u0927\u0928\u094c\u091c\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "16"},
    {"id": "1114", "name": "Dhankari", "name_ne": "\u0922\u0901\u0915\u093e\u0930\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "68"},
    {"id": "838", "name": "Dhankaul", "name_ne": "\u0927\u0928\u0915\u094c\u0932 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "21"},
    {"id": "739", "name": "Dhanpalthan", "name_ne": "\u0927\u0928\u092a\u093e\u0932\u0925\u093e\u0928",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "6"},
    {"id": "938", "name": "Dharche", "name_ne": "\u0927\u093e\u0930\u094d\u091a\u0947", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "37"},
    {"id": "960", "name": "Dhaulagiri", "name_ne": "\u0927\u0935\u0932\u093e\u0917\u093f\u0930\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "42"},
    {"id": "821", "name": "Dhobini", "name_ne": "\u0927\u094b\u092c\u0940\u0928\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "18"},
    {"id": "1002", "name": "Dhurkot", "name_ne": "\u0927\u0941\u0930\u094d\u0915\u094b\u091f", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "51"},
    {"id": "1117", "name": "Dilashaini", "name_ne": "\u0921\u093f\u0932\u093e\u0936\u0948\u0928\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "69"},
    {"id": "729", "name": "Diprung", "name_ne": "\u0926\u093f\u092a\u094d\u0930\u0941\u0919", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "5"},
    {"id": "1116", "name": "Dogdakedar", "name_ne": "\u0926\u094b\u0917\u0921\u093e\u0915\u0947\u0926\u093e\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "69"},
    {"id": "1067", "name": "Dolpo Buddha",
     "name_ne": "\u0921\u094b\u0932\u094d\u092a\u094b \u092c\u0941\u0926\u094d\u0927", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "59"},
    {"id": "900", "name": "Doramba", "name_ne": "\u0926\u094b\u0930\u092e\u094d\u092c\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "32"},
    {"id": "945", "name": "Dordi", "name_ne": "\u0926\u094b\u0930\u094d\u0926\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "39"},
    {"id": "763", "name": "Dudhakaushika", "name_ne": "\u0926\u0941\u0927\u0915\u094c\u0936\u093f\u0915\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "10"},
    {"id": "765", "name": "Dudhkoshi", "name_ne": "\u0926\u0941\u0927\u0915\u094b\u0936\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "10"},
    {"id": "946", "name": "Dudhpokhari", "name_ne": "\u0926\u0942\u0927\u092a\u094b\u0916\u0930\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "39"},
    {"id": "990", "name": "Duduwa", "name_ne": "\u0921\u0941\u0921\u0941\u0935\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "48"},
    {"id": "1146", "name": "Duhu", "name_ne": "\u0926\u0941\u0939\u0941", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "73"},
    {"id": "1062", "name": "Dungeshwar", "name_ne": "\u0921\u0941\u0902\u0917\u0947\u0936\u094d\u0935\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "58"},
    {"id": "889", "name": "Dupcheshwar", "name_ne": "\u0926\u0941\u092a\u094d\u091a\u0947\u0936\u094d\u0935\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "31"},
    {"id": "822", "name": "Durga Bhagawati",
     "name_ne": "\u0926\u0941\u0930\u094d\u0917\u093e \u092d\u0917\u0935\u0924\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "19"},
    {"id": "1128", "name": "Durgathali", "name_ne": "\u0926\u0941\u0930\u094d\u0917\u093e\u0925\u0932\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "70"},
    {"id": "810", "name": "Ekdara", "name_ne": "\u090f\u0915\u0921\u093e\u0930\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "17"},
    {"id": "995", "name": "Gadhawa", "name_ne": "\u0917\u0922\u0935\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "50"},
    {"id": "774", "name": "Gadhi", "name_ne": "\u0917\u0922\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "11"},
    {"id": "1046", "name": "Gaidhawa", "name_ne": "\u0917\u0948\u0921\u0939\u0935\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "57"},
    {"id": "855", "name": "Gajuri", "name_ne": "\u0917\u091c\u0941\u0930\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "25"},
    {"id": "854", "name": "Galchhi", "name_ne": "\u0917\u0932\u094d\u091b\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "25"},
    {"id": "935", "name": "Gandaki", "name_ne": "\u0917\u0923\u094d\u0921\u0915\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "37"},
    {"id": "1039", "name": "Gangadev", "name_ne": "\u0917\u0902\u0917\u093e\u0926\u0947\u0935",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "56"},
    {"id": "859", "name": "Gangajamuna", "name_ne": "\u0917\u0919\u094d\u0917\u093e\u091c\u092e\u0941\u0928\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "25"},
    {"id": "1139", "name": "Ganyapadhura", "name_ne": "\u0917\u0928\u094d\u092f\u093e\u092a\u0927\u0941\u0930\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "72"},
    {"id": "1029", "name": "Gaumukhi", "name_ne": "\u0917\u094c\u092e\u0941\u0916\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "55"},
    {"id": "1136", "name": "Gaumul", "name_ne": "\u0917\u094c\u092e\u0941\u0932", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "71"},
    {"id": "726", "name": "Gaurigunj", "name_ne": "\u0917\u094c\u0930\u0940\u0917\u0902\u091c",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "4"},
    {"id": "869", "name": "Gaurishankar", "name_ne": "\u0917\u094c\u0930\u093f\u0936\u0902\u0915\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "26"},
    {"id": "993", "name": "Geruwa", "name_ne": "\u0917\u0947\u0930\u0941\u0935\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "49"},
    {"id": "952", "name": "Gharpajhong", "name_ne": "\u0918\u0930\u092a\u091d\u094b\u0919", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "41"},
    {"id": "981", "name": "Ghiring", "name_ne": "\u0918\u093f\u0930\u093f\u0919", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "46"},
    {"id": "915", "name": "Ghyanglekh", "name_ne": "\u0918\u094d\u092f\u093e\u0919\u0932\u0947\u0916",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "34"},
    {"id": "901", "name": "Gokulganga", "name_ne": "\u0917\u094b\u0915\u0941\u0932\u0917\u0919\u094d\u0917\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "32"},
    {"id": "921", "name": "Bhotekoshi", "name_ne": "\u092d\u094b\u091f\u0947\u0915\u094b\u0936\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "35"},
    {"id": "762", "name": "Bhot Khola", "name_ne": "\u092d\u094b\u091f\u0916\u094b\u0932\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "9"},
    {"id": "1043", "name": "Bhume", "name_ne": "\u092d\u0942\u092e\u0947", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "77"},
    {"id": "873", "name": "Bhumlu", "name_ne": "\u092d\u0941\u092e\u094d\u0932\u0941", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "28"},
    {"id": "868", "name": "Bigu", "name_ne": "\u0935\u093f\u0917\u0941", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "26"},
    {"id": "969", "name": "Bihadi", "name_ne": "\u0935\u093f\u0939\u093e\u0926\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "44"},
    {"id": "1014", "name": "Bijaynagar", "name_ne": "\u0935\u093f\u091c\u092f\u0928\u0917\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "52"},
    {"id": "963", "name": "Binayi Triveni",
     "name_ne": "\u0935\u093f\u0928\u092f\u0940 \u0924\u094d\u0930\u093f\u0935\u0947\u0923\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "43"},
    {"id": "815", "name": "Bindabasini",
     "name_ne": "\u092c\u093f\u0928\u094d\u0926\u092c\u093e\u0938\u093f\u0928\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "18"},
    {"id": "972", "name": "Biruwa", "name_ne": "\u0935\u093f\u0930\u0941\u0935\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "45"},
    {"id": "839", "name": "Bishnu", "name_ne": "\u0935\u093f\u0937\u094d\u0923\u0941 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "21"},
    {"id": "798", "name": "Bishrampur", "name_ne": "\u0935\u093f\u0936\u094d\u0930\u093e\u092e\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "15"},
    {"id": "1124", "name": "Bitthadchir", "name_ne": "\u092c\u093f\u0924\u094d\u0925\u0921\u091a\u093f\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "70"},
    {"id": "834", "name": "Bramhapuri", "name_ne": "\u092c\u094d\u0930\u0939\u094d\u092e\u092a\u0941\u0930\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "21"},
    {"id": "722", "name": "Buddha Shanti",
     "name_ne": "\u092c\u0941\u0926\u094d\u0927\u0936\u093e\u0928\u094d\u0924\u093f", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "4"},
    {"id": "737", "name": "Budi Ganga", "name_ne": "\u092c\u0941\u0922\u0940\u0917\u0902\u0917\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "6"},
    {"id": "964", "name": "Bulingtar", "name_ne": "\u092c\u0941\u0932\u093f\u0919\u091f\u093e\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "43"},
    {"id": "836", "name": "Chakraghatta", "name_ne": "\u091a\u0915\u094d\u0930\u0918\u091f\u094d\u091f\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "21"},
    {"id": "950", "name": "Chame", "name_ne": "\u091a\u093e\u092e\u0947", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "40"},
    {"id": "745", "name": "Champadevi", "name_ne": "\u091a\u092e\u094d\u092a\u093e\u0926\u0947\u0935\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "7"},
    {"id": "1005", "name": "Chandrakot", "name_ne": "\u091a\u0928\u094d\u0926\u094d\u0930\u0915\u094b\u091f",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "51"},
    {"id": "913", "name": "Golanjor", "name_ne": "\u0917\u094b\u0932\u0928\u094d\u091c\u094b\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "34"},
    {"id": "907", "name": "Gosaikund", "name_ne": "\u0917\u094b\u0938\u093e\u0908\u0915\u0941\u0923\u094d\u0921",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "33"},
    {"id": "741", "name": "Gramthan", "name_ne": "\u0917\u094d\u0930\u093e\u092e\u0925\u093e\u0928",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "6"},
    {"id": "1003", "name": "Gulmi Durbar",
     "name_ne": "\u0917\u0941\u0932\u094d\u092e\u0940\u0926\u0930\u0935\u093e\u0930", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "51"},
    {"id": "1056", "name": "Gurans", "name_ne": "\u0917\u0941\u0930\u093e\u0901\u0938", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "58"},
    {"id": "1086", "name": "Guthichaur", "name_ne": "\u0917\u0941\u0920\u093f\u091a\u094c\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "62"},
    {"id": "727", "name": "Haldibari", "name_ne": "\u0939\u0932\u094d\u0926\u0940\u0935\u093e\u0930\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "4"},
    {"id": "911", "name": "Hariharpurgadhi",
     "name_ne": "\u0939\u0930\u093f\u0939\u0930\u092a\u0941\u0930\u0917\u0922\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "34"},
    {"id": "771", "name": "Harinagara", "name_ne": "\u0939\u0930\u093f\u0928\u0917\u0930\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "11"},
    {"id": "973", "name": "Harinas", "name_ne": "\u0939\u0930\u0940\u0928\u093e\u0938", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "45"},
    {"id": "704", "name": "Hatuwagadhi", "name_ne": "\u0939\u0924\u0941\u0935\u093e\u0917\u0922\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "1"},
    {"id": "920", "name": "Helambu", "name_ne": "\u0939\u0947\u0932\u092e\u094d\u092c\u0941", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "35"},
    {"id": "753", "name": "Hilihang", "name_ne": "\u0939\u093f\u0932\u093f\u0939\u093e\u0919", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "8"},
    {"id": "1085", "name": "Hima", "name_ne": "\u0939\u093f\u092e\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "62"},
    {"id": "1135", "name": "Himali", "name_ne": "\u0939\u093f\u092e\u093e\u0932\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "71"},
    {"id": "962", "name": "Hupsekot", "name_ne": "\u0939\u0941\u092a\u094d\u0938\u0947\u0915\u094b\u091f",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "43"},
    {"id": "851", "name": "Ichchhakamana", "name_ne": "\u0907\u091a\u094d\u091b\u093e\u0915\u093e\u092e\u0928\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "24"},
    {"id": "887", "name": "Indrasarowar",
     "name_ne": "\u0908\u0928\u094d\u0926\u094d\u0930 \u0938\u0930\u094b\u0935\u0930", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "30"}, {"id": "916", "name": "Indrawati",
                                                                                  "name_ne": "\u0930\u094d\u0907\u0928\u094d\u0926\u094d\u0930\u093e\u0935\u0924\u0940",
                                                                                  "alternative_names": [],
                                                                                  "alternative_names_ne": [],
                                                                                  "category": "Gaunpalika",
                                                                                  "district_id": "35"},
    {"id": "1008", "name": "Isma", "name_ne": "\u0908\u0938\u094d\u092e\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "51"},
    {"id": "1066", "name": "Jagadulla", "name_ne": "\u091c\u0917\u0926\u0941\u0932\u094d\u0932\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "59"},
    {"id": "1134", "name": "Jagannath", "name_ne": "\u091c\u0917\u0928\u094d\u0928\u093e\u0925",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "71"},
    {"id": "813", "name": "Jagarnathpur", "name_ne": "\u091c\u0917\u0930\u0928\u093e\u0925\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "18"},
    {"id": "736", "name": "Jahada", "name_ne": "\u091c\u0939\u0926\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "6"},
    {"id": "966", "name": "Jaljala", "name_ne": "\u091c\u0932\u091c\u0932\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "44"},
    {"id": "803", "name": "Janak Nandini", "name_ne": "\u091c\u0928\u0915\u0928\u0928\u094d\u0926\u093f\u0928\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "16"},
    {"id": "731", "name": "Jantedhunga", "name_ne": "\u091c\u0928\u094d\u0924\u0947\u0922\u0941\u0902\u0917\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "5"},
    {"id": "817", "name": "Jeera Bhavani", "name_ne": "\u091c\u093f\u0930\u093e \u092d\u0935\u093e\u0928\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "18"},
    {"id": "724", "name": "Jhapa", "name_ne": "\u091d\u093e\u092a\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "4"},
    {"id": "1028", "name": "Jhimaruk", "name_ne": "\u091d\u093f\u092e\u0930\u0941\u0915", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "55"},
    {"id": "1152", "name": "Jorayal", "name_ne": "\u091c\u094b\u0930\u093e\u092f\u0932", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "74"},
    {"id": "1158", "name": "Joshipur", "name_ne": "\u091c\u094b\u0936\u0940\u092a\u0941\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "75"},
    {"id": "918", "name": "Jugal", "name_ne": "\u091c\u0941\u0917\u0932", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "35"},
    {"id": "1076", "name": "Junichande", "name_ne": "\u091c\u0941\u0928\u0940\u091a\u093e\u0901\u0926\u0947",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "61"},
    {"id": "856", "name": "Jwalamukhi", "name_ne": "\u091c\u094d\u0935\u093e\u0932\u093e\u092e\u0942\u0916\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "25"},
    {"id": "723", "name": "Kachankawal", "name_ne": "\u0915\u091a\u0928\u0915\u0935\u0932", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "4"},
    {"id": "1064", "name": "Kaike", "name_ne": "\u0915\u093e\u0908\u0915\u0947", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "59"},
    {"id": "1157", "name": "Kailari", "name_ne": "\u0915\u0948\u0932\u093e\u0930\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "75"},
    {"id": "885", "name": "Kailash", "name_ne": "\u0915\u0948\u0932\u093e\u0936", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "30"},
    {"id": "888", "name": "Kakani", "name_ne": "\u0915\u0915\u0928\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "31"},
    {"id": "905", "name": "Kalika", "name_ne": "\u0915\u093e\u0932\u093f\u0915\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "33"},
    {"id": "818", "name": "Kalikamai", "name_ne": "\u0915\u093e\u0932\u093f\u0915\u093e\u092e\u093e\u0908 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "18"},
    {"id": "1100", "name": "Kalimati", "name_ne": "\u0915\u093e\u0932\u0940\u092e\u093e\u091f\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "66"},
    {"id": "863", "name": "Kalinchok", "name_ne": "\u0915\u093e\u0932\u093f\u0928\u094d\u091a\u094b\u0915",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "26"},
    {"id": "721", "name": "Kamal", "name_ne": "\u0915\u092e\u0932", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "4"},
    {"id": "1083", "name": "Kanaka Sundari",
     "name_ne": "\u0915\u0928\u0915\u093e\u0938\u0941\u0928\u094d\u0926\u0930\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "62"},
    {"id": "1055", "name": "Kanchan", "name_ne": "\u0915\u091e\u094d\u091a\u0928", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "57"},
    {"id": "740", "name": "Kanepokhari", "name_ne": "\u0915\u093e\u0928\u0947\u092a\u094b\u0916\u0930\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "6"},
    {"id": "1103", "name": "Kapurkot", "name_ne": "\u0915\u092a\u0941\u0930\u0915\u094b\u091f",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "66"},
    {"id": "796", "name": "Karaiyamai", "name_ne": "\u0915\u0930\u0948\u092f\u093e\u092e\u093e\u0908 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "15"},
    {"id": "738", "name": "Katahari", "name_ne": "\u0915\u091f\u0939\u0930\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "6"},
    {"id": "926", "name": "Kathekhola", "name_ne": "\u0915\u093e\u0920\u0947\u0916\u094b\u0932\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "36"},
    {"id": "837", "name": "Kaudena", "name_ne": "\u0915\u094c\u0921\u0947\u0928\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "21"},
    {"id": "1122", "name": "Kedarsyu", "name_ne": "\u0915\u0947\u0926\u093e\u0930\u0938\u094d\u092f\u0941",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "70"},
    {"id": "732", "name": "Kepilasgadhi", "name_ne": "\u0915\u0947\u092a\u093f\u0932\u093e\u0938\u0917\u0922\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "5"},
    {"id": "742", "name": "Kerabari", "name_ne": "\u0915\u0947\u0930\u093e\u0935\u093e\u0930\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "6"},
    {"id": "988", "name": "Khajura", "name_ne": "\u0916\u091c\u0941\u0930\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "48"},
    {"id": "713", "name": "Khalsa Chhintang Sahidbhumi",
     "name_ne": "\u0916\u093e\u0932\u094d\u0938\u093e \u091b\u093f\u0928\u094d\u0924\u093e\u0919 \u0938\u0939\u0940\u0926\u092d\u0942\u092e\u093f",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "2"},
    {"id": "898", "name": "Khandadevi", "name_ne": "\u0916\u093e\u0901\u0921\u093e\u0926\u0947\u0935\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "32"},
    {"id": "876", "name": "Khanikhola", "name_ne": "\u0916\u093e\u0928\u0940\u0916\u094b\u0932\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "28"},
    {"id": "861", "name": "Khaniyabas", "name_ne": "\u0916\u0928\u093f\u092f\u093e\u092c\u093e\u0938",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "25"},
    {"id": "1132", "name": "Khaptad Chhededaha",
     "name_ne": "\u0916\u092a\u094d\u0924\u0921 \u091b\u0947\u0921\u0947\u0926\u0939", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "71"},
    {"id": "1072", "name": "Kharpunath", "name_ne": "\u0916\u093e\u0930\u094d\u092a\u0941\u0928\u093e\u0925",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "60"},
    {"id": "1093", "name": "Khatyad", "name_ne": "\u0916\u0924\u094d\u092f\u093e\u0921", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "64"},
    {"id": "749", "name": "Khiji Demba", "name_ne": "\u0916\u093f\u091c\u093f\u0926\u0947\u092e\u094d\u092c\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "7"},
    {"id": "728", "name": "Khotehang", "name_ne": "\u0916\u094b\u091f\u0947\u0939\u093e\u0919",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "5"},
    {"id": "864", "name": "Melung", "name_ne": "\u092e\u0947\u0932\u0941\u0919", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "26"},
    {"id": "768", "name": "Khumbu Pasang Lhamu",
     "name_ne": "\u0916\u0941\u092e\u094d\u092c\u0941 \u092a\u093e\u0938\u093e\u0919\u0932\u094d\u0939\u092e\u0941",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "10"},
    {"id": "1151", "name": "K.I. Singh", "name_ne": "\u0915\u0947\u0906\u0908\u0938\u093f\u0902\u0939",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "74"},
    {"id": "896", "name": "Kispang", "name_ne": "\u0915\u093f\u0938\u094d\u092a\u093e\u0919", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "31"},
    {"id": "878", "name": "Konjyosom", "name_ne": "\u0915\u094b\u0928\u094d\u091c\u094d\u092f\u094b\u0938\u094b\u092e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "29"},
    {"id": "770", "name": "Koshi", "name_ne": "\u0915\u094b\u0936\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "11"},
    {"id": "1048", "name": "Kotahimai", "name_ne": "\u0915\u094b\u091f\u0939\u0940\u092e\u093e\u0908",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "57"},
    {"id": "1099", "name": "Kumakh", "name_ne": "\u0915\u0941\u092e\u093e\u0916", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "66"},
    {"id": "756", "name": "Kummayak", "name_ne": "\u0915\u0941\u092e\u094d\u092e\u093e\u092f\u0915",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "8"},
    {"id": "1077", "name": "Kuse", "name_ne": "\u0915\u0941\u0938\u0947", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "61"}, {"id": "947", "name": "Kwaholasothar",
                                                                                  "name_ne": "\u0915\u094d\u0935\u094d\u0939\u094b\u0932\u093e\u0938\u094b\u0925\u093e\u0930",
                                                                                  "alternative_names": [],
                                                                                  "alternative_names_ne": [],
                                                                                  "category": "Gaunpalika",
                                                                                  "district_id": "39"},
    {"id": "801", "name": "Laksminiya",
     "name_ne": "\u0932\u0915\u094d\u0937\u094d\u092e\u0940\u0928\u093f\u092f\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "16"},
    {"id": "842", "name": "Laksmipur Patari",
     "name_ne": "\u0932\u0915\u094d\u0937\u094d\u092e\u0940\u092a\u0941\u0930 \u092a\u0924\u093e\u0930\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "22"},
    {"id": "1162", "name": "Laljhadi", "name_ne": "\u0932\u093e\u0932\u091d\u093e\u0901\u0921\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "76"},
    {"id": "734", "name": "Lamidanda", "name_ne": "\u0932\u093e\u092e\u0940\u0921\u093e\u0901\u0921\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "5"},
    {"id": "1145", "name": "Lekam", "name_ne": "\u0932\u0947\u0915\u092e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "73"},
    {"id": "769", "name": "Likhu Pike", "name_ne": "\u0932\u093f\u0916\u0941\u092a\u093f\u0915\u0947",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "10"},
    {"id": "899", "name": "Likhu Tamakoshi",
     "name_ne": "\u0932\u093f\u0916\u0941 \u0924\u093e\u092e\u093e\u0915\u094b\u0936\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "32"},
    {"id": "791", "name": "Limchungbung", "name_ne": "\u0932\u093f\u092e\u094d\u091a\u0941\u0919\u092c\u0941\u0919",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "14"},
    {"id": "923", "name": "Lisankhu Pakhar",
     "name_ne": "\u0932\u093f\u0938\u0902\u0916\u0941 \u092a\u093e\u0916\u0930", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "35"},
    {"id": "955", "name": "Lomanthang", "name_ne": "\u0932\u094b\u092e\u0928\u094d\u0925\u093e\u0919",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "41"},
    {"id": "956", "name": "Lo-Thekar Damodarkunda",
     "name_ne": "\u0932\u094b-\u0925\u0947\u0915\u0930 \u0926\u093e\u092e\u094b\u0926\u0930\u0915\u0941\u0923\u094d\u0921",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "41"},
    {"id": "1036", "name": "Lungri", "name_ne": "\u0932\u0941\u0919\u094d\u0917\u094d\u0930\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "56"},
    {"id": "941", "name": "Machhapuchhre", "name_ne": "\u092e\u093e\u091b\u093e\u092a\u0941\u091b\u094d\u0930\u0947",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "38"},
    {"id": "1004", "name": "Madane", "name_ne": "\u092e\u0926\u093e\u0928\u0947", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "51"},
    {"id": "874", "name": "Mahabharat", "name_ne": "\u092e\u0939\u093e\u092d\u093e\u0930\u0924",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "28"},
    {"id": "1059", "name": "Mahabu", "name_ne": "\u092e\u0939\u093e\u0935\u0941", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "58"},
    {"id": "827", "name": "Mahadeva", "name_ne": "\u092e\u0939\u093e\u0926\u0947\u0935\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "20"},
    {"id": "766", "name": "Maha Kulung", "name_ne": "\u092e\u0939\u093e\u0915\u0941\u0932\u0941\u0919",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "10"},
    {"id": "879", "name": "Mahankal", "name_ne": "\u092e\u0939\u093e\u0919\u094d\u0915\u093e\u0932",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "29"},
    {"id": "970", "name": "Mahashila", "name_ne": "\u092e\u0939\u093e\u0936\u093f\u0932\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "44"},
    {"id": "1092", "name": "Mahawai", "name_ne": "\u092e\u0939\u093e\u0935\u0948", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "63"},
    {"id": "716", "name": "Mai Jogmai", "name_ne": "\u092e\u093e\u0908\u091c\u094b\u0917\u092e\u093e\u0908",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "3"},
    {"id": "782", "name": "Maiwa Khola", "name_ne": "\u092e\u0948\u0935\u093e\u0916\u094b\u0932\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "12"},
    {"id": "758", "name": "Makalu", "name_ne": "\u092e\u0915\u093e\u0932\u0941", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "9"},
    {"id": "884", "name": "Makawanpurgadhi",
     "name_ne": "\u092e\u0915\u0935\u093e\u0928\u092a\u0941\u0930\u0917\u0922\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "30"},
    {"id": "983", "name": "Malarani", "name_ne": "\u092e\u093e\u0932\u093e\u0930\u093e\u0928\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "47"},
    {"id": "1143", "name": "Malikarjun",
     "name_ne": "\u092e\u093e\u0932\u093f\u0915\u093e\u0930\u094d\u091c\u0941\u0928", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "73"},
    {"id": "1032", "name": "Mallarani", "name_ne": "\u092e\u0932\u094d\u0932\u0930\u093e\u0928\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "55"},
    {"id": "948", "name": "Manang Disyang",
     "name_ne": "\u092e\u0928\u093e\u0919 \u0921\u093f\u0938\u094d\u092f\u093e\u0919", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "40"},
    {"id": "1033", "name": "Mandavi", "name_ne": "\u092e\u093e\u0923\u094d\u0921\u0935\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "55"}, {"id": "744", "name": "Manebhanjyang",
                                                                                  "name_ne": "\u092e\u093e\u0928\u0947\u092d\u091e\u094d\u091c\u094d\u092f\u093e\u0919",
                                                                                  "alternative_names": [],
                                                                                  "alternative_names_ne": [],
                                                                                  "category": "Gaunpalika",
                                                                                  "district_id": "7"},
    {"id": "958", "name": "Mangala", "name_ne": "\u092e\u0902\u0917\u0932\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "42"},
    {"id": "719", "name": "Mangsebung", "name_ne": "\u092e\u093e\u0919\u0938\u0947\u092c\u0941\u0919",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "3"},
    {"id": "881", "name": "Manhari", "name_ne": "\u092e\u0928\u0939\u0930\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "30"},
    {"id": "1049", "name": "Marchawarimai",
     "name_ne": "\u092e\u0930\u094d\u091a\u0935\u093e\u0930\u0940\u092e\u093e\u0908", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "57"},
    {"id": "910", "name": "Marin", "name_ne": "\u092e\u0930\u093f\u0923", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "34"},
    {"id": "1144", "name": "Marma", "name_ne": "\u092e\u093e\u0930\u094d\u092e\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "73"},
    {"id": "944", "name": "Marsyangdi", "name_ne": "\u092e\u0930\u094d\u0938\u094d\u092f\u093e\u0919\u0926\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "39"},
    {"id": "1127", "name": "Masta", "name_ne": "\u092e\u0937\u094d\u091f\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "70"},
    {"id": "1020", "name": "Mathagadhi", "name_ne": "\u092e\u093e\u0925\u093e\u0917\u0922\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "54"},
    {"id": "1113", "name": "Mellekh", "name_ne": "\u092e\u0947\u0932\u094d\u0932\u0947\u0916", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "68"},
    {"id": "787", "name": "Menchayayem", "name_ne": "\u092e\u0947\u0928\u094d\u091b\u092f\u093e\u092f\u0947\u092e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "13"},
    {"id": "779", "name": "Meringden", "name_ne": "\u092e\u0947\u0930\u093f\u0919\u0926\u0947\u0928",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "12"},
    {"id": "783", "name": "Mikwa Khola", "name_ne": "\u092e\u093f\u0915\u094d\u0935\u093e\u0916\u094b\u0932\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "12"},
    {"id": "967", "name": "Modi", "name_ne": "\u092e\u094b\u0926\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "44"},
    {"id": "1160", "name": "Mohanyal", "name_ne": "\u092e\u094b\u0939\u0928\u094d\u092f\u093e\u0932",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "75"},
    {"id": "747", "name": "Molung", "name_ne": "\u092e\u094b\u0932\u0941\u0919", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "7"},
    {"id": "1063", "name": "Mudkechula", "name_ne": "\u092e\u0941\u0921\u094d\u0915\u0947\u091a\u0941\u0932\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "59"},
    {"id": "1095", "name": "Mugum Karmarong",
     "name_ne": "\u092e\u0941\u0917\u0941\u092e \u0915\u093e\u0930\u094d\u092e\u093e\u0930\u094b\u0902\u0917",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "64"},
    {"id": "802", "name": "Mukhiyapatti Musaharmiya",
     "name_ne": "\u092e\u0941\u0916\u093f\u092f\u093e\u092a\u091f\u094d\u091f\u0940 \u092e\u0941\u0938\u0939\u0930\u092e\u093f\u092f\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "16"},
    {"id": "897", "name": "Myagang", "name_ne": "\u092e\u094d\u092f\u093e\u0917\u0919", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "31"},
    {"id": "978", "name": "Myagde", "name_ne": "\u092e\u094d\u092f\u093e\u0917\u094d\u0926\u0947",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "46"},
    {"id": "1075", "name": "Namkha", "name_ne": "\u0928\u093e\u092e\u094d\u0916\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "60"},
    {"id": "847", "name": "Naraha", "name_ne": "\u0928\u0930\u0939\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "22"},
    {"id": "991", "name": "Narainapur", "name_ne": "\u0928\u0930\u0948\u0928\u093e\u092a\u0941\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "48"},
    {"id": "1087", "name": "Narharinath", "name_ne": "\u0928\u0930\u0939\u0930\u093f\u0928\u093e\u0925",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "63"},
    {"id": "951", "name": "Narpa Bhumi", "name_ne": "\u0928\u093e\u0930\u094d\u092a\u093e \u092d\u0942\u092e\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "40"},
    {"id": "949", "name": "Nason", "name_ne": "\u0928\u093e\u0938\u094b\u0901", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "40"},
    {"id": "1027", "name": "Naubahini", "name_ne": "\u0928\u094c\u092c\u0939\u093f\u0928\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "55"},
    {"id": "1142", "name": "Naugad", "name_ne": "\u0928\u094c\u0917\u093e\u0921", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "73"},
    {"id": "904", "name": "Naukunda", "name_ne": "\u0928\u094c\u0915\u0941\u0923\u094d\u0921", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "33"},
    {"id": "1058", "name": "Naumule", "name_ne": "\u0928\u094c\u092e\u0941\u0932\u0947", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "58"},
    {"id": "1137", "name": "Navadurga", "name_ne": "\u0928\u0935\u0926\u0941\u0930\u094d\u0917\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "72"},
    {"id": "848", "name": "Nawarajpur", "name_ne": "\u0928\u0935\u0930\u093e\u091c\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "22"},
    {"id": "764", "name": "Necha Salyan", "name_ne": "\u0928\u0947\u091a\u093e\u0938\u0932\u094d\u092f\u093e\u0928",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "10"},
    {"id": "792", "name": "Subarna", "name_ne": "\u0938\u0941\u0935\u0930\u094d\u0923\u00a0 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "15"},
    {"id": "860", "name": "Netrawati Dabjong",
     "name_ne": "\u0928\u0947\u0924\u094d\u0930\u093e\u0935\u0924\u0940 \u0921\u092c\u091c\u094b\u0919",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "25"},
    {"id": "927", "name": "Nisikhola", "name_ne": "\u0928\u093f\u0938\u0940\u0916\u094b\u0932\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "36"},
    {"id": "1054", "name": "Om Satiya", "name_ne": "\u0913\u092e\u0938\u0924\u0940\u092f\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "57"},
    {"id": "1091", "name": "Pachaljharana", "name_ne": "\u092a\u091a\u093e\u0932\u091d\u0930\u0928\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "63"},
    {"id": "819", "name": "Pakaha Mainpur",
     "name_ne": "\u092a\u0915\u093e\u0939\u093e \u092e\u0948\u0928\u092a\u0941\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "18"},
    {"id": "1088", "name": "Palata", "name_ne": "\u092a\u0932\u093e\u0924\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "63"}, {"id": "1018", "name": "Palhi Nandan",
                                                                                  "name_ne": "\u092a\u093e\u0932\u094d\u0939\u0940\u0928\u0928\u094d\u0926\u0928",
                                                                                  "alternative_names": [],
                                                                                  "alternative_names_ne": [],
                                                                                  "category": "Gaunpalika",
                                                                                  "district_id": "53"},
    {"id": "894", "name": "Panchakanya", "name_ne": "\u092a\u091e\u094d\u091a\u0915\u0928\u094d\u092f\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "31"},
    {"id": "1119", "name": "Pancheshwar", "name_ne": "\u092a\u091e\u094d\u091a\u0947\u0936\u094d\u0935\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "69"},
    {"id": "917", "name": "Panchpokhari Thangpal",
     "name_ne": "\u092a\u093e\u0901\u091a\u092a\u094b\u0916\u0930\u0940 \u0925\u093e\u0919\u092a\u093e\u0932",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "35"},
    {"id": "984", "name": "Pandini", "name_ne": "\u092a\u093e\u0923\u093f\u0928\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "47"},
    {"id": "800", "name": "Parawanipur", "name_ne": "\u092a\u0930\u0935\u093e\u0928\u0940\u092a\u0941\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "15"},
    {"id": "1038", "name": "Paribartan", "name_ne": "\u092a\u0930\u093f\u0935\u0930\u094d\u0924\u0928",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "56"},
    {"id": "841", "name": "Parsa", "name_ne": "\u092a\u0930\u094d\u0938\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "21"},
    {"id": "1081", "name": "Patarasi", "name_ne": "\u092a\u093e\u0924\u093e\u0930\u093e\u0938\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "62"},
    {"id": "816", "name": "Paterwa Sugauli",
     "name_ne": "\u092a\u091f\u0947\u0930\u094d\u0935\u093e \u0938\u0941\u0917\u094c\u0932\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "18"},
    {"id": "778", "name": "Pathibhara Yangwarak",
     "name_ne": "\u092a\u093e\u0925\u0940\u092d\u0930\u093e \u092f\u093e\u0919\u0935\u0930\u0915",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "12"},
    {"id": "709", "name": "Pauwadungma", "name_ne": "\u092a\u094c\u0935\u093e\u0926\u0941\u0919\u092e\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "1"},
    {"id": "715", "name": "Phakphokthum", "name_ne": "\u092b\u093e\u0915\u092b\u094b\u0915\u0925\u0941\u092e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "3"},
    {"id": "781", "name": "Phaktanglung", "name_ne": "\u092b\u0915\u094d\u0924\u093e\u0919\u0932\u0941\u0919",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "12"},
    {"id": "754", "name": "Phalelung", "name_ne": "\u092b\u093e\u0932\u0947\u0932\u0941\u0919",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "8"},
    {"id": "752", "name": "Phalgunanda", "name_ne": "\u092b\u093e\u0932\u094d\u0917\u0941\u0928\u0928\u094d\u0926",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "8"},
    {"id": "785", "name": "Phedap", "name_ne": "\u092b\u0947\u0926\u093e\u092a", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "13"},
    {"id": "976", "name": "Phedikhola", "name_ne": "\u092b\u0947\u0926\u0940\u0916\u094b\u0932\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "45"},
    {"id": "795", "name": "Pheta", "name_ne": "\u092b\u0947\u091f\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "15"},
    {"id": "914", "name": "Phikkal", "name_ne": "\u092b\u093f\u0915\u094d\u0915\u0932", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "34"},
    {"id": "808", "name": "Pipara", "name_ne": "\u092a\u093f\u092a\u0930\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "17"},
    {"id": "797", "name": "Prasauni", "name_ne": "\u092a\u094d\u0930\u0938\u094c\u0928\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "15"},
    {"id": "1016", "name": "Pratappur", "name_ne": "\u092a\u094d\u0930\u0924\u093e\u092a\u092a\u0941\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "53"},
    {"id": "1024", "name": "Purbakhola", "name_ne": "\u092a\u0942\u0930\u094d\u0935\u0916\u094b\u0932\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "54"},
    {"id": "1150", "name": "Purbichauki", "name_ne": "\u092a\u0942\u0930\u094d\u0935\u0940\u091a\u094c\u0915\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "74"},
    {"id": "1044", "name": "Putha Uttarganga",
     "name_ne": "\u092a\u0941\u0920\u093e \u0909\u0924\u094d\u0924\u0930\u0917\u0902\u0917\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "77"},
    {"id": "959", "name": "Raghuganga", "name_ne": "\u0930\u0918\u0941\u0917\u0902\u0917\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "42"},
    {"id": "1019", "name": "Rainadevi Chhahara",
     "name_ne": "\u0930\u0948\u0928\u093e\u0926\u0947\u0935\u0940 \u091b\u0939\u0930\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "54"},
    {"id": "998", "name": "Rajpur", "name_ne": "\u0930\u093e\u091c\u092a\u0941\u0930", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "50"},
    {"id": "883", "name": "Raksirang", "name_ne": "\u0930\u093e\u0915\u094d\u0938\u093f\u0930\u093e\u0919\u094d\u0917",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "30"},
    {"id": "1110", "name": "Ramaroshan", "name_ne": "\u0930\u093e\u092e\u093e\u0930\u094b\u0936\u0928",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "68"},
    {"id": "1023", "name": "Rambha", "name_ne": "\u0930\u092e\u094d\u092d\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "54"},
    {"id": "835", "name": "Ramnagar", "name_ne": "\u0930\u093e\u092e\u0928\u0917\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "21"}, {"id": "705", "name": "Ramprasad Rai",
                                                                                  "name_ne": "\u0930\u093e\u092e\u092a\u094d\u0930\u0938\u093e\u0926 \u0930\u093e\u0908",
                                                                                  "alternative_names": [],
                                                                                  "alternative_names_ne": [],
                                                                                  "category": "Gaunpalika",
                                                                                  "district_id": "1"},
    {"id": "994", "name": "Rapti", "name_ne": "\u0930\u093e\u092a\u094d\u0924\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "50"}, {"id": "986", "name": "Raptisonari",
                                                                                  "name_ne": "\u0930\u093e\u092a\u094d\u0924\u0940 \u0938\u094b\u0928\u093e\u0930\u0940",
                                                                                  "alternative_names": [],
                                                                                  "alternative_names_ne": [],
                                                                                  "category": "Gaunpalika",
                                                                                  "district_id": "48"},
    {"id": "789", "name": "Rautamai", "name_ne": "\u0930\u094c\u0924\u093e\u092e\u093e\u0908", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "14"},
    {"id": "1026", "name": "Ribdikot", "name_ne": "\u0930\u093f\u092c\u094d\u0926\u0940\u0915\u094b\u091f",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "54"},
    {"id": "977", "name": "Rishing", "name_ne": "\u090b\u0937\u093f\u0919\u094d\u0917", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "46"},
    {"id": "1052", "name": "Rohini", "name_ne": "\u0930\u094b\u0939\u093f\u0923\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "57"},
    {"id": "718", "name": "Rong", "name_ne": "\u0930\u094b\u0919", "alternative_names": [], "alternative_names_ne": [],
     "category": "Gaunpalika", "district_id": "3"},
    {"id": "870", "name": "Roshi", "name_ne": "\u0930\u094b\u0936\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "28"},
    {"id": "862", "name": "Ruby Valley", "name_ne": "\u0930\u0941\u0935\u0940 \u092d\u094d\u092f\u093e\u0932\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "25"},
    {"id": "1035", "name": "Runtigadhi", "name_ne": "\u0930\u0941\u0928\u094d\u091f\u0940\u0917\u0922\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "56"},
    {"id": "943", "name": "Rupa", "name_ne": "\u0930\u0942\u092a\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "38"},
    {"id": "829", "name": "Rupani", "name_ne": "\u0930\u0941\u092a\u0928\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "20"},
    {"id": "1010", "name": "Ruru", "name_ne": "\u0930\u0941\u0930\u0941", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "51"},
    {"id": "760", "name": "Sabhapokhari", "name_ne": "\u0938\u092d\u093e\u092a\u094b\u0916\u0930\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "9"},
    {"id": "1131", "name": "Saipal", "name_ne": "\u0938\u0907\u092a\u093e\u0932", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "70"},
    {"id": "735", "name": "Sakela", "name_ne": "\u0938\u093e\u0915\u0947\u0932\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "5"},
    {"id": "849", "name": "Sakhuwanankarkatti",
     "name_ne": "\u0938\u0916\u0941\u0935\u093e\u0928\u093e\u0928\u094d\u0915\u093e\u0930\u0915\u091f\u094d\u091f\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "22"},
    {"id": "812", "name": "Sakhuwa Prasauni",
     "name_ne": "\u0938\u0916\u0941\u0935\u093e \u092a\u094d\u0930\u0938\u094c\u0928\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "18"}, {"id": "710", "name": "Salpasilichho",
                                                                                  "name_ne": "\u0938\u093e\u0932\u094d\u092a\u093e\u0938\u093f\u0932\u093f\u091b\u094b",
                                                                                  "alternative_names": [],
                                                                                  "alternative_names_ne": [],
                                                                                  "category": "Gaunpalika",
                                                                                  "district_id": "1"},
    {"id": "1051", "name": "Sammarimai", "name_ne": "\u0938\u092e\u094d\u092e\u0930\u0940\u092e\u093e\u0908",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "57"},
    {"id": "809", "name": "Samsi", "name_ne": "\u0938\u093e\u092e\u094d\u0938\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "17"},
    {"id": "720", "name": "Sandakpur", "name_ne": "\u0938\u0928\u094d\u0926\u0915\u092a\u0941\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "3"},
    {"id": "711", "name": "Sangurigadhi", "name_ne": "\u0938\u093e\u0917\u0941\u0930\u0940\u0917\u0922\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "2"},
    {"id": "1096", "name": "Sani Bheri", "name_ne": "\u0938\u093e\u0928\u0940\u092d\u0947\u0930\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "65"},
    {"id": "1090", "name": "Sanni Triveni",
     "name_ne": "\u0938\u093e\u0928\u094d\u0928\u0940 \u0924\u094d\u0930\u093f\u0935\u0947\u0923\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "63"},
    {"id": "1017", "name": "Sarawal", "name_ne": "\u0938\u0930\u093e\u0935\u0932", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "53"},
    {"id": "1070", "name": "Sarkegad", "name_ne": "\u0938\u0930\u094d\u0915\u0947\u0917\u093e\u0921",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "60"},
    {"id": "1031", "name": "Sarumarani", "name_ne": "\u0938\u0930\u0941\u092e\u093e\u0930\u093e\u0928\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "55"},
    {"id": "1001", "name": "Satyawati", "name_ne": "\u0938\u0924\u094d\u092f\u0935\u0924\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "51"},
    {"id": "1153", "name": "Sayal", "name_ne": "\u0938\u093e\u092f\u0932", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "74"},
    {"id": "931", "name": "Shahid Lakhan", "name_ne": "\u0936\u0939\u093f\u0926 \u0932\u0916\u0928",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "37"},
    {"id": "865", "name": "Shailung", "name_ne": "\u0936\u0948\u0932\u0941\u0919", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "26"},
    {"id": "997", "name": "Shantinagar", "name_ne": "\u0936\u093e\u0928\u094d\u0924\u093f\u0928\u0917\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "50"},
    {"id": "1065", "name": "She Phoksundo",
     "name_ne": "\u0936\u0947 \u092b\u094b\u0915\u094d\u0938\u0941\u0928\u094d\u0921\u094b", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "59"},
    {"id": "1079", "name": "Shivalaya", "name_ne": "\u0936\u093f\u0935\u093e\u0932\u092f", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "61"},
    {"id": "1121", "name": "Shivanath", "name_ne": "\u0936\u093f\u0935\u0928\u093e\u0925", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "69"},
    {"id": "890", "name": "Shivapuri", "name_ne": "\u0936\u093f\u0935\u092a\u0941\u0930\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "31"},
    {"id": "1089", "name": "Shubha Kalika", "name_ne": "\u0936\u0941\u092d \u0915\u093e\u0932\u093f\u0915\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "63"},
    {"id": "1105", "name": "Siddha Kumakh", "name_ne": "\u0938\u093f\u0926\u094d\u0927 \u0915\u0941\u092e\u093e\u0916",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "66"},
    {"id": "857", "name": "Siddhalekh", "name_ne": "\u0938\u093f\u0926\u094d\u0927\u0932\u0947\u0915",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "25"},
    {"id": "780", "name": "Sidingwa", "name_ne": "\u0938\u093f\u0926\u093f\u0919\u094d\u0935\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "12"},
    {"id": "1118", "name": "Sigas", "name_ne": "\u0938\u093f\u0917\u093e\u0938", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "69"},
    {"id": "759", "name": "Silichong", "name_ne": "\u0938\u093f\u0932\u0940\u091a\u094b\u0919",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "9"},
    {"id": "1069", "name": "Simkot", "name_ne": "\u0938\u093f\u092e\u0915\u094b\u091f", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "60"},
    {"id": "1107", "name": "Simta", "name_ne": "\u0938\u093f\u092e\u094d\u0924\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "67"},
    {"id": "1084", "name": "Sinja", "name_ne": "\u0938\u093f\u0902\u091c\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "62"},
    {"id": "934", "name": "Siranchok", "name_ne": "\u0938\u093f\u0930\u093e\u0928\u091a\u094b\u0915",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "37"},
    {"id": "776", "name": "Sirijangha", "name_ne": "\u0938\u093f\u0930\u0940\u091c\u0919\u094d\u0918\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "12"},
    {"id": "1045", "name": "Sisne", "name_ne": "\u0938\u093f\u0938\u094d\u0928\u0947", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "77"},
    {"id": "1050", "name": "Siyari", "name_ne": "\u0938\u093f\u092f\u093e\u0930\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "57"},
    {"id": "807", "name": "Sonama", "name_ne": "\u0938\u094b\u0928\u092e\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "17"},
    {"id": "1094", "name": "Soru", "name_ne": "\u0938\u094b\u0930\u0941", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "64"},
    {"id": "767", "name": "Sotang", "name_ne": "\u0938\u094b\u0924\u093e\u0919", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "10"},
    {"id": "902", "name": "Sunapati", "name_ne": "\u0938\u0941\u0928\u093e\u092a\u0924\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "32"},
    {"id": "1041", "name": "Sunchhahari", "name_ne": "\u0938\u0941\u0928\u091b\u0939\u0930\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "56"},
    {"id": "1034", "name": "Sunil Smriti",
     "name_ne": "\u0938\u0941\u0928\u093f\u0932 \u0938\u094d\u092e\u0943\u0924\u093f", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "56"},
    {"id": "1130", "name": "Surma", "name_ne": "\u0938\u0941\u0930\u094d\u092e\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "70"},
    {"id": "1120", "name": "Surnaya", "name_ne": "\u0938\u0941\u0930\u094d\u0928\u092f\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "69"},
    {"id": "893", "name": "Suryagadhi", "name_ne": "\u0938\u0941\u0930\u094d\u092f\u0917\u0922\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "31"},
    {"id": "1133", "name": "Swami Kartik Khapar",
     "name_ne": "\u0938\u094d\u0935\u093e\u092e\u093f\u0915\u093e\u0930\u094d\u0924\u093f\u0915 \u0916\u093e\u092a\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "71"},
    {"id": "891", "name": "Tadi", "name_ne": "\u0924\u093e\u0926\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "31"},
    {"id": "1129", "name": "Talkot", "name_ne": "\u0924\u0932\u0915\u094b\u091f", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "70"},
    {"id": "867", "name": "Tamakoshi", "name_ne": "\u0924\u093e\u092e\u093e\u0915\u094b\u0936\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "26"},
    {"id": "930", "name": "Tamankhola", "name_ne": "\u0924\u092e\u093e\u0928\u0916\u094b\u0932\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "36"},
    {"id": "1073", "name": "Tanjakot", "name_ne": "\u0924\u093e\u0901\u091c\u093e\u0915\u094b\u091f",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "60"},
    {"id": "790", "name": "Tapli", "name_ne": "\u0924\u093e\u092a\u094d\u0932\u0940", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "14"},
    {"id": "929", "name": "Tarakhola", "name_ne": "\u0924\u093e\u0930\u093e\u0916\u094b\u0932\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "36"},
    {"id": "895", "name": "Tarkeshwar", "name_ne": "\u0924\u093e\u0930\u0915\u0947\u0936\u094d\u0935\u0930",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "31"},
    {"id": "1080", "name": "Tatopani", "name_ne": "\u0924\u093e\u0924\u094b\u092a\u093e\u0928\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "62"},
    {"id": "871", "name": "Temal", "name_ne": "\u0924\u0947\u092e\u093e\u0932", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "28"},
    {"id": "852", "name": "Thakre", "name_ne": "\u0925\u093e\u0915\u094d\u0930\u0947 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "25"},
    {"id": "1123", "name": "Thalara", "name_ne": "\u0925\u0932\u093e\u0930\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "70"},
    {"id": "1060", "name": "Thantikandh", "name_ne": "\u0920\u093e\u0901\u091f\u0940\u0915\u093e\u0901\u0927",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "58"},
    {"id": "953", "name": "Thasang", "name_ne": "\u0925\u093e\u0938\u093e\u0919", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "41"},
    {"id": "1042", "name": "Thawang", "name_ne": "\u0925\u0935\u093e\u0919", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "56"},
    {"id": "820", "name": "Thori", "name_ne": "\u0920\u094b\u0930\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "18"},
    {"id": "1082", "name": "Tila", "name_ne": "\u0924\u093f\u0932\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "62"},
    {"id": "824", "name": "Tilathi Koiladi",
     "name_ne": "\u0924\u093f\u0932\u093e\u0920\u0940 \u0915\u094b\u0908\u0932\u093e\u0921\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "20"},
    {"id": "1025", "name": "Tinau", "name_ne": "\u0924\u093f\u0928\u093e\u0909", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "54"},
    {"id": "909", "name": "Tinpatan", "name_ne": "\u0924\u093f\u0928\u092a\u093e\u091f\u0928", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "34"},
    {"id": "832", "name": "Tirhut", "name_ne": "\u0924\u093f\u0930\u0939\u0941\u0924 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "20"},
    {"id": "1015", "name": "Triveni Susta",
     "name_ne": "\u0924\u094d\u0930\u093f\u0935\u0947\u0923\u0940 \u0938\u0941\u0938\u094d\u0924\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "53"},
    {"id": "757", "name": "Tumbewa", "name_ne": "\u0924\u0941\u092e\u094d\u092c\u0947\u0935\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "8"},
    {"id": "1112", "name": "Turmakhand", "name_ne": "\u0924\u0941\u0930\u094d\u092e\u093e\u0916\u093e\u0901\u0926",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "68"},
    {"id": "707", "name": "Tyamke Maiyunm",
     "name_ne": "\u091f\u094d\u092f\u093e\u092e\u094d\u0915\u0947\u092e\u0948\u092f\u0941\u092e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "1"},
    {"id": "788", "name": "Udayapurgadhi", "name_ne": "\u0909\u0926\u092f\u092a\u0941\u0930\u0917\u0922\u0940",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "14"},
    {"id": "903", "name": "Umakunda", "name_ne": "\u0909\u092e\u093e\u0915\u0941\u0923\u094d\u0921",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "32"},
    {"id": "906", "name": "Uttargaya", "name_ne": "\u0909\u0924\u094d\u0924\u0930\u0917\u092f\u093e",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "33"},
    {"id": "1147", "name": "Vyans", "name_ne": "\u092c\u094d\u092f\u093e\u0901\u0938", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "73"},
    {"id": "823", "name": "Yamunamai", "name_ne": "\u092f\u092e\u0941\u0928\u093e\u092e\u093e\u0908 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "19"},
    {"id": "755", "name": "Yangwarak", "name_ne": "\u092f\u093e\u0919\u0935\u0930\u0915", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "8"},
    {"id": "1013", "name": "Yasodhara", "name_ne": "\u092f\u0938\u094b\u0927\u0930\u093e", "alternative_names": [],
     "alternative_names_ne": [], "category": "Gaunpalika", "district_id": "52"},
    {"id": "551", "name": "Kankai", "name_ne": "\u0915\u0928\u094d\u0915\u093e\u0908 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "4"},
    {"id": "558", "name": "Khadak", "name_ne": "\u0916\u0921\u0915 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "20"},
    {"id": "560", "name": "Khandachakra", "name_ne": "\u0916\u093e\u0901\u0921\u093e\u091a\u0915\u094d\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "63"},
    {"id": "561", "name": "Khandbari", "name_ne": "\u0916\u093e\u0926\u0901\u0935\u093e\u0930\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "9"},
    {"id": "564", "name": "Kolhabi", "name_ne": "\u0915\u094b\u0932\u094d\u0939\u0935\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "15"},
    {"id": "567", "name": "Kshireshwor Nath",
     "name_ne": "\u0915\u094d\u0937\u093f\u0930\u0947\u0936\u094d\u0935\u0930\u0928\u093e\u0925 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "16"},
    {"id": "568", "name": "Kushma", "name_ne": "\u0915\u0941\u0936\u094d\u092e\u093e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "44"},
    {"id": "571", "name": "Laligurans", "name_ne": "\u0932\u093e\u0932\u093f\u0917\u0941\u0930\u093e\u0901\u0938 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "13"},
    {"id": "573", "name": "Lamahi", "name_ne": "\u0932\u092e\u0939\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "50"},
    {"id": "575", "name": "Lekbeshi", "name_ne": "\u0932\u0947\u0915\u092c\u0947\u0936\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "67"},
    {"id": "576", "name": "Letang", "name_ne": "\u0932\u0947\u091f\u093e\u0919 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "6"},
    {"id": "580", "name": "Madhuwan", "name_ne": "\u092e\u0927\u0941\u0935\u0928 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "49"},
    {"id": "581", "name": "Madhya Nepal", "name_ne": "\u092e\u0927\u094d\u092f\u0928\u0947\u092a\u093e\u0932 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "39"},
    {"id": "593", "name": "Malangwa", "name_ne": "\u092e\u0932\u0919\u094d\u0917\u0935\u093e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "21"},
    {"id": "595", "name": "Mandandeupur",
     "name_ne": "\u092e\u0923\u094d\u0921\u0928\u0926\u0947\u0909\u092a\u0941\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "28"},
    {"id": "596", "name": "Mangalsen", "name_ne": "\u092e\u0902\u0917\u0932\u0938\u0947\u0928 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "68"},
    {"id": "597", "name": "Manthali", "name_ne": "\u092e\u0928\u094d\u0925\u0932\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "32"},
    {"id": "601", "name": "Melamchi", "name_ne": "\u092e\u0947\u0932\u092e\u094d\u091a\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "35"},
    {"id": "602", "name": "Melauli", "name_ne": "\u092e\u0947\u0932\u094c\u0932\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "69"},
    {"id": "608", "name": "Myanglung", "name_ne": "\u092e\u094d\u092f\u093e\u0919\u0932\u0941\u0919 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "13"},
    {"id": "611", "name": "Nalgad", "name_ne": "\u0928\u0932\u0917\u093e\u0921 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "61"},
    {"id": "612", "name": "Namobuddha", "name_ne": "\u0928\u092e\u094b\u092c\u0941\u0926\u094d\u0927 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "28"},
    {"id": "613", "name": "Narayan", "name_ne": "\u0928\u093e\u0930\u093e\u092f\u0923 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "58"},
    {"id": "615", "name": "Nijgadh", "name_ne": "\u0928\u093f\u091c\u0917\u0922 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "15"},
    {"id": "618", "name": "Pakhribas", "name_ne": "\u092a\u093e\u0916\u094d\u0930\u093f\u0935\u093e\u0938 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "2"},
    {"id": "619", "name": "Palungtar", "name_ne": "\u092a\u093e\u0932\u0941\u0919\u091f\u093e\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "37"},
    {"id": "620", "name": "Panchadewal Binayak",
     "name_ne": "\u092a\u091e\u094d\u091a\u0926\u0947\u0935\u0932 \u0935\u093f\u0928\u093e\u092f\u0915 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "68"},
    {"id": "621", "name": "Panchapuri", "name_ne": "\u092a\u091e\u094d\u091a\u092a\u0941\u0930\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "67"},
    {"id": "622", "name": "Panchkhal", "name_ne": "\u092a\u093e\u0901\u091a\u0916\u093e\u0932 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "28"},
    {"id": "623", "name": "Panchkhapan", "name_ne": "\u092a\u093e\u0901\u091a\u0916\u092a\u0928 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "9"},
    {"id": "624", "name": "Parashuram", "name_ne": "\u092a\u0930\u0936\u0941\u0930\u093e\u092e ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "72"},
    {"id": "627", "name": "Patan", "name_ne": "\u092a\u093e\u091f\u0928 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "69"},
    {"id": "629", "name": "Paunauti", "name_ne": "\u092a\u0928\u094c\u0924\u0940 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "28"},
    {"id": "630", "name": "Phalewas", "name_ne": "\u092b\u0932\u0947\u0935\u093e\u0938 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "44"},
    {"id": "632", "name": "Phidim", "name_ne": "\u092b\u093f\u0926\u093f\u092e ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "8"},
    {"id": "633", "name": "Phungling", "name_ne": "\u092b\u0941\u0919\u0932\u093f\u0919 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "12"},
    {"id": "637", "name": "Purchaundi", "name_ne": "\u092a\u0941\u0930\u094d\u091a\u094c\u0921\u0940 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "69"},
    {"id": "638", "name": "Putalibaazar", "name_ne": "\u092a\u0941\u0924\u0932\u0940\u092c\u091c\u093e\u0930 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "45"},
    {"id": "639", "name": "Pyuthan", "name_ne": "\u092a\u094d\u092f\u0942\u0920\u093e\u0928 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "55"},
    {"id": "640", "name": "Rainas", "name_ne": "\u0930\u093e\u0930\u094d\u0907\u0928\u093e\u0938 ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "39"},
    {"id": "646", "name": "Ramechhap", "name_ne": "\u0930\u093e\u092e\u0947\u091b\u093e\u092a ",
     "alternative_names": [], "alternative_names_ne": [], "category": "Municipality", "district_id": "32"},
    {"id": "649", "name": "Rampur", "name_ne": "\u0930\u093e\u092e\u092a\u0941\u0930 ", "alternative_names": [],
     "alternative_names_ne": [], "category": "Municipality", "district_id": "54"}]


class Command(BaseCommand):
    help = "Populate database with location"

    def handle(self, *args, **options):
        count = 0

        # Seed countries
        for count, country_data in enumerate(COUNTRIES, start=1):
            _id = country_data.pop('id')
            Country.objects.get_or_create(id=_id, defaults={
                'name': country_data.get('name')
            })
        print(f"Seeded {count} countries.")

        # seed provinces
        nepal = Country.objects.get(name="Nepal")
        for count, province in enumerate(PROVINCES, start=1):
            _id = province.pop('id')
            data = {
                "country": nepal,
                "name": province.get('name')
            }
            Province.objects.get_or_create(id=_id, defaults=data)
        print(f"Seeded {count} provinces.")

        for count, district in enumerate(DISTRICTS, start=1):
            _id = district["id"]

            data = {
                "province_id": district["province_id"],
                "name": district["name"].title(),
            }
            District.objects.get_or_create(id=_id, defaults=data)
        print(f"Seeded {count} districts.")

        for count, city in enumerate(CITIES, start=1):
            _id = city.pop("id")
            data = {
                'district_id': city.get('district_id'),
                'name': city.get('name')
            }
            City.objects.get_or_create(id=_id, defaults=data)

        print(f"Seeded {count} cities.")
