# MITRE SITE
MITRE_BASE_URL = "https://attack.mitre.org"
TACTICS_URI = "/tactics"
TECHNIQUES_URI = "/techniques"

# REGEX EXPRESSIONS
TACTICS_REGEX = r'\/tactics\/(TA\d+)'
TECHNIQUES_REGEX = r'<a href="\/techniques\/T\d+">\s(T\d+)\s<\/a>'
TECHNIQUE_NAME_REGEX = r'href="\/techniques\/{technique}">\s(.*)\s<'
TECHNIQUE_DESC_REGEX = r'href="\/techniques\/{technique}">\s{technique}\s<\/a>.*?\n\s++(?!<)(.*?)\n'
SUB_TECHNIQUES_REGEX= r'<a\shref="\/techniques\/{technique}\/\d+">\s(\.\d+)\s<\/a>'
SUB_TECHNIQUE_NAME_REGEX = r'href="\/techniques\/{technique}\/{sub_technique}">\s(.*)\s<'
SUB_TECHNIQUE_DESC_REGEX = r'href="\/techniques\/{technique}\/{sub_technique_num}">\s{sub_technique}\s<\/a>.*?\n\s++(?!<)(.*?)\n'

# OTHER
FILE_NAME = "mitre_data"
