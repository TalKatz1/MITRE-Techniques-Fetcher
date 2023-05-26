import requests
import argparse
import re
import json
import csv
import warnings
from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning
from conf import *


def fetch_mitre_data(add_sub_techniques=False):
    all_mitre_techniques = []

    try:
        main_page_content = get_page_content(MITRE_BASE_URL)
        all_tactics = get_all_tactics(main_page_content)

        for tactic in all_tactics:
            tactic_page_content = get_page_content(f"{MITRE_BASE_URL}{TACTICS_URI}/{tactic}")
            tactic_techniques = get_tactic_techniques(tactic_page_content)

            for technique in tactic_techniques:
                technique_name = get_technique_name(tactic_page_content, technique)
                technique_description = get_technique_description(tactic_page_content, technique)

                all_mitre_techniques.append({
                    "technique": f"{tactic}:{technique}",
                    "technique_name": technique_name,
                    "technique_description": technique_description,
                    "technique_link": f"{MITRE_BASE_URL}{TECHNIQUES_URI}/{technique}"
                })
                
                if add_sub_techniques:
                    sub_techniques = get_sub_techniques(tactic_page_content, technique)
                    for sub_technique in sub_techniques:
                        sub_technique_name = get_sub_technique_name(tactic_page_content, technique, sub_technique)
                        sub_technique_description = get_sub_technique_description(tactic_page_content, technique, sub_technique)

                        all_mitre_techniques.append({
                        "technique": f"{tactic}:{technique}{sub_technique}",
                        "technique_name": sub_technique_name,
                        "technique_description": sub_technique_description,
                        "technique_link": f"{MITRE_BASE_URL}{TECHNIQUES_URI}/{technique}/{sub_technique[1:]}"
                    })

        return all_mitre_techniques

    except requests.exceptions.RequestException as e:
        return {"ERROR": str(e)}


def get_page_content(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.text
    else:
        raise requests.exceptions.RequestException(f"Failed to fetch page: {url}")


def get_all_tactics(main_page_content):
    return list(set(re.findall(TACTICS_REGEX, main_page_content)))


def get_tactic_techniques(tactic_page_content):
    return list(set(re.findall(TECHNIQUES_REGEX, tactic_page_content)))


def get_sub_techniques(tactic_page_content, technique):
    return list(set(re.findall(SUB_TECHNIQUES_REGEX.format(technique=technique), tactic_page_content)))


def get_technique_name(tactic_page_content, technique):
    return re.findall(TECHNIQUE_NAME_REGEX.format(technique=technique), tactic_page_content)[1].strip()


def get_sub_technique_name(tactic_page_content, technique, sub_technique):
    return re.findall(SUB_TECHNIQUE_NAME_REGEX.format(technique=technique, sub_technique=sub_technique[1:]), tactic_page_content)[1].strip()


def get_technique_description(tactic_page_content, technique):
    description = re.search(TECHNIQUE_DESC_REGEX.format(technique=technique),tactic_page_content, re.DOTALL).group(1)
    return BeautifulSoup(description, 'html.parser').get_text().strip()


def get_sub_technique_description(tactic_page_content, technique, sub_technique):
    description = re.search(SUB_TECHNIQUE_DESC_REGEX.format(technique=technique, sub_technique_num=sub_technique[1:], sub_technique=sub_technique),tactic_page_content, re.DOTALL).group(1)
    return BeautifulSoup(description, 'html.parser').get_text().strip()


def write_to_json(data):
    with open(f'{FILE_NAME}.json', 'w') as json_file:
        json.dump(fetched_data, json_file)
    print(f"Data saved in JSON format - ./{FILE_NAME}.json")


def write_to_csv(data):
    with open(f'{FILE_NAME}.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(fetched_data[0].keys())
        for row in fetched_data:
            writer.writerow(row.values())
    print(f"Data saved in CSV format - ./{FILE_NAME}.csv")


if __name__ == '__main__':
    warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

    parser = argparse.ArgumentParser(description='MITRE Data Fetcher')
    parser.add_argument('--add-sub-techniques', action='store_true', help='Include sub-techniques')
    parser.add_argument('--to-json', action='store_true', help='Output data in JSON format')
    parser.add_argument('--to-csv', action='store_true', help='Output data in CSV format')
    args = parser.parse_args()

    fetched_data = fetch_mitre_data(add_sub_techniques=args.add_sub_techniques)

    if args.to_json:
        write_to_json(fetched_data)

    elif args.to_csv:
        write_to_csv(fetched_data)

    else:
        print(fetched_data)