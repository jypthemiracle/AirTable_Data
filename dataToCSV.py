import requests
import json
import csv
from pprint import pprint
import csv

DATA_URL = "https://airtable.com/v0.3/application/apppcI0nClUwo3GCb/read?stringifiedObjectParams=%7B%22includeDataForTableIds%22%3A%5B%22tbllShMbhc5jooPRb%22%5D%2C%22includeDataForViewIds%22%3A%5B%22viwymTshkJuerbyeT%22%5D%2C%22shouldIncludeSchemaChecksum%22%3Atrue%2C%22mayOnlyIncludeRowAndCellDataForIncludedViews%22%3Atrue%7D&requestId=req5ASeonsmgzb8tI&accessPolicy=%7B%22allowedActions%22%3A%5B%7B%22modelClassName%22%3A%22application%22%2C%22modelIdSelector%22%3A%22apppcI0nClUwo3GCb%22%2C%22action%22%3A%22read%22%7D%2C%7B%22modelClassName%22%3A%22application%22%2C%22modelIdSelector%22%3A%22apppcI0nClUwo3GCb%22%2C%22action%22%3A%22readForDetailView%22%7D%2C%7B%22modelClassName%22%3A%22table%22%2C%22modelIdSelector%22%3A%22apppcI0nClUwo3GCb+*%22%2C%22action%22%3A%22read%22%7D%2C%7B%22modelClassName%22%3A%22table%22%2C%22modelIdSelector%22%3A%22apppcI0nClUwo3GCb+*%22%2C%22action%22%3A%22readData%22%7D%2C%7B%22modelClassName%22%3A%22table%22%2C%22modelIdSelector%22%3A%22apppcI0nClUwo3GCb+*%22%2C%22action%22%3A%22readDataForRowCards%22%7D%2C%7B%22modelClassName%22%3A%22view%22%2C%22modelIdSelector%22%3A%22apppcI0nClUwo3GCb+*%22%2C%22action%22%3A%22readRowOrder%22%7D%2C%7B%22modelClassName%22%3A%22view%22%2C%22modelIdSelector%22%3A%22apppcI0nClUwo3GCb+*%22%2C%22action%22%3A%22readData%22%7D%2C%7B%22modelClassName%22%3A%22view%22%2C%22modelIdSelector%22%3A%22apppcI0nClUwo3GCb+*%22%2C%22action%22%3A%22getMetadataForPrinting%22%7D%2C%7B%22modelClassName%22%3A%22row%22%2C%22modelIdSelector%22%3A%22apppcI0nClUwo3GCb+*%22%2C%22action%22%3A%22readDataForDetailView%22%7D%2C%7B%22modelClassName%22%3A%22row%22%2C%22modelIdSelector%22%3A%22apppcI0nClUwo3GCb+*%22%2C%22action%22%3A%22createBoxDocumentSession%22%7D%2C%7B%22modelClassName%22%3A%22row%22%2C%22modelIdSelector%22%3A%22apppcI0nClUwo3GCb+*%22%2C%22action%22%3A%22createDocumentPreviewSession%22%7D%5D%2C%22shareId%22%3A%22shrP7uEmnxbv7dUEV%22%2C%22applicationId%22%3A%22apppcI0nClUwo3GCb%22%2C%22sessionId%22%3A%22sesyFv6CIOYkOXhz7%22%2C%22generationNumber%22%3A0%2C%22signature%22%3A%227df53ffbd60ea291f4d66f1ea93dae4ffa44c3f8d6d8eac1986cfb3619220ac9%22%7D"

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection" : "keep-alive",
    "Cookie": "brw=brwjvpTNJrUE3qQuf; lightstep_guid%2FsharedViewOrApp=555d14543e935c84; lightstep_session_id=0f31b5353407fff6; AWSELB=F5E9CFCB0C87D62DB5D03914FDC2A2D2D45FBECE9253BE434965F4D2126129E0338EBA226991AC3560650744EDFEAB3519A6F71FB94FBE4FB16E110225AF1F90036B42B5AE; AWSELBCORS=F5E9CFCB0C87D62DB5D03914FDC2A2D2D45FBECE9253BE434965F4D2126129E0338EBA226991AC3560650744EDFEAB3519A6F71FB94FBE4FB16E110225AF1F90036B42B5AE; lightstep_guid%2Fliveapp=5f38f2ce087f05e1; OptanonConsent=isIABGlobal=false&datestamp=Thu+Jan+06+2022+13%3A35%3A31+GMT%2B0900+(%ED%95%9C%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=6.7.0&hosts=&landingPath=https%3A%2F%2Fairtable.com%2Fapi&groups=C0004%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1; login-status-p=1; phg=0; __Host-airtable-session=eyJzZXNzaW9uSWQiOiJzZXN5RnY2Q0lPWWtPWGh6NyIsImNzcmZTZWNyZXQiOiJfSTZacEIwWDdlWEhDZmhXRWZEaVlzVjciLCJoaWdoU2VjdXJpdHlNb2RlRW5hYmxlZFRpbWUiOjE2NDE0NDY5OTQ3MzMsInVzZXJJZCI6InVzcmE4UXlUbmMxS2o0UmY4In0=; __Host-airtable-session.sig=eHR6OzyALS0Zrd0BE4TUXn-4YRImjUliLWvP9N6qbE4; __zlcmid=17ukbrHsaMfVZ9R; intercom-session-wb1whb4b=OGY2dlRvaTBNTHRlcTBzTG9nM0N6bTY0b083UDJ6NDJaNnhkSXlLencvTXdhOXhvcFhtWmk0bnE4ZHJ4TUZWVC0tVXYxRC9nckRVeldpR29mb2VadVI5QT09--f4e194ee01d4b69821976783fd6f13108a9f51bd; mbpg=2023-01-07T01:25:29.929Zusra8QyTnc1Kj4Rf8free; mbpg.sig=FWp1TAFClPgOTMkjd_QoEgHjm7MQ52impuQgvE21zeY",
    "Host": "airtable.com",
    "ot-tracer-sampled": "true",
    "ot-tracer-spanid": "3a90d94b2180c270",
    "ot-tracer-traceid": "081107792de795af",
    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "x-airtable-application-id": "apppcI0nClUwo3GCb",
    # "x-airtable-client-queue-time": "18.699999999254942",
    "x-airtable-inter-service-client": "webClient",
    "x-airtable-inter-service-client-code-version": 'eaa966f3a691e96ea6bebb9f92486fe380cb5017',
    "x-airtable-page-load-id": "pglUVkg4zY1QJMM6R",
    "X-Requested-With": "XMLHttpRequest",
    "x-time-zone": "Asia/Seoul",
    "x-user-locale": "ko"
}
ROUND = {
    "id": "fld0t86SH12Fx2aD6",
    "name": "Round",
    "type": "select",
    "typeOptions": {
        "choices": {
            "selgHB8IGYBFvFX7u": {
                "id": "selgHB8IGYBFvFX7u",
                "name": "Seed",
                "color": "green"
            },
            "selS3xjcFccbYr79M": {
                "id": "selS3xjcFccbYr79M",
                "name": "Series A",
                "color": "blue"
            },
            "selTs7gEM1R2D1GqU": {
                "id": "selTs7gEM1R2D1GqU",
                "name": "Strategic",
                "color": "cyan"
            },
            "sel3uaGplB5DVdcIH": {
                "id": "sel3uaGplB5DVdcIH",
                "name": "Series B",
                "color": "teal"
            },
            "selCiEcJXHYVPYSkq": {
                "id": "selCiEcJXHYVPYSkq",
                "name": "Series D",
                "color": "yellow"
            },
            "selDrJmeyXXvLPoQy": {
                "id": "selDrJmeyXXvLPoQy",
                "name": "Pre-Seed",
                "color": "orange"
            },
            "sel8dmY1LRk8dMQO2": {
                "id": "sel8dmY1LRk8dMQO2",
                "name": "Extended Seed",
                "color": "red"
            },
            "selAqYcjIJJXgibXH": {
                "id": "selAqYcjIJJXgibXH",
                "name": "Series C",
                "color": "pink"
            },
            "selwCbdYLPHBhzPxV": {
                "id": "selwCbdYLPHBhzPxV",
                "name": "Pre-IPO",
                "color": "blue"
            },
            "sel647AZMgzqETw42": {
                "id": "sel647AZMgzqETw42",
                "name": "Pre-Series A",
                "color": "purpleMedium"
            },
            "sell33r2gnqyjuILn": {
                "id": "sell33r2gnqyjuILn",
                "name": "Unknown",
                "color": "green"
            },
            "selFH28SbhuQbJwGZ": {
                "id": "selFH28SbhuQbJwGZ",
                "name": "Treasury Diversification",
                "color": "orange"
            },
            "selXkv5WwafrjGTGX": {
                "id": "selXkv5WwafrjGTGX",
                "name": "Extended Series B",
                "color": "orange"
            },
            "selPAXNYonUzoXj38": {
                "id": "selPAXNYonUzoXj38",
                "name": "Post-IPO",
                "color": "cyanMedium"
            },
            "sel5B28gk4wbjKqKi": {
                "id": "sel5B28gk4wbjKqKi",
                "name": "Growth",
                "color": "cyanDark"
            },
            "sell9S6X4wCO0VLWq": {
                "id": "sell9S6X4wCO0VLWq",
                "name": "Pre-IDO",
                "color": "blue"
            },
            "selYkAbMt01iD8Ms3": {
                "id": "selYkAbMt01iD8Ms3",
                "name": "Series E",
                "color": "grayMedium"
            },
            "selQ20VCPr6fsuTLD": {
                "id": "selQ20VCPr6fsuTLD",
                "name": "ICO",
                "color": "tealDark"
            },
            "selULaXzqS9FOAl0g": {
                "id": "selULaXzqS9FOAl0g",
                "name": "Community Raise",
                "color": "orangeDarker"
            },
            "selliKytyoX6SEgNk": {
                "id": "selliKytyoX6SEgNk",
                "name": "Post-IPO Debt",
                "color": "purple"
            },
            "selIKF6hLoMK7y6h5": {
                "id": "selIKF6hLoMK7y6h5",
                "name": "Series H",
                "color": "cyan"
            },
            "selAPd2GWY8REWDqh": {
                "id": "selAPd2GWY8REWDqh",
                "name": "Series G",
                "color": "red"
            },
            "sel3ZO1gBgTw8mttG": {
                "id": "sel3ZO1gBgTw8mttG",
                "name": "Series F",
                "color": "yellowDarker"
            },
            "selvvTgGgvDxfIXbK": {
                "id": "selvvTgGgvDxfIXbK",
                "name": "Equity Crowdfunding",
                "color": "blue"
            },
            "selRe9JgSbYJvc1hk": {
                "id": "selRe9JgSbYJvc1hk",
                "name": "Extended Series D",
                "color": "blueMedium"
            },
            "sel3vpuPM7InzWMe5": {
                "id": "sel3vpuPM7InzWMe5",
                "name": "Extended Series A",
                "color": "tealMedium"
            },
            "selqVjC5bJOe2NMNG": {
                "id": "selqVjC5bJOe2NMNG",
                "name": "Debt Financing",
                "color": "pink"
            },
            "selvBduXeFAjY9d1C": {
                "id": "selvBduXeFAjY9d1C",
                "name": "Series B-1",
                "color": "tealMedium"
            },
            "sel3JVWl6sS8x3zfW": {
                "id": "sel3JVWl6sS8x3zfW",
                "name": "Seed Extension",
                "color": "tealDark"
            },
            "selK49w0wKK9KnEr8": {
                "id": "selK49w0wKK9KnEr8",
                "name": "Series B-2",
                "color": "cyan"
            }
        },
        "disableColors": False
    }
}
FOUNDER = {
    "id": "fldZpYosKMqtY2nqQ",
    "name": "Founder",
    "type": "multiSelect",
    "typeOptions": {
        "choices": {
            "sel0kgCD5mVfPq2Kv": {
                "id": "sel0kgCD5mVfPq2Kv",
                "name": "Steve Ngok",
                "color": "blue"
            },
            "sel6c7eG6LMhMFVZC": {
                "id": "sel6c7eG6LMhMFVZC",
                "name": "Alex Gluchowski",
                "color": "cyan"
            },
            "sel51JamK4fTM0MIP": {
                "id": "sel51JamK4fTM0MIP",
                "name": "Edan Yago",
                "color": "teal"
            },
            "sel6xS4ynEHVzBNzC": {
                "id": "sel6xS4ynEHVzBNzC",
                "name": "Austin Woodward",
                "color": "green"
            },
            "selhvSCGrOHi3N37X": {
                "id": "selhvSCGrOHi3N37X",
                "name": "Chad Liu",
                "color": "yellow"
            },
            "selykP6x8RyLkG1F6": {
                "id": "selykP6x8RyLkG1F6",
                "name": "Henson Orser",
                "color": "orange"
            },
            "selSwJ1KmfRCH7IKV": {
                "id": "selSwJ1KmfRCH7IKV",
                "name": "Lei Wang",
                "color": "red"
            },
            "selg8h1hIaG4Y6FJB": {
                "id": "selg8h1hIaG4Y6FJB",
                "name": "Whit Gibbs",
                "color": "pink"
            },
            "selWzwH23s5JrKITy": {
                "id": "selWzwH23s5JrKITy",
                "name": "Thomas Heller",
                "color": "purple"
            },
            "sel0b1Sog4jQgC3Hk": {
                "id": "sel0b1Sog4jQgC3Hk",
                "name": "Paul Gosker",
                "color": "gray"
            },
            "selbb4OK9lXcgbPn0": {
                "id": "selbb4OK9lXcgbPn0",
                "name": "Thi Truong",
                "color": "blue"
            },
            "selqyBYnZQocPB06u": {
                "id": "selqyBYnZQocPB06u",
                "name": "Anonymous",
                "color": "cyan"
            },
            "sel8uQ8A3yuMpxPIz": {
                "id": "sel8uQ8A3yuMpxPIz",
                "name": "Jayden Antonio",
                "color": "teal"
            },
            "selZkqUr4Lf0oC4w4": {
                "id": "selZkqUr4Lf0oC4w4",
                "name": "Michael Kong",
                "color": "green"
            },
            "selCWk3iX2leBewbz": {
                "id": "selCWk3iX2leBewbz",
                "name": "Joey Krug",
                "color": "yellow"
            },
            "selwzGBdzH5oPAgeW": {
                "id": "selwzGBdzH5oPAgeW",
                "name": "Prabhakar Reddy",
                "color": "red"
            },
            "selq3rQiDENEM0VFq": {
                "id": "selq3rQiDENEM0VFq",
                "name": "Raghu Yarlagadda",
                "color": "pink"
            },
            "seldZ09P0syBc5lDh": {
                "id": "seldZ09P0syBc5lDh",
                "name": "Joey Santoro",
                "color": "purple"
            },
            "seljz0bI82x01PKQ5": {
                "id": "seljz0bI82x01PKQ5",
                "name": "Sebastian Delgado",
                "color": "gray"
            },
            "selXIzmrkIIWP4ZGD": {
                "id": "selXIzmrkIIWP4ZGD",
                "name": "Ivan Yeung",
                "color": "blue"
            },
            "selS1aCckG2dl8UqG": {
                "id": "selS1aCckG2dl8UqG",
                "name": "Chris Spadafora",
                "color": "cyan"
            },
            "selMhTmrcRXXjstyk": {
                "id": "selMhTmrcRXXjstyk",
                "name": "Lars Seier Christensen",
                "color": "teal"
            },
            "selgU77Zkv35Lh3ou": {
                "id": "selgU77Zkv35Lh3ou",
                "name": "Chris Forrester",
                "color": "green"
            },
            "selG93N8iQ16T39iO": {
                "id": "selG93N8iQ16T39iO",
                "name": "Joseph Weinberg",
                "color": "yellow"
            },
            "sel84LLYBxEWoSWk7": {
                "id": "sel84LLYBxEWoSWk7",
                "name": "Kris Coward",
                "color": "orange"
            },
            "selkOiOF8EgT1V8kF": {
                "id": "selkOiOF8EgT1V8kF",
                "name": "Zac Prince",
                "color": "red"
            },
            "sel5EGxAcCcWlvDB7": {
                "id": "sel5EGxAcCcWlvDB7",
                "name": "Ted Shao",
                "color": "pink"
            },
            "selVz8s7UfMsHz7oq": {
                "id": "selVz8s7UfMsHz7oq",
                "name": "Joshua Goldbard",
                "color": "purple"
            },
            "seldFbSHsnLmWmvuT": {
                "id": "seldFbSHsnLmWmvuT",
                "name": "Dan Danay",
                "color": "gray"
            },
            "selsCbyfYyKouvsYl": {
                "id": "selsCbyfYyKouvsYl",
                "name": "Alina Aseeva",
                "color": "blue"
            },
            "sela5cYcmpqU13q4w": {
                "id": "sela5cYcmpqU13q4w",
                "name": "Prashant Kale",
                "color": "cyan"
            },
            "selRkFrpHkYwJROpe": {
                "id": "selRkFrpHkYwJROpe",
                "name": "Santosh",
                "color": "teal"
            },
            "sel0eICYpYsuTeFNa": {
                "id": "sel0eICYpYsuTeFNa",
                "name": "Justin Hartzman",
                "color": "green"
            },
            "sel3MckyT7A7CxwRk": {
                "id": "sel3MckyT7A7CxwRk",
                "name": "Yudi Xu",
                "color": "yellow"
            },
            "selmJaKWkUHmctfNT": {
                "id": "selmJaKWkUHmctfNT",
                "name": "Gautham J",
                "color": "orange"
            },
            "selXpp7adXZqEHSx7": {
                "id": "selXpp7adXZqEHSx7",
                "name": "Stephen Young",
                "color": "red"
            },
            "selQckBTAshNfIK1d": {
                "id": "selQckBTAshNfIK1d",
                "name": "Sandeep Sudagani",
                "color": "pink"
            },
            "selm0HpfhwujvXSPS": {
                "id": "selm0HpfhwujvXSPS",
                "name": "Alvin Lee",
                "color": "purple"
            },
            "seleK5sMEDC6w4SY8": {
                "id": "seleK5sMEDC6w4SY8",
                "name": "Vladimir Tomko",
                "color": "gray"
            },
            "selUAydr3HDTVyhvx": {
                "id": "selUAydr3HDTVyhvx",
                "name": "Patrick Baron",
                "color": "blue"
            },
            "selLmFjNVfF8dSn4p": {
                "id": "selLmFjNVfF8dSn4p",
                "name": "Evan Forbes",
                "color": "cyan"
            },
            "sel8rhvtl4zP2woty": {
                "id": "sel8rhvtl4zP2woty",
                "name": "Bogdan Baiceanu",
                "color": "teal"
            },
            "selIbBfPUGoF9Xm0d": {
                "id": "selIbBfPUGoF9Xm0d",
                "name": "Denko Mancheski",
                "color": "green"
            },
            "selUMRJLrhwcrBq7d": {
                "id": "selUMRJLrhwcrBq7d",
                "name": "Viveik V.",
                "color": "yellow"
            },
            "selbbjmEPEcgc7xay": {
                "id": "selbbjmEPEcgc7xay",
                "name": "Sam Zou",
                "color": "orange"
            },
            "selb4kKJxDoomGHQu": {
                "id": "selb4kKJxDoomGHQu",
                "name": "Emmanuelle Collet",
                "color": "red"
            },
            "sel4TwJsPeZJlC2T4": {
                "id": "sel4TwJsPeZJlC2T4",
                "name": "Justin Banon",
                "color": "pink"
            },
            "selC6NiLv6qIcrL8c": {
                "id": "selC6NiLv6qIcrL8c",
                "name": "Humayun Sheikh",
                "color": "purple"
            },
            "selTALiMJpQkZpeFf": {
                "id": "selTALiMJpQkZpeFf",
                "name": "Kieran Warwick",
                "color": "gray"
            },
            "selDBRjN4FQniaSjx": {
                "id": "selDBRjN4FQniaSjx",
                "name": "Jack Zampolin",
                "color": "blue"
            },
            "selxBLfwlFaVb6vNd": {
                "id": "selxBLfwlFaVb6vNd",
                "name": "Roy Lai",
                "color": "cyan"
            },
            "selze2ER5IJSktHZ3": {
                "id": "selze2ER5IJSktHZ3",
                "name": "Robert Weir",
                "color": "teal"
            },
            "sel4uuh90mL61WDzX": {
                "id": "sel4uuh90mL61WDzX",
                "name": "Keagan McClelland",
                "color": "green"
            },
            "selmDZVIWGKHF6I1U": {
                "id": "selmDZVIWGKHF6I1U",
                "name": "Arun Pudur",
                "color": "yellow"
            },
            "selPw2reTZt5pmYSY": {
                "id": "selPw2reTZt5pmYSY",
                "name": "Imran Ashfaq",
                "color": "orange"
            },
            "selsZCcfgr5S3crV4": {
                "id": "selsZCcfgr5S3crV4",
                "name": "Ryan Park",
                "color": "red"
            },
            "selIpI3A5MOYFeYVP": {
                "id": "selIpI3A5MOYFeYVP",
                "name": "Kyle Kahlenberg",
                "color": "pink"
            },
            "selAt0GUFWPKubrHW": {
                "id": "selAt0GUFWPKubrHW",
                "name": "Devin Finzer",
                "color": "purple"
            },
            "selx98Q8PJ25oj61R": {
                "id": "selx98Q8PJ25oj61R",
                "name": "Alex Atallah",
                "color": "gray"
            },
            "selkMwkZQ3N4qT0RY": {
                "id": "selkMwkZQ3N4qT0RY",
                "name": "Sherry Zhang",
                "color": "blue"
            },
            "selSjg7N3P1mKDN5U": {
                "id": "selSjg7N3P1mKDN5U",
                "name": "Manohara K",
                "color": "cyan"
            },
            "selTjZiK33QBWrjBs": {
                "id": "selTjZiK33QBWrjBs",
                "name": "Dmitri Tsumak",
                "color": "teal"
            },
            "sel9UwBBAn48vwvUp": {
                "id": "sel9UwBBAn48vwvUp",
                "name": "Dimitriy Remerov",
                "color": "green"
            },
            "sel5TKe1SB7h0xZWO": {
                "id": "sel5TKe1SB7h0xZWO",
                "name": "Boris Yang",
                "color": "yellow"
            },
            "selWGzGyBmPb4et4O": {
                "id": "selWGzGyBmPb4et4O",
                "name": "Gabby Dizon",
                "color": "orange"
            },
            "selxUK74ev6q2dfAg": {
                "id": "selxUK74ev6q2dfAg",
                "name": "Juan M. Hernandez",
                "color": "red"
            },
            "selFfjcJ1AtbzJBZ2": {
                "id": "selFfjcJ1AtbzJBZ2",
                "name": "Rabeel Jawaid",
                "color": "pink"
            },
            "selHW4dUPvwYf1bM9": {
                "id": "selHW4dUPvwYf1bM9",
                "name": "Deli Gong",
                "color": "purple"
            },
            "selouqMNURcbBz1lh": {
                "id": "selouqMNURcbBz1lh",
                "name": "Justin Kellison",
                "color": "gray"
            },
            "selTcGOaYKRfuVUM5": {
                "id": "selTcGOaYKRfuVUM5",
                "name": "Slava Kim",
                "color": "blue"
            },
            "selao1IUg41zvkA3x": {
                "id": "selao1IUg41zvkA3x",
                "name": "Chandler Song",
                "color": "cyan"
            },
            "selnNJ4Ep3lzNW3va": {
                "id": "selnNJ4Ep3lzNW3va",
                "name": "Ryan Fang",
                "color": "teal"
            },
            "selRnqTgxS2nW4oh8": {
                "id": "selRnqTgxS2nW4oh8",
                "name": "Kenneth Ballenegger",
                "color": "green"
            },
            "selKoa9RWLCBuU5uR": {
                "id": "selKoa9RWLCBuU5uR",
                "name": "Scoopy Trooples",
                "color": "yellow"
            },
            "selL1VY0pK6epx0km": {
                "id": "selL1VY0pK6epx0km",
                "name": "Ramsey Khoury",
                "color": "orange"
            },
            "selY6SM5DkUgo1lVG": {
                "id": "selY6SM5DkUgo1lVG",
                "name": "Barney Mannerings",
                "color": "red"
            },
            "selDUiuaMXfB9jiWn": {
                "id": "selDUiuaMXfB9jiWn",
                "name": "Cole Kennelly",
                "color": "pink"
            },
            "sel2sL9Qoz7T6RiVA": {
                "id": "sel2sL9Qoz7T6RiVA",
                "name": "Dennison Bertram",
                "color": "purple"
            },
            "sellnQffcyZ3ggPs6": {
                "id": "sellnQffcyZ3ggPs6",
                "name": "Rafael Solari",
                "color": "gray"
            },
            "selsOuP81okB30STO": {
                "id": "selsOuP81okB30STO",
                "name": "Sidney Powell",
                "color": "blue"
            },
            "selcu5snd11P88u88": {
                "id": "selcu5snd11P88u88",
                "name": "Ian Lee",
                "color": "cyan"
            },
            "sel9cDU7koA7PYrJS": {
                "id": "sel9cDU7koA7PYrJS",
                "name": "Will Papper",
                "color": "teal"
            },
            "selw59iLk22CkG0PT": {
                "id": "selw59iLk22CkG0PT",
                "name": "Adam Kay",
                "color": "green"
            },
            "selRO3qCXFXpDbwZq": {
                "id": "selRO3qCXFXpDbwZq",
                "name": "Cora Chen",
                "color": "yellow"
            },
            "selJCfT5iNxguGsJl": {
                "id": "selJCfT5iNxguGsJl",
                "name": "Taulant Ramabaja",
                "color": "orange"
            },
            "self6FN32KGdmhFgK": {
                "id": "self6FN32KGdmhFgK",
                "name": "David Jin",
                "color": "red"
            },
            "selrC4QmNhjXBnxvH": {
                "id": "selrC4QmNhjXBnxvH",
                "name": "Nader Al-Naji",
                "color": "pink"
            },
            "seloFLocjWSb7nx62": {
                "id": "seloFLocjWSb7nx62",
                "name": "Robert Materazzi",
                "color": "purple"
            },
            "sel0ukXq8jvyke4QK": {
                "id": "sel0ukXq8jvyke4QK",
                "name": "Harsh Rajat",
                "color": "gray"
            },
            "selBdCtKMGB7URv8g": {
                "id": "selBdCtKMGB7URv8g",
                "name": "Satheesh",
                "color": "blue"
            },
            "selE9dPkLkzYkBUZE": {
                "id": "selE9dPkLkzYkBUZE",
                "name": "Lennart Brandt",
                "color": "cyan"
            },
            "sel8eXGXRX7j7d1cV": {
                "id": "sel8eXGXRX7j7d1cV",
                "name": "Alexander Shishow",
                "color": "teal"
            },
            "selrgqgMTz6z4XF8E": {
                "id": "selrgqgMTz6z4XF8E",
                "name": "Peter Smith",
                "color": "green"
            },
            "selKuy7Is5kU6Df4F": {
                "id": "selKuy7Is5kU6Df4F",
                "name": "Ganesh Swami",
                "color": "yellow"
            },
            "selFNmMfCkfQH3Wsr": {
                "id": "selFNmMfCkfQH3Wsr",
                "name": "Nilotpal Mukherjee",
                "color": "orange"
            },
            "selJrLdNB1PDsefU0": {
                "id": "selJrLdNB1PDsefU0",
                "name": "Garlam Won",
                "color": "red"
            },
            "selCM8rt6ZPQweGxr": {
                "id": "selCM8rt6ZPQweGxr",
                "name": "Chris Longden",
                "color": "pink"
            },
            "selAS6q3IicKNvAzy": {
                "id": "selAS6q3IicKNvAzy",
                "name": "Emile Dubi\u00e9",
                "color": "purple"
            },
            "selMdPjVsLqRFSg6X": {
                "id": "selMdPjVsLqRFSg6X",
                "name": "Tom",
                "color": "gray"
            },
            "selgx971OCqL1r5WD": {
                "id": "selgx971OCqL1r5WD",
                "name": "Kevin Tseng",
                "color": "blue"
            },
            "sel4A1gPkPgoh6Vqa": {
                "id": "sel4A1gPkPgoh6Vqa",
                "name": "Zach Bruch",
                "color": "cyan"
            },
            "selqfRekZowkY35DC": {
                "id": "selqfRekZowkY35DC",
                "name": "Trevor George",
                "color": "teal"
            },
            "selwhpdtNW8xAMh0b": {
                "id": "selwhpdtNW8xAMh0b",
                "name": "Soups Ranjan",
                "color": "green"
            },
            "selC2B1IS3cJWfSmA": {
                "id": "selC2B1IS3cJWfSmA",
                "name": "Calvin Pak",
                "color": "yellow"
            },
            "selSDmg9T9GMgr9Fm": {
                "id": "selSDmg9T9GMgr9Fm",
                "name": "Andrew Bakst",
                "color": "orange"
            },
            "sel3EAicjos9Vdh9G": {
                "id": "sel3EAicjos9Vdh9G",
                "name": "Arjun Bhuptani",
                "color": "red"
            },
            "selzsrFvvq9YTDVBx": {
                "id": "selzsrFvvq9YTDVBx",
                "name": "Layne Haber",
                "color": "pink"
            },
            "selsNHrcFOuCB2Lfn": {
                "id": "selsNHrcFOuCB2Lfn",
                "name": "Rahul Sethuram",
                "color": "purple"
            },
            "selNquiTrMzS1MLou": {
                "id": "selNquiTrMzS1MLou",
                "name": "Jeff Marsilio",
                "color": "gray"
            },
            "seljaeEv6kbZXPHGZ": {
                "id": "seljaeEv6kbZXPHGZ",
                "name": "Jolyon Layard Horsfall",
                "color": "blue"
            },
            "sel9JU4pMj4rWVl10": {
                "id": "sel9JU4pMj4rWVl10",
                "name": "Antoine Mouran",
                "color": "cyan"
            },
            "selINezNmEjQqVqbJ": {
                "id": "selINezNmEjQqVqbJ",
                "name": "Michael Yeates",
                "color": "teal"
            },
            "sel8hIevbjvSuMldy": {
                "id": "sel8hIevbjvSuMldy",
                "name": "Saro Mckenna",
                "color": "green"
            },
            "seljWRU6i0CNJrl2k": {
                "id": "seljWRU6i0CNJrl2k",
                "name": "Nikola Madjarevic",
                "color": "yellow"
            },
            "selLnU2byCPI0spJU": {
                "id": "selLnU2byCPI0spJU",
                "name": "Michael Gronager",
                "color": "orange"
            },
            "selaViJoyFhAw46M2": {
                "id": "selaViJoyFhAw46M2",
                "name": "Uri Kolodny",
                "color": "red"
            },
            "sel3cL39WnWpJQoja": {
                "id": "sel3cL39WnWpJQoja",
                "name": "Eli Ben-Sasson",
                "color": "pink"
            },
            "selOnLwgXqzo83yz1": {
                "id": "selOnLwgXqzo83yz1",
                "name": "Michael Riabzev",
                "color": "purple"
            },
            "sel6mttMUsfgRRdl5": {
                "id": "sel6mttMUsfgRRdl5",
                "name": "Alessandro Chiesa",
                "color": "gray"
            },
            "selozYWqAc7vPXeYw": {
                "id": "selozYWqAc7vPXeYw",
                "name": "Robert Lauko",
                "color": "blue"
            },
            "seluxp4k0n2ZJli95": {
                "id": "seluxp4k0n2ZJli95",
                "name": "Derek Yoo",
                "color": "cyan"
            },
            "selv2892E59hFYQcI": {
                "id": "selv2892E59hFYQcI",
                "name": "John Crain",
                "color": "teal"
            },
            "selLf6AeTyxZy2QlR": {
                "id": "selLf6AeTyxZy2QlR",
                "name": "Roham Gharegozlou",
                "color": "green"
            },
            "selE4T79JAHXQAhDh": {
                "id": "selE4T79JAHXQAhDh",
                "name": "Bohdan Kit",
                "color": "yellow"
            },
            "selizJD2eLIlelNul": {
                "id": "selizJD2eLIlelNul",
                "name": "Pankaj Balani",
                "color": "orange"
            },
            "seltwKjDjCXDar8W8": {
                "id": "seltwKjDjCXDar8W8",
                "name": "Hannes Graah",
                "color": "red"
            },
            "selgd1aAbQKCJ9mJJ": {
                "id": "selgd1aAbQKCJ9mJJ",
                "name": "Remy Carpinito",
                "color": "pink"
            },
            "sels1Y1CdhnNis0Tx": {
                "id": "sels1Y1CdhnNis0Tx",
                "name": "Ben He",
                "color": "purple"
            },
            "selnkom738yeoq3iZ": {
                "id": "selnkom738yeoq3iZ",
                "name": "Will Villanueva",
                "color": "gray"
            },
            "selk3rBIvVoCpD0GN": {
                "id": "selk3rBIvVoCpD0GN",
                "name": "Jonny Rhea",
                "color": "blue"
            },
            "selqDkRJdCo7UxHpd": {
                "id": "selqDkRJdCo7UxHpd",
                "name": "Iulian Nita",
                "color": "cyan"
            },
            "sel3mhdqy4D9IfPYd": {
                "id": "sel3mhdqy4D9IfPYd",
                "name": "Yehuda Lindell",
                "color": "teal"
            },
            "selDkd0TBnGEXM5fw": {
                "id": "selDkd0TBnGEXM5fw",
                "name": "Jan Kne\u017eevi\u0107",
                "color": "green"
            },
            "selJETxd8bJbiccNP": {
                "id": "selJETxd8bJbiccNP",
                "name": "Fred Jin",
                "color": "yellow"
            },
            "selRc4byl9SAlEQS1": {
                "id": "selRc4byl9SAlEQS1",
                "name": "Anna Norrevik",
                "color": "orange"
            },
            "selTDK71wEHKiHSeM": {
                "id": "selTDK71wEHKiHSeM",
                "name": "Sunil Srivatsa",
                "color": "red"
            },
            "selInnU9tm2PiZILU": {
                "id": "selInnU9tm2PiZILU",
                "name": "Alex Grebnev",
                "color": "pink"
            },
            "sel0UKslvkskY498U": {
                "id": "sel0UKslvkskY498U",
                "name": "Abdullah Almoaiqel",
                "color": "purple"
            },
            "selqW3gIApz4GP0Z7": {
                "id": "selqW3gIApz4GP0Z7",
                "name": "AJ Nelson",
                "color": "gray"
            },
            "selqjJlQoHHYwc2H2": {
                "id": "selqjJlQoHHYwc2H2",
                "name": "Joseph Dallago",
                "color": "blue"
            },
            "selUF3ndTghT3e5zo": {
                "id": "selUF3ndTghT3e5zo",
                "name": "Felix Xu",
                "color": "cyan"
            },
            "sela1FRukaviATNGp": {
                "id": "sela1FRukaviATNGp",
                "name": "Yemu Xu",
                "color": "teal"
            },
            "selSWzK6nhNCZ5SIJ": {
                "id": "selSWzK6nhNCZ5SIJ",
                "name": "Ramani 'Ram' Ramachandran",
                "color": "green"
            },
            "selSGKuFVmMHoJVat": {
                "id": "selSGKuFVmMHoJVat",
                "name": "Chandan Choudhury",
                "color": "yellow"
            },
            "seluHwP7gtM2XHXTz": {
                "id": "seluHwP7gtM2XHXTz",
                "name": "Marsel Adawi",
                "color": "orange"
            },
            "selfkpQeW3AQiboGO": {
                "id": "selfkpQeW3AQiboGO",
                "name": "Kim Raath",
                "color": "red"
            },
            "seldEglEFQKcVNhbK": {
                "id": "seldEglEFQKcVNhbK",
                "name": "Chris Georgen",
                "color": "pink"
            },
            "sel3kvGqL6kwbciEb": {
                "id": "sel3kvGqL6kwbciEb",
                "name": "James Aman",
                "color": "purple"
            },
            "selELZfM81GIKwfRz": {
                "id": "selELZfM81GIKwfRz",
                "name": "Giorgio Andrews",
                "color": "gray"
            },
            "selu4s7YP73fs7EAw": {
                "id": "selu4s7YP73fs7EAw",
                "name": "Samson Mow",
                "color": "blue"
            },
            "sel6eFNFIg2q62CXl": {
                "id": "sel6eFNFIg2q62CXl",
                "name": "Amir Bandeali",
                "color": "cyan"
            },
            "seluFkCmSU1VoVzA7": {
                "id": "seluFkCmSU1VoVzA7",
                "name": "Will Warren",
                "color": "teal"
            },
            "selJAzJHCvDKvB4F4": {
                "id": "selJAzJHCvDKvB4F4",
                "name": "Paulo Jacinto Rodrigues",
                "color": "green"
            },
            "sel3rKZrGGNXDKzjk": {
                "id": "sel3rKZrGGNXDKzjk",
                "name": "Ricardo Marques",
                "color": "yellow"
            },
            "selhc5jcLAJc6tkr6": {
                "id": "selhc5jcLAJc6tkr6",
                "name": "Francisco Louren\u00e7o",
                "color": "orange"
            },
            "sel1xuGry5EBTRhZL": {
                "id": "sel1xuGry5EBTRhZL",
                "name": "Elon Musk",
                "color": "red"
            },
            "selF58bzNYHpYiR5f": {
                "id": "selF58bzNYHpYiR5f",
                "name": "Jeff Garzik",
                "color": "pink"
            },
            "selnmlrRBlC7vyLjf": {
                "id": "selnmlrRBlC7vyLjf",
                "name": "Jordan Kruger",
                "color": "purple"
            },
            "selZH2GCfwWA7WBui": {
                "id": "selZH2GCfwWA7WBui",
                "name": "Matthew Roszak",
                "color": "gray"
            },
            "selWWtVLb5z5F6zkr": {
                "id": "selWWtVLb5z5F6zkr",
                "name": "Adam Reeds",
                "color": "blue"
            },
            "sel3HRUvD0S4SlPvK": {
                "id": "sel3HRUvD0S4SlPvK",
                "name": "Mauricio Di Bartolomeo",
                "color": "cyan"
            },
            "sel9gHns3CZwkANgf": {
                "id": "sel9gHns3CZwkANgf",
                "name": "Sota Watanabe",
                "color": "teal"
            },
            "selX1EnsAgHQtgHit": {
                "id": "selX1EnsAgHQtgHit",
                "name": "Alexei Falin",
                "color": "green"
            },
            "selRiDne3raIqFI6y": {
                "id": "selRiDne3raIqFI6y",
                "name": "Alexander Salnikov",
                "color": "yellow"
            },
            "selFooAZbE6g9Zv1V": {
                "id": "selFooAZbE6g9Zv1V",
                "name": "Aronu Ugochukwu",
                "color": "orange"
            },
            "selhuZrcKNHb0oBYm": {
                "id": "selhuZrcKNHb0oBYm",
                "name": "Kain Warwick",
                "color": "red"
            },
            "seln3aOJ5W0ghfAL9": {
                "id": "seln3aOJ5W0ghfAL9",
                "name": "Viktor Tron",
                "color": "pink"
            },
            "selOgTOlgtf7T3Ged": {
                "id": "selOgTOlgtf7T3Ged",
                "name": "Suji Yan",
                "color": "purple"
            },
            "selj7OACmhmywHXMm": {
                "id": "selj7OACmhmywHXMm",
                "name": "Hugh Karp",
                "color": "gray"
            },
            "selL6NIJQeQPSZYNF": {
                "id": "selL6NIJQeQPSZYNF",
                "name": "Rob Secord",
                "color": "blue"
            },
            "selqaa2Nx4PQOgx0p": {
                "id": "selqaa2Nx4PQOgx0p",
                "name": "Ben Lakoff",
                "color": "cyan"
            },
            "selEKH8hugc6y6391": {
                "id": "selEKH8hugc6y6391",
                "name": "Richard Simpson",
                "color": "teal"
            },
            "sel8KGumy1KJUda1A": {
                "id": "sel8KGumy1KJUda1A",
                "name": "Tuan Anh Nguyen",
                "color": "green"
            },
            "sel4MxlQp8YsAlfp5": {
                "id": "sel4MxlQp8YsAlfp5",
                "name": "Nick Rose Ntertsas",
                "color": "yellow"
            },
            "selr4liyf1g1HNzvc": {
                "id": "selr4liyf1g1HNzvc",
                "name": "Andriy Velykyy",
                "color": "orange"
            },
            "seloOFGfV0457Nh2K": {
                "id": "seloOFGfV0457Nh2K",
                "name": "Viven Kirby",
                "color": "red"
            },
            "selgXH1s2u4ZG7hlO": {
                "id": "selgXH1s2u4ZG7hlO",
                "name": "Norelle Ng",
                "color": "pink"
            },
            "sel2qZBI6L36PBaFW": {
                "id": "sel2qZBI6L36PBaFW",
                "name": "Burak Ke\u00e7eli",
                "color": "purple"
            },
            "selwM464OcekpbxPX": {
                "id": "selwM464OcekpbxPX",
                "name": "Stefan Ionescu",
                "color": "gray"
            },
            "seljpGRhTaD3CnYk3": {
                "id": "seljpGRhTaD3CnYk3",
                "name": "Conlan Rios",
                "color": "blue"
            },
            "sel1e7VZJLVnRRhYM": {
                "id": "sel1e7VZJLVnRRhYM",
                "name": "Guilherme Guimaraes",
                "color": "cyan"
            },
            "selt4XUzLkj2tFR1Z": {
                "id": "selt4XUzLkj2tFR1Z",
                "name": "Robson Silva",
                "color": "teal"
            },
            "selIEpntZXy2fcYk7": {
                "id": "selIEpntZXy2fcYk7",
                "name": "Rafaella Baraldo",
                "color": "green"
            },
            "seljEibt1T5Pv7yNZ": {
                "id": "seljEibt1T5Pv7yNZ",
                "name": "Anand Kamath",
                "color": "yellow"
            },
            "selWcfHyvjmfUvTWA": {
                "id": "selWcfHyvjmfUvTWA",
                "name": "Danny B",
                "color": "orange"
            },
            "selNiZjDLHcm35ea3": {
                "id": "selNiZjDLHcm35ea3",
                "name": "Chester B",
                "color": "red"
            },
            "selhTNlr9M20bcrD0": {
                "id": "selhTNlr9M20bcrD0",
                "name": "Anandan Pandurangan",
                "color": "pink"
            },
            "selttzIZKimXXO89d": {
                "id": "selttzIZKimXXO89d",
                "name": "Zain Rana",
                "color": "purple"
            },
            "seluzCyR8AO7BnfxF": {
                "id": "seluzCyR8AO7BnfxF",
                "name": "Aishwarya Shivakumar Haroshivanahalli",
                "color": "gray"
            },
            "selz2NIYaz1l3dsJ8": {
                "id": "selz2NIYaz1l3dsJ8",
                "name": "Shreedhar K Shreenivasa",
                "color": "blue"
            },
            "selJiRFOXstESLO2x": {
                "id": "selJiRFOXstESLO2x",
                "name": "Aleksandras Ga\u0161ka",
                "color": "cyan"
            },
            "sel9geLASXUNUxmwS": {
                "id": "sel9geLASXUNUxmwS",
                "name": "Hayden Adams",
                "color": "teal"
            },
            "selWqPC5cG7HSpkmC": {
                "id": "selWqPC5cG7HSpkmC",
                "name": "Nicolas Julia",
                "color": "green"
            },
            "sel0aauIO66n8YKeJ": {
                "id": "sel0aauIO66n8YKeJ",
                "name": "Henry Chan",
                "color": "yellow"
            },
            "selRPAFevHj9GxXXX": {
                "id": "selRPAFevHj9GxXXX",
                "name": "Kevin Zhang",
                "color": "orange"
            },
            "selwchNPipmGqS5Gv": {
                "id": "selwchNPipmGqS5Gv",
                "name": "Oliver Xie",
                "color": "red"
            },
            "selPk86QKbmmmZtHx": {
                "id": "selPk86QKbmmmZtHx",
                "name": "Dylan Dewdney",
                "color": "pink"
            },
            "selOzo2KLme8LYkg9": {
                "id": "selOzo2KLme8LYkg9",
                "name": "Michael Shaulov",
                "color": "purple"
            },
            "sellxBi1drynr9NJY": {
                "id": "sellxBi1drynr9NJY",
                "name": "Nicolas Girard",
                "color": "gray"
            },
            "sel2ImHykGbFDwBRO": {
                "id": "sel2ImHykGbFDwBRO",
                "name": "Pierre Steckmeyer",
                "color": "blue"
            },
            "selN9scNE98wC08uT": {
                "id": "selN9scNE98wC08uT",
                "name": "Elliot Chen",
                "color": "cyan"
            },
            "selIbWVtBT4cBWN3T": {
                "id": "selIbWVtBT4cBWN3T",
                "name": "Jason Evans",
                "color": "teal"
            },
            "sel8ejypIZdX68mqB": {
                "id": "sel8ejypIZdX68mqB",
                "name": "Yoann Bentz",
                "color": "green"
            },
            "selamot3cg2MNq0lZ": {
                "id": "selamot3cg2MNq0lZ",
                "name": "Matt Cutler",
                "color": "yellow"
            },
            "sel0N6l7c4Pe388je": {
                "id": "sel0N6l7c4Pe388je",
                "name": "Michael Beck",
                "color": "orange"
            },
            "seloQmHCPlwBcSvQ2": {
                "id": "seloQmHCPlwBcSvQ2",
                "name": "Georgios Vlachos",
                "color": "red"
            },
            "selUJ6hVwkBArWU1u": {
                "id": "selUJ6hVwkBArWU1u",
                "name": "Sergey Gorbunov",
                "color": "pink"
            },
            "selPXekkQGtn8lAgb": {
                "id": "selPXekkQGtn8lAgb",
                "name": "Zak Cole",
                "color": "purple"
            },
            "selvHOhtg3kncyz5M": {
                "id": "selvHOhtg3kncyz5M",
                "name": "Heikki V\u00e4nttinen",
                "color": "gray"
            },
            "selaZnVVxfxgzZevj": {
                "id": "selaZnVVxfxgzZevj",
                "name": "Seb Audet",
                "color": "blue"
            },
            "selTmC20xGyY0Rlp7": {
                "id": "selTmC20xGyY0Rlp7",
                "name": "Nodar Janashia",
                "color": "cyan"
            },
            "selzVQNa8m9fQOIFB": {
                "id": "selzVQNa8m9fQOIFB",
                "name": "William Bergamo",
                "color": "teal"
            },
            "sel3s4f4fQ4tgr5gu": {
                "id": "sel3s4f4fQ4tgr5gu",
                "name": "Samuele Cester",
                "color": "green"
            },
            "selKhm40XiZG3ovIS": {
                "id": "selKhm40XiZG3ovIS",
                "name": "Matteo Pandolfi",
                "color": "yellow"
            },
            "selF0AgeDOKI0cNMe": {
                "id": "selF0AgeDOKI0cNMe",
                "name": "Nate Geier",
                "color": "orange"
            },
            "selP0PVOisA0tC1KP": {
                "id": "selP0PVOisA0tC1KP",
                "name": "James West",
                "color": "red"
            },
            "selqyW2AS0HT5Hjqc": {
                "id": "selqyW2AS0HT5Hjqc",
                "name": "Shaun Ng",
                "color": "pink"
            },
            "selcuwKbd09YCiQ0p": {
                "id": "selcuwKbd09YCiQ0p",
                "name": "Trung Nguyen",
                "color": "purple"
            },
            "seliPdXcZuXu9WsIP": {
                "id": "seliPdXcZuXu9WsIP",
                "name": "Sergej Kunz",
                "color": "gray"
            },
            "selbGwbN7kfBTDaNL": {
                "id": "selbGwbN7kfBTDaNL",
                "name": "Anton Bukov",
                "color": "blue"
            },
            "selawLjcYwWTS2x03": {
                "id": "selawLjcYwWTS2x03",
                "name": "Amarnath Reddy T",
                "color": "cyan"
            },
            "selm9BP1fGE0N0Tu6": {
                "id": "selm9BP1fGE0N0Tu6",
                "name": "Eric Yu",
                "color": "teal"
            },
            "selvMXSP3S9LDBvTw": {
                "id": "selvMXSP3S9LDBvTw",
                "name": "Darshan Bathija",
                "color": "green"
            },
            "selKkINxXWDHz0mV8": {
                "id": "selKkINxXWDHz0mV8",
                "name": "Sanju Sony Kurian",
                "color": "yellow"
            },
            "selKnEqQo5gTY1cOi": {
                "id": "selKnEqQo5gTY1cOi",
                "name": "Kenzi Wang",
                "color": "orange"
            },
            "selCXmj1OQSUSvaoP": {
                "id": "selCXmj1OQSUSvaoP",
                "name": "Ian Duggan",
                "color": "red"
            },
            "selnIibgapXCT9KCH": {
                "id": "selnIibgapXCT9KCH",
                "name": "Michael Bentley",
                "color": "pink"
            },
            "selUVxWclbFSmlqL6": {
                "id": "selUVxWclbFSmlqL6",
                "name": "Nuno Fernandes",
                "color": "purple"
            },
            "selFDtvv53cgEJmix": {
                "id": "selFDtvv53cgEJmix",
                "name": "Francisco Varela",
                "color": "gray"
            },
            "selmQuxJyWkyV4GUr": {
                "id": "selmQuxJyWkyV4GUr",
                "name": "Ashish Singhal",
                "color": "blue"
            },
            "sel75mqoRiTq4mHlZ": {
                "id": "sel75mqoRiTq4mHlZ",
                "name": "Vimal Sagar Tiwari",
                "color": "cyan"
            },
            "selj44I4drF1SmhxD": {
                "id": "selj44I4drF1SmhxD",
                "name": "Marcus Lim",
                "color": "teal"
            },
            "selv2Dz2VOkJBLcER": {
                "id": "selv2Dz2VOkJBLcER",
                "name": "Niels Bosma",
                "color": "green"
            },
            "selSYiMqEwXIKctVB": {
                "id": "selSYiMqEwXIKctVB",
                "name": "\u017diga Toni",
                "color": "yellow"
            },
            "sel8Wg019S0Ncnpit": {
                "id": "sel8Wg019S0Ncnpit",
                "name": "Matej Gregorcic",
                "color": "orange"
            },
            "selSkLgR4NXMmjSYk": {
                "id": "selSkLgR4NXMmjSYk",
                "name": "Dejan Roljic",
                "color": "red"
            },
            "selbANZh2XU1LT1xK": {
                "id": "selbANZh2XU1LT1xK",
                "name": "Christoph Zaknun",
                "color": "pink"
            },
            "selz24kDMwH1pbwEM": {
                "id": "selz24kDMwH1pbwEM",
                "name": "Kyle Chasse",
                "color": "purple"
            },
            "selvjNqq79O3sOIhO": {
                "id": "selvjNqq79O3sOIhO",
                "name": "Hsuan-Ting",
                "color": "gray"
            },
            "selXgob6O3C2hbLwC": {
                "id": "selXgob6O3C2hbLwC",
                "name": "Ahmed Al-Balaghi",
                "color": "blue"
            },
            "selekKP2JORhpqZu1": {
                "id": "selekKP2JORhpqZu1",
                "name": "Sachin Tomar",
                "color": "cyan"
            },
            "selS4iVJevIuKjMmE": {
                "id": "selS4iVJevIuKjMmE",
                "name": "Aniket Jindal",
                "color": "teal"
            },
            "sel8w63Yy8YHNIPbv": {
                "id": "sel8w63Yy8YHNIPbv",
                "name": "Guy Oren",
                "color": "green"
            },
            "sel8rkE2dKhxrulDg": {
                "id": "sel8rkE2dKhxrulDg",
                "name": "Antonio Juliano",
                "color": "yellow"
            },
            "selc4V9p8UoDan6ZB": {
                "id": "selc4V9p8UoDan6ZB",
                "name": "Daniel Shin",
                "color": "orange"
            },
            "selyzfZcGFsU2SVbl": {
                "id": "selyzfZcGFsU2SVbl",
                "name": "Mrinal Manohar",
                "color": "red"
            },
            "selp62HZVhVf2qZH5": {
                "id": "selp62HZVhVf2qZH5",
                "name": "Daniel Tanner",
                "color": "pink"
            },
            "sel0WEK2wcOYmRKob": {
                "id": "sel0WEK2wcOYmRKob",
                "name": "Evan Shapiro",
                "color": "purple"
            },
            "selPjrShAYe9KVsIZ": {
                "id": "selPjrShAYe9KVsIZ",
                "name": "Eric Chen",
                "color": "gray"
            },
            "sell405l947SkwTVL": {
                "id": "sell405l947SkwTVL",
                "name": "Paul Mak",
                "color": "blue"
            },
            "sel9igCzHDOHXRS05": {
                "id": "sel9igCzHDOHXRS05",
                "name": "Kevin Lee",
                "color": "cyan"
            },
            "sel10znfEvmN1NBqF": {
                "id": "sel10znfEvmN1NBqF",
                "name": "Peter Kieltyka",
                "color": "teal"
            },
            "selQvlOEhorcno0Ou": {
                "id": "selQvlOEhorcno0Ou",
                "name": "Jon Myers",
                "color": "green"
            },
            "selWatWp0m2NyCfNF": {
                "id": "selWatWp0m2NyCfNF",
                "name": "Mounir Benchemled",
                "color": "yellow"
            },
            "selKjjBEBb74v2xks": {
                "id": "selKjjBEBb74v2xks",
                "name": "Will Shahda",
                "color": "orange"
            },
            "selmS3W4I0VvNeHHI": {
                "id": "selmS3W4I0VvNeHHI",
                "name": "Keyang (Jeff) R",
                "color": "red"
            },
            "seleL6fgcOlhPPAtz": {
                "id": "seleL6fgcOlhPPAtz",
                "name": "Chandresh Aharwar",
                "color": "pink"
            },
            "selpSfSUsSbVFcK5X": {
                "id": "selpSfSUsSbVFcK5X",
                "name": "Suryansh Kumar",
                "color": "purple"
            },
            "selAKmiWM8WvxOLLM": {
                "id": "selAKmiWM8WvxOLLM",
                "name": "Tarun Malik",
                "color": "gray"
            },
            "selhFhjxTSGkNEJCP": {
                "id": "selhFhjxTSGkNEJCP",
                "name": "Kevin Tai",
                "color": "blue"
            },
            "selMBJWrS7A5ddwHv": {
                "id": "selMBJWrS7A5ddwHv",
                "name": "Jason Eisen",
                "color": "cyan"
            },
            "selZQxa8Ngx0fqifF": {
                "id": "selZQxa8Ngx0fqifF",
                "name": "Dr. Bastian Blankenburg",
                "color": "teal"
            },
            "selxI9Lt1J48GxzJw": {
                "id": "selxI9Lt1J48GxzJw",
                "name": "Hilmar Orth",
                "color": "green"
            },
            "seloK27HBKHmP17pz": {
                "id": "seloK27HBKHmP17pz",
                "name": "Luis Schliesske",
                "color": "yellow"
            },
            "seltIROg6KPYGYUjs": {
                "id": "seltIROg6KPYGYUjs",
                "name": "Troy Murray",
                "color": "orange"
            },
            "selTw3hrULXyysC2p": {
                "id": "selTw3hrULXyysC2p",
                "name": "Tyler Ward",
                "color": "red"
            },
            "selBwHcbH2QWxGorS": {
                "id": "selBwHcbH2QWxGorS",
                "name": "Milad Mostavi",
                "color": "pink"
            },
            "sellN02ApNe35brnt": {
                "id": "sellN02ApNe35brnt",
                "name": "Dragos Rizescu",
                "color": "purple"
            },
            "selv0aX5BQbWzqiM4": {
                "id": "selv0aX5BQbWzqiM4",
                "name": "Bogdan Gheorghe",
                "color": "gray"
            },
            "sel53hNlhXAzreFGY": {
                "id": "sel53hNlhXAzreFGY",
                "name": "Tushar Aggarwal",
                "color": "blue"
            },
            "selPjcRn2bjmTVjG5": {
                "id": "selPjcRn2bjmTVjG5",
                "name": "Deepanshu Tripathi",
                "color": "cyan"
            },
            "sel28mmlbT6VkhasJ": {
                "id": "sel28mmlbT6VkhasJ",
                "name": "James Sangalli",
                "color": "teal"
            },
            "selx1mjgFqkbDAQ8E": {
                "id": "selx1mjgFqkbDAQ8E",
                "name": "Jenil Thakker",
                "color": "green"
            },
            "selwiZvpLYBLmkiBC": {
                "id": "selwiZvpLYBLmkiBC",
                "name": "Itay Malinger",
                "color": "yellow"
            },
            "selkqgoceRFRHq6bV": {
                "id": "selkqgoceRFRHq6bV",
                "name": "Dan Yadlin",
                "color": "orange"
            },
            "selDF834ZpxXangLB": {
                "id": "selDF834ZpxXangLB",
                "name": "Tim Wagner",
                "color": "red"
            },
            "seltNxDzYk1weQWsh": {
                "id": "seltNxDzYk1weQWsh",
                "name": "Shruthi Rao",
                "color": "pink"
            },
            "sel2EXGNTte4pn5MD": {
                "id": "sel2EXGNTte4pn5MD",
                "name": "Aditya Palepu",
                "color": "purple"
            },
            "selfnTDNtWNNrrLaE": {
                "id": "selfnTDNtWNNrrLaE",
                "name": "Evgeny Gaevoy",
                "color": "gray"
            },
            "selVc590itUzyNIoL": {
                "id": "selVc590itUzyNIoL",
                "name": "Piers Ridyard",
                "color": "blue"
            },
            "selidowPlMaT4FP1O": {
                "id": "selidowPlMaT4FP1O",
                "name": "Dan Hughes",
                "color": "cyan"
            },
            "sel6KM3iA1LtKl0Kc": {
                "id": "sel6KM3iA1LtKl0Kc",
                "name": "Sebastian B\u00fcrgel",
                "color": "teal"
            },
            "selh9kSQOnDLtaHrR": {
                "id": "selh9kSQOnDLtaHrR",
                "name": "Kfir Nissan",
                "color": "green"
            },
            "selD1F6T2bkhLvdSH": {
                "id": "selD1F6T2bkhLvdSH",
                "name": "Yuval Rooz",
                "color": "yellow"
            },
            "selCCFoHsPBhF6cmQ": {
                "id": "selCCFoHsPBhF6cmQ",
                "name": "Adrien Treccani",
                "color": "orange"
            },
            "selr2Azfac4fJEY1T": {
                "id": "selr2Azfac4fJEY1T",
                "name": "J. Gdanski",
                "color": "red"
            },
            "selKl6dg4LMvq4wW3": {
                "id": "selKl6dg4LMvq4wW3",
                "name": "Raymond Zenkich",
                "color": "pink"
            },
            "sellpDRKdOfAbkFxl": {
                "id": "sellpDRKdOfAbkFxl",
                "name": "Ryan Berkun",
                "color": "purple"
            },
            "selGdIivq5fYjfdLz": {
                "id": "selGdIivq5fYjfdLz",
                "name": "Ivan Perez",
                "color": "gray"
            },
            "sell1mgRMpdLzrjl0": {
                "id": "sell1mgRMpdLzrjl0",
                "name": "Lihan Hyunwoo Lee",
                "color": "blue"
            },
            "selFWrunup62yyrCW": {
                "id": "selFWrunup62yyrCW",
                "name": "Pawe\u0142 Kuskowski",
                "color": "cyan"
            },
            "seltCAmi1ReT7X21S": {
                "id": "seltCAmi1ReT7X21S",
                "name": "Gilbert Verdian",
                "color": "teal"
            },
            "selhFKGfzfZQe8jTW": {
                "id": "selhFKGfzfZQe8jTW",
                "name": "Farzam Ehsani",
                "color": "green"
            },
            "seln0Ss50itiDNmHE": {
                "id": "seln0Ss50itiDNmHE",
                "name": "Sasha Ivanova",
                "color": "yellow"
            },
            "selouSNG7DlzuTT0F": {
                "id": "selouSNG7DlzuTT0F",
                "name": "Mona El Isa",
                "color": "orange"
            },
            "selRGwX1c6WAdijlJ": {
                "id": "selRGwX1c6WAdijlJ",
                "name": "Leo Li",
                "color": "red"
            },
            "selfsQ1PDSFYJwt0O": {
                "id": "selfsQ1PDSFYJwt0O",
                "name": "Albert Chon",
                "color": "pink"
            },
            "sel6GznlRjYGJ76WS": {
                "id": "sel6GznlRjYGJ76WS",
                "name": "Kader Kutun",
                "color": "purple"
            },
            "selPZyLsXoBGXV3FF": {
                "id": "selPZyLsXoBGXV3FF",
                "name": "Roneil Rumburg",
                "color": "gray"
            },
            "selxsUzGEUdCUaXXL": {
                "id": "selxsUzGEUdCUaXXL",
                "name": "Jeremy Allaire",
                "color": "blue"
            },
            "sel9ogzlfP2Bk2lBc": {
                "id": "sel9ogzlfP2Bk2lBc",
                "name": "Zach Burks",
                "color": "cyan"
            },
            "selDhRiiYlRXsh5bF": {
                "id": "selDhRiiYlRXsh5bF",
                "name": "Maxim Blagov",
                "color": "teal"
            },
            "selU8g2YnWEngIwcM": {
                "id": "selU8g2YnWEngIwcM",
                "name": "Antoine Scalia",
                "color": "green"
            },
            "selSEIplDfm3IhsO0": {
                "id": "selSEIplDfm3IhsO0",
                "name": "Shane Benjamin",
                "color": "yellow"
            },
            "selZvafu8P8c9Z2yC": {
                "id": "selZvafu8P8c9Z2yC",
                "name": "Sid Jha",
                "color": "orange"
            },
            "selgkPVatI7Lp2JaE": {
                "id": "selgkPVatI7Lp2JaE",
                "name": "Ben Andre",
                "color": "red"
            },
            "selFCag9I7hwKge0W": {
                "id": "selFCag9I7hwKge0W",
                "name": "Philippe Heilberg",
                "color": "pink"
            },
            "selvEM6Mg9KNiQdDw": {
                "id": "selvEM6Mg9KNiQdDw",
                "name": "Osho Jha",
                "color": "purple"
            },
            "selL0GkxgYeWvDMEn": {
                "id": "selL0GkxgYeWvDMEn",
                "name": "Vladim\u00edr Lieger",
                "color": "gray"
            },
            "selC8XmKqP6JEiTZy": {
                "id": "selC8XmKqP6JEiTZy",
                "name": "Dion Dalton-Bridges",
                "color": "blue"
            },
            "selbXdXTQIdi6StWw": {
                "id": "selbXdXTQIdi6StWw",
                "name": "Balint Orosz",
                "color": "cyan"
            },
            "selmXqvHojmwPauOj": {
                "id": "selmXqvHojmwPauOj",
                "name": "Mik Mironov",
                "color": "teal"
            },
            "sel4JwezXc5gIQihU": {
                "id": "sel4JwezXc5gIQihU",
                "name": "Logan Saether",
                "color": "green"
            },
            "selXs4pw3BU15dHcU": {
                "id": "selXs4pw3BU15dHcU",
                "name": "Andrii Kotsur",
                "color": "yellow"
            },
            "selcyyr7twMO7uUFL": {
                "id": "selcyyr7twMO7uUFL",
                "name": "Louis Liu",
                "color": "orange"
            },
            "selm35DqjtQkqxEd9": {
                "id": "selm35DqjtQkqxEd9",
                "name": "Julian Sun",
                "color": "red"
            },
            "sel2ukCZlgMeDh2iM": {
                "id": "sel2ukCZlgMeDh2iM",
                "name": "Mike Tang",
                "color": "pink"
            },
            "seloKRq9zGeVEpfBl": {
                "id": "seloKRq9zGeVEpfBl",
                "name": "Bart R. Bordallo",
                "color": "purple"
            },
            "seli76UJI2wmfdEv8": {
                "id": "seli76UJI2wmfdEv8",
                "name": "David Rodr\u00edguez",
                "color": "gray"
            },
            "seleDjy3i6Ayjd808": {
                "id": "seleDjy3i6Ayjd808",
                "name": "Abdul Rafay Gadit",
                "color": "blue"
            },
            "sel8hAD2GC7Cl62s1": {
                "id": "sel8hAD2GC7Cl62s1",
                "name": "Alex Melikhov",
                "color": "cyan"
            },
            "seluQvhbMMpt8dKyn": {
                "id": "seluQvhbMMpt8dKyn",
                "name": "Mira Brezhynskaia",
                "color": "teal"
            },
            "selQ2JyAYjpomp8pn": {
                "id": "selQ2JyAYjpomp8pn",
                "name": "Camila Russo",
                "color": "green"
            },
            "sel4WknRFxPM3yfB0": {
                "id": "sel4WknRFxPM3yfB0",
                "name": "Sam Cassatt",
                "color": "yellow"
            },
            "selXaMN8npR6DFLCL": {
                "id": "selXaMN8npR6DFLCL",
                "name": "Joseph Lubin",
                "color": "orange"
            },
            "selLei2EcyxIJ29PH": {
                "id": "selLei2EcyxIJ29PH",
                "name": "Julian Koh",
                "color": "red"
            },
            "sellvC5zaIsj9J1NU": {
                "id": "sellvC5zaIsj9J1NU",
                "name": "Erick Calderon",
                "color": "pink"
            },
            "selh0gSWN48EEo1QH": {
                "id": "selh0gSWN48EEo1QH",
                "name": "Saeed Hareb Al Darmaki",
                "color": "blue"
            },
            "selISvYSlb2ZRfzfl": {
                "id": "selISvYSlb2ZRfzfl",
                "name": "Georga Harrap",
                "color": "blue"
            },
            "selkU2aL4kmxUQTAl": {
                "id": "selkU2aL4kmxUQTAl",
                "name": "Connor Howe",
                "color": "blue"
            },
            "seloqLhtbBihyQ5ip": {
                "id": "seloqLhtbBihyQ5ip",
                "name": "Rachel Lin",
                "color": "blue"
            },
            "selOhX6QoOWrWzAXb": {
                "id": "selOhX6QoOWrWzAXb",
                "name": "Jeffrey Lin",
                "color": "blue"
            },
            "selSLFcwcuIeEN5jm": {
                "id": "selSLFcwcuIeEN5jm",
                "name": "Roy",
                "color": "blue"
            },
            "selYGczzYhs5zwzBW": {
                "id": "selYGczzYhs5zwzBW",
                "name": "Dan Mgbor",
                "color": "blue"
            },
            "selnwTQaEdtkilsKS": {
                "id": "selnwTQaEdtkilsKS",
                "name": "Thanh Le",
                "color": "blue"
            },
            "seliYrmUXJnOdBq0r": {
                "id": "seliYrmUXJnOdBq0r",
                "name": "Kevin Owocki",
                "color": "blue"
            },
            "selowhIOLQ2Mf7dtw": {
                "id": "selowhIOLQ2Mf7dtw",
                "name": "Eric Demuth",
                "color": "blue"
            },
            "selwFJb2O8sxBNcSE": {
                "id": "selwFJb2O8sxBNcSE",
                "name": "Simon Chamorro",
                "color": "blue"
            },
            "selV63VRG8pV5d2sL": {
                "id": "selV63VRG8pV5d2sL",
                "name": "Mark Webster",
                "color": "blue"
            },
            "selyyN4VDTsH74LBQ": {
                "id": "selyyN4VDTsH74LBQ",
                "name": "Carson Smith",
                "color": "blue"
            },
            "selI50t1GBemGhkWp": {
                "id": "selI50t1GBemGhkWp",
                "name": "William Le",
                "color": "cyan"
            },
            "selgpdjeu17nGow4J": {
                "id": "selgpdjeu17nGow4J",
                "name": "Rayne S.",
                "color": "teal"
            },
            "selUVTCB9EolZjxcX": {
                "id": "selUVTCB9EolZjxcX",
                "name": "Guido Buehler",
                "color": "green"
            },
            "selr4AikQhJieYCZ8": {
                "id": "selr4AikQhJieYCZ8",
                "name": "Julian Traversa",
                "color": "yellow"
            },
            "selAEIvYOapt2FCkp": {
                "id": "selAEIvYOapt2FCkp",
                "name": "Tim Frost",
                "color": "orange"
            },
            "selxuZUIhZCgWXZ6x": {
                "id": "selxuZUIhZCgWXZ6x",
                "name": "Andrey Belyakov",
                "color": "red"
            },
            "selz99GadVNQ3QuLL": {
                "id": "selz99GadVNQ3QuLL",
                "name": "Lorien Gabel",
                "color": "pink"
            },
            "sel1WqhPrvIVNnGmR": {
                "id": "sel1WqhPrvIVNnGmR",
                "name": "Shayne Coplan",
                "color": "purple"
            },
            "selLZJ5bVsK0zn5mw": {
                "id": "selLZJ5bVsK0zn5mw",
                "name": "Mike Hutting",
                "color": "gray"
            },
            "sel692jNDGVWnpemG": {
                "id": "sel692jNDGVWnpemG",
                "name": "Vlad Tenev",
                "color": "blue"
            },
            "selw1m4wV0H9b5rUD": {
                "id": "selw1m4wV0H9b5rUD",
                "name": "Edward Woodford",
                "color": "cyan"
            },
            "selXy1un0Oe0lKRAb": {
                "id": "selXy1un0Oe0lKRAb",
                "name": "Archit Aggarwal",
                "color": "teal"
            },
            "selLwzuBaCqHPRoCQ": {
                "id": "selLwzuBaCqHPRoCQ",
                "name": "Lewis Rock",
                "color": "green"
            },
            "selcoLzynAbo8FiNO": {
                "id": "selcoLzynAbo8FiNO",
                "name": "Malcolm Lerider",
                "color": "yellow"
            },
            "selDpZCuQ6CaR1YKj": {
                "id": "selDpZCuQ6CaR1YKj",
                "name": "George Yang",
                "color": "blue"
            },
            "selzuGthfRiPHO6lm": {
                "id": "selzuGthfRiPHO6lm",
                "name": "Neil Sisson",
                "color": "blue"
            },
            "selWPsL78t14eSYbV": {
                "id": "selWPsL78t14eSYbV",
                "name": "Ruitao Su",
                "color": "blue"
            },
            "selC2Dki74p6VXAWO": {
                "id": "selC2Dki74p6VXAWO",
                "name": "Alex Wearn",
                "color": "blue"
            },
            "selIPoQqCxWLfGxWu": {
                "id": "selIPoQqCxWLfGxWu",
                "name": "Liam Young",
                "color": "blue"
            },
            "sel5qCpJMyqlAlUtQ": {
                "id": "sel5qCpJMyqlAlUtQ",
                "name": "John Liu",
                "color": "gray"
            },
            "selt21ldY8qzC9UFd": {
                "id": "selt21ldY8qzC9UFd",
                "name": "Palash Jain",
                "color": "blue"
            },
            "selitZD0LIHlidQF0": {
                "id": "selitZD0LIHlidQF0",
                "name": "Yenwen Feng",
                "color": "blue"
            },
            "selB1tm2RSwXbqpRQ": {
                "id": "selB1tm2RSwXbqpRQ",
                "name": "Lawrence Lim",
                "color": "blue"
            },
            "selZSjFRgpHyhtZXF": {
                "id": "selZSjFRgpHyhtZXF",
                "name": "Bova Chen",
                "color": "blue"
            },
            "selCwxQtcr7Ox6RfJ": {
                "id": "selCwxQtcr7Ox6RfJ",
                "name": "Milana Valmont",
                "color": "blue"
            },
            "selmBu3L4VYRH4PDz": {
                "id": "selmBu3L4VYRH4PDz",
                "name": "Ish Goel",
                "color": "blue"
            },
            "selMgoPuOlVfeNey9": {
                "id": "selMgoPuOlVfeNey9",
                "name": "Jason W.",
                "color": "blue"
            },
            "sel1fzBghitfF34Cf": {
                "id": "sel1fzBghitfF34Cf",
                "name": "Arpit Agarwal",
                "color": "blue"
            },
            "selLY1DTaoFYWOCdC": {
                "id": "selLY1DTaoFYWOCdC",
                "name": "Hrishikesh Huilgolkar",
                "color": "blue"
            },
            "selUwZw9ey9QL419W": {
                "id": "selUwZw9ey9QL419W",
                "name": "Max Boonen",
                "color": "blue"
            },
            "sel2uoGsryloJWe0n": {
                "id": "sel2uoGsryloJWe0n",
                "name": "Emin Gun Sirer",
                "color": "blue"
            },
            "seliFaf8pRQuxdHWx": {
                "id": "seliFaf8pRQuxdHWx",
                "name": "Gavin Wood",
                "color": "blue"
            },
            "selQk98hYN4aXv6h6": {
                "id": "selQk98hYN4aXv6h6",
                "name": "Stani Kulechov",
                "color": "blue"
            },
            "selZq1akM0v45Kb2M": {
                "id": "selZq1akM0v45Kb2M",
                "name": "Brandon Ramirez",
                "color": "pink"
            },
            "selBSIu3wbWses3gW": {
                "id": "selBSIu3wbWses3gW",
                "name": "Yuriy Sorokin",
                "color": "blue"
            },
            "selGSHR4syMTcwDWY": {
                "id": "selGSHR4syMTcwDWY",
                "name": "Fernando Martinelli",
                "color": "blue"
            },
            "selvDwrqgrf05VbjD": {
                "id": "selvDwrqgrf05VbjD",
                "name": "Gary Bracey",
                "color": "blue"
            },
            "sel03iP7Cdm87hnZ0": {
                "id": "sel03iP7Cdm87hnZ0",
                "name": "Benjamin Jones",
                "color": "blue"
            },
            "sellwKIE8S4qTH6Nr": {
                "id": "sellwKIE8S4qTH6Nr",
                "name": "Ivan Poon",
                "color": "blue"
            },
            "seltuy1ZwhSx5H9Qs": {
                "id": "seltuy1ZwhSx5H9Qs",
                "name": "Sia Mohajer",
                "color": "blue"
            },
            "selhGSXm8D9bzpbVs": {
                "id": "selhGSXm8D9bzpbVs",
                "name": "Chandrashekar Ramu",
                "color": "blue"
            },
            "seljhfII65PCciHew": {
                "id": "seljhfII65PCciHew",
                "name": "Evgheny Turvinenko",
                "color": "blue"
            },
            "selv1Z4FLk6bfnZEp": {
                "id": "selv1Z4FLk6bfnZEp",
                "name": "Mohit Madan",
                "color": "blue"
            },
            "selpaOb1HoTBho5oA": {
                "id": "selpaOb1HoTBho5oA",
                "name": "Ryan Gittleson",
                "color": "blue"
            },
            "selM7alNGPOIXZ6vt": {
                "id": "selM7alNGPOIXZ6vt",
                "name": "James Hong",
                "color": "gray"
            },
            "selrqeV05uUtwQsqo": {
                "id": "selrqeV05uUtwQsqo",
                "name": "Dhanraj Dadhich",
                "color": "cyan"
            },
            "selNflACKrbbwL4vr": {
                "id": "selNflACKrbbwL4vr",
                "name": "Kor Kiang Sean",
                "color": "yellow"
            },
            "selIMi95NgIUdrCUD": {
                "id": "selIMi95NgIUdrCUD",
                "name": "Perrin Quarshie",
                "color": "red"
            },
            "sel8m4eLZQf9Kuij9": {
                "id": "sel8m4eLZQf9Kuij9",
                "name": "Naman Srivastava",
                "color": "green"
            },
            "seluUKICiqmUExCFI": {
                "id": "seluUKICiqmUExCFI",
                "name": "Kevin De Patoul",
                "color": "yellow"
            },
            "selu03Z0j1EDHSmAU": {
                "id": "selu03Z0j1EDHSmAU",
                "name": "Vadym Kurylovych",
                "color": "pink"
            },
            "sel60TDqgcSzJOFst": {
                "id": "sel60TDqgcSzJOFst",
                "name": "Alex Svanevik",
                "color": "pink"
            },
            "selUmJBQq6damB9yQ": {
                "id": "selUmJBQq6damB9yQ",
                "name": "Bradley Miles",
                "color": "blue"
            },
            "selBvfETZgAvSSWwJ": {
                "id": "selBvfETZgAvSSWwJ",
                "name": "Jacob Horne",
                "color": "blue"
            },
            "selVlmUxyRs4bmq8B": {
                "id": "selVlmUxyRs4bmq8B",
                "name": "Teddy Woodward",
                "color": "green"
            },
            "selaUNTwIvTZPMM4S": {
                "id": "selaUNTwIvTZPMM4S",
                "name": "Graham Rodford",
                "color": "teal"
            },
            "selrwc2Hif2YROAlL": {
                "id": "selrwc2Hif2YROAlL",
                "name": "Nick Dodson",
                "color": "teal"
            },
            "seljaynK3e9RaSIFG": {
                "id": "seljaynK3e9RaSIFG",
                "name": "Luke Hoersten",
                "color": "teal"
            },
            "seliCELlmnsxLy65k": {
                "id": "seliCELlmnsxLy65k",
                "name": "Tascha Punyaneramitdee",
                "color": "blue"
            },
            "selYrts8EpwouyvH4": {
                "id": "selYrts8EpwouyvH4",
                "name": "Tarun Chitra",
                "color": "blue"
            },
            "selUBZnFwIG9cJAHn": {
                "id": "selUBZnFwIG9cJAHn",
                "name": "secures critical supplier",
                "color": "blue"
            },
            "selWi4FXi5h4mq69I": {
                "id": "selWi4FXi5h4mq69I",
                "name": "product",
                "color": "cyan"
            },
            "selsTBnw5H8dP0r68": {
                "id": "selsTBnw5H8dP0r68",
                "name": "and shipment data to give customers a competitive edge in the increasingly dynamic global marketplace",
                "color": "teal"
            },
            "sel3Oysku4NExpQdJ": {
                "id": "sel3Oysku4NExpQdJ",
                "name": "Mingda Lei",
                "color": "blue"
            },
            "sel2gWPu3CeMJcGJ4": {
                "id": "sel2gWPu3CeMJcGJ4",
                "name": "Adam Jackson",
                "color": "blue"
            },
            "selPYPWxcndLexckU": {
                "id": "selPYPWxcndLexckU",
                "name": "Natalia Karayaneva",
                "color": "teal"
            },
            "seluoBeQh1zKIwj9o": {
                "id": "seluoBeQh1zKIwj9o",
                "name": "Gil Shpirman",
                "color": "blue"
            },
            "selASBKtEDqb62kyN": {
                "id": "selASBKtEDqb62kyN",
                "name": "Jon Lister",
                "color": "blue"
            },
            "selC66MtrlxfENoR6": {
                "id": "selC66MtrlxfENoR6",
                "name": "Vishal Shah",
                "color": "gray"
            },
            "selICaJHIv1jNQiYy": {
                "id": "selICaJHIv1jNQiYy",
                "name": "Martin Froehler",
                "color": "blue"
            },
            "selKqkR9OwuSsmLMI": {
                "id": "selKqkR9OwuSsmLMI",
                "name": "Tung Dao",
                "color": "blue"
            },
            "selN10GkK9YCGBpNz": {
                "id": "selN10GkK9YCGBpNz",
                "name": "Andrzej Horoszczak",
                "color": "cyan"
            },
            "selCkXS9uHLv3awIk": {
                "id": "selCkXS9uHLv3awIk",
                "name": "Wojciech Kostrzewa",
                "color": "orange"
            },
            "selXlofexrcVadaFs": {
                "id": "selXlofexrcVadaFs",
                "name": "Paul Claudius",
                "color": "blue"
            },
            "selPG1oPNUIOELb9J": {
                "id": "selPG1oPNUIOELb9J",
                "name": "Sam Bankman-Fried",
                "color": "blue"
            },
            "selxvksHTBer0xPW2": {
                "id": "selxvksHTBer0xPW2",
                "name": "Will Harborne",
                "color": "pink"
            },
            "sel0MqMTll0xEXNF4": {
                "id": "sel0MqMTll0xEXNF4",
                "name": "Illia Polosukhin",
                "color": "teal"
            },
            "selKxJEenNcPVVjMe": {
                "id": "selKxJEenNcPVVjMe",
                "name": "Alexander Skidanov",
                "color": "green"
            },
            "sel5R5eQfd2m2WnIz": {
                "id": "sel5R5eQfd2m2WnIz",
                "name": "Chris Maurice",
                "color": "yellow"
            },
            "selG8Oq8vXfdv2LES": {
                "id": "selG8Oq8vXfdv2LES",
                "name": "Sebastien Borget",
                "color": "orange"
            },
            "selD7oAvABXXOcWYP": {
                "id": "selD7oAvABXXOcWYP",
                "name": "Igor Barinov ",
                "color": "cyan"
            },
            "sel9Rhxd1s33Yal4H": {
                "id": "sel9Rhxd1s33Yal4H",
                "name": "Nicolas Andreoulis",
                "color": "pink"
            },
            "selLaghjt9Uyzq0PC": {
                "id": "selLaghjt9Uyzq0PC",
                "name": "Amo Huang",
                "color": "teal"
            },
            "selbC4AlAjwbyt665": {
                "id": "selbC4AlAjwbyt665",
                "name": "Emanuele Francioni",
                "color": "red"
            },
            "selhFwhiOGxwetiLH": {
                "id": "selhFwhiOGxwetiLH",
                "name": "Payom Dousti",
                "color": "blue"
            },
            "selfj3YncHq3pSPU8": {
                "id": "selfj3YncHq3pSPU8",
                "name": "Jack Tan",
                "color": "blue"
            },
            "selY2GIT1A8YTcWez": {
                "id": "selY2GIT1A8YTcWez",
                "name": "Mark Pimentel",
                "color": "teal"
            },
            "sel7O99GcAiJT7mXZ": {
                "id": "sel7O99GcAiJT7mXZ",
                "name": "Marco Chen",
                "color": "tealDark"
            },
            "selIR3gAUXH5bOsX7": {
                "id": "selIR3gAUXH5bOsX7",
                "name": "Howard Wu",
                "color": "blueDarker"
            },
            "selcNZRA6VjDiUz3q": {
                "id": "selcNZRA6VjDiUz3q",
                "name": "Nick Sawinyh",
                "color": "cyanDarker"
            },
            "sel02IcC7H8bfVKf7": {
                "id": "sel02IcC7H8bfVKf7",
                "name": "Jo\u00ebl Hubert",
                "color": "red"
            },
            "selPd4U4rvFVtriTs": {
                "id": "selPd4U4rvFVtriTs",
                "name": "Dunstan Teo",
                "color": "purpleDark"
            },
            "selwVG49MFQqHewRP": {
                "id": "selwVG49MFQqHewRP",
                "name": "Anish Mohammed",
                "color": "grayDarker"
            },
            "selmqmu9ilsiee3YX": {
                "id": "selmqmu9ilsiee3YX",
                "name": "Philippe Bekhazi",
                "color": "redDark"
            },
            "selkr9q7arSPh9xcv": {
                "id": "selkr9q7arSPh9xcv",
                "name": "Juliun Brabon",
                "color": "blue"
            },
            "sellAfruUL811QsIF": {
                "id": "sellAfruUL811QsIF",
                "name": "Dennis Mak",
                "color": "orange"
            },
            "seldvXUSECLSz2WIB": {
                "id": "seldvXUSECLSz2WIB",
                "name": "Bill Walsh",
                "color": "red"
            },
            "sel8j1qP1ZnmRpO6H": {
                "id": "sel8j1qP1ZnmRpO6H",
                "name": "Daniel Stockhaus",
                "color": "pinkMedium"
            },
            "seleto2biv70Topv0": {
                "id": "seleto2biv70Topv0",
                "name": "Andy Cheung",
                "color": "cyanDark"
            },
            "selhGDNkE7hqRhGbw": {
                "id": "selhGDNkE7hqRhGbw",
                "name": "Hang Yin",
                "color": "pink"
            },
            "seleTTirRgzlJGDRm": {
                "id": "seleTTirRgzlJGDRm",
                "name": "Dohyun Pak",
                "color": "greenDarker"
            },
            "selvahDC7crH8wlw7": {
                "id": "selvahDC7crH8wlw7",
                "name": "Thibaut Sahaghian",
                "color": "purpleDarker"
            },
            "sel7DHz280V2q17n1": {
                "id": "sel7DHz280V2q17n1",
                "name": "Tomas Ronn",
                "color": "blue"
            },
            "sel6upW1XfyCqbrb3": {
                "id": "sel6upW1XfyCqbrb3",
                "name": "David Johansson",
                "color": "cyanMedium"
            },
            "selb6vrJocl81eMUT": {
                "id": "selb6vrJocl81eMUT",
                "name": "TN",
                "color": "pinkMedium"
            },
            "selo2Ye1juqKjZVNV": {
                "id": "selo2Ye1juqKjZVNV",
                "name": "Andrei Terentiev",
                "color": "cyan"
            },
            "selTZAZZNgpqVjgla": {
                "id": "selTZAZZNgpqVjgla",
                "name": "Tiantian Kullander",
                "color": "blueMedium"
            },
            "seliNXlFGXcAB677A": {
                "id": "seliNXlFGXcAB677A",
                "name": "Allen Wong",
                "color": "cyanMedium"
            },
            "selWTm1nx6nXmslqo": {
                "id": "selWTm1nx6nXmslqo",
                "name": "Nathaniel Mendoza",
                "color": "blueMedium"
            },
            "selNN2WuprjK3sU3z": {
                "id": "selNN2WuprjK3sU3z",
                "name": "Richard Parris",
                "color": "blue"
            },
            "selvnfjmFZegObqb0": {
                "id": "selvnfjmFZegObqb0",
                "name": "David Lancashire",
                "color": "yellowDarker"
            },
            "seleQoUAnP8qoyrHR": {
                "id": "seleQoUAnP8qoyrHR",
                "name": "Tim Ho",
                "color": "blueDark"
            },
            "sel7U0M5cqKPaxFsH": {
                "id": "sel7U0M5cqKPaxFsH",
                "name": "Cindy Wu",
                "color": "cyanMedium"
            },
            "selQLW48KR8evtdCx": {
                "id": "selQLW48KR8evtdCx",
                "name": "Ioannis Giannaros",
                "color": "grayDark"
            },
            "selcb9lMiPUhLUlzj": {
                "id": "selcb9lMiPUhLUlzj",
                "name": "Anand Gomes",
                "color": "pinkDarker"
            },
            "selVv5tyULk3rTLft": {
                "id": "selVv5tyULk3rTLft",
                "name": "Pelle Br\u00e6ndgaard",
                "color": "red"
            },
            "sel5SDGpsiqJXtlf5": {
                "id": "sel5SDGpsiqJXtlf5",
                "name": "Jonas Lamis",
                "color": "redMedium"
            },
            "selQNG2K5AmAUhpIr": {
                "id": "selQNG2K5AmAUhpIr",
                "name": "Miles Anthony",
                "color": "orangeDarker"
            },
            "seleHqlxAfmzMg0cE": {
                "id": "seleHqlxAfmzMg0cE",
                "name": "Romain Rouphael",
                "color": "red"
            },
            "selvBonPNC8PgBcbA": {
                "id": "selvBonPNC8PgBcbA",
                "name": "Richard Byworth",
                "color": "redDarker"
            },
            "sel0QZ5rtF0k0kFkg": {
                "id": "sel0QZ5rtF0k0kFkg",
                "name": "Jerome F",
                "color": "yellowMedium"
            },
            "selNSGtiyQFiIZ1TD": {
                "id": "selNSGtiyQFiIZ1TD",
                "name": "Greg Waisman ",
                "color": "pinkDarker"
            },
            "selMA7KI2fjWclaNo": {
                "id": "selMA7KI2fjWclaNo",
                "name": "Jeffery Liu",
                "color": "teal"
            },
            "selM1KmePIENJTMLO": {
                "id": "selM1KmePIENJTMLO",
                "name": "Leo Wang Crust",
                "color": "purpleDarker"
            },
            "selLqxA5l02L4nUi8": {
                "id": "selLqxA5l02L4nUi8",
                "name": "Guo Tao",
                "color": "cyanDark"
            },
            "selTBzKTL5QVfkPKN": {
                "id": "selTBzKTL5QVfkPKN",
                "name": "David Vorick",
                "color": "redDark"
            },
            "selBQTQjUzqu6syHB": {
                "id": "selBQTQjUzqu6syHB",
                "name": "Joel Birch",
                "color": "redMedium"
            },
            "seliI3tDdLQAzEWoV": {
                "id": "seliI3tDdLQAzEWoV",
                "name": "Paul Gambill",
                "color": "cyanDark"
            },
            "selgBNI7U9R0xlKmO": {
                "id": "selgBNI7U9R0xlKmO",
                "name": "Andrew Bruce",
                "color": "cyanDarker"
            },
            "seloxYzx7VWQ8l1KE": {
                "id": "seloxYzx7VWQ8l1KE",
                "name": "Fredrik Haga",
                "color": "yellowDarker"
            },
            "selt1tIz658ooBaJM": {
                "id": "selt1tIz658ooBaJM",
                "name": "Lim Hong Zhuang",
                "color": "redDark"
            },
            "sel3mge9nSBIFg7ep": {
                "id": "sel3mge9nSBIFg7ep",
                "name": "Joshua Noble",
                "color": "yellowDark"
            },
            "selaok1CeITfKT118": {
                "id": "selaok1CeITfKT118",
                "name": "Kevin Nielsen",
                "color": "tealDark"
            },
            "seloNt0xEhEEOUaeQ": {
                "id": "seloNt0xEhEEOUaeQ",
                "name": "Carson Cook",
                "color": "redMedium"
            },
            "selZswM7ODWSDbcTJ": {
                "id": "selZswM7ODWSDbcTJ",
                "name": "Alex Masmejean",
                "color": "yellowMedium"
            },
            "selyKVcXH8vAKZcx7": {
                "id": "selyKVcXH8vAKZcx7",
                "name": "Alex Adelman",
                "color": "blue"
            },
            "sel5eMnAR3U7jU6dS": {
                "id": "sel5eMnAR3U7jU6dS",
                "name": "Allan Ta",
                "color": "cyan"
            },
            "sel1oIv1l5Id7Ue6t": {
                "id": "sel1oIv1l5Id7Ue6t",
                "name": "Elena Nadolinski",
                "color": "yellowDark"
            },
            "selDOpXR8HHgEB5Yz": {
                "id": "selDOpXR8HHgEB5Yz",
                "name": "Shivam Tandon",
                "color": "blue"
            },
            "selcGyQM8C704TtPL": {
                "id": "selcGyQM8C704TtPL",
                "name": "Adrian Brink",
                "color": "blue"
            },
            "sel371aB9DfkCe1en": {
                "id": "sel371aB9DfkCe1en",
                "name": "Charles Storry",
                "color": "blue"
            },
            "selJMImjynbrYpelj": {
                "id": "selJMImjynbrYpelj",
                "name": "Sam Bacha",
                "color": "blue"
            },
            "selb9fLmhQ2Z9bPJG": {
                "id": "selb9fLmhQ2Z9bPJG",
                "name": "Nikil Viswanathan",
                "color": "yellowDarker"
            },
            "selQV4Tz2yDGxkuCk": {
                "id": "selQV4Tz2yDGxkuCk",
                "name": "Leonardo Carvalho",
                "color": "blue"
            },
            "selafklrnUw11ogXd": {
                "id": "selafklrnUw11ogXd",
                "name": "Alessandro Palombo",
                "color": "blue"
            },
            "selMqHuwj4IO23xy3": {
                "id": "selMqHuwj4IO23xy3",
                "name": "Eric Poh",
                "color": "purpleMedium"
            },
            "selrJ9Wc0C5CGIZ4S": {
                "id": "selrJ9Wc0C5CGIZ4S",
                "name": "Ivan on Tech",
                "color": "blue"
            },
            "selus1TgwT8X0mJbL": {
                "id": "selus1TgwT8X0mJbL",
                "name": "Marcello Mari",
                "color": "cyanDark"
            },
            "seliGZhfDuqLhKkZ8": {
                "id": "seliGZhfDuqLhKkZ8",
                "name": "Gareth David Bowles",
                "color": "blue"
            },
            "selSZaizwLGQXdNhD": {
                "id": "selSZaizwLGQXdNhD",
                "name": "https://fantom.foundation/",
                "color": "blue"
            },
            "sel1HEyHLuJRQ9D4g": {
                "id": "sel1HEyHLuJRQ9D4g",
                "name": "Akash Nigam",
                "color": "blue"
            },
            "selNIx5pwz44WnCu0": {
                "id": "selNIx5pwz44WnCu0",
                "name": "Dan Roberts",
                "color": "blue"
            },
            "selgEzZHKL9FFfqu0": {
                "id": "selgEzZHKL9FFfqu0",
                "name": "Sathvik Vishwanath",
                "color": "blue"
            },
            "selFLC2mX8iYmjpUa": {
                "id": "selFLC2mX8iYmjpUa",
                "name": "Tor Bair",
                "color": "blue"
            },
            "selwT5AREACt5SxFM": {
                "id": "selwT5AREACt5SxFM",
                "name": "Liem Thai",
                "color": "blue"
            },
            "seleIZoHQKaOshMl8": {
                "id": "seleIZoHQKaOshMl8",
                "name": "Darius Kozlovskis",
                "color": "blue"
            },
            "selQcr2WC8aZFIXdp": {
                "id": "selQcr2WC8aZFIXdp",
                "name": "Jack O'Holleran",
                "color": "cyanDark"
            },
            "selW4qeTP8RIf9Txv": {
                "id": "selW4qeTP8RIf9Txv",
                "name": "MacLane Wilkison",
                "color": "orangeDarker"
            },
            "selfAffI6Xzhqlrlk": {
                "id": "selfAffI6Xzhqlrlk",
                "name": "Justin Wu",
                "color": "cyanDarker"
            },
            "selPHCGTur8vP2CwY": {
                "id": "selPHCGTur8vP2CwY",
                "name": " Shahaf Bar-Geffen",
                "color": "redMedium"
            },
            "sely9sYlO9SMOG57f": {
                "id": "sely9sYlO9SMOG57f",
                "name": "Christopher Whinfrey",
                "color": "green"
            },
            "selj07JD43aoKKybD": {
                "id": "selj07JD43aoKKybD",
                "name": "Miguel Mota",
                "color": "pinkDark"
            },
            "selCsIZ1Klo2tyH5Z": {
                "id": "selCsIZ1Klo2tyH5Z",
                "name": " Eran Haggiag",
                "color": "purpleMedium"
            },
            "selbHBIHqMUnoUgMK": {
                "id": "selbHBIHqMUnoUgMK",
                "name": " Gal Hochberg",
                "color": "cyanDarker"
            },
            "selrqjmfnp3nwbEcR": {
                "id": "selrqjmfnp3nwbEcR",
                "name": "Jack Tao",
                "color": "tealDark"
            },
            "selbiVrMCapThhjjr": {
                "id": "selbiVrMCapThhjjr",
                "name": "Travis Schwab",
                "color": "blue"
            },
            "selG1h3GyatLOzFaV": {
                "id": "selG1h3GyatLOzFaV",
                "name": "Donnie Dinch",
                "color": "blueDark"
            },
            "selZOfHSRnsMyDPIA": {
                "id": "selZOfHSRnsMyDPIA",
                "name": "Julian Tescher",
                "color": "green"
            },
            "selkoGmiIEnYcTuZW": {
                "id": "selkoGmiIEnYcTuZW",
                "name": "Steve Jang",
                "color": "orangeDark"
            },
            "selNjmK7qwGFTinJD": {
                "id": "selNjmK7qwGFTinJD",
                "name": "Holger",
                "color": "blue"
            },
            "selGgfDe0Ebgf6p6x": {
                "id": "selGgfDe0Ebgf6p6x",
                "name": "Jeff Kramer",
                "color": "blue"
            },
            "selswjZpoTgch5Jud": {
                "id": "selswjZpoTgch5Jud",
                "name": "Adam White",
                "color": "greenDarker"
            },
            "selxf6rygdjGsATfX": {
                "id": "selxf6rygdjGsATfX",
                "name": "Derek Alia",
                "color": "blue"
            },
            "selDcseC8M77lUyuM": {
                "id": "selDcseC8M77lUyuM",
                "name": "Caitlin Long",
                "color": "blue"
            },
            "sela7VaYmjmqlLXY2": {
                "id": "sela7VaYmjmqlLXY2",
                "name": "Michael Phelps",
                "color": "blue"
            },
            "selGf2E8TFHycLAmk": {
                "id": "selGf2E8TFHycLAmk",
                "name": "Emmanuel Goh",
                "color": "blue"
            },
            "selDBBpUOXvCiRryD": {
                "id": "selDBBpUOXvCiRryD",
                "name": "Brian Cole",
                "color": "blue"
            },
            "seliFxuox5Gvl9NPj": {
                "id": "seliFxuox5Gvl9NPj",
                "name": "Christopher Brown",
                "color": "blue"
            },
            "selVAEUJ1FyUgcsVk": {
                "id": "selVAEUJ1FyUgcsVk",
                "name": "Nevin Freeman",
                "color": "tealMedium"
            },
            "selqipQYKhLO3JedR": {
                "id": "selqipQYKhLO3JedR",
                "name": "Thor Alexander",
                "color": "blue"
            },
            "sel4CjRaFDnphCeOM": {
                "id": "sel4CjRaFDnphCeOM",
                "name": "Peter Watts",
                "color": "blue"
            },
            "selOq7jkSWijBKmpH": {
                "id": "selOq7jkSWijBKmpH",
                "name": "Adi Sideman",
                "color": "blue"
            },
            "selexEaQNWcB0PceI": {
                "id": "selexEaQNWcB0PceI",
                "name": "Richard Craib",
                "color": "blue"
            },
            "selQrtix4uCvIC6Ui": {
                "id": "selQrtix4uCvIC6Ui",
                "name": "Daniel Vogel",
                "color": "blue"
            },
            "seleiynlsttTsFIyJ": {
                "id": "seleiynlsttTsFIyJ",
                "name": "Mike Van Rossum",
                "color": "purple"
            },
            "sel08HmM8Fx5Offz6": {
                "id": "sel08HmM8Fx5Offz6",
                "name": "Zubin Singh Koticha",
                "color": "greenMedium"
            },
            "selOsJunSqzOu5rJf": {
                "id": "selOsJunSqzOu5rJf",
                "name": "Sneha Kataria",
                "color": "blue"
            },
            "selXSwSpcN7YEHoU8": {
                "id": "selXSwSpcN7YEHoU8",
                "name": "Anubhav Sonthalia",
                "color": "blue"
            },
            "selm1QflZkFBVHEWR": {
                "id": "selm1QflZkFBVHEWR",
                "name": "Konstantin Lomashuk",
                "color": "blue"
            },
            "seljZK1LSWnyD6yXI": {
                "id": "seljZK1LSWnyD6yXI",
                "name": "Greg Osuri",
                "color": "blue"
            },
            "sel5PNpzY4wYsbFlD": {
                "id": "sel5PNpzY4wYsbFlD",
                "name": "Anthony Foy",
                "color": "blue"
            },
            "selcSDObWZPOzhv3y": {
                "id": "selcSDObWZPOzhv3y",
                "name": "Nik Storonsky",
                "color": "blue"
            },
            "selPRzEtsHFUe3SLH": {
                "id": "selPRzEtsHFUe3SLH",
                "name": "Merrick Okamoto",
                "color": "blue"
            },
            "selUlg7iW21KWX5qW": {
                "id": "selUlg7iW21KWX5qW",
                "name": "Aaron Henshaw",
                "color": "blue"
            },
            "selqujc2tDjBHosm0": {
                "id": "selqujc2tDjBHosm0",
                "name": " Joe Lallouz",
                "color": "tealMedium"
            },
            "selzQQvn80e4a1Qdw": {
                "id": "selzQQvn80e4a1Qdw",
                "name": "Yuesheng GE",
                "color": "blue"
            },
            "seligbKjF49glbOYs": {
                "id": "seligbKjF49glbOYs",
                "name": "Robert Leshner",
                "color": "blue"
            },
            "sel1TGfdix2kZqqbQ": {
                "id": "sel1TGfdix2kZqqbQ",
                "name": "Sali Christeson",
                "color": "blue"
            },
            "selqJbU9ohkiaWLlz": {
                "id": "selqJbU9ohkiaWLlz",
                "name": "Zahid Rahman",
                "color": "blue"
            },
            "sel1GCET6U9qBM1CV": {
                "id": "sel1GCET6U9qBM1CV",
                "name": "Matt Luongo",
                "color": "blue"
            },
            "selYDxXzftolBPDb1": {
                "id": "selYDxXzftolBPDb1",
                "name": "Allan Niemerg",
                "color": "blue"
            },
            "selhjeifXOpjmMxNv": {
                "id": "selhjeifXOpjmMxNv",
                "name": "Brian Brater",
                "color": "blue"
            },
            "selBObtXNtATh8rOY": {
                "id": "selBObtXNtATh8rOY",
                "name": "John Linden",
                "color": "blue"
            },
            "selNvZNaPAjOla802": {
                "id": "selNvZNaPAjOla802",
                "name": "Arnab Naskar",
                "color": "pinkMedium"
            },
            "seligUxKVEam8iUQQ": {
                "id": "seligUxKVEam8iUQQ",
                "name": "Alessio Quaglini",
                "color": "blue"
            },
            "selCNK2LIly2qXY2o": {
                "id": "selCNK2LIly2qXY2o",
                "name": "Murat F\u0131rat",
                "color": "blue"
            },
            "selHBQx8JS7zWyXwK": {
                "id": "selHBQx8JS7zWyXwK",
                "name": "Matt Hawkins",
                "color": "blue"
            },
            "seldig2qm3NSIhXVn": {
                "id": "seldig2qm3NSIhXVn",
                "name": "Jinglan Wang",
                "color": "blue"
            },
            "selOhwPcP8JjWzbiN": {
                "id": "selOhwPcP8JjWzbiN",
                "name": "Han Gao",
                "color": "blue"
            },
            "selWFZrUt4tsu7DgY": {
                "id": "selWFZrUt4tsu7DgY",
                "name": "Alfredo Terrero",
                "color": "blue"
            },
            "selH3MTuii6T3qCYH": {
                "id": "selH3MTuii6T3qCYH",
                "name": "Nicos Vekiarides",
                "color": "blue"
            },
            "selGfeIASsG3jiJtD": {
                "id": "selGfeIASsG3jiJtD",
                "name": "https://optimism.io/",
                "color": "blue"
            },
            "sel9hhncUmrq5VDiE": {
                "id": "sel9hhncUmrq5VDiE",
                "name": "Michael Feng",
                "color": "blue"
            },
            "selK5liv2Dl7DxGUP": {
                "id": "selK5liv2Dl7DxGUP",
                "name": "Alex Fedosseev",
                "color": "blue"
            },
            "selwMktlsQxqoCnyB": {
                "id": "selwMktlsQxqoCnyB",
                "name": "Michael P O'Rourke",
                "color": "blue"
            },
            "selPRPC1FvfJYnNkq": {
                "id": "selPRPC1FvfJYnNkq",
                "name": "Kevin March",
                "color": "blue"
            },
            "selcQmtkK25DXLGEb": {
                "id": "selcQmtkK25DXLGEb",
                "name": "Konstantin Richter",
                "color": "blue"
            },
            "selplvDr4FRefoJJj": {
                "id": "selplvDr4FRefoJJj",
                "name": "Matthew McClure",
                "color": "blue"
            },
            "selq1i9BSdaTkG01R": {
                "id": "selq1i9BSdaTkG01R",
                "name": "Rosario Ingargiola",
                "color": "blue"
            },
            "selCVKZV0bx8RMU5K": {
                "id": "selCVKZV0bx8RMU5K",
                "name": "Nick Emmons",
                "color": "blue"
            },
            "selAG8uyqDNXfjQZW": {
                "id": "selAG8uyqDNXfjQZW",
                "name": "Barry Silbert",
                "color": "blue"
            },
            "seluPwte59S2ReUBM": {
                "id": "seluPwte59S2ReUBM",
                "name": "Burnt Banksy",
                "color": "blue"
            },
            "sel432MCLBD85WQgS": {
                "id": "sel432MCLBD85WQgS",
                "name": "Edgar Moreau",
                "color": "blue"
            },
            "selTNgPRVDO3GP0Nb": {
                "id": "selTNgPRVDO3GP0Nb",
                "name": "Ramon Recuero",
                "color": "blue"
            },
            "selM2wnQJqzIYYa8k": {
                "id": "selM2wnQJqzIYYa8k",
                "name": "Nirbhik Jangid",
                "color": "blue"
            },
            "selIVktwf9Ma8FXrc": {
                "id": "selIVktwf9Ma8FXrc",
                "name": "Lucas Vogelsang",
                "color": "blue"
            },
            "selojI2s0uWU0O1D4": {
                "id": "selojI2s0uWU0O1D4",
                "name": "Bin Zhu",
                "color": "yellow"
            },
            "seliJLGemMp6Pz4G9": {
                "id": "seliJLGemMp6Pz4G9",
                "name": "Sam Williams",
                "color": "blue"
            },
            "sel3WXVRckV43QgO8": {
                "id": "sel3WXVRckV43QgO8",
                "name": "Mike Cagney",
                "color": "blue"
            },
            "selsx6bL7JM3VKwSs": {
                "id": "selsx6bL7JM3VKwSs",
                "name": "Benoit Pagotto",
                "color": "blue"
            },
            "selk5c1CklAhTxWGC": {
                "id": "selk5c1CklAhTxWGC",
                "name": "Ryan Chow",
                "color": "tealMedium"
            },
            "sel363ycns1Mtasw2": {
                "id": "sel363ycns1Mtasw2",
                "name": "Reda Berrehili",
                "color": "blue"
            },
            "selPxDe39xiWtjLTc": {
                "id": "selPxDe39xiWtjLTc",
                "name": "Vikram Anand Bhushan",
                "color": "blue"
            },
            "selmZr5TjdZgQPCYF": {
                "id": "selmZr5TjdZgQPCYF",
                "name": "Frank Wilder",
                "color": "pink"
            },
            "selyRpAO3zq4heUYQ": {
                "id": "selyRpAO3zq4heUYQ",
                "name": "Jonathan DeCarteret",
                "color": "redMedium"
            },
            "selmK37E0Phu20mOJ": {
                "id": "selmK37E0Phu20mOJ",
                "name": "Pedro Rente Louren\u00e7o",
                "color": "blue"
            },
            "selFhURbci9gnDPSg": {
                "id": "selFhURbci9gnDPSg",
                "name": "Dave Balter",
                "color": "orangeDark"
            },
            "selw6SL6FLbsNejx7": {
                "id": "selw6SL6FLbsNejx7",
                "name": "David Ratiney",
                "color": "blue"
            },
            "selxSnK0JZhI7OtxO": {
                "id": "selxSnK0JZhI7OtxO",
                "name": "Chris Trew",
                "color": "blue"
            },
            "sel40NzDFAjX5TDHF": {
                "id": "sel40NzDFAjX5TDHF",
                "name": " Tate Berenbaum",
                "color": "blueDark"
            },
            "selRExsRtpXgSh7en": {
                "id": "selRExsRtpXgSh7en",
                "name": "Eric Satz",
                "color": "blue"
            },
            "selFAG0FwzjKA0sar": {
                "id": "selFAG0FwzjKA0sar",
                "name": "Echul Shin",
                "color": "orangeDark"
            },
            "selDfvn4QKjNyMe8X": {
                "id": "selDfvn4QKjNyMe8X",
                "name": "Leemon Baird",
                "color": "blue"
            },
            "selwXQKlgCFTkIKO9": {
                "id": "selwXQKlgCFTkIKO9",
                "name": "Mance Harmon",
                "color": "cyan"
            },
            "selZUrYVvR2qnCTOl": {
                "id": "selZUrYVvR2qnCTOl",
                "name": "Zenobia Godschalk",
                "color": "teal"
            },
            "selEDqRV9EYK6hZ0x": {
                "id": "selEDqRV9EYK6hZ0x",
                "name": "Felix Feng",
                "color": "yellowDark"
            },
            "selH9IjrJxjaW7pF6": {
                "id": "selH9IjrJxjaW7pF6",
                "name": "Siong Ong",
                "color": "blue"
            },
            "selFiY5jRNQdlUyDU": {
                "id": "selFiY5jRNQdlUyDU",
                "name": "Alexis Sellier",
                "color": "teal"
            },
            "sellOXbIcESJ70szG": {
                "id": "sellOXbIcESJ70szG",
                "name": "Eleftherios Diakomichalis",
                "color": "yellowDarker"
            },
            "selaWzf2ZHTEHRsSI": {
                "id": "selaWzf2ZHTEHRsSI",
                "name": "Nick Neuman",
                "color": "red"
            },
            "selzBhdwehIFZT4yM": {
                "id": "selzBhdwehIFZT4yM",
                "name": "Shumo Chu",
                "color": "blue"
            },
            "selq9mc4iTwVN8R0H": {
                "id": "selq9mc4iTwVN8R0H",
                "name": "Erwin Werring",
                "color": "blue"
            },
            "selN838OPRj5DL8UD": {
                "id": "selN838OPRj5DL8UD",
                "name": "Danh Vo",
                "color": "blue"
            },
            "sel75t6OpUEz1a9iT": {
                "id": "sel75t6OpUEz1a9iT",
                "name": "Sumit Gupta",
                "color": "cyanMedium"
            },
            "selmCZ62Nt4SxBfHp": {
                "id": "selmCZ62Nt4SxBfHp",
                "name": "J. Ayo Akinyele",
                "color": "blue"
            },
            "sel2hnXV6mbrfgXuE": {
                "id": "sel2hnXV6mbrfgXuE",
                "name": "Alex Fowler",
                "color": "cyanMedium"
            },
            "selpdAetPp203Q8wp": {
                "id": "selpdAetPp203Q8wp",
                "name": "Dmitry Tokarev",
                "color": "blue"
            },
            "seldJYM3u36OfuZ8o": {
                "id": "seldJYM3u36OfuZ8o",
                "name": "Daniel Haudenschild",
                "color": "blue"
            },
            "selz7rSOk5tlwihuY": {
                "id": "selz7rSOk5tlwihuY",
                "name": "Peter Hunn",
                "color": "blue"
            },
            "selMA92DasMn9YKmC": {
                "id": "selMA92DasMn9YKmC",
                "name": "Krzysztof Gagacki",
                "color": "blue"
            },
            "selHjm9EVquJmqq94": {
                "id": "selHjm9EVquJmqq94",
                "name": "Ah Go",
                "color": "blue"
            },
            "selsU4upibaXjUr9g": {
                "id": "selsU4upibaXjUr9g",
                "name": "Alwin Chang",
                "color": "cyan"
            },
            "selA1FlgTuj3R6PA1": {
                "id": "selA1FlgTuj3R6PA1",
                "name": "Jayson Tan",
                "color": "teal"
            },
            "selWZh7AThYkDdXmo": {
                "id": "selWZh7AThYkDdXmo",
                "name": "Evgeny Yurtaev",
                "color": "blue"
            },
            "selw7rVldija89dlx": {
                "id": "selw7rVldija89dlx",
                "name": "Ouriel Ohayon",
                "color": "blue"
            },
            "selEYMazIJaJwPFdw": {
                "id": "selEYMazIJaJwPFdw",
                "name": "Alexey Koloskov",
                "color": "pinkDarker"
            },
            "seldkpIym8eUvZIAC": {
                "id": "seldkpIym8eUvZIAC",
                "name": "Ari Meilich",
                "color": "blue"
            },
            "selg5lN10ql2u00wl": {
                "id": "selg5lN10ql2u00wl",
                "name": "Ray Lu",
                "color": "grayDark"
            },
            "selo3yTRVbreqjVEp": {
                "id": "selo3yTRVbreqjVEp",
                "name": "WB",
                "color": "blue"
            },
            "selGiEVKKt4L1aSM1": {
                "id": "selGiEVKKt4L1aSM1",
                "name": "Alex Berstein",
                "color": "pinkMedium"
            },
            "seltEpdoe96CdNN8j": {
                "id": "seltEpdoe96CdNN8j",
                "name": "Nikita Ngan Nguyen",
                "color": "orangeMedium"
            },
            "selL82IN0NQKGWo4V": {
                "id": "selL82IN0NQKGWo4V",
                "name": "J.Bach",
                "color": "yellow"
            },
            "selliaY7jmgyRq1er": {
                "id": "selliaY7jmgyRq1er",
                "name": "Rayane Hocine",
                "color": "tealMedium"
            },
            "selbcNf2eZUPAfIMw": {
                "id": "selbcNf2eZUPAfIMw",
                "name": "Harrison Noh",
                "color": "blue"
            },
            "selHQ6IVw1N1crFhF": {
                "id": "selHQ6IVw1N1crFhF",
                "name": "Jacobo Toll-Messia",
                "color": "purple"
            },
            "selfnQpNvbtwAKGnV": {
                "id": "selfnQpNvbtwAKGnV",
                "name": "Logino Dujardin",
                "color": "purpleMedium"
            },
            "selwaFSI0HlswaZw1": {
                "id": "selwaFSI0HlswaZw1",
                "name": "Chlo\u00e9 Bigot",
                "color": "blue"
            },
            "selMNMxGRIYKUZpzD": {
                "id": "selMNMxGRIYKUZpzD",
                "name": "James Carney",
                "color": "cyanDarker"
            },
            "selbwXhJlei9Q1tfV": {
                "id": "selbwXhJlei9Q1tfV",
                "name": "Daniel Delouya",
                "color": "blue"
            },
            "selynHJ7zWWIp2Lay": {
                "id": "selynHJ7zWWIp2Lay",
                "name": "Peter Mitchell",
                "color": "yellowMedium"
            },
            "selOKK0ENt6LUIAGn": {
                "id": "selOKK0ENt6LUIAGn",
                "name": "Jasper De Gooijer",
                "color": "greenDarker"
            },
            "selOzbtz0Z1YNU6wv": {
                "id": "selOzbtz0Z1YNU6wv",
                "name": "Ralf Gerteis",
                "color": "cyanMedium"
            },
            "selvZZ50P18O94G1x": {
                "id": "selvZZ50P18O94G1x",
                "name": "Dillon Chen",
                "color": "blue"
            },
            "selmOAqZe9eQcFwCS": {
                "id": "selmOAqZe9eQcFwCS",
                "name": "Drew Stone",
                "color": "orangeMedium"
            },
            "selnU6jwwB104o50i": {
                "id": "selnU6jwwB104o50i",
                "name": "Raymond Zhong",
                "color": "cyanDark"
            },
            "selkvHu8A3zWScHmx": {
                "id": "selkvHu8A3zWScHmx",
                "name": " Drew Stone",
                "color": "greenDark"
            },
            "selVQPjepB6yECSCb": {
                "id": "selVQPjepB6yECSCb",
                "name": "James Wilcox",
                "color": "redMedium"
            },
            "sel3pn3Io9ntKmZDv": {
                "id": "sel3pn3Io9ntKmZDv",
                "name": "Hsuan Lee",
                "color": "yellowMedium"
            },
            "selOG4rHMjEbHvix3": {
                "id": "selOG4rHMjEbHvix3",
                "name": "Josh Williams",
                "color": "pink"
            },
            "selEMu4rfLMJII1me": {
                "id": "selEMu4rfLMJII1me",
                "name": "Brett Seyler",
                "color": "blue"
            },
            "selV6tzyqaiDhbON0": {
                "id": "selV6tzyqaiDhbON0",
                "name": "Kent Wakeford",
                "color": "cyan"
            },
            "selYpy6qYrmVcKKyY": {
                "id": "selYpy6qYrmVcKKyY",
                "name": "Kevin Chou",
                "color": "teal"
            },
            "selU0PkFMFk5jlQ0I": {
                "id": "selU0PkFMFk5jlQ0I",
                "name": "Mahesh Vellanki",
                "color": "green"
            },
            "selT09UvtzLvw006q": {
                "id": "selT09UvtzLvw006q",
                "name": "Alex Wang",
                "color": "blue"
            },
            "selaLfQafAr0WXj06": {
                "id": "selaLfQafAr0WXj06",
                "name": "Mahadev Vasireddy",
                "color": "greenDarker"
            },
            "selNmDxeAB1WMUQul": {
                "id": "selNmDxeAB1WMUQul",
                "name": "Hisham Khan",
                "color": "teal"
            },
            "selMZSNM0dHPDwkGR": {
                "id": "selMZSNM0dHPDwkGR",
                "name": "Liu Jie",
                "color": "yellow"
            },
            "selF0Na58fGDXXocw": {
                "id": "selF0Na58fGDXXocw",
                "name": "Serge Levin",
                "color": "blueMedium"
            },
            "sel00yImqxe0vAs7P": {
                "id": "sel00yImqxe0vAs7P",
                "name": "Dmitry Shklovsky",
                "color": "pink"
            },
            "seliFZt3ifhr1UsnC": {
                "id": "seliFZt3ifhr1UsnC",
                "name": "Lin Dai ",
                "color": "orangeDarker"
            },
            "selSzW9yxQ8nibpi8": {
                "id": "selSzW9yxQ8nibpi8",
                "name": "Mattias Tyrberg",
                "color": "greenDark"
            },
            "selA3LX5h52dA7D7A": {
                "id": "selA3LX5h52dA7D7A",
                "name": "Leighton Cusack",
                "color": "blue"
            },
            "sel8lrQdvFNNtP6EQ": {
                "id": "sel8lrQdvFNNtP6EQ",
                "name": "Jeth Soetoyo",
                "color": "purpleDark"
            },
            "selXZX0yZmg2lMrRH": {
                "id": "selXZX0yZmg2lMrRH",
                "name": "Matt Luczynski",
                "color": "orangeMedium"
            },
            "selt1E0sVGa8PSqEv": {
                "id": "selt1E0sVGa8PSqEv",
                "name": "Bryson Warsap",
                "color": "cyan"
            },
            "selwrQYfuXhj5xEPW": {
                "id": "selwrQYfuXhj5xEPW",
                "name": "Flavian Manea",
                "color": "cyan"
            },
            "selHTv8eEn9fw4OGw": {
                "id": "selHTv8eEn9fw4OGw",
                "name": "Komy",
                "color": "orange"
            },
            "sela7QKo4jphXTkmX": {
                "id": "sela7QKo4jphXTkmX",
                "name": "Bram Cohen",
                "color": "blue"
            },
            "sel1PNlsoqRAbV5Nl": {
                "id": "sel1PNlsoqRAbV5Nl",
                "name": " Asaf Meir",
                "color": "blueDark"
            },
            "selct2VQWdErwo1Sc": {
                "id": "selct2VQWdErwo1Sc",
                "name": "Dave Hendricks",
                "color": "orangeDarker"
            },
            "selGHTtgETpYpJLMV": {
                "id": "selGHTtgETpYpJLMV",
                "name": "Vygandas Masilionis",
                "color": "blue"
            },
            "sel3KT00W5dEwuhht": {
                "id": "sel3KT00W5dEwuhht",
                "name": "Stuart Thom ",
                "color": "orange"
            },
            "selpuxzg4xFn36DEy": {
                "id": "selpuxzg4xFn36DEy",
                "name": "Tejas Chitnis",
                "color": "orange"
            },
            "selEWSRfDeTStkVuW": {
                "id": "selEWSRfDeTStkVuW",
                "name": "Alex Borutskiy",
                "color": "gray"
            },
            "sel9EiWJYoCauaIIl": {
                "id": "sel9EiWJYoCauaIIl",
                "name": "Enrico Rubboli ",
                "color": "orangeMedium"
            },
            "selS8oy8vFO0cqM83": {
                "id": "selS8oy8vFO0cqM83",
                "name": "Anton Katz",
                "color": "blue"
            },
            "selaVkkm0734JYRfj": {
                "id": "selaVkkm0734JYRfj",
                "name": "Christian Hentschel",
                "color": "blue"
            },
            "sellszlVCnH7cYOzA": {
                "id": "sellszlVCnH7cYOzA",
                "name": "Jun Ming Yong",
                "color": "blue"
            },
            "selUeDLlp7xBBzX78": {
                "id": "selUeDLlp7xBBzX78",
                "name": "Greg Schvey",
                "color": "blue"
            },
            "sel4cegudZvwrNBPF": {
                "id": "sel4cegudZvwrNBPF",
                "name": "Jeff Schvey",
                "color": "cyan"
            },
            "selOqGnKYAUGT4L1G": {
                "id": "selOqGnKYAUGT4L1G",
                "name": "AJ Smith",
                "color": "yellowDark"
            },
            "selpvIvudn4nu4Vuk": {
                "id": "selpvIvudn4nu4Vuk",
                "name": "Joel Neidig",
                "color": "grayDarker"
            },
            "sel9pSDYWYlS1hWll": {
                "id": "sel9pSDYWYlS1hWll",
                "name": "David Lighton",
                "color": "yellowDarker"
            },
            "selLVVkoNtxxa6krh": {
                "id": "selLVVkoNtxxa6krh",
                "name": "Cosmin Grigore",
                "color": "redDark"
            },
            "selEH3fy6pacbNjIy": {
                "id": "selEH3fy6pacbNjIy",
                "name": "Oliver Gale",
                "color": "pink"
            },
            "selpXbRsNl44GH8Va": {
                "id": "selpXbRsNl44GH8Va",
                "name": "Adam ",
                "color": "yellowMedium"
            },
            "sel127vxSLGAmV3Or": {
                "id": "sel127vxSLGAmV3Or",
                "name": "Marc-Antoine Ross",
                "color": "purple"
            },
            "selJ4hq6vuxKZaK8o": {
                "id": "selJ4hq6vuxKZaK8o",
                "name": "Stas Oskin",
                "color": "blue"
            },
            "selB6jDaX3Nu71dwr": {
                "id": "selB6jDaX3Nu71dwr",
                "name": "Robbie Heeger",
                "color": "blue"
            },
            "selaiOeZlI8UL4Wr0": {
                "id": "selaiOeZlI8UL4Wr0",
                "name": "Flex Yang",
                "color": "blue"
            },
            "selto7wl10eqsAHmy": {
                "id": "selto7wl10eqsAHmy",
                "name": "Eyal Eithcowich",
                "color": "tealDarker"
            },
            "sel0v4ipLlNjvc132": {
                "id": "sel0v4ipLlNjvc132",
                "name": "Peter Danihel",
                "color": "blue"
            },
            "selFK01n06YUa6Ycf": {
                "id": "selFK01n06YUa6Ycf",
                "name": "Jack Sanford",
                "color": "pinkDarker"
            },
            "selSDj4Qc9cOQg8VX": {
                "id": "selSDj4Qc9cOQg8VX",
                "name": "Evert Kors",
                "color": "blueDarker"
            },
            "selEAnu77858ebPNN": {
                "id": "selEAnu77858ebPNN",
                "name": "Vladimir Nikitin",
                "color": "gray"
            },
            "seltxaAYoE1iIWm1v": {
                "id": "seltxaAYoE1iIWm1v",
                "name": "Norbert Bodziony",
                "color": "purpleDark"
            },
            "sel7UGjUh4XFMsL20": {
                "id": "sel7UGjUh4XFMsL20",
                "name": "Piyush Gupta",
                "color": "orange"
            },
            "sel0cz6tObhrPj2z3": {
                "id": "sel0cz6tObhrPj2z3",
                "name": "Joris Huijbregts",
                "color": "blue"
            },
            "selTuU3ILmYe7FfCs": {
                "id": "selTuU3ILmYe7FfCs",
                "name": "Mark Laursen",
                "color": "cyan"
            },
            "sellmsDRIaeta6HvB": {
                "id": "sellmsDRIaeta6HvB",
                "name": "Sage Durain",
                "color": "teal"
            },
            "seloMsNvOI7RvAbyY": {
                "id": "seloMsNvOI7RvAbyY",
                "name": "Sune Thorsen",
                "color": "green"
            },
            "sel1mSV9hDvPIcFjm": {
                "id": "sel1mSV9hDvPIcFjm",
                "name": "Kerman Kohli",
                "color": "blue"
            },
            "selLj6WlojXhsyDQn": {
                "id": "selLj6WlojXhsyDQn",
                "name": "Dave Jevans",
                "color": "blue"
            },
            "selBr0g8o36K1xvJM": {
                "id": "selBr0g8o36K1xvJM",
                "name": "Shannon Holland",
                "color": "cyan"
            },
            "seltppseYPTl6H3yd": {
                "id": "seltppseYPTl6H3yd",
                "name": "Stephen Ryan",
                "color": "teal"
            },
            "selo20vGx4etuGljx": {
                "id": "selo20vGx4etuGljx",
                "name": "Alexander Morris",
                "color": "blue"
            },
            "selPOHWOUT2vfjhFt": {
                "id": "selPOHWOUT2vfjhFt",
                "name": "Joseph Kelly",
                "color": "blue"
            },
            "selbcW3XFZPgnMuH0": {
                "id": "selbcW3XFZPgnMuH0",
                "name": "Gregory Landua",
                "color": "blue"
            },
            "selqNJVJPMyiv9lpB": {
                "id": "selqNJVJPMyiv9lpB",
                "name": "Todor Kolev",
                "color": "blueMedium"
            },
            "sel9tBuRf7Vef0maX": {
                "id": "sel9tBuRf7Vef0maX",
                "name": "Alexander Leishman",
                "color": "blue"
            },
            "selYzk7owQRA1jdO7": {
                "id": "selYzk7owQRA1jdO7",
                "name": "Andrew Benson",
                "color": "cyan"
            },
            "sell4r4BtOE2s5z7N": {
                "id": "sell4r4BtOE2s5z7N",
                "name": "Michael Smyers",
                "color": "blue"
            },
            "sel1Gs24iOAFl9M85": {
                "id": "sel1Gs24iOAFl9M85",
                "name": "Neil Bergquist",
                "color": "cyan"
            },
            "selfTXqbp1vPH1RvB": {
                "id": "selfTXqbp1vPH1RvB",
                "name": "Mindao Yang",
                "color": "blue"
            },
            "selzedJ4DyBaV76FL": {
                "id": "selzedJ4DyBaV76FL",
                "name": "Maggie Love",
                "color": "blue"
            },
            "selfjhYQq5E7cASJW": {
                "id": "selfjhYQq5E7cASJW",
                "name": "Sami Issa",
                "color": "blue"
            },
            "sel0hF8VzZKBxLBlP": {
                "id": "sel0hF8VzZKBxLBlP",
                "name": "Wael Aburida",
                "color": "orangeDark"
            },
            "selCHzRW44cFL8H8i": {
                "id": "selCHzRW44cFL8H8i",
                "name": "Cory Klippsten",
                "color": "blue"
            },
            "seliw7LECA9syOgWi": {
                "id": "seliw7LECA9syOgWi",
                "name": "Yan Pritzker",
                "color": "cyan"
            },
            "selnC4gKKEWMfMebP": {
                "id": "selnC4gKKEWMfMebP",
                "name": "Frida Cai",
                "color": "redDark"
            },
            "seliPJbhdsoXtPEUH": {
                "id": "seliPJbhdsoXtPEUH",
                "name": "Aristotle Andrulakis",
                "color": "blue"
            },
            "selzCuPMRAsdfxz14": {
                "id": "selzCuPMRAsdfxz14",
                "name": "Ben Cooper",
                "color": "cyan"
            },
            "selTdYuEkr22tjSJA": {
                "id": "selTdYuEkr22tjSJA",
                "name": "Brian Mahoney",
                "color": "teal"
            },
            "selzzT6GQBG0dDJHQ": {
                "id": "selzzT6GQBG0dDJHQ",
                "name": "Ryan Breen",
                "color": "green"
            },
            "selnZbfRaczPoHPyI": {
                "id": "selnZbfRaczPoHPyI",
                "name": "Ritam Gupta",
                "color": "blue"
            },
            "selRRTfqUNyWsqNeD": {
                "id": "selRRTfqUNyWsqNeD",
                "name": "Moiz Kohari",
                "color": "blue"
            },
            "selMQPRLFRFpDEmMA": {
                "id": "selMQPRLFRFpDEmMA",
                "name": "Hendrik Hey",
                "color": "yellowDark"
            },
            "selUzvrf6fUZtjuzM": {
                "id": "selUzvrf6fUZtjuzM",
                "name": "Dan Gunsberg",
                "color": "grayDark"
            },
            "seldFjeZZcbT6s0fx": {
                "id": "seldFjeZZcbT6s0fx",
                "name": "Arya Soltanieh",
                "color": "blue"
            },
            "selRsJpOERUVQENG0": {
                "id": "selRsJpOERUVQENG0",
                "name": "Mark Beylin  ",
                "color": "redMedium"
            },
            "selQO5OeJXvSsW8W7": {
                "id": "selQO5OeJXvSsW8W7",
                "name": "Neil Zumwalde",
                "color": "tealDarker"
            },
            "selhh4ooKZHNVFrpY": {
                "id": "selhh4ooKZHNVFrpY",
                "name": "Momin Ahmad",
                "color": "yellow"
            },
            "selUuBMl8lOhY02Sx": {
                "id": "selUuBMl8lOhY02Sx",
                "name": "Paul Murphy",
                "color": "yellow"
            },
            "selnE7SjzwOUknyhy": {
                "id": "selnE7SjzwOUknyhy",
                "name": "James Roy Poulter",
                "color": "cyanDarker"
            },
            "selb5HU1aQsT8HZrD": {
                "id": "selb5HU1aQsT8HZrD",
                "name": "Zhanna Sharipova",
                "color": "blue"
            },
            "selVj5kdrJabXUlap": {
                "id": "selVj5kdrJabXUlap",
                "name": "Hugo Philion",
                "color": "blue"
            },
            "selSsfEryq95j3ps3": {
                "id": "selSsfEryq95j3ps3",
                "name": "Yifan He",
                "color": "pink"
            },
            "selH8dJg4SNw9v0Z0": {
                "id": "selH8dJg4SNw9v0Z0",
                "name": "Bonna Zhu",
                "color": "blue"
            },
            "selVXDjSfngAOfuV6": {
                "id": "selVXDjSfngAOfuV6",
                "name": "Pascal Gauthier",
                "color": "gray"
            },
            "sel2kFaWzHEtNzsn7": {
                "id": "sel2kFaWzHEtNzsn7",
                "name": "Eric Larchev\u00eaque",
                "color": "green"
            },
            "selQLPD5AAa1ypNht": {
                "id": "selQLPD5AAa1ypNht",
                "name": "Bruno \u0160kvorc",
                "color": "blue"
            },
            "sela88BcMouZ7seds": {
                "id": "sela88BcMouZ7seds",
                "name": "Jonathan M. Padilla",
                "color": "blue"
            },
            "selg4asewqJV6rPHN": {
                "id": "selg4asewqJV6rPHN",
                "name": "James Ryan Moreau",
                "color": "blue"
            },
            "selng6q5Kt5iStL1N": {
                "id": "selng6q5Kt5iStL1N",
                "name": "Nick Hansen",
                "color": "yellow"
            },
            "selAJugQjINO6slBj": {
                "id": "selAJugQjINO6slBj",
                "name": "Hugh Madden",
                "color": "cyanDarker"
            },
            "sel15tYfoKSabVRWz": {
                "id": "sel15tYfoKSabVRWz",
                "name": "Sowmay Jain",
                "color": "orangeDarker"
            },
            "selTnH7QsSyjSVkhF": {
                "id": "selTnH7QsSyjSVkhF",
                "name": "Douglas Johnson-Poensgen",
                "color": "grayDarker"
            },
            "selfHBVf5qpzjDsc3": {
                "id": "selfHBVf5qpzjDsc3",
                "name": "Tony Cai",
                "color": "blue"
            },
            "selXme7QDvGKRxAfV": {
                "id": "selXme7QDvGKRxAfV",
                "name": "Rudy Koch",
                "color": "purpleDark"
            },
            "sel4pn46vh2NyHTL0": {
                "id": "sel4pn46vh2NyHTL0",
                "name": "Szymon Sypniewicz",
                "color": "purple"
            },
            "selGbaFPPyl8GXBT5": {
                "id": "selGbaFPPyl8GXBT5",
                "name": "Alan ma",
                "color": "blue"
            },
            "selWpH8rS93pQeltx": {
                "id": "selWpH8rS93pQeltx",
                "name": "Leon Liu",
                "color": "cyan"
            },
            "selrgBNMcBdNHDBhw": {
                "id": "selrgBNMcBdNHDBhw",
                "name": "Zach Herbert",
                "color": "blue"
            },
            "selnAbsj5JzKXPRqv": {
                "id": "selnAbsj5JzKXPRqv",
                "name": "Jim Jin",
                "color": "blue"
            },
            "selEzTq74V1g4qc2E": {
                "id": "selEzTq74V1g4qc2E",
                "name": "Tim Glover",
                "color": "cyan"
            },
            "selY9EwfJ3rrKAVoM": {
                "id": "selY9EwfJ3rrKAVoM",
                "name": "Srikanth Srinivas",
                "color": "blue"
            },
            "selpmA7ooaUR4Vjip": {
                "id": "selpmA7ooaUR4Vjip",
                "name": "Andy Alekhin",
                "color": "blue"
            },
            "selZCNHKP4UZuUoAr": {
                "id": "selZCNHKP4UZuUoAr",
                "name": "Misha Libman",
                "color": "cyan"
            },
            "selEZUzF1OpRFmUz5": {
                "id": "selEZUzF1OpRFmUz5",
                "name": "Erich Wood",
                "color": "blue"
            },
            "selgbLVRlgxee9ilP": {
                "id": "selgbLVRlgxee9ilP",
                "name": "Peter Wood",
                "color": "blue"
            },
            "selN8ZSUetp8f1GlC": {
                "id": "selN8ZSUetp8f1GlC",
                "name": "Shawn Yu",
                "color": "blue"
            },
            "selesKo1for3V9ZHU": {
                "id": "selesKo1for3V9ZHU",
                "name": "Julio Faura",
                "color": "red"
            },
            "seliBzjTW5JFhzqXW": {
                "id": "seliBzjTW5JFhzqXW",
                "name": "Edward Budd",
                "color": "pinkDarker"
            },
            "sel7ZEmrkqVBf55BF": {
                "id": "sel7ZEmrkqVBf55BF",
                "name": "Peter Munnings",
                "color": "pinkDarker"
            },
            "selUTyzjbqkC4xdmq": {
                "id": "selUTyzjbqkC4xdmq",
                "name": "Louis Buys",
                "color": "blue"
            },
            "selHR0EJ4xkonNmMx": {
                "id": "selHR0EJ4xkonNmMx",
                "name": "Sean Andrew Sanders",
                "color": "cyan"
            },
            "sel8W8MRDZASoQJah": {
                "id": "sel8W8MRDZASoQJah",
                "name": "Daniel Tang",
                "color": "blue"
            },
            "seln4TgF0OVfw3qTn": {
                "id": "seln4TgF0OVfw3qTn",
                "name": "Terry Lam",
                "color": "cyan"
            },
            "sel3MgMTRosQaWx46": {
                "id": "sel3MgMTRosQaWx46",
                "name": "Julia P\u00f6nitzsch",
                "color": "blue"
            },
            "selcz9gsg8MiwJH3E": {
                "id": "selcz9gsg8MiwJH3E",
                "name": "Leonard Dorl\u00f6chter",
                "color": "cyan"
            },
            "selfchgKn3szat8uf": {
                "id": "selfchgKn3szat8uf",
                "name": "Max Thake",
                "color": "teal"
            },
            "seluDcbd8O4wwx4NB": {
                "id": "seluDcbd8O4wwx4NB",
                "name": "Pavel Fomenko",
                "color": "green"
            },
            "selqgNEQh7TdzVebM": {
                "id": "selqgNEQh7TdzVebM",
                "name": "Till Wendler",
                "color": "yellow"
            },
            "sel8Zcy3yd1nC9VDg": {
                "id": "sel8Zcy3yd1nC9VDg",
                "name": "Brent Xu",
                "color": "blue"
            },
            "selsapDiSSQ2jKkcZ": {
                "id": "selsapDiSSQ2jKkcZ",
                "name": "Tom Tirman",
                "color": "blue"
            },
            "selQuSDMoVpqL4ub4": {
                "id": "selQuSDMoVpqL4ub4",
                "name": "Hunter Horsley",
                "color": "blue"
            },
            "selvj62ktGA0infel": {
                "id": "selvj62ktGA0infel",
                "name": "Elad Gil",
                "color": "blue"
            },
            "selF1Agod2TW8KTzT": {
                "id": "selF1Agod2TW8KTzT",
                "name": "Hong Kim",
                "color": "cyan"
            },
            "selSs5ffqiLFkNsWT": {
                "id": "selSs5ffqiLFkNsWT",
                "name": "Jeremy Born",
                "color": "grayDark"
            },
            "sel4YgB1Mv2VJguXh": {
                "id": "sel4YgB1Mv2VJguXh",
                "name": "Yubo Ruan",
                "color": "yellowDark"
            },
            "sel9ALgg4voTiLmcO": {
                "id": "sel9ALgg4voTiLmcO",
                "name": "Mike Sall",
                "color": "blue"
            },
            "selDi6qsI7pQv6j97": {
                "id": "selDi6qsI7pQv6j97",
                "name": "Esteban Casta\u00f1o",
                "color": "blue"
            },
            "selEBikeQQWGGayVj": {
                "id": "selEBikeQQWGGayVj",
                "name": "Lokesh Rao",
                "color": "blue"
            },
            "selZBx6TX3fTzCsKx": {
                "id": "selZBx6TX3fTzCsKx",
                "name": "Sunil Arora",
                "color": "cyan"
            },
            "selJygfskGOxY2JkQ": {
                "id": "selJygfskGOxY2JkQ",
                "name": "Jaeyong An",
                "color": "blue"
            },
            "selEeGhQErnwpr7BD": {
                "id": "selEeGhQErnwpr7BD",
                "name": "Alain Brenzikofer",
                "color": "greenDarker"
            },
            "selXoHWIYMtwVWux2": {
                "id": "selXoHWIYMtwVWux2",
                "name": "Waldemar Scherer",
                "color": "purpleDark"
            },
            "seltdGXiC65xRYii6": {
                "id": "seltdGXiC65xRYii6",
                "name": "Yichen Wu",
                "color": "blue"
            },
            "selhsxDyEwd3FqgOH": {
                "id": "selhsxDyEwd3FqgOH",
                "name": "Tarun Jaswani",
                "color": "blue"
            },
            "selUfvxeG039OLGi6": {
                "id": "selUfvxeG039OLGi6",
                "name": "Julius Serenas",
                "color": "blue"
            },
            "selSgursu5lbt9tPc": {
                "id": "selSgursu5lbt9tPc",
                "name": "Sylvia Savi",
                "color": "redMedium"
            },
            "selyu8ykkNGxf9lwm": {
                "id": "selyu8ykkNGxf9lwm",
                "name": "Arthur Britto",
                "color": "blue"
            },
            "selWva3rU9yhsKeJl": {
                "id": "selWva3rU9yhsKeJl",
                "name": "David Schwartz",
                "color": "cyan"
            },
            "selCFaxpuvPMmZJ1r": {
                "id": "selCFaxpuvPMmZJ1r",
                "name": "Jack Mallers",
                "color": "blue"
            },
            "self1bnu4KUkeQkon": {
                "id": "self1bnu4KUkeQkon",
                "name": "Alexander Filatov",
                "color": "blue"
            },
            "seltoflCOatCcOAqw": {
                "id": "seltoflCOatCcOAqw",
                "name": "Adrian Garelik",
                "color": "blue"
            },
            "sel9F1izlzVtiyyba": {
                "id": "sel9F1izlzVtiyyba",
                "name": "Adri\u00e1n Eidelman",
                "color": "cyan"
            },
            "selP7N4YIecMqZmVw": {
                "id": "selP7N4YIecMqZmVw",
                "name": "Diego Guti\u00e9rrez Zald\u00edvar",
                "color": "teal"
            },
            "selCHBpD0F0GazbbV": {
                "id": "selCHBpD0F0GazbbV",
                "name": "Ruben Altman",
                "color": "green"
            },
            "selFURAqtSWJAynUn": {
                "id": "selFURAqtSWJAynUn",
                "name": "Sergio Demi\u00e1n Lerner",
                "color": "yellow"
            },
            "sel0mIUjlNOhMga4w": {
                "id": "sel0mIUjlNOhMga4w",
                "name": "Arthur Vayloyan",
                "color": "blue"
            },
            "selAt2iijhNS3jHgj": {
                "id": "selAt2iijhNS3jHgj",
                "name": "Niklas Nikolajsen",
                "color": "cyan"
            },
            "sely23IvSEL8y4POA": {
                "id": "sely23IvSEL8y4POA",
                "name": "Carlos Domingo",
                "color": "blue"
            },
            "sel1cLbWiAuzd12jy": {
                "id": "sel1cLbWiAuzd12jy",
                "name": "Jamie H. Finn",
                "color": "cyan"
            },
            "selvwlwLBlljmUfLK": {
                "id": "selvwlwLBlljmUfLK",
                "name": "Shay Finkelstein",
                "color": "teal"
            },
            "sel5Txg8jidwVpiDS": {
                "id": "sel5Txg8jidwVpiDS",
                "name": "Tal Elyashiv",
                "color": "green"
            },
            "selmiBzMwQL9RuZME": {
                "id": "selmiBzMwQL9RuZME",
                "name": "Rune Christensen",
                "color": "blue"
            },
            "selTfOn3vgkSN1vf4": {
                "id": "selTfOn3vgkSN1vf4",
                "name": "Michael Ou",
                "color": "blue"
            },
            "sel8ol768LYEgK4BL": {
                "id": "sel8ol768LYEgK4BL",
                "name": "Greg Tusar",
                "color": "blue"
            },
            "selk5ADBMafF1bZVN": {
                "id": "selk5ADBMafF1bZVN",
                "name": "Jennifer Campbell",
                "color": "cyan"
            },
            "selGPtk0ad72Ks1xh": {
                "id": "selGPtk0ad72Ks1xh",
                "name": "Kevin Johnson",
                "color": "teal"
            },
            "selY99NdeD6ogQJah": {
                "id": "selY99NdeD6ogQJah",
                "name": "Marc Bhargava",
                "color": "green"
            },
            "selOzA1ImT3gHrkdp": {
                "id": "selOzA1ImT3gHrkdp",
                "name": "Gunnar Jaerv",
                "color": "blue"
            },
            "seljV889R9hOLOaRj": {
                "id": "seljV889R9hOLOaRj",
                "name": "Vincent Chok",
                "color": "cyan"
            },
            "selbrxhLFXxcz4jpi": {
                "id": "selbrxhLFXxcz4jpi",
                "name": "Ben Constanty",
                "color": "blue"
            },
            "selRd8GXiZJvlGOcs": {
                "id": "selRd8GXiZJvlGOcs",
                "name": "Eric Benz",
                "color": "blue"
            },
            "selDfPr9STij2ZOAD": {
                "id": "selDfPr9STij2ZOAD",
                "name": "Paul Nattapatsiri",
                "color": "blue"
            },
            "selzxgLIAqxAfMuoy": {
                "id": "selzxgLIAqxAfMuoy",
                "name": "Soravis Srinawakoon",
                "color": "cyan"
            },
            "sel57nIpCA2B3XGCS": {
                "id": "sel57nIpCA2B3XGCS",
                "name": "Sorawit Suriyakarn",
                "color": "teal"
            },
            "selBZaE842Y6jdmCh": {
                "id": "selBZaE842Y6jdmCh",
                "name": "Greg Beard",
                "color": "blue"
            },
            "selzKFRvYAWOPZyob": {
                "id": "selzKFRvYAWOPZyob",
                "name": "Marcelo Sampaio",
                "color": "blue"
            },
            "selmJCeXJDjXy9rIY": {
                "id": "selmJCeXJDjXy9rIY",
                "name": "Yin Yin Wu",
                "color": "blue"
            },
            "selHMkcmVPhm9jXUX": {
                "id": "selHMkcmVPhm9jXUX",
                "name": "Ambre Soubiran",
                "color": "blue"
            },
            "selreFZzifNJf9Rd8": {
                "id": "selreFZzifNJf9Rd8",
                "name": "Jackson Jessup",
                "color": "blue"
            },
            "selYY9NjXsxfUHmTX": {
                "id": "selYY9NjXsxfUHmTX",
                "name": "Luke Li",
                "color": "blue"
            },
            "sel5YpGce4aiOmOkT": {
                "id": "sel5YpGce4aiOmOkT",
                "name": "Michael Wu",
                "color": "cyan"
            },
            "selzrGgZHuC01jXiC": {
                "id": "selzrGgZHuC01jXiC",
                "name": "Thomas Zhu",
                "color": "teal"
            },
            "sel177aKKkv4Gw1Ft": {
                "id": "sel177aKKkv4Gw1Ft",
                "name": "Tony He",
                "color": "green"
            },
            "sel511ORJSmruJiJt": {
                "id": "sel511ORJSmruJiJt",
                "name": "Wayne Huo",
                "color": "yellow"
            },
            "selNIxoZchKB2mY7S": {
                "id": "selNIxoZchKB2mY7S",
                "name": "Daniel Bloch",
                "color": "blue"
            },
            "selkpdv9T7ApSSDUl": {
                "id": "selkpdv9T7ApSSDUl",
                "name": "Phillip Jarman",
                "color": "cyan"
            },
            "sel2G2ddgu9tFw3ee": {
                "id": "sel2G2ddgu9tFw3ee",
                "name": "Brian Armstrong",
                "color": "blue"
            },
            "selShwcLxGKLzofqX": {
                "id": "selShwcLxGKLzofqX",
                "name": "Fred Ehrsam",
                "color": "cyan"
            },
            "sela1znbUOCJmDyv4": {
                "id": "sela1znbUOCJmDyv4",
                "name": "Changpeng Zhao",
                "color": "blue"
            },
            "selXEcHt8yL9NQ2Ic": {
                "id": "selXEcHt8yL9NQ2Ic",
                "name": "Yi He",
                "color": "cyan"
            },
            "selzXMB8p57i2mXoa": {
                "id": "selzXMB8p57i2mXoa",
                "name": "Taiyang Zhang",
                "color": "blue"
            },
            "selaLMwwJtUeH7sVp": {
                "id": "selaLMwwJtUeH7sVp",
                "name": "Stuart Popejoy",
                "color": "blue"
            },
            "sel5OosuOMfYxF9kT": {
                "id": "sel5OosuOMfYxF9kT",
                "name": "William Martino",
                "color": "cyan"
            },
            "selaUDQma43x26x4h": {
                "id": "selaUDQma43x26x4h",
                "name": "Andy Bromberg",
                "color": "blue"
            },
            "selbJ4vPQnntNX0CE": {
                "id": "selbJ4vPQnntNX0CE",
                "name": "Brian Tubergen",
                "color": "cyan"
            },
            "sel9XcocwBTVnhrne": {
                "id": "sel9XcocwBTVnhrne",
                "name": "Graham Jenkin",
                "color": "teal"
            },
            "sel0euvegEDBUBkj4": {
                "id": "sel0euvegEDBUBkj4",
                "name": "Joshua Slayton",
                "color": "green"
            },
            "seldUQT0EQ4w9UwJE": {
                "id": "seldUQT0EQ4w9UwJE",
                "name": "Kendrick Nguyen",
                "color": "yellow"
            },
            "sel4WhxraiYjlQDUL": {
                "id": "sel4WhxraiYjlQDUL",
                "name": "Paul Menchov",
                "color": "orange"
            },
            "selvDZQggCCS2TgZo": {
                "id": "selvDZQggCCS2TgZo",
                "name": "Dan McArdle",
                "color": "blue"
            },
            "sel0Lu2Jbk7JYnmej": {
                "id": "sel0Lu2Jbk7JYnmej",
                "name": "Ryan Selkis",
                "color": "cyan"
            },
            "sel1KoOMozNH9qCX1": {
                "id": "sel1KoOMozNH9qCX1",
                "name": "Alex Mashinsky",
                "color": "blue"
            },
            "sel9aNsWPCAy2AJZu": {
                "id": "sel9aNsWPCAy2AJZu",
                "name": "Nuke Goldstein",
                "color": "cyan"
            },
            "selvXJdTVBM1cOPfB": {
                "id": "selvXJdTVBM1cOPfB",
                "name": "S. Daniel Leon",
                "color": "teal"
            },
            "selvDLsXX3Yt9OquP": {
                "id": "selvDLsXX3Yt9OquP",
                "name": "Drew Patel",
                "color": "blue"
            },
            "selKi0RLPqeXRd2El": {
                "id": "selKi0RLPqeXRd2El",
                "name": "Raouf Ben-Har",
                "color": "blue"
            },
            "selQSwkZC7KKdEqqR": {
                "id": "selQSwkZC7KKdEqqR",
                "name": "Jesse Proudman",
                "color": "blue"
            },
            "selvRztg182yPbD1w": {
                "id": "selvRztg182yPbD1w",
                "name": "Diogo Monica",
                "color": "blue"
            },
            "selZtklk1zm0Lm9mr": {
                "id": "selZtklk1zm0Lm9mr",
                "name": "Nathan McCauley",
                "color": "cyan"
            },
            "selIChRG4JXvLYNxk": {
                "id": "selIChRG4JXvLYNxk",
                "name": "Brian Flynn",
                "color": "blueDark"
            },
            "selH2sH28hLSIi93f": {
                "id": "selH2sH28hLSIi93f",
                "name": "Benny Giang",
                "color": "blue"
            },
            "sel3FSefVJin2lr5W": {
                "id": "sel3FSefVJin2lr5W",
                "name": "Bryce Bladon",
                "color": "cyan"
            },
            "selDQ5r84R6uxYHmm": {
                "id": "selDQ5r84R6uxYHmm",
                "name": "Dieter Shirley",
                "color": "teal"
            },
            "selS08E6OGOl4PunN": {
                "id": "selS08E6OGOl4PunN",
                "name": "Fabiano Soriani",
                "color": "green"
            },
            "sel0B9juY7iWiFZQc": {
                "id": "sel0B9juY7iWiFZQc",
                "name": "Guile Gaspar",
                "color": "yellow"
            },
            "selay3Edu64UWIG8m": {
                "id": "selay3Edu64UWIG8m",
                "name": "Mack Flavelle",
                "color": "orange"
            },
            "selxtodhsnvhYObPJ": {
                "id": "selxtodhsnvhYObPJ",
                "name": "Mik Naayem",
                "color": "red"
            },
            "sel33b7tkW32dfg1T": {
                "id": "sel33b7tkW32dfg1T",
                "name": "Garen Vartanian",
                "color": "blue"
            },
            "selhPxKpodbSzHxzR": {
                "id": "selhPxKpodbSzHxzR",
                "name": "William Bentley De Vogelaere",
                "color": "cyan"
            },
            "sel19p5zOJdYJMSco": {
                "id": "sel19p5zOJdYJMSco",
                "name": "Yogesh Srihari",
                "color": "teal"
            },
            "selfPm2M0UlhazPzX": {
                "id": "selfPm2M0UlhazPzX",
                "name": "Jeremy Longley",
                "color": "blue"
            },
            "selZjbOr015gMteg4": {
                "id": "selZjbOr015gMteg4",
                "name": "Jez San",
                "color": "cyan"
            },
            "selI2LikDp3cXMBJh": {
                "id": "selI2LikDp3cXMBJh",
                "name": "Oliver Hopton",
                "color": "teal"
            },
            "selQVyc6CM53JN0rm": {
                "id": "selQVyc6CM53JN0rm",
                "name": "Dan Teree",
                "color": "blue"
            },
            "selUQGSXlnirOU4v5": {
                "id": "selUQGSXlnirOU4v5",
                "name": "Naveen Jain",
                "color": "cyan"
            },
            "sel9hfPObBXg606Ww": {
                "id": "sel9hfPObBXg606Ww",
                "name": "Riccardo Spagni",
                "color": "teal"
            },
            "selzX8dvW9MtjsaxR": {
                "id": "selzX8dvW9MtjsaxR",
                "name": "Daniel C. McCabe",
                "color": "blue"
            },
            "seln9IhVjlUzE08uu": {
                "id": "seln9IhVjlUzE08uu",
                "name": "Trevor Filter",
                "color": "cyan"
            },
            "selu1I1zXRsYZgIjU": {
                "id": "selu1I1zXRsYZgIjU",
                "name": "Tyler Spalding",
                "color": "teal"
            },
            "selwDyEPSSa62pTh9": {
                "id": "selwDyEPSSa62pTh9",
                "name": "Zachary Kilgore",
                "color": "green"
            },
            "sel9zY6cjrYaF1n9R": {
                "id": "sel9zY6cjrYaF1n9R",
                "name": "Cyrus Taghehchian",
                "color": "blue"
            },
            "sel5VqB6mZwErg3KL": {
                "id": "sel5VqB6mZwErg3KL",
                "name": "Emma Liu",
                "color": "blue"
            },
            "selkDIj5YuthreVRI": {
                "id": "selkDIj5YuthreVRI",
                "name": "Dan Khomenko",
                "color": "blue"
            },
            "sel32mz3HpS8AftWF": {
                "id": "sel32mz3HpS8AftWF",
                "name": "Brian Fox",
                "color": "blue"
            },
            "selOEhWW5V4mSxWLQ": {
                "id": "selOEhWW5V4mSxWLQ",
                "name": "Jay Freeman",
                "color": "cyan"
            },
            "selOZzhUlaZ3OEUhs": {
                "id": "selOZzhUlaZ3OEUhs",
                "name": "Stephen Bell",
                "color": "teal"
            },
            "selNJX8VA1o8oa3rX": {
                "id": "selNJX8VA1o8oa3rX",
                "name": "Steven (Seven) Waterhouse",
                "color": "green"
            },
            "sel4VFCsGFY9X3VIo": {
                "id": "sel4VFCsGFY9X3VIo",
                "name": "Ilia Maksimenka",
                "color": "blue"
            },
            "selxYOn11f8FvJa3Q": {
                "id": "selxYOn11f8FvJa3Q",
                "name": "Kunal Sadani",
                "color": "teal"
            },
            "selVcCYsjukn5YVGu": {
                "id": "selVcCYsjukn5YVGu",
                "name": "Anthony Thomas",
                "color": "greenMedium"
            },
            "selAkzLBLxTPQT00q": {
                "id": "selAkzLBLxTPQT00q",
                "name": "Sainath Gupta",
                "color": "yellowMedium"
            },
            "selF7nMwfL8idG7xk": {
                "id": "selF7nMwfL8idG7xk",
                "name": "Grace Hyeyeon Yoon",
                "color": "blue"
            },
            "sel6Le1SFcm34dr23": {
                "id": "sel6Le1SFcm34dr23",
                "name": "Stephane Laurent Villedieu",
                "color": "blue"
            },
            "selER8CZIgHKodQvo": {
                "id": "selER8CZIgHKodQvo",
                "name": "Nick Almond",
                "color": "blue"
            },
            "selV0I4Ym37n5pCkl": {
                "id": "selV0I4Ym37n5pCkl",
                "name": "Elliot Wainman",
                "color": "grayMedium"
            },
            "selEHQ66jlP6oGA9R": {
                "id": "selEHQ66jlP6oGA9R",
                "name": "Mike Miglio",
                "color": "blue"
            },
            "seld4kBe0ns6L0BFV": {
                "id": "seld4kBe0ns6L0BFV",
                "name": "Ronghui Gu",
                "color": "blue"
            },
            "selbMQRVW0bZ3OCSb": {
                "id": "selbMQRVW0bZ3OCSb",
                "name": "Zhong Shao",
                "color": "cyan"
            },
            "selJ8efFz7U3HGUsD": {
                "id": "selJ8efFz7U3HGUsD",
                "name": "Ekaterina Volkova",
                "color": "blue"
            },
            "selefjRp20AsGPuJD": {
                "id": "selefjRp20AsGPuJD",
                "name": "Kailash Ahirwar",
                "color": "blue"
            },
            "seldgijTlTgGrQxwI": {
                "id": "seldgijTlTgGrQxwI",
                "name": "Rahul Vishwakarma",
                "color": "cyan"
            },
            "seluJgACDz5uUHE9u": {
                "id": "seluJgACDz5uUHE9u",
                "name": "Shannon Lee",
                "color": "teal"
            },
            "sel0zRW00NizjMMmt": {
                "id": "sel0zRW00NizjMMmt",
                "name": "Sherman Lee",
                "color": "green"
            },
            "selGWGojXQkBLe4yc": {
                "id": "selGWGojXQkBLe4yc",
                "name": "Hope Liu",
                "color": "blue"
            },
            "selGwYGk2pljKJAzH": {
                "id": "selGwYGk2pljKJAzH",
                "name": "Juan Sebastian Huertas",
                "color": "cyan"
            },
            "sel8sGI7ohi76Mgwl": {
                "id": "sel8sGI7ohi76Mgwl",
                "name": "Eric Shim",
                "color": "blue"
            },
            "seleMSX0shnG9XkJZ": {
                "id": "seleMSX0shnG9XkJZ",
                "name": "Jason Huan",
                "color": "blue"
            },
            "sel88f0hPxdwZHpmi": {
                "id": "sel88f0hPxdwZHpmi",
                "name": "Dai Pan",
                "color": "blue"
            },
            "seljeJZargetbnMQT": {
                "id": "seljeJZargetbnMQT",
                "name": "Daniel Wang",
                "color": "blue"
            },
            "sel8rFyS43dvJTKxv": {
                "id": "sel8rFyS43dvJTKxv",
                "name": "Jay Zhou",
                "color": "cyan"
            },
            "selqeP2liOxiGu4Ti": {
                "id": "selqeP2liOxiGu4Ti",
                "name": "Chase Lochmiller",
                "color": "blue"
            },
            "sel7xL8SdgiKfJUCt": {
                "id": "sel7xL8SdgiKfJUCt",
                "name": "Cully Cavness",
                "color": "blue"
            },
            "selV9CASxaZlPk7IQ": {
                "id": "selV9CASxaZlPk7IQ",
                "name": "Says Hanwen Cheng",
                "color": "blue"
            },
            "selLHyRQPIU8F9vPQ": {
                "id": "selLHyRQPIU8F9vPQ",
                "name": "Andrew Lee",
                "color": "purpleMedium"
            },
            "selqkwu7Bactgo1NM": {
                "id": "selqkwu7Bactgo1NM",
                "name": "Jun Hur",
                "color": "blue"
            },
            "sel4tqMe9IytiUghy": {
                "id": "sel4tqMe9IytiUghy",
                "name": "Peter Kris",
                "color": "blue"
            },
            "selAxnqmWfK0rvn2W": {
                "id": "selAxnqmWfK0rvn2W",
                "name": "Taylor Monahan",
                "color": "blue"
            },
            "selJnXnxv3U5qO5vA": {
                "id": "selJnXnxv3U5qO5vA",
                "name": "Maciej Baj",
                "color": "blue"
            },
            "selT4x8vtN7WQP1p4": {
                "id": "selT4x8vtN7WQP1p4",
                "name": "Nir BlumbergerView Nir Blumberger\u2019s profile",
                "color": "blue"
            },
            "selw2wy8E94vsoka4": {
                "id": "selw2wy8E94vsoka4",
                "name": "Sherlock Shi",
                "color": "blue"
            },
            "selOYDmONlB0Uq8Li": {
                "id": "selOYDmONlB0Uq8Li",
                "name": "Ishan Garg",
                "color": "blue"
            },
            "selGd1xe7sp1YDPUs": {
                "id": "selGd1xe7sp1YDPUs",
                "name": "Ace Tsui",
                "color": "blue"
            },
            "selZlt5GS9dEzIkYc": {
                "id": "selZlt5GS9dEzIkYc",
                "name": "Loi Luu",
                "color": "blue"
            },
            "selVCJl9b7r5hpM5h": {
                "id": "selVCJl9b7r5hpM5h",
                "name": "Victor Tran",
                "color": "cyan"
            },
            "seloKgJaTaxmXUOpl": {
                "id": "seloKgJaTaxmXUOpl",
                "name": "Yaron Velner",
                "color": "teal"
            },
            "sel6PukjSxxOJYrfI": {
                "id": "sel6PukjSxxOJYrfI",
                "name": "Jai An",
                "color": "blue"
            },
            "selY6HQ1fMOwAeGqj": {
                "id": "selY6HQ1fMOwAeGqj",
                "name": "Rafael Cosman",
                "color": "cyan"
            },
            "selae4ancfJtsEzZa": {
                "id": "selae4ancfJtsEzZa",
                "name": "Stephen Kade",
                "color": "teal"
            },
            "selX0wknCFF6u0pfN": {
                "id": "selX0wknCFF6u0pfN",
                "name": "Tory Reiss",
                "color": "green"
            },
            "selTIO7rBiUnu6ym4": {
                "id": "selTIO7rBiUnu6ym4",
                "name": "Josh Chen",
                "color": "blue"
            },
            "sel9FemtYLzRsvXtI": {
                "id": "sel9FemtYLzRsvXtI",
                "name": "Lawrence Diao",
                "color": "cyan"
            },
            "selWPW84FItjzZlNy": {
                "id": "selWPW84FItjzZlNy",
                "name": "Brandon Iles",
                "color": "blue"
            },
            "selfU2j7Rpsq31Ehy": {
                "id": "selfU2j7Rpsq31Ehy",
                "name": "Evan Kuo",
                "color": "cyan"
            },
            "seledvO7v3MUXYa7F": {
                "id": "seledvO7v3MUXYa7F",
                "name": "Kenny White",
                "color": "purpleMedium"
            },
            "seldlsktDJvqXWeb1": {
                "id": "seldlsktDJvqXWeb1",
                "name": "Charles Cascarilla",
                "color": "blue"
            },
            "selSmb7H5WNIWZ76t": {
                "id": "selSmb7H5WNIWZ76t",
                "name": "Richmond Teo",
                "color": "cyan"
            },
            "sel5Q9fexeAHIPofa": {
                "id": "sel5Q9fexeAHIPofa",
                "name": "Ryan Garner",
                "color": "blue"
            },
            "sel1IyzLhufW0dYb6": {
                "id": "sel1IyzLhufW0dYb6",
                "name": "Brendan Blumer",
                "color": "blue"
            },
            "selfhhsCc7sefkdrE": {
                "id": "selfhhsCc7sefkdrE",
                "name": "Daniel Larimer",
                "color": "cyan"
            },
            "selp29ubOkDSaIURk": {
                "id": "selp29ubOkDSaIURk",
                "name": "Sam Kim",
                "color": "blue"
            },
            "sel94bLurNdiatYcW": {
                "id": "sel94bLurNdiatYcW",
                "name": "Shantanu Kumar",
                "color": "blue"
            },
            "selgVXW4B7n59RlOz": {
                "id": "selgVXW4B7n59RlOz",
                "name": "Lisa Sun",
                "color": "blueMedium"
            },
            "selyfeC2xztaMxZsP": {
                "id": "selyfeC2xztaMxZsP",
                "name": "Jess Houlgrave",
                "color": "blue"
            },
            "seldDNx7GGrtRZTCq": {
                "id": "seldDNx7GGrtRZTCq",
                "name": "John Forrest",
                "color": "cyan"
            },
            "selB4ZKYgZb1cicvC": {
                "id": "selB4ZKYgZb1cicvC",
                "name": "Mark Lurie",
                "color": "teal"
            },
            "selvZy5zXRudrGpY3": {
                "id": "selvZy5zXRudrGpY3",
                "name": "Amrit Kumar",
                "color": "blue"
            },
            "sel3rqA2G34xO4n1s": {
                "id": "sel3rqA2G34xO4n1s",
                "name": "Jia Yaoqi",
                "color": "cyan"
            },
            "selp5QNnHh0s8x9FT": {
                "id": "selp5QNnHh0s8x9FT",
                "name": "Max Kantelia",
                "color": "teal"
            },
            "selZtnfHzSbHrlb1s": {
                "id": "selZtnfHzSbHrlb1s",
                "name": "Prateek Saxena",
                "color": "green"
            },
            "selqBn9Dv8K1Pb51p": {
                "id": "selqBn9Dv8K1Pb51p",
                "name": "Jun Hasegawa",
                "color": "blue"
            },
            "seluP9Bn4KfWYKVbR": {
                "id": "seluP9Bn4KfWYKVbR",
                "name": "Erik Voorhees",
                "color": "blue"
            },
            "sel3M6RZIC1oilbh9": {
                "id": "sel3M6RZIC1oilbh9",
                "name": "Sergey Nazarov",
                "color": "blue"
            },
            "selgT6hOGIZXW7Ayi": {
                "id": "selgT6hOGIZXW7Ayi",
                "name": "Hunter Zhang",
                "color": "blue"
            },
            "selcj9eQXncrJ23Ft": {
                "id": "selcj9eQXncrJ23Ft",
                "name": "Koshi Shiba",
                "color": "blue"
            },
            "selIzL1gtIiylKa4H": {
                "id": "selIzL1gtIiylKa4H",
                "name": "Michael Stoltzner ",
                "color": "greenDarker"
            },
            "selGgnKpROGnASKxt": {
                "id": "selGgnKpROGnASKxt",
                "name": "Leah Wald",
                "color": "blue"
            },
            "selcu12yO9qWK7ZH5": {
                "id": "selcu12yO9qWK7ZH5",
                "name": "Steven McClurg",
                "color": "cyan"
            },
            "selhJu7vpYxRD5LUx": {
                "id": "selhJu7vpYxRD5LUx",
                "name": "Alexander Liegl",
                "color": "blue"
            },
            "selOQZK3whlTzslKI": {
                "id": "selOQZK3whlTzslKI",
                "name": "Chen Fang",
                "color": "blue"
            },
            "selzXyWwpjAyZA4ZT": {
                "id": "selzXyWwpjAyZA4ZT",
                "name": "Louis de Valli\u00e8re",
                "color": "cyan"
            },
            "selk8WGOWIizmSnwZ": {
                "id": "selk8WGOWIizmSnwZ",
                "name": "Peter Pong",
                "color": "teal"
            },
            "selvW2j2jqn2XnJfl": {
                "id": "selvW2j2jqn2XnJfl",
                "name": "James Simpson",
                "color": "cyan"
            },
            "sel8lPD0vzksbtss6": {
                "id": "sel8lPD0vzksbtss6",
                "name": "Silvio Micali",
                "color": "blue"
            },
            "sel6C32s7iGtbpmdP": {
                "id": "sel6C32s7iGtbpmdP",
                "name": "Chris Gonsalves",
                "color": "grayDarker"
            },
            "selxB1wF581D9Dqab": {
                "id": "selxB1wF581D9Dqab",
                "name": "Evany Chang",
                "color": "yellowMedium"
            },
            "sel7pO14Xedm1QJxH": {
                "id": "sel7pO14Xedm1QJxH",
                "name": "Hayder Sharhan",
                "color": "greenDarker"
            },
            "selooTkvw849wSp2L": {
                "id": "selooTkvw849wSp2L",
                "name": "Josh Fraser",
                "color": "blue"
            },
            "selh3m2cJ7KDBdisQ": {
                "id": "selh3m2cJ7KDBdisQ",
                "name": "Matthew Liu",
                "color": "cyan"
            },
            "sel4dvbEI5QVfJgTG": {
                "id": "sel4dvbEI5QVfJgTG",
                "name": "Mauricio Chamati",
                "color": "green"
            },
            "seld2X3F3ycU1v1bX": {
                "id": "seld2X3F3ycU1v1bX",
                "name": "Gustavo Chamati",
                "color": "blueDark"
            },
            "selkqJeEpch9QbCd0": {
                "id": "selkqJeEpch9QbCd0",
                "name": "Alexander Vasiliev",
                "color": "blue"
            },
            "selftPH0S2hX65NUM": {
                "id": "selftPH0S2hX65NUM",
                "name": "Greg Waisman",
                "color": "cyan"
            },
            "selUV9abrC65dLBjW": {
                "id": "selUV9abrC65dLBjW",
                "name": "Petr Kozyakov",
                "color": "teal"
            },
            "selfmsSzOrqxlJ21b": {
                "id": "selfmsSzOrqxlJ21b",
                "name": "Nguyen Bui",
                "color": "blue"
            },
            "selIwvIkDsoXaESFy": {
                "id": "selIwvIkDsoXaESFy",
                "name": "Andrew Grachev",
                "color": "yellowDark"
            },
            "selU2GSrLOzRF9dhT": {
                "id": "selU2GSrLOzRF9dhT",
                "name": "0xAlpha",
                "color": "blue"
            },
            "selsvDWwlFHUxj9as": {
                "id": "selsvDWwlFHUxj9as",
                "name": "Yuriy Hotoviy",
                "color": "blue"
            },
            "selWNBmXJXpoMwdBc": {
                "id": "selWNBmXJXpoMwdBc",
                "name": "Tao Hu",
                "color": "blue"
            },
            "sel5BiB1w60BXu9y7": {
                "id": "sel5BiB1w60BXu9y7",
                "name": "Yat Siu",
                "color": "pinkMedium"
            },
            "sel0uH2UtmO9yQdAa": {
                "id": "sel0uH2UtmO9yQdAa",
                "name": "Meinhard Benn",
                "color": "blue"
            },
            "selLikzg8A44KGYoB": {
                "id": "selLikzg8A44KGYoB",
                "name": "Irfan Khan",
                "color": "blue"
            },
            "selYXEesjpEEskavu": {
                "id": "selYXEesjpEEskavu",
                "name": "Vishwas Bhushan",
                "color": "cyan"
            },
            "selZjWxL0B3Rr39se": {
                "id": "selZjWxL0B3Rr39se",
                "name": "Sherry Ye",
                "color": "pinkDarker"
            },
            "selu1FvRUUj7YaTaT": {
                "id": "selu1FvRUUj7YaTaT",
                "name": "Typto",
                "color": "teal"
            },
            "selM7340KwJIiwqH6": {
                "id": "selM7340KwJIiwqH6",
                "name": "Quincy Dagelet",
                "color": "blueMedium"
            },
            "selBRqEX18wYTr8MQ": {
                "id": "selBRqEX18wYTr8MQ",
                "name": "Elena Sinelnikova",
                "color": "blue"
            },
            "selXiddwJ2RXxZDaG": {
                "id": "selXiddwJ2RXxZDaG",
                "name": "Ang Kang Wei",
                "color": "blue"
            },
            "selOrgP1f5ciBnYiK": {
                "id": "selOrgP1f5ciBnYiK",
                "name": "Jonathan Ovadi",
                "color": "redMedium"
            },
            "selGYHEOnBVB3skjV": {
                "id": "selGYHEOnBVB3skjV",
                "name": "Ugoji Harry",
                "color": "blue"
            },
            "selUPvXVEyBotf59l": {
                "id": "selUPvXVEyBotf59l",
                "name": "Darin Feinstein",
                "color": "blue"
            },
            "selGlYb2Bhf2rm4D3": {
                "id": "selGlYb2Bhf2rm4D3",
                "name": "Paul Barroso",
                "color": "tealDarker"
            },
            "selvZuzGZxpaRbQue": {
                "id": "selvZuzGZxpaRbQue",
                "name": "Haydee Barroso",
                "color": "pink"
            },
            "selL9pVk7sz7jLUDK": {
                "id": "selL9pVk7sz7jLUDK",
                "name": "Pushkarr Vohra",
                "color": "blue"
            },
            "selMaz1M6ni2gcUq5": {
                "id": "selMaz1M6ni2gcUq5",
                "name": "Danny Chong",
                "color": "blue"
            },
            "selCl0lUKnNWX4lkQ": {
                "id": "selCl0lUKnNWX4lkQ",
                "name": "Eran Elhanani",
                "color": "blue"
            },
            "selardUkptuk7o0E4": {
                "id": "selardUkptuk7o0E4",
                "name": "Constantin Kogan",
                "color": "teal"
            },
            "selw2KJjbXpzeBGQ2": {
                "id": "selw2KJjbXpzeBGQ2",
                "name": "Grigory Rybalchenko",
                "color": "blue"
            },
            "selgPVMDXDzDOv2rn": {
                "id": "selgPVMDXDzDOv2rn",
                "name": "Chris Swenor",
                "color": "blue"
            },
            "sel02YempOzFvP06T": {
                "id": "sel02YempOzFvP06T",
                "name": "Chris Worsey",
                "color": "blue"
            },
            "seldhGSGb8bhPnRy3": {
                "id": "seldhGSGb8bhPnRy3",
                "name": "Ocean Liao",
                "color": "blue"
            },
            "sels3fJmKbFXfXIIJ": {
                "id": "sels3fJmKbFXfXIIJ",
                "name": "Junhaeng Lee",
                "color": "blue"
            },
            "selpBkWbTMDiB5Ayf": {
                "id": "selpBkWbTMDiB5Ayf",
                "name": "Danial Daychopan",
                "color": "blue"
            },
            "selhmVfjyZVSl9vNy": {
                "id": "selhmVfjyZVSl9vNy",
                "name": "Jasper Tay",
                "color": "purpleDark"
            },
            "selgjihc4Mp8hS6VW": {
                "id": "selgjihc4Mp8hS6VW",
                "name": "Amy Wan",
                "color": "blue"
            },
            "selxZ55V6W6dAjxe1": {
                "id": "selxZ55V6W6dAjxe1",
                "name": "Dan Rice",
                "color": "redDark"
            },
            "sel3cc5j9nuJQ5KYR": {
                "id": "sel3cc5j9nuJQ5KYR",
                "name": "Navjit Dhaliwal",
                "color": "blue"
            },
            "sel2MwSx1ASE5fkxA": {
                "id": "sel2MwSx1ASE5fkxA",
                "name": "Solo Ceesay",
                "color": "blue"
            },
            "seleWBvoNjZTMs3wD": {
                "id": "seleWBvoNjZTMs3wD",
                "name": "Spencer Dinwiddie",
                "color": "redMedium"
            },
            "selB9FjULLYUlha2f": {
                "id": "selB9FjULLYUlha2f",
                "name": "Dennis Lee",
                "color": "blue"
            },
            "selFQTTa45i3do0Sg": {
                "id": "selFQTTa45i3do0Sg",
                "name": "Joseph Thompson",
                "color": "blue"
            },
            "sel8R8GoYG1gwVOuy": {
                "id": "sel8R8GoYG1gwVOuy",
                "name": "Niall Dennehy",
                "color": "cyan"
            },
            "selIX7k3Sxq2fuwG7": {
                "id": "selIX7k3Sxq2fuwG7",
                "name": "Reuven Cohen",
                "color": "blue"
            },
            "selCrVzqPtfFkKZYx": {
                "id": "selCrVzqPtfFkKZYx",
                "name": "Garri Zmudze",
                "color": "blue"
            },
            "sel4ESX8fxcEpUJFh": {
                "id": "sel4ESX8fxcEpUJFh",
                "name": "Jan Goslicki",
                "color": "blue"
            },
            "seladnYyED6NsoXPo": {
                "id": "seladnYyED6NsoXPo",
                "name": "Jorg von Minckwitz",
                "color": "cyan"
            },
            "selPZGnTlDMHs3pGr": {
                "id": "selPZGnTlDMHs3pGr",
                "name": "Mike Edwards",
                "color": "blue"
            },
            "sel4J8mQLhRYig1XX": {
                "id": "sel4J8mQLhRYig1XX",
                "name": "Peter Wall",
                "color": "cyan"
            },
            "seloSDWivu5beSC76": {
                "id": "seloSDWivu5beSC76",
                "name": "Nicholas Chan",
                "color": "blue"
            },
            "seludFTmlYhWQLnzz": {
                "id": "seludFTmlYhWQLnzz",
                "name": "Simon Yu",
                "color": "blue"
            },
            "selrJiKqR0Fbvltmz": {
                "id": "selrJiKqR0Fbvltmz",
                "name": "Mike Davie",
                "color": "blue"
            },
            "seltlu5aG1PkKg4Gi": {
                "id": "seltlu5aG1PkKg4Gi",
                "name": "Qi Zhou",
                "color": "blue"
            },
            "selxxD1YfVB37WXCa": {
                "id": "selxxD1YfVB37WXCa",
                "name": "Don Mosites",
                "color": "blue"
            },
            "selp8qL0U95jEorvy": {
                "id": "selp8qL0U95jEorvy",
                "name": "Michael Oved",
                "color": "cyan"
            },
            "selmcjL5OT0pn6E3y": {
                "id": "selmcjL5OT0pn6E3y",
                "name": "Mattia Gagliardi",
                "color": "blue"
            },
            "sel4MNcELtiy1RoCV": {
                "id": "sel4MNcELtiy1RoCV",
                "name": "Christian Miccoli",
                "color": "blue"
            },
            "selPNdQNv6EXAwdCj": {
                "id": "selPNdQNv6EXAwdCj",
                "name": "Vincenzo Di Nicola",
                "color": "cyan"
            },
            "selw5oH049qZThXou": {
                "id": "selw5oH049qZThXou",
                "name": "Frank Schuil",
                "color": "cyan"
            },
            "sel7ObZEHP5Et1fe2": {
                "id": "sel7ObZEHP5Et1fe2",
                "name": "Andy Flury",
                "color": "blue"
            },
            "selZAWVhsdfvtEZaT": {
                "id": "selZAWVhsdfvtEZaT",
                "name": "Colin Sullivan",
                "color": "blue"
            },
            "sel3ZaT7jqBlNVGZj": {
                "id": "sel3ZaT7jqBlNVGZj",
                "name": "Kurt Melnychuk",
                "color": "tealDarker"
            },
            "sel7MguGXu8jirFYK": {
                "id": "sel7MguGXu8jirFYK",
                "name": "Jennifer Zee",
                "color": "purpleDarker"
            },
            "selXlJmkjXnLZs8Oc": {
                "id": "selXlJmkjXnLZs8Oc",
                "name": "Rahul P.",
                "color": "cyan"
            },
            "selck7DZPIutW8o1E": {
                "id": "selck7DZPIutW8o1E",
                "name": "Evan Vandenberg",
                "color": "blue"
            },
            "selYUvmdlmVK0bJsf": {
                "id": "selYUvmdlmVK0bJsf",
                "name": "Nadim Kobeissi",
                "color": "blue"
            },
            "seltnncwDshPWFoQ4": {
                "id": "seltnncwDshPWFoQ4",
                "name": "Francisco Benedito",
                "color": "blue"
            },
            "selzhxdCzbwjLDzlb": {
                "id": "selzhxdCzbwjLDzlb",
                "name": "Simon Judd",
                "color": "blue"
            },
            "selYKVAPuYv5Ga2s1": {
                "id": "selYKVAPuYv5Ga2s1",
                "name": "Allen Wookyun Kho",
                "color": "blue"
            },
            "selQ79nGq5j6Gzl7t": {
                "id": "selQ79nGq5j6Gzl7t",
                "name": "Eunsol Lee",
                "color": "cyan"
            },
            "selQDk7xqPlz3VNL5": {
                "id": "selQDk7xqPlz3VNL5",
                "name": "Stig Aleksander Kjos-Mathisen",
                "color": "blue"
            },
            "seluGWwTIf98VpQOW": {
                "id": "seluGWwTIf98VpQOW",
                "name": "Thomas Johnson",
                "color": "blue"
            },
            "selQ7fIKq94oP5jRW": {
                "id": "selQ7fIKq94oP5jRW",
                "name": "Guido Stroemer",
                "color": "blue"
            },
            "selSfJHw6J3Fd6j2n": {
                "id": "selSfJHw6J3Fd6j2n",
                "name": "Yifei Zhang",
                "color": "blue"
            },
            "selLeVK67LzdkV2Fc": {
                "id": "selLeVK67LzdkV2Fc",
                "name": "Scott Schulz",
                "color": "blue"
            },
            "selZiDnF4fOK46Fnj": {
                "id": "selZiDnF4fOK46Fnj",
                "name": "Michael Wagner",
                "color": "blue"
            },
            "selS55ilWimL00YQd": {
                "id": "selS55ilWimL00YQd",
                "name": "Mike Alfred",
                "color": "blue"
            },
            "selwvpDKlLBR2E4Mh": {
                "id": "selwvpDKlLBR2E4Mh",
                "name": "Eddie Alfred",
                "color": "blue"
            },
            "selkz7Y0EnDDR2fu9": {
                "id": "selkz7Y0EnDDR2fu9",
                "name": "Jason Yates",
                "color": "cyan"
            },
            "selTe9vSRdkpgDR1X": {
                "id": "selTe9vSRdkpgDR1X",
                "name": "Kurt Fenstermacher",
                "color": "teal"
            },
            "sellU5FdhlH486Krr": {
                "id": "sellU5FdhlH486Krr",
                "name": "https://solrise.finance/",
                "color": "blue"
            },
            "selp3srcq23v6kgMi": {
                "id": "selp3srcq23v6kgMi",
                "name": "Vidor Gencel",
                "color": "blue"
            },
            "selrV20cUuCynbdZx": {
                "id": "selrV20cUuCynbdZx",
                "name": "Matt Martin",
                "color": "orange"
            },
            "selIIuswsUuUiidFb": {
                "id": "selIIuswsUuUiidFb",
                "name": "Filip Dragoslavic",
                "color": "tealMedium"
            },
            "sel7GxniKbQx4USbJ": {
                "id": "sel7GxniKbQx4USbJ",
                "name": "Robert Gutmann",
                "color": "blue"
            },
            "seliVIyUrhFcrNwQb": {
                "id": "seliVIyUrhFcrNwQb",
                "name": "Ross Stevens",
                "color": "cyan"
            },
            "selmGkCBBeIcNS8KQ": {
                "id": "selmGkCBBeIcNS8KQ",
                "name": "Will Sheehan",
                "color": "pinkDarker"
            },
            "selaPG2AvNcRPD6AU": {
                "id": "selaPG2AvNcRPD6AU",
                "name": "David J. Namdar",
                "color": "blue"
            },
            "selC85t9EfDcxvGav": {
                "id": "selC85t9EfDcxvGav",
                "name": "Michael Novogratz",
                "color": "cyan"
            },
            "selgGLRo0Pd7O5K3E": {
                "id": "selgGLRo0Pd7O5K3E",
                "name": "Sam Englebardt",
                "color": "teal"
            },
            "selszyaSca43RF86O": {
                "id": "selszyaSca43RF86O",
                "name": "Ben Davenport",
                "color": "blue"
            },
            "selZmbS0H40edwLgF": {
                "id": "selZmbS0H40edwLgF",
                "name": "Mike Belshe",
                "color": "cyan"
            },
            "selL9jcayOSxVZqCm": {
                "id": "selL9jcayOSxVZqCm",
                "name": "Will O'Brien",
                "color": "teal"
            },
            "selIQDbJFNLJ22FfK": {
                "id": "selIQDbJFNLJ22FfK",
                "name": "Chris Larsen",
                "color": "blue"
            },
            "selwFjbgZ0zAGTc1T": {
                "id": "selwFjbgZ0zAGTc1T",
                "name": "Ryan Fugger",
                "color": "cyan"
            },
            "selic6jaqOVDLg7PI": {
                "id": "selic6jaqOVDLg7PI",
                "name": "Javier Sim",
                "color": "blue"
            },
            "selFuk9RBIv8R8NVy": {
                "id": "selFuk9RBIv8R8NVy",
                "name": "Chris Wang",
                "color": "blue"
            },
            "selj8KOtjMTYvRReW": {
                "id": "selj8KOtjMTYvRReW",
                "name": "Baiju Bhatt",
                "color": "blue"
            },
            "selxCz6r06GB3nXab": {
                "id": "selxCz6r06GB3nXab",
                "name": "Jihan Wu",
                "color": "blue"
            },
            "selAPsvEgT6To2ZoP": {
                "id": "selAPsvEgT6To2ZoP",
                "name": "Micree Zhan",
                "color": "cyan"
            },
            "selxfTpoJNi1UWPlZ": {
                "id": "selxfTpoJNi1UWPlZ",
                "name": "Muthu Venkitasubramaniam",
                "color": "blue"
            },
            "selcoqiNOey4r2JME": {
                "id": "selcoqiNOey4r2JME",
                "name": "Mark Lamb",
                "color": "blue"
            },
            "selRGCw2YWT2Lwq91": {
                "id": "selRGCw2YWT2Lwq91",
                "name": "Sudhu Arumugam",
                "color": "cyan"
            },
            "sel3MaVU0mRiw6pX5": {
                "id": "sel3MaVU0mRiw6pX5",
                "name": "Thomas Pocock",
                "color": "blue"
            },
            "sel2pQA1iDbB7jBxy": {
                "id": "sel2pQA1iDbB7jBxy",
                "name": "Zachary Williamson",
                "color": "cyan"
            },
            "selYS1DUpUQm5b5iW": {
                "id": "selYS1DUpUQm5b5iW",
                "name": "Daniel Paz",
                "color": "blue"
            },
            "selgC8ixbXdNSLqqC": {
                "id": "selgC8ixbXdNSLqqC",
                "name": "Trey Griffith",
                "color": "cyan"
            },
            "sel5ke3gKUFUfY74R": {
                "id": "sel5ke3gKUFUfY74R",
                "name": "Cipher Wang",
                "color": "blue"
            },
            "selTp7NIYJNIIyy2R": {
                "id": "selTp7NIYJNIIyy2R",
                "name": "Daniel Lv",
                "color": "cyan"
            },
            "sel2BdtZIaIn2CZaM": {
                "id": "sel2BdtZIaIn2CZaM",
                "name": "Jan Xie",
                "color": "teal"
            },
            "sel7ePuBwid9dl7i4": {
                "id": "sel7ePuBwid9dl7i4",
                "name": "Kevin Wang",
                "color": "green"
            },
            "sel5j5kD0pvrd99Fr": {
                "id": "sel5j5kD0pvrd99Fr",
                "name": "Terry Tai",
                "color": "yellow"
            },
            "sel9nF5UMXMumcCrk": {
                "id": "sel9nF5UMXMumcCrk",
                "name": "Will O\u2019Brien",
                "color": "blue"
            },
            "selCHGyMVD5midNr7": {
                "id": "selCHGyMVD5midNr7",
                "name": "Yeshu Agarwal",
                "color": "blue"
            },
            "selb9j4hBWRnn1cGf": {
                "id": "selb9j4hBWRnn1cGf",
                "name": "Sami Start",
                "color": "pinkDark"
            },
            "selT8JeOnqHNoTDit": {
                "id": "selT8JeOnqHNoTDit",
                "name": "Mark Stoter",
                "color": "blue"
            },
            "selKg3ctuTuH7pHoi": {
                "id": "selKg3ctuTuH7pHoi",
                "name": "Jieyi Long",
                "color": "blue"
            },
            "selsUQrphEnDBALyT": {
                "id": "selsUQrphEnDBALyT",
                "name": "Mitch Liu",
                "color": "cyan"
            },
            "sel8a2BSD2mRoS30u": {
                "id": "sel8a2BSD2mRoS30u",
                "name": "Ryan Nichols",
                "color": "teal"
            },
            "seloWT3MBRR94aZe6": {
                "id": "seloWT3MBRR94aZe6",
                "name": "David Hanson",
                "color": "blue"
            },
            "sel0gXqgPEgJ5GZWt": {
                "id": "sel0gXqgPEgJ5GZWt",
                "name": "Nicolas Gilot",
                "color": "cyan"
            },
            "sel5LZYmxPa8FHMM5": {
                "id": "sel5LZYmxPa8FHMM5",
                "name": "David Janczewski",
                "color": "blue"
            },
            "selaXJJ1XJAoIgRWg": {
                "id": "selaXJJ1XJAoIgRWg",
                "name": "David Bailey",
                "color": "blue"
            },
            "selos52uevKNZZ13T": {
                "id": "selos52uevKNZZ13T",
                "name": "Ethan Buchman",
                "color": "blue"
            },
            "selX7QFCpOpooRmQU": {
                "id": "selX7QFCpOpooRmQU",
                "name": "Jae Kwon",
                "color": "cyan"
            },
            "sel4DNvrp7m2VLjE7": {
                "id": "sel4DNvrp7m2VLjE7",
                "name": "Federico Cristina",
                "color": "blue"
            },
            "selxQzQwM5bmjHNhe": {
                "id": "selxQzQwM5bmjHNhe",
                "name": "Grant Sohn",
                "color": "blue"
            },
            "selJ2M3VNWdhgukF8": {
                "id": "selJ2M3VNWdhgukF8",
                "name": "Richard Choi",
                "color": "blue"
            },
            "selWoQklF1eFqX4i8": {
                "id": "selWoQklF1eFqX4i8",
                "name": "Jesse Powell",
                "color": "blue"
            },
            "selGqDHKUDPi4zD9N": {
                "id": "selGqDHKUDPi4zD9N",
                "name": "Allen Lee",
                "color": "redDark"
            },
            "selvJqdKGEhwhfI6s": {
                "id": "selvJqdKGEhwhfI6s",
                "name": "Alessandro Siniscalchi",
                "color": "blue"
            },
            "selBnvqkKYJ0mbnyv": {
                "id": "selBnvqkKYJ0mbnyv",
                "name": "Alun Evans",
                "color": "cyan"
            },
            "selqWHSqds5VsELBp": {
                "id": "selqWHSqds5VsELBp",
                "name": "Ferran Estalella",
                "color": "teal"
            },
            "selY15zkMOlfeWa8o": {
                "id": "selY15zkMOlfeWa8o",
                "name": "Toni Mateos",
                "color": "green"
            },
            "selor0OOHgMN1LMEs": {
                "id": "selor0OOHgMN1LMEs",
                "name": "A.V. Raviteja",
                "color": "blue"
            },
            "selJPpOZH3kPzF2sw": {
                "id": "selJPpOZH3kPzF2sw",
                "name": "Brian Hankey",
                "color": "blue"
            },
            "selutKrzSIvgHoJlg": {
                "id": "selutKrzSIvgHoJlg",
                "name": "Gregor Gregersen",
                "color": "cyan"
            },
            "selk1EE7PXHNijCsN": {
                "id": "selk1EE7PXHNijCsN",
                "name": "Aleksandar Mitrovic",
                "color": "blue"
            },
            "selZOLjXawz60t55P": {
                "id": "selZOLjXawz60t55P",
                "name": "Claude Eguienta",
                "color": "blue"
            },
            "sel9FUgYv0OEGtosd": {
                "id": "sel9FUgYv0OEGtosd",
                "name": "Paul Neuner",
                "color": "cyan"
            },
            "selHHt6AhLNxk0Qyb": {
                "id": "selHHt6AhLNxk0Qyb",
                "name": "Majd Alafifi",
                "color": "blue"
            },
            "selzt9jTSvfnVP7AI": {
                "id": "selzt9jTSvfnVP7AI",
                "name": "Mohamed El Kandri",
                "color": "cyan"
            },
            "selCX8XyzMIysZQ01": {
                "id": "selCX8XyzMIysZQ01",
                "name": "Hart Lambur",
                "color": "gray"
            },
            "selht0iq3xNXNc4hJ": {
                "id": "selht0iq3xNXNc4hJ",
                "name": "Adam Back",
                "color": "blue"
            },
            "selYdANt2RSzgiNSJ": {
                "id": "selYdANt2RSzgiNSJ",
                "name": "Erik Svenson",
                "color": "cyan"
            },
            "selrYpwAmyVylAgGe": {
                "id": "selrYpwAmyVylAgGe",
                "name": "Gregory Maxwell",
                "color": "teal"
            },
            "selsIzGGjCghTZkDH": {
                "id": "selsIzGGjCghTZkDH",
                "name": "Jonathan Wilkins",
                "color": "green"
            },
            "selUYjzyJQulvqNqW": {
                "id": "selUYjzyJQulvqNqW",
                "name": "Jorge Tim\u00f3n",
                "color": "yellow"
            },
            "selnbV5CnNhGUX3eY": {
                "id": "selnbV5CnNhGUX3eY",
                "name": "Mark Friedenbach",
                "color": "orange"
            },
            "selFYTkwPa5nyOwi9": {
                "id": "selFYTkwPa5nyOwi9",
                "name": "Matt Corallo",
                "color": "red"
            },
            "selkcNdiOnbqKhLvV": {
                "id": "selkcNdiOnbqKhLvV",
                "name": "Pieter Wuille",
                "color": "pink"
            },
            "selslP75HYXPiaZVU": {
                "id": "selslP75HYXPiaZVU",
                "name": "Stefan R\u00fcst",
                "color": "blue"
            },
            "sel3GYHVfbHWKosUe": {
                "id": "sel3GYHVfbHWKosUe",
                "name": "Tommy Nordam Jensen",
                "color": "blue"
            },
            "sel7cDFdKzEkIp78P": {
                "id": "sel7cDFdKzEkIp78P",
                "name": "H\u00e5kon Harberg",
                "color": "cyan"
            },
            "selKr8E6tAl7uIoY3": {
                "id": "selKr8E6tAl7uIoY3",
                "name": "Kieran Daniels",
                "color": "blue"
            },
            "sel13u094vjlOlKwp": {
                "id": "sel13u094vjlOlKwp",
                "name": "Dziugas Butkus",
                "color": "grayDarker"
            },
            "sel8E81DFuBXGY28F": {
                "id": "sel8E81DFuBXGY28F",
                "name": "Neel Popat",
                "color": "blue"
            },
            "sellNB2ypYlssFsrp": {
                "id": "sellNB2ypYlssFsrp",
                "name": "Josipa Majic",
                "color": "blue"
            },
            "selGYTGgDKDTlHToo": {
                "id": "selGYTGgDKDTlHToo",
                "name": "Florian Wimmer",
                "color": "blue"
            },
            "selwSqXHmpU7lJg8v": {
                "id": "selwSqXHmpU7lJg8v",
                "name": "Amir Haleem",
                "color": "blue"
            },
            "seleTuYEGDETOt8Ve": {
                "id": "seleTuYEGDETOt8Ve",
                "name": "Sean Carey",
                "color": "cyan"
            },
            "selgKHNMsuYWONxjG": {
                "id": "selgKHNMsuYWONxjG",
                "name": "Shawn Fanning",
                "color": "teal"
            },
            "sel6stMONGeqwvXZk": {
                "id": "sel6stMONGeqwvXZk",
                "name": "Dang Thai Hoa",
                "color": "blue"
            },
            "seluJzKNmvKZgMnrm": {
                "id": "seluJzKNmvKZgMnrm",
                "name": "Vu Thanh Tung",
                "color": "green"
            },
            "selwXDNNCAg3CEWWl": {
                "id": "selwXDNNCAg3CEWWl",
                "name": "https://lith.finance/",
                "color": "blue"
            },
            "seleeCLXeyilHrWw1": {
                "id": "seleeCLXeyilHrWw1",
                "name": "Merit Valdsalu",
                "color": "blue"
            },
            "selVYA2hr31OxiPZc": {
                "id": "selVYA2hr31OxiPZc",
                "name": "Andrus Aaslaid",
                "color": "blueMedium"
            },
            "selGn14uOPZLdJZ0Z": {
                "id": "selGn14uOPZLdJZ0Z",
                "name": "Guozi Yin",
                "color": "blue"
            },
            "seloQBUxiRpYsu4PP": {
                "id": "seloQBUxiRpYsu4PP",
                "name": "Alexander Shedogubov",
                "color": "blue"
            },
            "selysNQrGi4ShcelN": {
                "id": "selysNQrGi4ShcelN",
                "name": "Long Vuong",
                "color": "blue"
            },
            "sel77NmPRFuK1ej2S": {
                "id": "sel77NmPRFuK1ej2S",
                "name": "Kyung-Hun Ha",
                "color": "blue"
            },
            "seluGKYjpdBorkeEF": {
                "id": "seluGKYjpdBorkeEF",
                "name": "Richard Lohwasser",
                "color": "cyan"
            },
            "selcHwe3bdX6H8Rr7": {
                "id": "selcHwe3bdX6H8Rr7",
                "name": "Jan Brzezek",
                "color": "blue"
            },
            "selOVot9pgldgbKKY": {
                "id": "selOVot9pgldgbKKY",
                "name": "Tobias Reichmuth",
                "color": "cyan"
            },
            "seljiwcb5PDgUiern": {
                "id": "seljiwcb5PDgUiern",
                "name": "Randy Wasinger",
                "color": "blue"
            },
            "sel4EaQvOP0D8dbRu": {
                "id": "sel4EaQvOP0D8dbRu",
                "name": "Andrew J. Filipowski",
                "color": "blue"
            },
            "sel4k4y9Wz5UdRFMH": {
                "id": "sel4k4y9Wz5UdRFMH",
                "name": "Brian M. Platz",
                "color": "cyan"
            },
            "selzNknMPMWqQlRNg": {
                "id": "selzNknMPMWqQlRNg",
                "name": "Aidan McCarty",
                "color": "blue"
            },
            "selV6mh7TvPF4bmOf": {
                "id": "selV6mh7TvPF4bmOf",
                "name": "Liam McCarty",
                "color": "cyan"
            },
            "sels60d6hh61Cq2gd": {
                "id": "sels60d6hh61Cq2gd",
                "name": "Tomochika Kamiya",
                "color": "blue"
            },
            "selPMUnCJMJH3mnnP": {
                "id": "selPMUnCJMJH3mnnP",
                "name": "Alon Cohen",
                "color": "blue"
            },
            "sel0yq9wJAqG1skyt": {
                "id": "sel0yq9wJAqG1skyt",
                "name": "Andrey Iaremenko",
                "color": "cyan"
            },
            "selw5aj7T0idvOgq4": {
                "id": "selw5aj7T0idvOgq4",
                "name": "Eyal Moshe",
                "color": "teal"
            },
            "selex61lfz24kVMKE": {
                "id": "selex61lfz24kVMKE",
                "name": "James Poole",
                "color": "blue"
            },
            "selrzkP9qLju9soCP": {
                "id": "selrzkP9qLju9soCP",
                "name": "Mason Borda",
                "color": "cyan"
            },
            "selrzFDJH1ojVoAKt": {
                "id": "selrzFDJH1ojVoAKt",
                "name": "Eric Schiermeyer",
                "color": "cyanDark"
            },
            "sel9jGNeCVv2Qpk93": {
                "id": "sel9jGNeCVv2Qpk93",
                "name": "Zhaoxing Luo",
                "color": "blue"
            },
            "seldNEnO7aoE9X28S": {
                "id": "seldNEnO7aoE9X28S",
                "name": "Francesco George Renzi",
                "color": "redDarker"
            },
            "selmc49sPqTADMxK7": {
                "id": "selmc49sPqTADMxK7",
                "name": "Farmwell",
                "color": "tealDark"
            },
            "seluR5Nsull4PpvJC": {
                "id": "seluR5Nsull4PpvJC",
                "name": "Agustin Liserra",
                "color": "blue"
            },
            "selmYkOgwUp78eEKY": {
                "id": "selmYkOgwUp78eEKY",
                "name": "Federico Ogue",
                "color": "cyan"
            },
            "selsuL65agl5BT52d": {
                "id": "selsuL65agl5BT52d",
                "name": "Gonzalo Lema",
                "color": "teal"
            },
            "selxPpvI5LiLfZEUe": {
                "id": "selxPpvI5LiLfZEUe",
                "name": "Juli\u00e1n Fraiese",
                "color": "green"
            },
            "selDt7OM4NZrxUSOh": {
                "id": "selDt7OM4NZrxUSOh",
                "name": "Manuel Mauer",
                "color": "yellow"
            },
            "selTaea1xYsl5HZUd": {
                "id": "selTaea1xYsl5HZUd",
                "name": "Manuel Ponce Pe\u00f1alva",
                "color": "orange"
            },
            "selhh2mnbrerPeitj": {
                "id": "selhh2mnbrerPeitj",
                "name": "Andrew Cronk",
                "color": "blue"
            },
            "sel1u3AcG9NJGafLg": {
                "id": "sel1u3AcG9NJGafLg",
                "name": "Matt Harrop",
                "color": "cyan"
            },
            "sel8CSvxwh81T7unx": {
                "id": "sel8CSvxwh81T7unx",
                "name": "Mohak Agarwal",
                "color": "blue"
            },
            "sel4EWA1C3IR0CSRA": {
                "id": "sel4EWA1C3IR0CSRA",
                "name": "Brandon Millman",
                "color": "blue"
            },
            "selUfC4TNe3VcTAcf": {
                "id": "selUfC4TNe3VcTAcf",
                "name": "Chris Kalani",
                "color": "cyan"
            },
            "selavAcPUfshQfP9F": {
                "id": "selavAcPUfshQfP9F",
                "name": "Francesco Agosti",
                "color": "teal"
            },
            "selFc0ZvuD0OBt9Ff": {
                "id": "selFc0ZvuD0OBt9Ff",
                "name": "Bram Verstraeten",
                "color": "blue"
            },
            "sela3X6SLyyM3TIzi": {
                "id": "sela3X6SLyyM3TIzi",
                "name": "Padmakumar Nair",
                "color": "blue"
            },
            "selnEztYnhHpcTjde": {
                "id": "selnEztYnhHpcTjde",
                "name": "Shalini Nair",
                "color": "cyan"
            },
            "sel7khayDyTTxfG9e": {
                "id": "sel7khayDyTTxfG9e",
                "name": "Jess Sloss",
                "color": "blue"
            },
            "selnBcTAqCV6vMEll": {
                "id": "selnBcTAqCV6vMEll",
                "name": "Steve Wei",
                "color": "blue"
            },
            "selvVDH8t5WIAFknL": {
                "id": "selvVDH8t5WIAFknL",
                "name": "Dean Tribble",
                "color": "blue"
            },
            "seln4TlmHvJRKUwpH": {
                "id": "seln4TlmHvJRKUwpH",
                "name": "Mark S. Miller",
                "color": "cyan"
            },
            "selIVcLkZIU3ACzIr": {
                "id": "selIVcLkZIU3ACzIr",
                "name": "Frank Fang",
                "color": "blue"
            },
            "seljDLGzl5800EGKk": {
                "id": "seljDLGzl5800EGKk",
                "name": "Phil Zamani",
                "color": "blue"
            },
            "selHIe3wJvlsgUXH4": {
                "id": "selHIe3wJvlsgUXH4",
                "name": "Won-Beom Kim",
                "color": "cyan"
            },
            "seliKk145fV7AbGdm": {
                "id": "seliKk145fV7AbGdm",
                "name": "Filip Tomaska",
                "color": "blue"
            },
            "seljCNrKGFoxH2mOf": {
                "id": "seljCNrKGFoxH2mOf",
                "name": "Duc Luu",
                "color": "blue"
            },
            "selio1Wu0cvclzU0F": {
                "id": "selio1Wu0cvclzU0F",
                "name": "Eric Hung Nguyen",
                "color": "pinkDark"
            },
            "selCFBWn3tvQeiCFK": {
                "id": "selCFBWn3tvQeiCFK",
                "name": "Paven Do",
                "color": "blueDark"
            },
            "selas6Mgm6Xdk4Gmg": {
                "id": "selas6Mgm6Xdk4Gmg",
                "name": "Jakub Wojciechowski",
                "color": "blue"
            },
            "seljUnzwl0syUI358": {
                "id": "seljUnzwl0syUI358",
                "name": "Harry Halpin",
                "color": "blue"
            },
            "selQNJ23UFBsOE3n5": {
                "id": "selQNJ23UFBsOE3n5",
                "name": "James Hormuzdiar",
                "color": "blue"
            },
            "selcXaYT30fbHzik4": {
                "id": "selcXaYT30fbHzik4",
                "name": "Kieren James Lubin",
                "color": "cyan"
            },
            "selsCUqXMSau63yFn": {
                "id": "selsCUqXMSau63yFn",
                "name": "Victor Wong",
                "color": "teal"
            },
            "selP8KLyeoTSyPP9Q": {
                "id": "selP8KLyeoTSyPP9Q",
                "name": "Adam Krellenstein",
                "color": "blue"
            },
            "sel5PerQ77RSWmA5P": {
                "id": "sel5PerQ77RSWmA5P",
                "name": "Evan Wagner",
                "color": "cyan"
            },
            "selgt22XHgHfpHmhI": {
                "id": "selgt22XHgHfpHmhI",
                "name": "Mark Smith",
                "color": "teal"
            },
            "selHUJ6nvTqX52oEC": {
                "id": "selHUJ6nvTqX52oEC",
                "name": "Robby Dermody",
                "color": "green"
            },
            "sela7aTwsKqywQzaJ": {
                "id": "sela7aTwsKqywQzaJ",
                "name": "Adrian le Bas",
                "color": "blueDark"
            },
            "selRhkaQDuTg3qUBq": {
                "id": "selRhkaQDuTg3qUBq",
                "name": "Chris Laurent",
                "color": "blue"
            },
            "sel5ntxoZXuuMiUH6": {
                "id": "sel5ntxoZXuuMiUH6",
                "name": "Richard Li",
                "color": "blue"
            },
            "selr5zzZ6gXhVdQ5V": {
                "id": "selr5zzZ6gXhVdQ5V",
                "name": "Gary Wang",
                "color": "blue"
            },
            "selQA616uWGwZFPhP": {
                "id": "selQA616uWGwZFPhP",
                "name": "Arthur Jen",
                "color": "yellowDarker"
            },
            "selw17OWe06lmMh0d": {
                "id": "selw17OWe06lmMh0d",
                "name": "Jaemin Jin",
                "color": "grayMedium"
            },
            "selywZk5GkdBgU64l": {
                "id": "selywZk5GkdBgU64l",
                "name": "Sean Li",
                "color": "grayDarker"
            },
            "sel6PUSp1vBbVNg8o": {
                "id": "sel6PUSp1vBbVNg8o",
                "name": "Qin Jianxin",
                "color": "blue"
            },
            "selYMt2XF7RGtDbg7": {
                "id": "selYMt2XF7RGtDbg7",
                "name": "Nick Forster",
                "color": "blue"
            },
            "selUU3glQWBDEFyPT": {
                "id": "selUU3glQWBDEFyPT",
                "name": "Potter Li",
                "color": "blue"
            },
            "selJUqfn9EyDOhdRI": {
                "id": "selJUqfn9EyDOhdRI",
                "name": "Jon Lewis",
                "color": "blue"
            },
            "selTSyhQAC3Sxbej1": {
                "id": "selTSyhQAC3Sxbej1",
                "name": "Maciej Bulanda",
                "color": "cyan"
            },
            "selHsmZVDAaWxTKI1": {
                "id": "selHsmZVDAaWxTKI1",
                "name": "Gust Maker",
                "color": "pinkDark"
            },
            "sel37vjWeHGzrOAiH": {
                "id": "sel37vjWeHGzrOAiH",
                "name": "Borja Martel Seward",
                "color": "blue"
            },
            "selyhCDc8FXUohhFO": {
                "id": "selyhCDc8FXUohhFO",
                "name": "Marcelo Cavazzoli",
                "color": "cyan"
            },
            "seljijpzG5yAhbYo1": {
                "id": "seljijpzG5yAhbYo1",
                "name": "Eric Feldman",
                "color": "blue"
            },
            "seludtGrIEMBGZ6OL": {
                "id": "seludtGrIEMBGZ6OL",
                "name": "Garrett Camp",
                "color": "cyan"
            },
            "sel5blv4dgYxJPt5z": {
                "id": "sel5blv4dgYxJPt5z",
                "name": "Ryne Saxe",
                "color": "teal"
            },
            "selaNQYaqvAXlISDn": {
                "id": "selaNQYaqvAXlISDn",
                "name": "Jackie Bona",
                "color": "blue"
            },
            "sel2vssugkvzmA7Qp": {
                "id": "sel2vssugkvzmA7Qp",
                "name": "Jesse Reich",
                "color": "blue"
            },
            "selTLURdPBrRnX7VI": {
                "id": "selTLURdPBrRnX7VI",
                "name": "Leanne Kemp",
                "color": "blue"
            },
            "seldz9Zb13KPPoySh": {
                "id": "seldz9Zb13KPPoySh",
                "name": "George Yu",
                "color": "blue"
            },
            "selfCpQyWkqg4KhuZ": {
                "id": "selfCpQyWkqg4KhuZ",
                "name": "Dylan Macalinao",
                "color": "blue"
            },
            "selo9v206chaSRG4R": {
                "id": "selo9v206chaSRG4R",
                "name": "Andrej Bencic",
                "color": "blue"
            },
            "selJUzm35rbl4jTdx": {
                "id": "selJUzm35rbl4jTdx",
                "name": "Bogdan Habic",
                "color": "cyan"
            },
            "selydKfSMcI87fP2Z": {
                "id": "selydKfSMcI87fP2Z",
                "name": "Miljan Tekic",
                "color": "teal"
            },
            "selWR8yjmtcY9Mf9G": {
                "id": "selWR8yjmtcY9Mf9G",
                "name": "Nebojsa Urosevic",
                "color": "green"
            },
            "selz1JbqKzfKIp2j8": {
                "id": "selz1JbqKzfKIp2j8",
                "name": "Mike Levitt",
                "color": "blue"
            },
            "seloyz4cgevImwp4W": {
                "id": "seloyz4cgevImwp4W",
                "name": "Anand Babu",
                "color": "blue"
            },
            "selx5q0LH6Nic0t7v": {
                "id": "selx5q0LH6Nic0t7v",
                "name": "Mohammed Zakkiria. A",
                "color": "cyan"
            },
            "selCBC9aYLPeJmvpw": {
                "id": "selCBC9aYLPeJmvpw",
                "name": "Raghavendra Viswanathan",
                "color": "teal"
            },
            "selNsVEecwobN4G5N": {
                "id": "selNsVEecwobN4G5N",
                "name": "Raghavendran Viswanathan",
                "color": "green"
            },
            "selEazh3NCSovCByn": {
                "id": "selEazh3NCSovCByn",
                "name": "Adam Small",
                "color": "blue"
            },
            "sellOgtVVWPEu0xkO": {
                "id": "sellOgtVVWPEu0xkO",
                "name": "Doug Pepe",
                "color": "cyan"
            },
            "selO1wcEhXOcQt0v7": {
                "id": "selO1wcEhXOcQt0v7",
                "name": "Charles Adenuoye",
                "color": "blue"
            },
            "selU3Q9m0v1e2nhmv": {
                "id": "selU3Q9m0v1e2nhmv",
                "name": "Victor Ogunshina",
                "color": "cyan"
            },
            "selPdqiKnnr6ok2Ah": {
                "id": "selPdqiKnnr6ok2Ah",
                "name": "Scott Purcell",
                "color": "blue"
            },
            "sel1NVWt9QzOSWsTe": {
                "id": "sel1NVWt9QzOSWsTe",
                "name": "Abdumalik Mirakhmedov",
                "color": "blue"
            },
            "sel1hMGBmFwTubzny": {
                "id": "sel1hMGBmFwTubzny",
                "name": "Doug Petkanics",
                "color": "blue"
            },
            "selFncXivGK1A7Wzm": {
                "id": "selFncXivGK1A7Wzm",
                "name": "Eric Tang",
                "color": "cyan"
            },
            "sell6L6TCcxZ8ZMem": {
                "id": "sell6L6TCcxZ8ZMem",
                "name": "Daniel Racca",
                "color": "blue"
            },
            "selohYWXSWBZhxoah": {
                "id": "selohYWXSWBZhxoah",
                "name": "Ian Ha",
                "color": "cyan"
            },
            "sel6tkzNMbd92NPjP": {
                "id": "sel6tkzNMbd92NPjP",
                "name": "Michael Sanders",
                "color": "teal"
            },
            "selhCHsoCbBuxPLPc": {
                "id": "selhCHsoCbBuxPLPc",
                "name": "William Hua",
                "color": "green"
            },
            "seliaHUQpfvK2g8EL": {
                "id": "seliaHUQpfvK2g8EL",
                "name": "Victor Zhang",
                "color": "blue"
            },
            "sel0XGVj98pjZXSPU": {
                "id": "sel0XGVj98pjZXSPU",
                "name": "Hans Henrik Hoffmeyer .",
                "color": "blue"
            },
            "sela7IJTYLTHt9zYP": {
                "id": "sela7IJTYLTHt9zYP",
                "name": "Kris Henriksen",
                "color": "cyan"
            },
            "sel3IyFI5q4nwK7tL": {
                "id": "sel3IyFI5q4nwK7tL",
                "name": "Lasse Olesen",
                "color": "teal"
            },
            "selU35blsJuxVYN8H": {
                "id": "selU35blsJuxVYN8H",
                "name": "Mark H\u00f8jgaard",
                "color": "green"
            },
            "selZfsElPxdoFDNpL": {
                "id": "selZfsElPxdoFDNpL",
                "name": "Armando Kirwin",
                "color": "blue"
            },
            "sel317sGlThdNj6ZU": {
                "id": "sel317sGlThdNj6ZU",
                "name": "Ryan Horrigan",
                "color": "cyan"
            },
            "sel6fTiXbT53GIqhs": {
                "id": "sel6fTiXbT53GIqhs",
                "name": "Kenton Prescott",
                "color": "blue"
            },
            "selnfVUK9Fs85tm8Y": {
                "id": "selnfVUK9Fs85tm8Y",
                "name": "Dannie Chu",
                "color": "redDark"
            },
            "selC661SnLbXM1TDX": {
                "id": "selC661SnLbXM1TDX",
                "name": "Yash Nelapati",
                "color": "redDark"
            },
            "sel3CdasFmanBa7zq": {
                "id": "sel3CdasFmanBa7zq",
                "name": "Ryoma Ito",
                "color": "orange"
            },
            "selNmXTEK0evmNUWF": {
                "id": "selNmXTEK0evmNUWF",
                "name": "JC Kim",
                "color": "greenDark"
            },
            "selJxiYbfOklSR3jl": {
                "id": "selJxiYbfOklSR3jl",
                "name": "Kijun Seo",
                "color": "pink"
            },
            "selMTTTLDC9QaPNsW": {
                "id": "selMTTTLDC9QaPNsW",
                "name": "Sunny Jain",
                "color": "blue"
            },
            "selWg2O6XaA7XMyF1": {
                "id": "selWg2O6XaA7XMyF1",
                "name": "Tyrone Ross",
                "color": "blue"
            },
            "selOXnr81Gm3yMkpK": {
                "id": "selOXnr81Gm3yMkpK",
                "name": " Eric Ervin",
                "color": "yellowDark"
            },
            "selsc4Hf6RRyCQZdn": {
                "id": "selsc4Hf6RRyCQZdn",
                "name": "Yang He",
                "color": "blue"
            },
            "selMArWnBGLXIQwkS": {
                "id": "selMArWnBGLXIQwkS",
                "name": "Bryan Starbuck",
                "color": "blue"
            },
            "sel6p92PIwce7nBaf": {
                "id": "sel6p92PIwce7nBaf",
                "name": "Drew Nordstrom",
                "color": "cyan"
            },
            "sel0mBoXqU1IS9UuH": {
                "id": "sel0mBoXqU1IS9UuH",
                "name": "Patrick Larsen",
                "color": "teal"
            },
            "seloyTX8Bect5O11z": {
                "id": "seloyTX8Bect5O11z",
                "name": "Saqib Rasool",
                "color": "green"
            },
            "seloXnoBlPM2dhMCr": {
                "id": "seloXnoBlPM2dhMCr",
                "name": "Daniel Berz",
                "color": "blue"
            },
            "selnJlWBJKE35SRhi": {
                "id": "selnJlWBJKE35SRhi",
                "name": "Luis Daniel Odon",
                "color": "cyan"
            },
            "seldKG51dT3cKiLtl": {
                "id": "seldKG51dT3cKiLtl",
                "name": "Aleksandar Kuzmanovic",
                "color": "blue"
            },
            "seljoPDdRH4XheDgd": {
                "id": "seljoPDdRH4XheDgd",
                "name": "Emin G\u00fcn Sirer",
                "color": "cyan"
            },
            "selU1LxKUJznv8vi3": {
                "id": "selU1LxKUJznv8vi3",
                "name": "Soumya Basu",
                "color": "teal"
            },
            "sel92aSP05eS5XPjz": {
                "id": "sel92aSP05eS5XPjz",
                "name": "Uri Klarman",
                "color": "green"
            },
            "selDuStyA2iXLl3xZ": {
                "id": "selDuStyA2iXLl3xZ",
                "name": "Inga Mullins",
                "color": "blue"
            },
            "sellfloNI5acbjlp1": {
                "id": "sellfloNI5acbjlp1",
                "name": "Bach Adylbekov",
                "color": "blue"
            },
            "sel1tBfofWTar6Yxr": {
                "id": "sel1tBfofWTar6Yxr",
                "name": "Masakazu Kikuchi",
                "color": "cyan"
            },
            "selstVbDfxFUG2HGc": {
                "id": "selstVbDfxFUG2HGc",
                "name": "Mark Blick",
                "color": "blue"
            },
            "sel9GQtaBbKyj62ph": {
                "id": "sel9GQtaBbKyj62ph",
                "name": "Sishir Varghese",
                "color": "blue"
            },
            "selw74p2gnFjIgSd0": {
                "id": "selw74p2gnFjIgSd0",
                "name": "David Kim",
                "color": "blue"
            },
            "selsMbkat7zryKuds": {
                "id": "selsMbkat7zryKuds",
                "name": "Rex Hygate",
                "color": "redDarker"
            },
            "selZuwuzLekiuaIK1": {
                "id": "selZuwuzLekiuaIK1",
                "name": "Thessy Mehrain",
                "color": "blue"
            },
            "sel9RWJxbg8oyu19A": {
                "id": "sel9RWJxbg8oyu19A",
                "name": "David Bisang",
                "color": "blue"
            },
            "selBdNYdyKHNlQ229": {
                "id": "selBdNYdyKHNlQ229",
                "name": "Frank Hartmann",
                "color": "cyan"
            },
            "sel4N6YFvCTMaZwKt": {
                "id": "sel4N6YFvCTMaZwKt",
                "name": "Philipp Toth",
                "color": "teal"
            },
            "selZQY4fyA7xmVaju": {
                "id": "selZQY4fyA7xmVaju",
                "name": "Rob Viglione",
                "color": "blue"
            },
            "selSygzfvDk4q6igA": {
                "id": "selSygzfvDk4q6igA",
                "name": "Leonard Tan",
                "color": "blue"
            },
            "sel0VwA3IWaDV8R4k": {
                "id": "sel0VwA3IWaDV8R4k",
                "name": "Zen Yong",
                "color": "cyan"
            },
            "selaCZ1znlxrOf0zM": {
                "id": "selaCZ1znlxrOf0zM",
                "name": "David Garai",
                "color": "grayDarker"
            },
            "sel4xVqqpBKGtnAW1": {
                "id": "sel4xVqqpBKGtnAW1",
                "name": "Norbert Nopper",
                "color": "blue"
            },
            "selu9xUGQuPKw1GBC": {
                "id": "selu9xUGQuPKw1GBC",
                "name": "Thomas Kress",
                "color": "cyan"
            },
            "selZMAh8c8u8uD6ig": {
                "id": "selZMAh8c8u8uD6ig",
                "name": "Mohammed Roshan",
                "color": "blue"
            },
            "selVICxfyqkfQDcAA": {
                "id": "selVICxfyqkfQDcAA",
                "name": "Roshni Aslam",
                "color": "cyan"
            },
            "selZhxA4svV9evIEw": {
                "id": "selZhxA4svV9evIEw",
                "name": "Ling Wu",
                "color": "blue"
            },
            "selvakiAhWRTOdwZS": {
                "id": "selvakiAhWRTOdwZS",
                "name": "Hrish Lotlikar",
                "color": "blue"
            },
            "selzpxtwLDYLcOi8P": {
                "id": "selzpxtwLDYLcOi8P",
                "name": "Max Woon",
                "color": "cyan"
            },
            "selyDUkRskb42WjxW": {
                "id": "selyDUkRskb42WjxW",
                "name": "Gabriel Gruber",
                "color": "blue"
            },
            "selg4agIaIUFlAYAE": {
                "id": "selg4agIaIUFlAYAE",
                "name": "Lucas Lain",
                "color": "greenDarker"
            },
            "selG5zhX982VLawKQ": {
                "id": "selG5zhX982VLawKQ",
                "name": "Arif Khan",
                "color": "blue"
            },
            "selxtVuK6KnXqxx3t": {
                "id": "selxtVuK6KnXqxx3t",
                "name": "Patrick White",
                "color": "blue"
            },
            "sel7Or4OhH5462Y0x": {
                "id": "sel7Or4OhH5462Y0x",
                "name": "Philipp Banhardt",
                "color": "blue"
            },
            "selfKy5QAv1Ko9iu1": {
                "id": "selfKy5QAv1Ko9iu1",
                "name": "Markus Maier",
                "color": "greenMedium"
            },
            "sel1M2IKyOhJMWCuZ": {
                "id": "sel1M2IKyOhJMWCuZ",
                "name": "Dare Odumade",
                "color": "blue"
            },
            "selaSD6k2jC17RtQt": {
                "id": "selaSD6k2jC17RtQt",
                "name": "Oluwatosin Adelowo",
                "color": "cyan"
            },
            "selO3CT5W08hH4bTj": {
                "id": "selO3CT5W08hH4bTj",
                "name": "Samuel Ukhueleigbe",
                "color": "teal"
            },
            "selFsohEoKGSYBBTj": {
                "id": "selFsohEoKGSYBBTj",
                "name": "John RobertsonView John Robertson\u2019s profile",
                "color": "blue"
            },
            "selJb9kcJmd2bCZBc": {
                "id": "selJb9kcJmd2bCZBc",
                "name": "Alankar Saxena",
                "color": "blue"
            },
            "selEgrWsS2JZZ0Ws5": {
                "id": "selEgrWsS2JZZ0Ws5",
                "name": "Edul Patel",
                "color": "cyan"
            },
            "selVO2bqA8s8KHNtb": {
                "id": "selVO2bqA8s8KHNtb",
                "name": "Prince Arora",
                "color": "teal"
            },
            "sel1lqlrASn3KSa8T": {
                "id": "sel1lqlrASn3KSa8T",
                "name": "Rohit Goyal",
                "color": "green"
            },
            "selkRZxJVNzrCgMd0": {
                "id": "selkRZxJVNzrCgMd0",
                "name": "Snehil Buxy",
                "color": "yellow"
            },
            "sel8M7xfYojwXGzf0": {
                "id": "sel8M7xfYojwXGzf0",
                "name": "Bernhard BlahaView Bernhard Blaha\u2019s profile",
                "color": "blue"
            },
            "selyt91piFmpeGfRl": {
                "id": "selyt91piFmpeGfRl",
                "name": "Lloyd Lee",
                "color": "blue"
            },
            "selxfFUUq0e3SeFh0": {
                "id": "selxfFUUq0e3SeFh0",
                "name": "Sangrok Oh",
                "color": "cyan"
            },
            "selpEq8I8ukQerPo2": {
                "id": "selpEq8I8ukQerPo2",
                "name": "Woojin Kim",
                "color": "teal"
            },
            "selBmQJ9Ql53wq2Cv": {
                "id": "selBmQJ9Ql53wq2Cv",
                "name": "Bernie Moreno",
                "color": "blue"
            },
            "selmx5o4NkF35FZsd": {
                "id": "selmx5o4NkF35FZsd",
                "name": "Shane McRann Bigelow",
                "color": "cyan"
            },
            "selCmxSe9UZpo5Xds": {
                "id": "selCmxSe9UZpo5Xds",
                "name": "Nichel Gaba",
                "color": "blue"
            },
            "selpKg85sTxmuqh6r": {
                "id": "selpKg85sTxmuqh6r",
                "name": "Travis Wu",
                "color": "orange"
            },
            "selkRe1FOKThOXxeZ": {
                "id": "selkRe1FOKThOXxeZ",
                "name": "Simon Harman",
                "color": "blue"
            },
            "selYvH6QjWbOUSaFA": {
                "id": "selYvH6QjWbOUSaFA",
                "name": "Nathan Allman",
                "color": "blue"
            },
            "selnO9sfJDRyDuUet": {
                "id": "selnO9sfJDRyDuUet",
                "name": "Michael McKain",
                "color": "blue"
            },
            "sel4zgCRdOdVFfH22": {
                "id": "sel4zgCRdOdVFfH22",
                "name": "Shant Marootian",
                "color": "blue"
            },
            "selXP1TqEFOgIruZY": {
                "id": "selXP1TqEFOgIruZY",
                "name": "Denis Lam",
                "color": "blue"
            },
            "selPTRID33vwCyCX1": {
                "id": "selPTRID33vwCyCX1",
                "name": "Colton Dillion",
                "color": "blue"
            },
            "selO6HfISvPT09U88": {
                "id": "selO6HfISvPT09U88",
                "name": "Taylor Culbertson",
                "color": "yellowMedium"
            },
            "sel1jrDcm8ZfWZMXR": {
                "id": "sel1jrDcm8ZfWZMXR",
                "name": "Alan John",
                "color": "blue"
            },
            "selrzY29bFduCW1aN": {
                "id": "selrzY29bFduCW1aN",
                "name": "3LAU",
                "color": "pinkMedium"
            },
            "selkhAVAAgvotgspw": {
                "id": "selkhAVAAgvotgspw",
                "name": "JD Ross",
                "color": "grayDark"
            },
            "selUu9rEcQhh9Rtph": {
                "id": "selUu9rEcQhh9Rtph",
                "name": "Gabriel Dymowski",
                "color": "blue"
            },
            "selGpd1JA8Cs61suX": {
                "id": "selGpd1JA8Cs61suX",
                "name": "Marcin Lorenc",
                "color": "cyan"
            },
            "selDhBscbQ4xZoj2C": {
                "id": "selDhBscbQ4xZoj2C",
                "name": "Justin Amos",
                "color": "blue"
            },
            "selXbHCjvJAFNhLdF": {
                "id": "selXbHCjvJAFNhLdF",
                "name": "Paul Fan",
                "color": "blue"
            },
            "selfaClHbvL9wKGTQ": {
                "id": "selfaClHbvL9wKGTQ",
                "name": "Andy Chorlian",
                "color": "blue"
            },
            "selLdOaBHa0NxdRmQ": {
                "id": "selLdOaBHa0NxdRmQ",
                "name": "Bridge Craven",
                "color": "blue"
            },
            "selrDPzAzYrJeLa6m": {
                "id": "selrDPzAzYrJeLa6m",
                "name": "Joshua Meng",
                "color": "blue"
            },
            "seldqCho6ODF4wPjZ": {
                "id": "seldqCho6ODF4wPjZ",
                "name": "Mark Dao",
                "color": "yellowMedium"
            },
            "selDWMc5qIOJdOkXI": {
                "id": "selDWMc5qIOJdOkXI",
                "name": "Victor Truong",
                "color": "orange"
            },
            "selizNn4ZO8y6Jkzw": {
                "id": "selizNn4ZO8y6Jkzw",
                "name": "Bruce Chau",
                "color": "blue"
            },
            "seloQv02LnMyUE4Bo": {
                "id": "seloQv02LnMyUE4Bo",
                "name": "Vansa Chatikavanij",
                "color": "blue"
            },
            "seljKFcuPlZ6dnLh3": {
                "id": "seljKFcuPlZ6dnLh3",
                "name": "Thibault Launay",
                "color": "blue"
            },
            "selHnXo18jVmdn5eE": {
                "id": "selHnXo18jVmdn5eE",
                "name": "Romain Girbal",
                "color": "teal"
            },
            "selcHADcfnHB4katY": {
                "id": "selcHADcfnHB4katY",
                "name": "Mike Phulsuksombati",
                "color": "blue"
            },
            "sel7RUiDiNgY1t5l7": {
                "id": "sel7RUiDiNgY1t5l7",
                "name": "Juthica Chou",
                "color": "blue"
            },
            "sela2k2YH4qMOUbKL": {
                "id": "sela2k2YH4qMOUbKL",
                "name": "Paul Chau",
                "color": "cyan"
            },
            "selITvzCsAFQ9Feec": {
                "id": "selITvzCsAFQ9Feec",
                "name": "Paul L Chou",
                "color": "teal"
            },
            "selt2OIEwvcfgDMOl": {
                "id": "selt2OIEwvcfgDMOl",
                "name": "Zach Dexter",
                "color": "green"
            },
            "selTVCP12kNf9p7NE": {
                "id": "selTVCP12kNf9p7NE",
                "name": "Shane Mac",
                "color": "blue"
            },
            "seljMDYJ92agS9NTN": {
                "id": "seljMDYJ92agS9NTN",
                "name": "Matt Galligan",
                "color": "redMedium"
            },
            "seldMl38vV7E3Rkxp": {
                "id": "seldMl38vV7E3Rkxp",
                "name": "Ed Felten",
                "color": "blue"
            },
            "selgVd8T7V9EKzQJm": {
                "id": "selgVd8T7V9EKzQJm",
                "name": "Harry Kalodner",
                "color": "cyan"
            },
            "selbd9BQgoh587Cf2": {
                "id": "selbd9BQgoh587Cf2",
                "name": "Steven Goldfeder",
                "color": "teal"
            },
            "selFfWxN3YUeQBUWy": {
                "id": "selFfWxN3YUeQBUWy",
                "name": "Bryan Young",
                "color": "blue"
            },
            "selqITfGs7ysTVvNz": {
                "id": "selqITfGs7ysTVvNz",
                "name": "Steven Better",
                "color": "cyan"
            },
            "selPswMjFNkGLdLVP": {
                "id": "selPswMjFNkGLdLVP",
                "name": "Tim Roberson",
                "color": "teal"
            },
            "selpvfvotGK5Vw1xb": {
                "id": "selpvfvotGK5Vw1xb",
                "name": "Adrian Garcia",
                "color": "blue"
            },
            "selvfCvSDUvMF5iRe": {
                "id": "selvfCvSDUvMF5iRe",
                "name": "Christian Rodriguez",
                "color": "cyan"
            },
            "selceu8yID5O85m6M": {
                "id": "selceu8yID5O85m6M",
                "name": "Nico Torteli",
                "color": "teal"
            },
            "selJMPWEcfafYn3AD": {
                "id": "selJMPWEcfafYn3AD",
                "name": "Tim Retkoceri",
                "color": "blue"
            },
            "selfxUgEqCxjmdBYq": {
                "id": "selfxUgEqCxjmdBYq",
                "name": "Mario Gomez Lozada",
                "color": "blue"
            },
            "sel9zxO6HBo1cfH4Z": {
                "id": "sel9zxO6HBo1cfH4Z",
                "name": "Mike Kayamori",
                "color": "cyan"
            },
            "selzSle1g2jApLnDB": {
                "id": "selzSle1g2jApLnDB",
                "name": "Tanaka Masaaki",
                "color": "teal"
            },
            "sel8eZM5qIj86D4Gd": {
                "id": "sel8eZM5qIj86D4Gd",
                "name": "Matt Aaron",
                "color": "blue"
            },
            "seltIBcfszPW4NUUS": {
                "id": "seltIBcfszPW4NUUS",
                "name": "Temur Mirzosharipov",
                "color": "pinkMedium"
            },
            "selrdFvjxNDYUzvP4": {
                "id": "selrdFvjxNDYUzvP4",
                "name": "Scott Lewis",
                "color": "grayMedium"
            },
            "sel5MnrhfyFtxONxG": {
                "id": "sel5MnrhfyFtxONxG",
                "name": "Supriyo Roy",
                "color": "green"
            },
            "sel0XAVjh8T5mCdcF": {
                "id": "sel0XAVjh8T5mCdcF",
                "name": "Alex Batlin",
                "color": "blue"
            },
            "sel588WgirULbjJNj": {
                "id": "sel588WgirULbjJNj",
                "name": "Martin Jofre Celis",
                "color": "blue"
            },
            "selNNlkRj6jxIcaPY": {
                "id": "selNNlkRj6jxIcaPY",
                "name": "Rafael Meruane",
                "color": "cyan"
            },
            "selNJhVIurhIzMEsy": {
                "id": "selNJhVIurhIzMEsy",
                "name": "Arie Levy- Cohen",
                "color": "blue"
            },
            "sel31MrFsuoYuhQrM": {
                "id": "sel31MrFsuoYuhQrM",
                "name": "Abraham Milano",
                "color": "blue"
            },
            "selCRZHpwFygeclet": {
                "id": "selCRZHpwFygeclet",
                "name": "Beatriz Helena Ramos",
                "color": "cyan"
            },
            "selP901mMcfbtzq7C": {
                "id": "selP901mMcfbtzq7C",
                "name": "Yehudit Mam",
                "color": "teal"
            },
            "selc4Cu6uU0WgLRJ4": {
                "id": "selc4Cu6uU0WgLRJ4",
                "name": "David Casey",
                "color": "blue"
            },
            "sel0iVj2VOS9BlM6c": {
                "id": "sel0iVj2VOS9BlM6c",
                "name": "Liko Subakti",
                "color": "blue"
            },
            "sel2TA2Ln7oFEixnc": {
                "id": "sel2TA2Ln7oFEixnc",
                "name": "Adam Gagol",
                "color": "blue"
            },
            "sel45QnoFVPKebhXE": {
                "id": "sel45QnoFVPKebhXE",
                "name": "Antoni Zolciak",
                "color": "cyan"
            },
            "selIUIl9UddLYWozj": {
                "id": "selIUIl9UddLYWozj",
                "name": "Matthew Niemerg",
                "color": "teal"
            },
            "selXAuHIznEf5bbG4": {
                "id": "selXAuHIznEf5bbG4",
                "name": "Michal Swietek",
                "color": "green"
            },
            "selcXJBmxk6mliYQA": {
                "id": "selcXJBmxk6mliYQA",
                "name": "Kento ",
                "color": "pinkDarker"
            },
            "selvbDqKQsUVG3vJN": {
                "id": "selvbDqKQsUVG3vJN",
                "name": "0xMurloc",
                "color": "tealMedium"
            },
            "selIF2p5C9xbdQTiL": {
                "id": "selIF2p5C9xbdQTiL",
                "name": "Cryptofish",
                "color": "tealDark"
            },
            "selbqaB0ya0K13Evh": {
                "id": "selbqaB0ya0K13Evh",
                "name": "Maxime Hagenbourger",
                "color": "redMedium"
            },
            "selspr5ciDjCRqjSv": {
                "id": "selspr5ciDjCRqjSv",
                "name": "Sandeep Nailwal",
                "color": "tealDarker"
            },
            "seldxUJTPFsOAwTZr": {
                "id": "seldxUJTPFsOAwTZr",
                "name": "Anubhav Girdhar ",
                "color": "gray"
            },
            "selVUtHmTmDNxXsMX": {
                "id": "selVUtHmTmDNxXsMX",
                "name": "Hosam Mazawi",
                "color": "blue"
            },
            "selcAi4eYW8OWV75R": {
                "id": "selcAi4eYW8OWV75R",
                "name": "Jeffrey Carter",
                "color": "blue"
            },
            "selMxsaCqwJYnNunT": {
                "id": "selMxsaCqwJYnNunT",
                "name": "Mayank Tewari",
                "color": "blue"
            },
            "selB2yvnzXMED5AeB": {
                "id": "selB2yvnzXMED5AeB",
                "name": "Prerit Srivastava",
                "color": "cyan"
            },
            "selPXM4bLFjl407EI": {
                "id": "selPXM4bLFjl407EI",
                "name": "Aaron Penn",
                "color": "blue"
            },
            "selblv4bxieYqQFOS": {
                "id": "selblv4bxieYqQFOS",
                "name": "Alexander Valtingojer",
                "color": "cyan"
            },
            "selM89EMPAEp58ucA": {
                "id": "selM89EMPAEp58ucA",
                "name": "Matthias Zandanel",
                "color": "teal"
            },
            "sel6S8B5aCAUimuwV": {
                "id": "sel6S8B5aCAUimuwV",
                "name": "Saad J. Wohlgenannt",
                "color": "green"
            },
            "sel1yRR0bhI2fqbAy": {
                "id": "sel1yRR0bhI2fqbAy",
                "name": "Jackson Wong",
                "color": "blueDark"
            },
            "selIz934bc1I2m6rd": {
                "id": "selIz934bc1I2m6rd",
                "name": "Saravanan Jaichandaran",
                "color": "blue"
            },
            "seljR2RQxHM7CMhjj": {
                "id": "seljR2RQxHM7CMhjj",
                "name": "Phil Mataras",
                "color": "blue"
            },
            "selwRas1GuyxL4BGe": {
                "id": "selwRas1GuyxL4BGe",
                "name": "Mitrasish Mukherjee",
                "color": "blue"
            },
            "selHjxgpziSbBN2Tz": {
                "id": "selHjxgpziSbBN2Tz",
                "name": "Alex Smirnov",
                "color": "blue"
            },
            "selYIbYAUqnREfszt": {
                "id": "selYIbYAUqnREfszt",
                "name": "Gene Wu",
                "color": "blue"
            },
            "selmpgAmnqk5ymW1U": {
                "id": "selmpgAmnqk5ymW1U",
                "name": "Raymond Hsu",
                "color": "cyan"
            },
            "selH7IwMFYrUpUORz": {
                "id": "selH7IwMFYrUpUORz",
                "name": "Sreekanth Kalapur",
                "color": "blue"
            },
            "selY0BMP6sUr2UGc7": {
                "id": "selY0BMP6sUr2UGc7",
                "name": "Duke McKenzie",
                "color": "blue"
            },
            "selW0wFOKaFdwOg3a": {
                "id": "selW0wFOKaFdwOg3a",
                "name": "Ryan Li",
                "color": "cyan"
            },
            "selzLtwe11lrcD3KU": {
                "id": "selzLtwe11lrcD3KU",
                "name": "Shiyu Zhang",
                "color": "teal"
            },
            "selYyzMij3fS4vFDX": {
                "id": "selYyzMij3fS4vFDX",
                "name": "Wilson Wei",
                "color": "green"
            },
            "selRXBeoH8M5SH8KD": {
                "id": "selRXBeoH8M5SH8KD",
                "name": "Zhimao Liu",
                "color": "yellow"
            },
            "selhX37RmEElJvYrg": {
                "id": "selhX37RmEElJvYrg",
                "name": "Abhyudoy Das",
                "color": "blue"
            },
            "sel3fY7TnCfteSjPD": {
                "id": "sel3fY7TnCfteSjPD",
                "name": "krishna yogi",
                "color": "cyan"
            },
            "seluSUGpr3RgaodNr": {
                "id": "seluSUGpr3RgaodNr",
                "name": "Chris Piatt",
                "color": "blueDarker"
            },
            "selopBiMoRfWOTv98": {
                "id": "selopBiMoRfWOTv98",
                "name": "Jeffrey Quesnelle",
                "color": "orangeDarker"
            },
            "selVZhnlnv9h8GwIP": {
                "id": "selVZhnlnv9h8GwIP",
                "name": "Caleb Sheridan",
                "color": "orangeDarker"
            },
            "selY9ka1gswpUwPEG": {
                "id": "selY9ka1gswpUwPEG",
                "name": "Nika Oniani",
                "color": "blue"
            },
            "selTZp3hvv4iQrg0i": {
                "id": "selTZp3hvv4iQrg0i",
                "name": "John Bisu",
                "color": "orangeMedium"
            },
            "sel5Rr2bCop4ptYKe": {
                "id": "sel5Rr2bCop4ptYKe",
                "name": "Sean Kiernan",
                "color": "blue"
            },
            "selO2rVE7Xcoj4If1": {
                "id": "selO2rVE7Xcoj4If1",
                "name": "Mian Mohsin Masud",
                "color": "blue"
            },
            "selH1NpNA9nVmnYMO": {
                "id": "selH1NpNA9nVmnYMO",
                "name": "H\u00e9lder Vasconcelos",
                "color": "blue"
            },
            "selexlbbL5wfhxrmk": {
                "id": "selexlbbL5wfhxrmk",
                "name": "M\u00e1rio Ribeiro Alves",
                "color": "cyan"
            },
            "selDWrbMKW25ghE6h": {
                "id": "selDWrbMKW25ghE6h",
                "name": "Andrei Manuel",
                "color": "blue"
            },
            "sel9pbTArj5Lj5zX1": {
                "id": "sel9pbTArj5Lj5zX1",
                "name": "Leif Ferreira",
                "color": "cyan"
            },
            "selpejkSeBvzZkwP8": {
                "id": "selpejkSeBvzZkwP8",
                "name": "Zhivko Todorov",
                "color": "blue"
            },
            "selXHaO0f6H08RL9V": {
                "id": "selXHaO0f6H08RL9V",
                "name": "Luiz DT",
                "color": "cyan"
            },
            "seltkzVXP0uYh8v0K": {
                "id": "seltkzVXP0uYh8v0K",
                "name": " John Paller",
                "color": "tealDark"
            },
            "selpZX5iy5tQi9vgw": {
                "id": "selpZX5iy5tQi9vgw",
                "name": "Aldo Carrascoso",
                "color": "blue"
            },
            "seluK3L7b9EFxfsNj": {
                "id": "seluK3L7b9EFxfsNj",
                "name": "Marwan Forzley",
                "color": "cyan"
            },
            "seligRBPSkNv2i0OI": {
                "id": "seligRBPSkNv2i0OI",
                "name": "Minh Do",
                "color": "blue"
            },
            "selUSkj1iqKhPzvl1": {
                "id": "selUSkj1iqKhPzvl1",
                "name": "Darshan Vaidya",
                "color": "blue"
            },
            "selpSTkBfUD7cWuim": {
                "id": "selpSTkBfUD7cWuim",
                "name": "James Ferguson",
                "color": "blue"
            },
            "selF4BZSHhS1e3zKk": {
                "id": "selF4BZSHhS1e3zKk",
                "name": "Robbie Ferguson",
                "color": "cyan"
            },
            "selUttnqsMp7DFA8s": {
                "id": "selUttnqsMp7DFA8s",
                "name": "Shawn Douglass",
                "color": "blue"
            },
            "selCvumWCMRBhLTt7": {
                "id": "selCvumWCMRBhLTt7",
                "name": "Nils Pihl",
                "color": "blue"
            },
            "selGlqoxmjqIUKYEQ": {
                "id": "selGlqoxmjqIUKYEQ",
                "name": "Charlie Rhee",
                "color": "blue"
            },
            "selfHcyzeNnOxxOEq": {
                "id": "selfHcyzeNnOxxOEq",
                "name": "Guy Phipps",
                "color": "blue"
            },
            "selJRtoXUR51hsRvS": {
                "id": "selJRtoXUR51hsRvS",
                "name": "Dana Panzer",
                "color": "blue"
            },
            "selCsNLI1FJSgWgI8": {
                "id": "selCsNLI1FJSgWgI8",
                "name": "Hossein Azari",
                "color": "cyan"
            },
            "sell3fqvJ7spwxsRu": {
                "id": "sell3fqvJ7spwxsRu",
                "name": "Wenjun Gui",
                "color": "teal"
            },
            "selQCyjAFY1U9zjRd": {
                "id": "selQCyjAFY1U9zjRd",
                "name": "Duke Vu",
                "color": "blue"
            },
            "selaKifFmlFDDefvO": {
                "id": "selaKifFmlFDDefvO",
                "name": "Akinbode Ademola Bamgboye",
                "color": "blue"
            },
            "selXW6VB8li0yvl9l": {
                "id": "selXW6VB8li0yvl9l",
                "name": "Alberto Rodriguez Fernandez",
                "color": "cyan"
            },
            "selHFQsQtF86PSbYv": {
                "id": "selHFQsQtF86PSbYv",
                "name": "Ataberk \u00c7a\u015fur",
                "color": "blue"
            },
            "sele8I9golUMrsm3R": {
                "id": "sele8I9golUMrsm3R",
                "name": "Arseny Akinfiev",
                "color": "blue"
            },
            "seldCRnYthdBCg8eA": {
                "id": "seldCRnYthdBCg8eA",
                "name": "Bill Barhydt",
                "color": "tealMedium"
            },
            "selJl1rXtcUkfvHVG": {
                "id": "selJl1rXtcUkfvHVG",
                "name": "Canaan Linder",
                "color": "cyanDarker"
            },
            "selWw05H3BapFOkal": {
                "id": "selWw05H3BapFOkal",
                "name": "Adrian Kolody.",
                "color": "blue"
            },
            "selXy8kEEkQbLmo2u": {
                "id": "selXy8kEEkQbLmo2u",
                "name": "Michal Cymbalisty",
                "color": "orangeMedium"
            },
            "selILzNkUVIT9IoyE": {
                "id": "selILzNkUVIT9IoyE",
                "name": "Vincenzo Lee",
                "color": "pink"
            },
            "selIIaHBvxcxA9Cd0": {
                "id": "selIIaHBvxcxA9Cd0",
                "name": "Joey DeBruin",
                "color": "blue"
            },
            "seleGskpCA2CZ9Dd4": {
                "id": "seleGskpCA2CZ9Dd4",
                "name": "Carlos Gomes",
                "color": "grayDark"
            },
            "selk8Zx3rIYihQ7L7": {
                "id": "selk8Zx3rIYihQ7L7",
                "name": "Ryan Zarick",
                "color": "blue"
            },
            "selqEKbXAEoKArdZQ": {
                "id": "selqEKbXAEoKArdZQ",
                "name": "Josh Rogers",
                "color": "blue"
            },
            "selSI73RJ8NPoOUfV": {
                "id": "selSI73RJ8NPoOUfV",
                "name": "Ruyi Ren",
                "color": "blue"
            },
            "selF2sGvGOilERVAP": {
                "id": "selF2sGvGOilERVAP",
                "name": "Quyet Huynh",
                "color": "blue"
            },
            "selWdNcsBfGvhOJh8": {
                "id": "selWdNcsBfGvhOJh8",
                "name": "Quang Nguyen",
                "color": "blue"
            },
            "selwFumsp44seu9it": {
                "id": "selwFumsp44seu9it",
                "name": "Getty Hill",
                "color": "blue"
            },
            "selA0h3C3JEuoCkzU": {
                "id": "selA0h3C3JEuoCkzU",
                "name": "Bulent Tekmen",
                "color": "blue"
            },
            "selDMrAs3dccFafBN": {
                "id": "selDMrAs3dccFafBN",
                "name": "Eray Eren",
                "color": "cyan"
            },
            "selYKsmz1cDxkJNu2": {
                "id": "selYKsmz1cDxkJNu2",
                "name": "Mihriban Ersin Tekmen",
                "color": "teal"
            },
            "sel5YwTNUTpp4au3P": {
                "id": "sel5YwTNUTpp4au3P",
                "name": "Serkan Omerbeyoglu",
                "color": "green"
            },
            "selavqLDA91oPiHIB": {
                "id": "selavqLDA91oPiHIB",
                "name": "Matteo Panzavolta",
                "color": "blue"
            },
            "sellmFxyCF8cco9lg": {
                "id": "sellmFxyCF8cco9lg",
                "name": "Nicola Fantini",
                "color": "cyan"
            },
            "selLNRR8j6rTAi8NJ": {
                "id": "selLNRR8j6rTAi8NJ",
                "name": "Shahzaib Ali",
                "color": "blue"
            },
            "selgfMWjRDyk5NFxl": {
                "id": "selgfMWjRDyk5NFxl",
                "name": "Nicholas Adams",
                "color": "blue"
            },
            "selKVrGHZ3jy2IWdp": {
                "id": "selKVrGHZ3jy2IWdp",
                "name": "Gary Loh",
                "color": "blue"
            },
            "sel8QWAmlveW4hk4H": {
                "id": "sel8QWAmlveW4hk4H",
                "name": "Thomas Scaria",
                "color": "yellow"
            },
            "selW8hUAJdSFxabSn": {
                "id": "selW8hUAJdSFxabSn",
                "name": "Shelby Thomas",
                "color": "yellow"
            },
            "selJdGMu5fV2KSaoK": {
                "id": "selJdGMu5fV2KSaoK",
                "name": "Artem Wright",
                "color": "blue"
            },
            "selNGVEoLuDWiWfsc": {
                "id": "selNGVEoLuDWiWfsc",
                "name": "Mateen Motavaf",
                "color": "yellowDarker"
            },
            "selzuRuzc2AvK4aIu": {
                "id": "selzuRuzc2AvK4aIu",
                "name": "William Birks",
                "color": "blue"
            },
            "selk6klNNiEnCjmhZ": {
                "id": "selk6klNNiEnCjmhZ",
                "name": "Sylvan Doyle",
                "color": "yellowMedium"
            },
            "sel3vRYt2i5cmD1Yo": {
                "id": "sel3vRYt2i5cmD1Yo",
                "name": "Nikos Andrikogiannopoulos",
                "color": "blue"
            },
            "selpfVVXAi9peEefA": {
                "id": "selpfVVXAi9peEefA",
                "name": "Obie Fernandez",
                "color": "blue"
            },
            "selnaUPxHmgkpKhwO": {
                "id": "selnaUPxHmgkpKhwO",
                "name": "Francesco Simoneschi",
                "color": "blue"
            },
            "selbrJ0KCZrV0QnVn": {
                "id": "selbrJ0KCZrV0QnVn",
                "name": "Luca Martinetti",
                "color": "cyan"
            },
            "selqjf8CMRxQk758P": {
                "id": "selqjf8CMRxQk758P",
                "name": "Eric Peters",
                "color": "blue"
            },
            "selht4D4OW1TxjLmm": {
                "id": "selht4D4OW1TxjLmm",
                "name": "Eric Martindale",
                "color": "blue"
            },
            "sel77l7cSxXIYBWNz": {
                "id": "sel77l7cSxXIYBWNz",
                "name": "Manoj Duggirala",
                "color": "redDarker"
            },
            "selrpgP81aZGoYAFw": {
                "id": "selrpgP81aZGoYAFw",
                "name": "Luciana Gruszeczka",
                "color": "blue"
            },
            "selaL9MjqH3YcNLck": {
                "id": "selaL9MjqH3YcNLck",
                "name": "Mugur Marculescu",
                "color": "cyan"
            },
            "selcDQ8nVylhajR5y": {
                "id": "selcDQ8nVylhajR5y",
                "name": "Sebastian Serrano",
                "color": "teal"
            },
            "selyn7x1VQcTLl45o": {
                "id": "selyn7x1VQcTLl45o",
                "name": "Discus Fish",
                "color": "orangeDarker"
            },
            "selh3ULUGiApF6J8m": {
                "id": "selh3ULUGiApF6J8m",
                "name": "Changhao Jiang",
                "color": "tealDarker"
            },
            "selNhewF2iy2bpdn1": {
                "id": "selNhewF2iy2bpdn1",
                "name": "Yutaro Mori",
                "color": "blue"
            },
            "seleZLrubBRcOMNQB": {
                "id": "seleZLrubBRcOMNQB",
                "name": "Grace \u201cOri\u201d Kwan",
                "color": "yellowDarker"
            },
            "selU6htGFseg3wJAz": {
                "id": "selU6htGFseg3wJAz",
                "name": "Angel Xu",
                "color": "blue"
            },
            "selJeSOo7aveov488": {
                "id": "selJeSOo7aveov488",
                "name": "Max Galka",
                "color": "red"
            },
            "selP4TsryCqSokn2f": {
                "id": "selP4TsryCqSokn2f",
                "name": "Mike Kalomeni",
                "color": "pinkDarker"
            },
            "seluTIUfQKC4dehEs": {
                "id": "seluTIUfQKC4dehEs",
                "name": "Nuria Gutierrez",
                "color": "redDark"
            },
            "selYMz4L3dfbFA5pN": {
                "id": "selYMz4L3dfbFA5pN",
                "name": "Dean Pappas",
                "color": "blue"
            },
            "sel6YziGAazDz2eVP": {
                "id": "sel6YziGAazDz2eVP",
                "name": "Julian Vasil",
                "color": "blue"
            },
            "selQLP0azEA0lAQWN": {
                "id": "selQLP0azEA0lAQWN",
                "name": "Ankur Banerjee",
                "color": "blue"
            },
            "selJJPDN3E4R0VB0s": {
                "id": "selJJPDN3E4R0VB0s",
                "name": "Fraser Edwards",
                "color": "cyan"
            },
            "selPRXQOXF4T5onwE": {
                "id": "selPRXQOXF4T5onwE",
                "name": "Niky Achivei",
                "color": "blue"
            },
            "sel5RK3OPynp23GC1": {
                "id": "sel5RK3OPynp23GC1",
                "name": "Anshum Bhambri",
                "color": "blue"
            },
            "selWcgAqrfctdSd2h": {
                "id": "selWcgAqrfctdSd2h",
                "name": "Kushagra Kohli",
                "color": "cyan"
            },
            "selRHigCIXEL8tpM3": {
                "id": "selRHigCIXEL8tpM3",
                "name": "Joseph Liu",
                "color": "purpleMedium"
            },
            "sel2ZOhnmscgIAcXp": {
                "id": "sel2ZOhnmscgIAcXp",
                "name": "Reza Naeeni",
                "color": "blue"
            },
            "selgBA9cs68ZGNOC2": {
                "id": "selgBA9cs68ZGNOC2",
                "name": "Idris",
                "color": "blue"
            },
            "seltFK4N1vkN4q0sm": {
                "id": "seltFK4N1vkN4q0sm",
                "name": "Robert Alcorn",
                "color": "blue"
            },
            "seltpT5sgmJ4yH4El": {
                "id": "seltpT5sgmJ4yH4El",
                "name": "Pablo Veyrat",
                "color": "yellowMedium"
            },
            "selNAMv82NxUPKlmz": {
                "id": "selNAMv82NxUPKlmz",
                "name": "Alex Diaz",
                "color": "blue"
            },
            "selqATnjNJx6K7XWL": {
                "id": "selqATnjNJx6K7XWL",
                "name": "Carlos Blanco",
                "color": "cyan"
            },
            "selOTuezkan34nsI6": {
                "id": "selOTuezkan34nsI6",
                "name": "Jared Gil",
                "color": "teal"
            },
            "selRh9PdkibO22Txg": {
                "id": "selRh9PdkibO22Txg",
                "name": "Marc Torres",
                "color": "green"
            },
            "selpesi7Ax67PblrH": {
                "id": "selpesi7Ax67PblrH",
                "name": "Maria Hidalgo",
                "color": "yellow"
            },
            "selPz6KewXaycotkg": {
                "id": "selPz6KewXaycotkg",
                "name": "Jeff Tong",
                "color": "purpleMedium"
            },
            "sel6wrGZnpra4ado3": {
                "id": "sel6wrGZnpra4ado3",
                "name": "Tarun Gupta",
                "color": "blue"
            },
            "seltVDyY5WjeuN4bD": {
                "id": "seltVDyY5WjeuN4bD",
                "name": "Manuel Gonzalez Alzuru",
                "color": "blue"
            },
            "selUoPuq8i2827FOg": {
                "id": "selUoPuq8i2827FOg",
                "name": "Andrew Kline",
                "color": "red"
            },
            "selGoQL2vZvJPWFzl": {
                "id": "selGoQL2vZvJPWFzl",
                "name": "Guillaume Nervo",
                "color": "tealMedium"
            },
            "selrB6RRwStaxcILr": {
                "id": "selrB6RRwStaxcILr",
                "name": "Picodes",
                "color": "greenDark"
            },
            "selv8Xl0UzRLOEyIO": {
                "id": "selv8Xl0UzRLOEyIO",
                "name": "Jwon Do",
                "color": "blue"
            },
            "selitIH7aDnTUFYZC": {
                "id": "selitIH7aDnTUFYZC",
                "name": "Brandon Kumar",
                "color": "blue"
            },
            "selFl3xAzR4p0mRyH": {
                "id": "selFl3xAzR4p0mRyH",
                "name": "Dariya Khojasteh",
                "color": "purpleMedium"
            },
            "seluBWWChrG7Fd9Es": {
                "id": "seluBWWChrG7Fd9Es",
                "name": "Demian Brener",
                "color": "blue"
            },
            "sel9xUa4mlqk39KvX": {
                "id": "sel9xUa4mlqk39KvX",
                "name": "Agyle",
                "color": "blue"
            },
            "selvCfKujMOKeZmam": {
                "id": "selvCfKujMOKeZmam",
                "name": "Nanne Dekking",
                "color": "blue"
            },
            "sel6ZrdkKT3BUtxi7": {
                "id": "sel6ZrdkKT3BUtxi7",
                "name": "S\u00e9bastien Claeys",
                "color": "blue"
            },
            "sel8RQpjgkxVIhEy4": {
                "id": "sel8RQpjgkxVIhEy4",
                "name": "Gabriele Muse",
                "color": "blue"
            },
            "selTclohkazq1TxhG": {
                "id": "selTclohkazq1TxhG",
                "name": "Oleg Giberstein",
                "color": "cyan"
            },
            "selaHg1W827uaxSMB": {
                "id": "selaHg1W827uaxSMB",
                "name": "Zden\u011bk H\u00f6fler",
                "color": "teal"
            },
            "selONxcNBzWgXAkmm": {
                "id": "selONxcNBzWgXAkmm",
                "name": "Mark Hipperson",
                "color": "blue"
            },
            "seldoOdlRNs8EsfAG": {
                "id": "seldoOdlRNs8EsfAG",
                "name": "Niall McConnell",
                "color": "cyan"
            },
            "selSfv3gDsp67ZjXY": {
                "id": "selSfv3gDsp67ZjXY",
                "name": "Philip Goffin",
                "color": "teal"
            },
            "selD0VxhJA16VC047": {
                "id": "selD0VxhJA16VC047",
                "name": "a crypto-financial services company",
                "color": "blue"
            },
            "selX6CA62odavmoHJ": {
                "id": "selX6CA62odavmoHJ",
                "name": "Matt Hu",
                "color": "blue"
            },
            "sels5qPkXTUf0Q48l": {
                "id": "sels5qPkXTUf0Q48l",
                "name": "Julien Genestoux",
                "color": "blue"
            },
            "selp0W88XbYLONT91": {
                "id": "selp0W88XbYLONT91",
                "name": "Mriganka Pattnaik",
                "color": "blue"
            },
            "selfgbBNRWRjSK13A": {
                "id": "selfgbBNRWRjSK13A",
                "name": "Andrea Marec",
                "color": "blue"
            },
            "selwgxdmilfrcL1wh": {
                "id": "selwgxdmilfrcL1wh",
                "name": "Giulio Bozzo",
                "color": "cyan"
            },
            "selQhmPKnZRWvKEyH": {
                "id": "selQhmPKnZRWvKEyH",
                "name": "Tom Mizzone",
                "color": "blue"
            },
            "sellmqgjL91WsybJA": {
                "id": "sellmqgjL91WsybJA",
                "name": "Paddy Carroll",
                "color": "blue"
            },
            "selKLR1dm7buXT5Do": {
                "id": "selKLR1dm7buXT5Do",
                "name": "Nikolaos Kostopoulos",
                "color": "blue"
            },
            "selG1aWMvQD6mw1oD": {
                "id": "selG1aWMvQD6mw1oD",
                "name": "Joel Lin",
                "color": "blue"
            },
            "sellNm2coklkcl0Qf": {
                "id": "sellNm2coklkcl0Qf",
                "name": "Denis Znamenskiy",
                "color": "blue"
            },
            "selveVXM8yx7W8KV1": {
                "id": "selveVXM8yx7W8KV1",
                "name": "Hal Bame",
                "color": "blue"
            },
            "selF40ehZIZMfYv5V": {
                "id": "selF40ehZIZMfYv5V",
                "name": "Trevor McFedries",
                "color": "blue"
            },
            "selZPCAkdEOfmAQ8q": {
                "id": "selZPCAkdEOfmAQ8q",
                "name": "Eric Diep",
                "color": "blue"
            },
            "selZ7CH9gQomSWBej": {
                "id": "selZ7CH9gQomSWBej",
                "name": "Richerd Chan",
                "color": "pinkMedium"
            },
            "seli3PkyvkyfvtXzM": {
                "id": "seli3PkyvkyfvtXzM",
                "name": "Wilkins Chung",
                "color": "blueMedium"
            },
            "selinhoEZCUeXdw9U": {
                "id": "selinhoEZCUeXdw9U",
                "name": "Binh Doan",
                "color": "pinkDark"
            },
            "selnXybzmvM4oDaS9": {
                "id": "selnXybzmvM4oDaS9",
                "name": "Daniel Robenek",
                "color": "blue"
            },
            "selOMsTvFUvJ6uYSQ": {
                "id": "selOMsTvFUvJ6uYSQ",
                "name": "Ola Doudin",
                "color": "cyan"
            },
            "selRsowftfHgujzVv": {
                "id": "selRsowftfHgujzVv",
                "name": "Ming Wu",
                "color": "blue"
            },
            "selpeDee1nKsgXkF7": {
                "id": "selpeDee1nKsgXkF7",
                "name": "Swaroop Hegde",
                "color": "blue"
            },
            "selJYh60AEGKqhozn": {
                "id": "selJYh60AEGKqhozn",
                "name": "Harmeet Dhaliwal",
                "color": "blue"
            },
            "selWuDedDuKPMNii1": {
                "id": "selWuDedDuKPMNii1",
                "name": "Marco van den Heuvel ",
                "color": "greenDark"
            },
            "selrnqwY3xJj634R1": {
                "id": "selrnqwY3xJj634R1",
                "name": "Amitej Gajjala",
                "color": "blue"
            },
            "selArTBu8Jrnx2TtD": {
                "id": "selArTBu8Jrnx2TtD",
                "name": "Kaan Eryilmaz",
                "color": "blue"
            },
            "seli19R2lQoOwDTAq": {
                "id": "seli19R2lQoOwDTAq",
                "name": "Adrian Mazza",
                "color": "blue"
            },
            "selNnWq3bmlzoHC44": {
                "id": "selNnWq3bmlzoHC44",
                "name": "Ezequiel Baum",
                "color": "cyan"
            },
            "selRvRZFq7umijGQU": {
                "id": "selRvRZFq7umijGQU",
                "name": "Gloria Canseco",
                "color": "teal"
            },
            "seliwe8U0KGpSJ0ah": {
                "id": "seliwe8U0KGpSJ0ah",
                "name": "Juan Manuel Truffa",
                "color": "green"
            },
            "selFkyHZPPFhukZkz": {
                "id": "selFkyHZPPFhukZkz",
                "name": "Ryan Rudin",
                "color": "blue"
            },
            "selnW4GMesnmSLHE5": {
                "id": "selnW4GMesnmSLHE5",
                "name": "Ugnius Kiguolis",
                "color": "blue"
            },
            "selScST5rQvxfP6kC": {
                "id": "selScST5rQvxfP6kC",
                "name": "Janine GraingerView Janine Grainger\u2019s profile",
                "color": "blue"
            },
            "sel6yRt3rtzsd1Awh": {
                "id": "sel6yRt3rtzsd1Awh",
                "name": "Neor Basteker",
                "color": "blue"
            },
            "selnBDvaM5tPdbGvK": {
                "id": "selnBDvaM5tPdbGvK",
                "name": "Chase Freo",
                "color": "blue"
            },
            "selZghQEnjsPq68F7": {
                "id": "selZghQEnjsPq68F7",
                "name": "Paul Gadi",
                "color": "pink"
            },
            "seljaDgkUKps7cD30": {
                "id": "seljaDgkUKps7cD30",
                "name": "Nickev Vale",
                "color": "blue"
            },
            "sel8K2psf9xsnOy7D": {
                "id": "sel8K2psf9xsnOy7D",
                "name": "Naz Vavryk",
                "color": "teal"
            },
            "selpKsjkhuoqNVsWO": {
                "id": "selpKsjkhuoqNVsWO",
                "name": "Sumit Ghosh",
                "color": "blue"
            },
            "selYh1OnHHtHjoQEQ": {
                "id": "selYh1OnHHtHjoQEQ",
                "name": "Duke Nguyen",
                "color": "blue"
            },
            "selvp9rVCF8QFcsPU": {
                "id": "selvp9rVCF8QFcsPU",
                "name": "Venkatesh Karanalu",
                "color": "blue"
            },
            "selmsaCSNFqrdqJqj": {
                "id": "selmsaCSNFqrdqJqj",
                "name": "Shane Zhu",
                "color": "green"
            },
            "selIwrzLFqQbeziau": {
                "id": "selIwrzLFqQbeziau",
                "name": "James Smith",
                "color": "yellowMedium"
            },
            "selBQHmaHaKDMHS4q": {
                "id": "selBQHmaHaKDMHS4q",
                "name": "Tom Robinson",
                "color": "orange"
            },
            "selLPMVztftzLM5G3": {
                "id": "selLPMVztftzLM5G3",
                "name": "Adam Joyce",
                "color": "purple"
            },
            "selvivLQQ6Ncdb0gm": {
                "id": "selvivLQQ6Ncdb0gm",
                "name": "Yash Jejani",
                "color": "green"
            },
            "sele7i1j6vVwk4mVq": {
                "id": "sele7i1j6vVwk4mVq",
                "name": "Varun Satyam",
                "color": "grayDark"
            },
            "sel98WjjqbCdfBXsy": {
                "id": "sel98WjjqbCdfBXsy",
                "name": "Victor Faramond",
                "color": "purpleDark"
            },
            "selljNXM0kG7Hxhzk": {
                "id": "selljNXM0kG7Hxhzk",
                "name": "Ivan Soto-Wright",
                "color": "grayMedium"
            },
            "selBiA6R2ImxvFVgm": {
                "id": "selBiA6R2ImxvFVgm",
                "name": "Nir Kabessa",
                "color": "blue"
            },
            "sel8DM7R7rjLorzf8": {
                "id": "sel8DM7R7rjLorzf8",
                "name": "Vernon Johnson",
                "color": "purpleDarker"
            },
            "selJxUO6l74blEHlN": {
                "id": "selJxUO6l74blEHlN",
                "name": "Daniel Bar",
                "color": "purpleDark"
            },
            "self0GdaSbA1JUI7i": {
                "id": "self0GdaSbA1JUI7i",
                "name": "Henrik Andersson",
                "color": "blue"
            },
            "selLcUA8e0WGqIxyk": {
                "id": "selLcUA8e0WGqIxyk",
                "name": "Alexander Klus",
                "color": "blueDarker"
            },
            "selCGhzpjiL2o6rkY": {
                "id": "selCGhzpjiL2o6rkY",
                "name": "Gokalp Icer",
                "color": "blue"
            },
            "sel4ykYw5POksQJQr": {
                "id": "sel4ykYw5POksQJQr",
                "name": "Henrik Gradin",
                "color": "blue"
            },
            "sel2Q1zwSpaeL0eZD": {
                "id": "sel2Q1zwSpaeL0eZD",
                "name": "Diponkor Talukdar",
                "color": "blue"
            },
            "sele21D7EPwBCvXbH": {
                "id": "sele21D7EPwBCvXbH",
                "name": "Hashim Seead N Alsharif",
                "color": "cyan"
            },
            "selA0PXD7QgWmUx2t": {
                "id": "selA0PXD7QgWmUx2t",
                "name": "Arnaud Carrere",
                "color": "blue"
            },
            "sellmD111QcDi1JOI": {
                "id": "sellmD111QcDi1JOI",
                "name": "Oliver Yates",
                "color": "cyan"
            },
            "selct5WWAoVeR38qn": {
                "id": "selct5WWAoVeR38qn",
                "name": "Simon Douyer",
                "color": "teal"
            },
            "selyuruJUMn1jpsKo": {
                "id": "selyuruJUMn1jpsKo",
                "name": "Rohendra Singh",
                "color": "blue"
            },
            "sel9fx54YuESaI2I8": {
                "id": "sel9fx54YuESaI2I8",
                "name": "Toshendra Sharma",
                "color": "cyan"
            },
            "selbCvKLMwnMyji8t": {
                "id": "selbCvKLMwnMyji8t",
                "name": "ParaFi",
                "color": "blue"
            },
            "selw95GDH334fDrIl": {
                "id": "selw95GDH334fDrIl",
                "name": "Romain Figuereo",
                "color": "orangeMedium"
            },
            "sell6z7A9sRpy209Q": {
                "id": "sell6z7A9sRpy209Q",
                "name": "Aravindh Kumar",
                "color": "blue"
            },
            "selAHjNC2rHPMhvAE": {
                "id": "selAHjNC2rHPMhvAE",
                "name": "Tuan Nhu Dinh",
                "color": "blue"
            },
            "selc6dl7zxgWAR6fh": {
                "id": "selc6dl7zxgWAR6fh",
                "name": "Jake Tran",
                "color": "tealDarker"
            },
            "selLOYBwNSofbedCK": {
                "id": "selLOYBwNSofbedCK",
                "name": "Tom Sichel",
                "color": "blue"
            },
            "selBGMSUXSDNE15Zd": {
                "id": "selBGMSUXSDNE15Zd",
                "name": "Liran Peretz",
                "color": "blue"
            },
            "selzPJjthfaBC0Sze": {
                "id": "selzPJjthfaBC0Sze",
                "name": "Alex Shevchenko",
                "color": "blue"
            },
            "sel3qZeou0LRLPxyC": {
                "id": "sel3qZeou0LRLPxyC",
                "name": "Michael Halimi",
                "color": "blue"
            },
            "selo56MJRs6VzoS7R": {
                "id": "selo56MJRs6VzoS7R",
                "name": "Hassan Ibrahim",
                "color": "blue"
            },
            "selI2n7kg3o1qC7Fl": {
                "id": "selI2n7kg3o1qC7Fl",
                "name": "Henry Tran",
                "color": "cyan"
            },
            "selDOjtbCPs3lIhuZ": {
                "id": "selDOjtbCPs3lIhuZ",
                "name": "Maximilian Fiege",
                "color": "blue"
            },
            "selWZk5L0T0YFrb44": {
                "id": "selWZk5L0T0YFrb44",
                "name": "Aron Beierschmitt",
                "color": "blue"
            },
            "selGm1xKottbjMBhr": {
                "id": "selGm1xKottbjMBhr",
                "name": "Collin Myers",
                "color": "blue"
            },
            "selBBCSresZsccsps": {
                "id": "selBBCSresZsccsps",
                "name": "Jay Chang",
                "color": "blue"
            },
            "selRQC9EG6z9i7hn4": {
                "id": "selRQC9EG6z9i7hn4",
                "name": "Abhay Aggarwal",
                "color": "blue"
            },
            "sel15e5mniyusBqXH": {
                "id": "sel15e5mniyusBqXH",
                "name": "Taylor Johnson",
                "color": "blueMedium"
            },
            "selje6pZCUhpzzLle": {
                "id": "selje6pZCUhpzzLle",
                "name": "Tommy Johnson",
                "color": "orangeDark"
            },
            "selKw6v3BZiahZL7J": {
                "id": "selKw6v3BZiahZL7J",
                "name": "Ritik Dutta",
                "color": "blue"
            },
            "selXEWMLMH6wmg5lr": {
                "id": "selXEWMLMH6wmg5lr",
                "name": "Andr\u00e9 Neves",
                "color": "blue"
            },
            "seldPDMlHgbe7irTw": {
                "id": "seldPDMlHgbe7irTw",
                "name": "Christian Moss",
                "color": "cyan"
            },
            "sel5mneplWxFVUZZG": {
                "id": "sel5mneplWxFVUZZG",
                "name": "Simon Cowell",
                "color": "teal"
            },
            "selTWFc1PUlSZWQ8W": {
                "id": "selTWFc1PUlSZWQ8W",
                "name": " Jeff Gluck",
                "color": "yellowMedium"
            },
            "selbsYijYS4XUleNU": {
                "id": "selbsYijYS4XUleNU",
                "name": "Jeff Gluck",
                "color": "blue"
            },
            "selU20MT25vddfkF4": {
                "id": "selU20MT25vddfkF4",
                "name": "Jeremy Kerbel",
                "color": "pinkDarker"
            },
            "selUKjCpDrYAb7O7e": {
                "id": "selUKjCpDrYAb7O7e",
                "name": "James Zhang",
                "color": "purpleDark"
            },
            "seloMT8NJvSg0BfwN": {
                "id": "seloMT8NJvSg0BfwN",
                "name": "Vadim Suchkov",
                "color": "grayMedium"
            },
            "selkX0c18QheBZD24": {
                "id": "selkX0c18QheBZD24",
                "name": "Paul Budnitz",
                "color": "green"
            },
            "selXyUiBBDesMxQY0": {
                "id": "selXyUiBBDesMxQY0",
                "name": "Zaki Manian",
                "color": "pinkDarker"
            },
            "selrUGVGJfEgGfJHU": {
                "id": "selrUGVGJfEgGfJHU",
                "name": "Josh Bull",
                "color": "blue"
            },
            "selILXBo0c68sh9ib": {
                "id": "selILXBo0c68sh9ib",
                "name": "Gautham Santhosh",
                "color": "cyanMedium"
            },
            "selk2VPBWPXxkvLWk": {
                "id": "selk2VPBWPXxkvLWk",
                "name": "Maximilian von Wallenberg-Pachaly",
                "color": "blue"
            },
            "selW51zpZEbjqnXRm": {
                "id": "selW51zpZEbjqnXRm",
                "name": "Raz Friedman",
                "color": "blue"
            },
            "sel3xJtkH8FGMPFAt": {
                "id": "sel3xJtkH8FGMPFAt",
                "name": "Bofu Chen",
                "color": "green"
            },
            "selWHmW10zCQdfxxO": {
                "id": "selWHmW10zCQdfxxO",
                "name": "Abhimanyu Kashyap",
                "color": "yellowDarker"
            },
            "selBgo0YJSt9skOW8": {
                "id": "selBgo0YJSt9skOW8",
                "name": "Keith Rumjahn",
                "color": "greenDarker"
            },
            "selJhy8zT63FnSePq": {
                "id": "selJhy8zT63FnSePq",
                "name": "Robert Tran",
                "color": "pinkDarker"
            },
            "selv2ccwWeB32tmrh": {
                "id": "selv2ccwWeB32tmrh",
                "name": "Nelly Chatue-Diop",
                "color": "teal"
            },
            "seliIHG0qQLqNRjQn": {
                "id": "seliIHG0qQLqNRjQn",
                "name": "Dan Kinsley",
                "color": "blue"
            },
            "selLHN8XLOP28oJNd": {
                "id": "selLHN8XLOP28oJNd",
                "name": "Paul Frambot",
                "color": "blue"
            },
            "selWE81XBXfATUxo4": {
                "id": "selWE81XBXfATUxo4",
                "name": "Vince Yang",
                "color": "blue"
            },
            "selFTDpJ4asL0YTlb": {
                "id": "selFTDpJ4asL0YTlb",
                "name": "Andrew Fraser",
                "color": "blue"
            },
            "selYMJEkjJwZRQIEA": {
                "id": "selYMJEkjJwZRQIEA",
                "name": "Scott Lawin",
                "color": "grayDarker"
            },
            "sel61jdMcRBi8DLot": {
                "id": "sel61jdMcRBi8DLot",
                "name": "Gary Vaynerchuk",
                "color": "blue"
            },
            "selqPZDX5je6fBgoy": {
                "id": "selqPZDX5je6fBgoy",
                "name": "Sam Altman",
                "color": "cyan"
            },
            "selDSNiUxZlgDILaN": {
                "id": "selDSNiUxZlgDILaN",
                "name": "Nick Avramov",
                "color": "orange"
            },
            "selu6qBbmGSjPZn7w": {
                "id": "selu6qBbmGSjPZn7w",
                "name": "Lin Yalu",
                "color": "yellowDark"
            },
            "sel3ukhT5rYgaEzvM": {
                "id": "sel3ukhT5rYgaEzvM",
                "name": "Matt Huang ",
                "color": "purpleMedium"
            },
            "selUthccUpNAYtcwd": {
                "id": "selUthccUpNAYtcwd",
                "name": "Elie Le Rest",
                "color": "pink"
            },
            "selFCZ6SL14gSxxWs": {
                "id": "selFCZ6SL14gSxxWs",
                "name": "Myrtle Anne",
                "color": "cyanDark"
            },
            "selat4GOruV28aM1U": {
                "id": "selat4GOruV28aM1U",
                "name": "Harry Liu",
                "color": "orangeDark"
            },
            "selszKCZixQeELRFz": {
                "id": "selszKCZixQeELRFz",
                "name": "Will Weinraub",
                "color": "greenDarker"
            },
            "selli4cMBfWKpvDuz": {
                "id": "selli4cMBfWKpvDuz",
                "name": "Nik Kalyani",
                "color": "cyanDark"
            },
            "selZG8KqJT279dmD7": {
                "id": "selZG8KqJT279dmD7",
                "name": "Adi K Mishra",
                "color": "purple"
            },
            "sel59ydjCz4ruk0dh": {
                "id": "sel59ydjCz4ruk0dh",
                "name": "AJ Milne",
                "color": "purpleDark"
            },
            "seliGXSMtGfRssQyk": {
                "id": "seliGXSMtGfRssQyk",
                "name": "Grigore Ro\u0219u",
                "color": "pinkDark"
            },
            "selWa4pN9y8ofxsUW": {
                "id": "selWa4pN9y8ofxsUW",
                "name": "David Lu",
                "color": "yellow"
            },
            "seltBthWEnNGfN1Sq": {
                "id": "seltBthWEnNGfN1Sq",
                "name": "John Letey",
                "color": "tealDarker"
            },
            "sellLItILEuSQFQyK": {
                "id": "sellLItILEuSQFQyK",
                "name": "Tin Nguyen",
                "color": "teal"
            },
            "selFahcwAdX0ffSVa": {
                "id": "selFahcwAdX0ffSVa",
                "name": "Mitchell Amador",
                "color": "yellowDarker"
            },
            "selMCUIuj5FJ4KxAA": {
                "id": "selMCUIuj5FJ4KxAA",
                "name": "Brandon Da Silva",
                "color": "blue"
            },
            "selgJRSoLfvXzHW6K": {
                "id": "selgJRSoLfvXzHW6K",
                "name": "Dzung Tran",
                "color": "greenDark"
            },
            "sel3wNocdBQIpdMqb": {
                "id": "sel3wNocdBQIpdMqb",
                "name": "Sunny Aggarwal",
                "color": "grayMedium"
            },
            "selELTVqMYkkB1g5g": {
                "id": "selELTVqMYkkB1g5g",
                "name": "Alexander Nabutovsky",
                "color": "orangeMedium"
            },
            "selfJnjQnOFCo9TH7": {
                "id": "selfJnjQnOFCo9TH7",
                "name": "Garrett See",
                "color": "cyanDarker"
            },
            "sel0XY4JmoQMhTErz": {
                "id": "sel0XY4JmoQMhTErz",
                "name": "Dino Verbrugge",
                "color": "purpleDark"
            },
            "sellJEmx7baKd9TtV": {
                "id": "sellJEmx7baKd9TtV",
                "name": "Jared Vegosen",
                "color": "cyanDark"
            },
            "seleLXj5my88naeF1": {
                "id": "seleLXj5my88naeF1",
                "name": "momo",
                "color": "pinkDarker"
            },
            "selXvp076d1mrJ1R3": {
                "id": "selXvp076d1mrJ1R3",
                "name": "senx",
                "color": "grayDark"
            },
            "selsJSA2RJ2lzpL02": {
                "id": "selsJSA2RJ2lzpL02",
                "name": "Joe Lau",
                "color": "green"
            },
            "selRYHsJWd3nkvMiC": {
                "id": "selRYHsJWd3nkvMiC",
                "name": "Pham Van Phuong",
                "color": "tealDarker"
            },
            "sel56hBtdjF7FzZqx": {
                "id": "sel56hBtdjF7FzZqx",
                "name": "Ryan Matovu",
                "color": "yellow"
            },
            "selFFYtyyf0Yn4dHE": {
                "id": "selFFYtyyf0Yn4dHE",
                "name": "Jim McNelis",
                "color": "blue"
            },
            "selvGAU4hwvV480xT": {
                "id": "selvGAU4hwvV480xT",
                "name": "Stephen Ehrlich",
                "color": "grayDarker"
            },
            "sel8pqNrNx9jqYRwu": {
                "id": "sel8pqNrNx9jqYRwu",
                "name": "Stepan Simkin",
                "color": "redDarker"
            },
            "selwykxXzbJINokyd": {
                "id": "selwykxXzbJINokyd",
                "name": "Charlie Graham",
                "color": "cyan"
            },
            "sel5B4Iakf0WPvL67": {
                "id": "sel5B4Iakf0WPvL67",
                "name": "Will Hay",
                "color": "grayDark"
            },
            "selnKBnNUNQi8YTQ9": {
                "id": "selnKBnNUNQi8YTQ9",
                "name": "Danny Adkins ",
                "color": "tealDark"
            },
            "seloNPhyLSqK0Nvga": {
                "id": "seloNPhyLSqK0Nvga",
                "name": " Cooper Turley",
                "color": "grayDarker"
            },
            "selaFGMZ1ltuIlGo1": {
                "id": "selaFGMZ1ltuIlGo1",
                "name": "Chris King",
                "color": "blue"
            },
            "selygoD2vZdN2qw0P": {
                "id": "selygoD2vZdN2qw0P",
                "name": "Jason Bailey",
                "color": "cyan"
            },
            "sel6MMhBPCHR2Jg1a": {
                "id": "sel6MMhBPCHR2Jg1a",
                "name": "Nikolai Gurskyi",
                "color": "teal"
            },
            "selm7tiS1rSO7zunN": {
                "id": "selm7tiS1rSO7zunN",
                "name": "Thomas Caddick",
                "color": "purpleMedium"
            },
            "sel4MhNaueuSNGweQ": {
                "id": "sel4MhNaueuSNGweQ",
                "name": "Chris Ciszak",
                "color": "yellow"
            },
            "selmhD4Wx8vK2uLur": {
                "id": "selmhD4Wx8vK2uLur",
                "name": "Kris Vaivods",
                "color": "grayMedium"
            },
            "selbqfpB93BHNHayJ": {
                "id": "selbqfpB93BHNHayJ",
                "name": "Steven Douglas Pruitt",
                "color": "blueDark"
            },
            "selfEyJpzW0M1DtiZ": {
                "id": "selfEyJpzW0M1DtiZ",
                "name": "Kimi Lee",
                "color": "gray"
            },
            "selfdmR4D9kaZS66F": {
                "id": "selfdmR4D9kaZS66F",
                "name": "Roy Aaron",
                "color": "purpleDark"
            },
            "seloWTEr1ieFFubGd": {
                "id": "seloWTEr1ieFFubGd",
                "name": "Alvin Tang ",
                "color": "grayDark"
            },
            "seliVogHEjGP6qY3G": {
                "id": "seliVogHEjGP6qY3G",
                "name": "Prakash Somosundram",
                "color": "redDarker"
            },
            "selfH15KE80gppcOD": {
                "id": "selfH15KE80gppcOD",
                "name": "Dave Weisberger",
                "color": "blue"
            },
            "seljSX6FSmmhHwZjx": {
                "id": "seljSX6FSmmhHwZjx",
                "name": "Ian Weisberger",
                "color": "cyan"
            },
            "selWyyQDqtYUHr2eh": {
                "id": "selWyyQDqtYUHr2eh",
                "name": "Soban Saqib",
                "color": "blue"
            },
            "selHDlh6SgIvqcpZ1": {
                "id": "selHDlh6SgIvqcpZ1",
                "name": "Neil Kothari",
                "color": "blue"
            },
            "sel68gEQY0niBBSrd": {
                "id": "sel68gEQY0niBBSrd",
                "name": "Pushkar Mukewar",
                "color": "cyan"
            },
            "seloxd1Z7PFHpFyNB": {
                "id": "seloxd1Z7PFHpFyNB",
                "name": "Sascha Darius Mojtahedi",
                "color": "blue"
            },
            "selOTRJ2tX1YhSGtM": {
                "id": "selOTRJ2tX1YhSGtM",
                "name": "Wayne Chang ",
                "color": "redDark"
            },
            "seln2CwRTkNNUYTPd": {
                "id": "seln2CwRTkNNUYTPd",
                "name": "Gregory Rocco",
                "color": "yellow"
            },
            "selMeQlUHHDrl2RLy": {
                "id": "selMeQlUHHDrl2RLy",
                "name": "George Cao",
                "color": "greenDark"
            },
            "selR0VoS7D3qwyiXQ": {
                "id": "selR0VoS7D3qwyiXQ",
                "name": "Ariel Ling",
                "color": "grayDarker"
            },
            "selGESaDnxDkvpT2T": {
                "id": "selGESaDnxDkvpT2T",
                "name": "Ali Vira",
                "color": "cyanDark"
            },
            "selZwLplHjm1rMHyQ": {
                "id": "selZwLplHjm1rMHyQ",
                "name": "Winston Robson",
                "color": "orangeDark"
            },
            "seluvsXFfBzvJJ7Zz": {
                "id": "seluvsXFfBzvJJ7Zz",
                "name": "Michael J. Cohen",
                "color": "purple"
            },
            "selek2M29vXMJcY1U": {
                "id": "selek2M29vXMJcY1U",
                "name": "Henry de Valence",
                "color": "blue"
            },
            "sel6KA5dC6tMj5k0u": {
                "id": "sel6KA5dC6tMj5k0u",
                "name": "Wengie/Wraya",
                "color": "purpleMedium"
            },
            "selq7BD4dyO69qT29": {
                "id": "selq7BD4dyO69qT29",
                "name": "Maxmerro",
                "color": "gray"
            },
            "sele9wTEyIy5POr30": {
                "id": "sele9wTEyIy5POr30",
                "name": "Ahmad Abbasi",
                "color": "redMedium"
            },
            "selupx2cSMooWPIe1": {
                "id": "selupx2cSMooWPIe1",
                "name": "Danial Abbasi",
                "color": "orangeMedium"
            },
            "selodRqEtwFn45At9": {
                "id": "selodRqEtwFn45At9",
                "name": "Vincenzo Alagna",
                "color": "orange"
            },
            "selUVHCZzkHnn59SW": {
                "id": "selUVHCZzkHnn59SW",
                "name": "Alex Paley",
                "color": "redDarker"
            },
            "selYvFP5Sz6DLhFW4": {
                "id": "selYvFP5Sz6DLhFW4",
                "name": "Dennis Zdonov",
                "color": "grayMedium"
            },
            "selRkpigEp4NmvXuI": {
                "id": "selRkpigEp4NmvXuI",
                "name": "Mike Hepburn",
                "color": "blue"
            },
            "selRWBXIkgzAStpyn": {
                "id": "selRWBXIkgzAStpyn",
                "name": "Dirk Lueth",
                "color": "blue"
            },
            "selfa1AFPXGqz8yYq": {
                "id": "selfa1AFPXGqz8yYq",
                "name": "Idan Zuckerman",
                "color": "cyan"
            },
            "sel7RAyxlNXEg6U0G": {
                "id": "sel7RAyxlNXEg6U0G",
                "name": "Mani Honigstein",
                "color": "teal"
            },
            "sel2Tk9s14HaRLxeB": {
                "id": "sel2Tk9s14HaRLxeB",
                "name": "Chatchaval Jiaravanon",
                "color": "blue"
            },
            "selqq1wVHzMzdfvrR": {
                "id": "selqq1wVHzMzdfvrR",
                "name": "Tridbodi Arunanondchai",
                "color": "cyan"
            },
            "selSVejGEMX6GF8jv": {
                "id": "selSVejGEMX6GF8jv",
                "name": "Peter Hume",
                "color": "blue"
            },
            "selWg1VXdhduhmoRS": {
                "id": "selWg1VXdhduhmoRS",
                "name": "Ivo Grigorov",
                "color": "blue"
            },
            "selxyYsfaxHGM4qZU": {
                "id": "selxyYsfaxHGM4qZU",
                "name": "Han Nguyen",
                "color": "green"
            },
            "selIaMK7lBAfknPfP": {
                "id": "selIaMK7lBAfknPfP",
                "name": "Ahmed Hamed Aly",
                "color": "blue"
            },
            "selg0i5bj4LcVJ1qW": {
                "id": "selg0i5bj4LcVJ1qW",
                "name": "Wil Barnes",
                "color": "tealDarker"
            },
            "selOoTQyj6sSQCEg6": {
                "id": "selOoTQyj6sSQCEg6",
                "name": "James Moreau",
                "color": "redDark"
            },
            "selAAwuLgdGAHearS": {
                "id": "selAAwuLgdGAHearS",
                "name": "Dina Sam'an",
                "color": "redMedium"
            },
            "sellUPsLoCQBIybXJ": {
                "id": "sellUPsLoCQBIybXJ",
                "name": "Talal Tabbaa",
                "color": "pinkDarker"
            },
            "selC9pd8kMp8tGLgc": {
                "id": "selC9pd8kMp8tGLgc",
                "name": "Yazan Barghuthi",
                "color": "green"
            },
            "selF5FPd8CADwONwQ": {
                "id": "selF5FPd8CADwONwQ",
                "name": "Ham Serunjogi",
                "color": "blue"
            },
            "selCkTedELnd73yzX": {
                "id": "selCkTedELnd73yzX",
                "name": "Maijid Moujaled",
                "color": "cyan"
            },
            "selnraRiAuhldCWtO": {
                "id": "selnraRiAuhldCWtO",
                "name": "Zach Hamilton",
                "color": "cyanMedium"
            },
            "selO8nNHrWFSfYI5e": {
                "id": "selO8nNHrWFSfYI5e",
                "name": "Marina Guryeva",
                "color": "cyanDark"
            },
            "sel7U9MysyoTaGZCv": {
                "id": "sel7U9MysyoTaGZCv",
                "name": "Brandon Arvanaghi",
                "color": "pinkDark"
            },
            "selNkv7ZlH4H7j4PX": {
                "id": "selNkv7ZlH4H7j4PX",
                "name": "Jimmy Yin",
                "color": "tealDark"
            },
            "selX9aQmMTgaMt9QA": {
                "id": "selX9aQmMTgaMt9QA",
                "name": "Pelle Braendgaard",
                "color": "yellow"
            },
            "selxkoii5EwuuJRWf": {
                "id": "selxkoii5EwuuJRWf",
                "name": "Alice Nawfal, Andres Junge, Ania Lipinska, Pelle Braendgaard",
                "color": "teal"
            },
            "selNkz0IE4ZczzEO4": {
                "id": "selNkz0IE4ZczzEO4",
                "name": "Alice Nawfal",
                "color": "greenMedium"
            },
            "sel3620BTleBooJUl": {
                "id": "sel3620BTleBooJUl",
                "name": "Andres Junge",
                "color": "green"
            },
            "selc4XR664IpwsbAL": {
                "id": "selc4XR664IpwsbAL",
                "name": "Ania Lipinska",
                "color": "gray"
            },
            "selsOJYbctppA9LqW": {
                "id": "selsOJYbctppA9LqW",
                "name": "Stefan Rust",
                "color": "yellowDarker"
            },
            "selKu6Acspyzs79hT": {
                "id": "selKu6Acspyzs79hT",
                "name": "Dmitry Zhelezov",
                "color": "red"
            },
            "selimslTwCkDbbHxM": {
                "id": "selimslTwCkDbbHxM",
                "name": "Maxine Ryan ",
                "color": "blue"
            },
            "selbvkcL4LHKgeYwX": {
                "id": "selbvkcL4LHKgeYwX",
                "name": "Damir Vodenicarevic",
                "color": "pink"
            },
            "seltffguY6dJVXg1r": {
                "id": "seltffguY6dJVXg1r",
                "name": "Adrien Laversanne-Finot",
                "color": "orangeDarker"
            },
            "sel5dicxMwZKpOVT9": {
                "id": "sel5dicxMwZKpOVT9",
                "name": "Pierre-Yves Nogue",
                "color": "tealDark"
            },
            "sele2r9EhrXeXd0cC": {
                "id": "sele2r9EhrXeXd0cC",
                "name": "Chris Seline",
                "color": "gray"
            },
            "sel8iwwg9LOfzFzKR": {
                "id": "sel8iwwg9LOfzFzKR",
                "name": "Evan Fellers",
                "color": "redMedium"
            },
            "sel7J3R83pXYroXhC": {
                "id": "sel7J3R83pXYroXhC",
                "name": "Noritaka Okabe",
                "color": "grayDark"
            },
            "selfqE2Ph5tkxaxmQ": {
                "id": "selfqE2Ph5tkxaxmQ",
                "name": "Jarindr Thitadilaka",
                "color": "pinkMedium"
            },
            "sel6DsCPB22eFVMbm": {
                "id": "sel6DsCPB22eFVMbm",
                "name": "Sungmin Aum",
                "color": "yellowDark"
            },
            "selzrIQ1shiWqws26": {
                "id": "selzrIQ1shiWqws26",
                "name": "David Braut",
                "color": "purpleMedium"
            },
            "selqhY6lKtsD1gAsc": {
                "id": "selqhY6lKtsD1gAsc",
                "name": "Vincent Lee",
                "color": "cyanMedium"
            },
            "selqKyxiVOid26Bzq": {
                "id": "selqKyxiVOid26Bzq",
                "name": "Justin",
                "color": "green"
            },
            "selRVcxQPJofS9JjB": {
                "id": "selRVcxQPJofS9JjB",
                "name": "Simon Vieira",
                "color": "orangeDarker"
            },
            "selmO4K3SeWCJa9Cs": {
                "id": "selmO4K3SeWCJa9Cs",
                "name": "Sam Thapaliya",
                "color": "blue"
            },
            "selAqLmT8f7hjf3gb": {
                "id": "selAqLmT8f7hjf3gb",
                "name": "Chidozie Ogbo",
                "color": "cyanMedium"
            },
            "selzaOmOP76PTBqgM": {
                "id": "selzaOmOP76PTBqgM",
                "name": "Ugochukwu Aronu",
                "color": "yellowDarker"
            },
            "selnpRAqqC5bcCRzp": {
                "id": "selnpRAqqC5bcCRzp",
                "name": "Vitomir Jevremovic",
                "color": "blue"
            },
            "selb9h0LwhazXFrhT": {
                "id": "selb9h0LwhazXFrhT",
                "name": " Jovan Tisma",
                "color": "purpleMedium"
            },
            "sel4bTLEMAmSWekJU": {
                "id": "sel4bTLEMAmSWekJU",
                "name": "Xiankun Wu",
                "color": "tealDark"
            },
            "selELMiyfXXuVSYlX": {
                "id": "selELMiyfXXuVSYlX",
                "name": "Yan Zhang ",
                "color": "cyanDarker"
            },
            "sel2mcsahKvZpau8k": {
                "id": "sel2mcsahKvZpau8k",
                "name": "Yuheng Chen",
                "color": "cyanDark"
            },
            "sel05m5QlwBalaVs2": {
                "id": "sel05m5QlwBalaVs2",
                "name": "Shailesh Gupta",
                "color": "yellowDark"
            },
            "selUwKKmVZvhzHek7": {
                "id": "selUwKKmVZvhzHek7",
                "name": "Miljan Martic",
                "color": "greenDark"
            },
            "selLHaXHYJhcRlYYU": {
                "id": "selLHaXHYJhcRlYYU",
                "name": "Peter Toth",
                "color": "cyanDark"
            },
            "sel6mUoOV2rsqDciN": {
                "id": "sel6mUoOV2rsqDciN",
                "name": "Sadiq Ahamed",
                "color": "pinkMedium"
            },
            "selF7ALjrCrk3KZNQ": {
                "id": "selF7ALjrCrk3KZNQ",
                "name": "Dan Ngo",
                "color": "greenDark"
            },
            "sel0xkdgzwBGnnGLU": {
                "id": "sel0xkdgzwBGnnGLU",
                "name": " Jayz Nguyen",
                "color": "yellowDarker"
            },
            "selp9aWSWDhTC78SH": {
                "id": "selp9aWSWDhTC78SH",
                "name": "Patrik Arnesson",
                "color": "yellowDark"
            },
            "selv3ecCCRQotD7kR": {
                "id": "selv3ecCCRQotD7kR",
                "name": "Mikael Pawlo",
                "color": "yellowDark"
            },
            "selfZIo2iixfVQT9C": {
                "id": "selfZIo2iixfVQT9C",
                "name": "Erik Sunner\u00f6",
                "color": "pinkDark"
            },
            "sels07dNzYhdG3VoI": {
                "id": "sels07dNzYhdG3VoI",
                "name": " Tushar Aggarwal",
                "color": "orangeMedium"
            },
            "selZCcOGh4cJY36Fu": {
                "id": "selZCcOGh4cJY36Fu",
                "name": " Andros Wong",
                "color": "yellow"
            },
            "selqVFTn6B4iuDZgd": {
                "id": "selqVFTn6B4iuDZgd",
                "name": "Rahul Sood",
                "color": "yellow"
            },
            "sel9B1Ax11y6mVd72": {
                "id": "sel9B1Ax11y6mVd72",
                "name": "Chiente Hsu",
                "color": "blueDark"
            },
            "selxptLIArNUl3Hoh": {
                "id": "selxptLIArNUl3Hoh",
                "name": "Rachel Yu",
                "color": "redDarker"
            },
            "selWm6eOgEQefiO4M": {
                "id": "selWm6eOgEQefiO4M",
                "name": "Mike Wen",
                "color": "blueMedium"
            },
            "selSN8poqNAKIOJAq": {
                "id": "selSN8poqNAKIOJAq",
                "name": " Wilson Wei ",
                "color": "cyanDarker"
            },
            "sel1GXWlYTq9zW0Tp": {
                "id": "sel1GXWlYTq9zW0Tp",
                "name": "Nigel Eccles",
                "color": "pinkDarker"
            },
            "selECVQKSzAUbBang": {
                "id": "selECVQKSzAUbBang",
                "name": "Varun Sudhakar",
                "color": "yellowMedium"
            },
            "selNiFZpKlHRTqoTS": {
                "id": "selNiFZpKlHRTqoTS",
                "name": "Stuart Tonner",
                "color": "redMedium"
            },
            "selzar7kMqFviKHpe": {
                "id": "selzar7kMqFviKHpe",
                "name": "Barrett Williams",
                "color": "red"
            },
            "selqLLPO7nx2aUkBL": {
                "id": "selqLLPO7nx2aUkBL",
                "name": "Wesley Kayne",
                "color": "gray"
            },
            "selqYUjf2sZW9GcUY": {
                "id": "selqYUjf2sZW9GcUY",
                "name": "Cameron Winklevoss",
                "color": "red"
            },
            "sel7u2P8m1ZF5PgQV": {
                "id": "sel7u2P8m1ZF5PgQV",
                "name": "Tyler Winklevoss",
                "color": "greenDarker"
            },
            "sel3urKzEmvCIpUHp": {
                "id": "sel3urKzEmvCIpUHp",
                "name": "Eric Zhang",
                "color": "redDark"
            },
            "sellIek7Wb5JMPjvU": {
                "id": "sellIek7Wb5JMPjvU",
                "name": "Brian Guan",
                "color": "cyanMedium"
            },
            "selHtswTchJIJ74Fi": {
                "id": "selHtswTchJIJ74Fi",
                "name": "Abhi Vyas",
                "color": "yellowDark"
            },
            "selkvXiH1J9aXyqfI": {
                "id": "selkvXiH1J9aXyqfI",
                "name": "Pierre Cumenal",
                "color": "cyan"
            },
            "sel35dBofNsocrFWe": {
                "id": "sel35dBofNsocrFWe",
                "name": "Peter Ing",
                "color": "grayDarker"
            },
            "sel59E2QvFD4030By": {
                "id": "sel59E2QvFD4030By",
                "name": "Felix Xing",
                "color": "redDark"
            },
            "sel8PU0k0coMBtnmj": {
                "id": "sel8PU0k0coMBtnmj",
                "name": " Adrian Brink",
                "color": "blueDark"
            },
            "selDabzkt8bo4eGqb": {
                "id": "selDabzkt8bo4eGqb",
                "name": "Awa Sun Yin",
                "color": "cyanMedium"
            },
            "selxSNpbBhZDtYFoH": {
                "id": "selxSNpbBhZDtYFoH",
                "name": "Christopher Goes",
                "color": "blue"
            },
            "seldNQ6MCgIu17kdy": {
                "id": "seldNQ6MCgIu17kdy",
                "name": "Fabien Marino",
                "color": "blue"
            },
            "selaW2Yuce66u5AOq": {
                "id": "selaW2Yuce66u5AOq",
                "name": "Patrick Kiefer",
                "color": "orange"
            },
            "selpgnwoEoZ3RvkTE": {
                "id": "selpgnwoEoZ3RvkTE",
                "name": "Edward Mehrez",
                "color": "yellowDarker"
            },
            "sellDQW1ASkVOxddY": {
                "id": "sellDQW1ASkVOxddY",
                "name": "Dinh Nguyen",
                "color": "orangeMedium"
            },
            "selj0Rmgc6B07i5Bb": {
                "id": "selj0Rmgc6B07i5Bb",
                "name": "Tam Dinh",
                "color": "cyanDarker"
            },
            "seloICKrTil98nbkl": {
                "id": "seloICKrTil98nbkl",
                "name": "Truong Pham",
                "color": "grayMedium"
            },
            "selODLOidkBlMCKsC": {
                "id": "selODLOidkBlMCKsC",
                "name": "Imran Palem",
                "color": "orangeMedium"
            },
            "selISPGEIaJJuQ5jb": {
                "id": "selISPGEIaJJuQ5jb",
                "name": "Bhargav Varma",
                "color": "blueDarker"
            },
            "seltZacrnN9fo1CKj": {
                "id": "seltZacrnN9fo1CKj",
                "name": "Olivier Roussy Newton",
                "color": "purpleMedium"
            },
            "selF5JEPPnI97C4xZ": {
                "id": "selF5JEPPnI97C4xZ",
                "name": "Cassio Jose Krupinsk",
                "color": "gray"
            },
            "selB29sN9Jo9zf2zp": {
                "id": "selB29sN9Jo9zf2zp",
                "name": "Justin Giudici",
                "color": "yellowDark"
            },
            "selgxdBRROECS8tVv": {
                "id": "selgxdBRROECS8tVv",
                "name": "Keyur Patel",
                "color": "yellowMedium"
            },
            "selaviktyRHAMvc7F": {
                "id": "selaviktyRHAMvc7F",
                "name": "Ramkumar Subramaniam",
                "color": "pinkDark"
            },
            "selLKm0JF3qaSkPxl": {
                "id": "selLKm0JF3qaSkPxl",
                "name": "Arjun Reddy",
                "color": "grayDark"
            },
            "sel8i1ILrExAgGN5B": {
                "id": "sel8i1ILrExAgGN5B",
                "name": "Kameshwaran Elangovan",
                "color": "purpleMedium"
            },
            "sel4AxUVsIw7nRkhj": {
                "id": "sel4AxUVsIw7nRkhj",
                "name": "Andras Vajda",
                "color": "blueDarker"
            },
            "selmZ6LrRoaEzKDpX": {
                "id": "selmZ6LrRoaEzKDpX",
                "name": "Roy Liu",
                "color": "grayDark"
            },
            "selz0Z5QR4c1hJmha": {
                "id": "selz0Z5QR4c1hJmha",
                "name": " Mihai Pohontu",
                "color": "pinkMedium"
            },
            "selVxd9FsqsGKy6ZC": {
                "id": "selVxd9FsqsGKy6ZC",
                "name": "Michel Dahdah",
                "color": "pinkDarker"
            },
            "sel7eLH5qWZze5akv": {
                "id": "sel7eLH5qWZze5akv",
                "name": " Eloi Henrard",
                "color": "red"
            },
            "selt7PR7wnfeqBtmI": {
                "id": "selt7PR7wnfeqBtmI",
                "name": " Justin Blau",
                "color": "pink"
            },
            "sel8WCsjpHTVGEgkY": {
                "id": "sel8WCsjpHTVGEgkY",
                "name": "Justin Oren",
                "color": "yellowDarker"
            },
            "selH6Iu4pj3YjkQjH": {
                "id": "selH6Iu4pj3YjkQjH",
                "name": "Mirko Schmiedl",
                "color": "yellowDark"
            },
            "selrS76O1Y2xrRnwY": {
                "id": "selrS76O1Y2xrRnwY",
                "name": "Jannik Schmiedl",
                "color": "orangeDark"
            },
            "sel2nogvwrHulVYPU": {
                "id": "sel2nogvwrHulVYPU",
                "name": "Marguerite deCourcelle",
                "color": "teal"
            },
            "selbnJKGvoorcPZak": {
                "id": "selbnJKGvoorcPZak",
                "name": "Ben Heidorn",
                "color": "blueDark"
            },
            "selBMHwKMYKrOktSn": {
                "id": "selBMHwKMYKrOktSn",
                "name": "Marc Cercos",
                "color": "orange"
            },
            "sel3u9vLJpbFC6IVg": {
                "id": "sel3u9vLJpbFC6IVg",
                "name": "Patxi Barrios",
                "color": "redMedium"
            },
            "selpZ3TVYYtYf9keh": {
                "id": "selpZ3TVYYtYf9keh",
                "name": "Alex Fiestas",
                "color": "redMedium"
            },
            "selZMWM32DZR0wvQX": {
                "id": "selZMWM32DZR0wvQX",
                "name": "Brendan Wong",
                "color": "orangeDarker"
            },
            "selfNbFhZQ7tol9zz": {
                "id": "selfNbFhZQ7tol9zz",
                "name": "Khoa Phan",
                "color": "blue"
            },
            "selJM84CoyvCKA2Xk": {
                "id": "selJM84CoyvCKA2Xk",
                "name": "Denis Suslov",
                "color": "redDarker"
            },
            "selSIgSmR1nI9Rg67": {
                "id": "selSIgSmR1nI9Rg67",
                "name": "Yaroslav Madarakh",
                "color": "blue"
            },
            "selptR74xHuM94hW1": {
                "id": "selptR74xHuM94hW1",
                "name": "Kirill Suslov",
                "color": "grayDarker"
            },
            "seljgpNgqXgrB13zi": {
                "id": "seljgpNgqXgrB13zi",
                "name": "Sascha Zehe",
                "color": "orangeDarker"
            },
            "selq5RgiwSt2Tz3KD": {
                "id": "selq5RgiwSt2Tz3KD",
                "name": "Trey Kelly",
                "color": "orangeDarker"
            },
            "selXJ6rLCMdlBzyvS": {
                "id": "selXJ6rLCMdlBzyvS",
                "name": "Michael Adeyeri,",
                "color": "cyanDarker"
            },
            "sel3QCGAONGU4AePH": {
                "id": "sel3QCGAONGU4AePH",
                "name": "Michael Adeyeri",
                "color": "purple"
            },
            "selqO1nBbwswnR5PF": {
                "id": "selqO1nBbwswnR5PF",
                "name": "Moyo Sodipo",
                "color": "pinkDarker"
            },
            "seltz0imCMIGF9KPs": {
                "id": "seltz0imCMIGF9KPs",
                "name": "Canh Ho",
                "color": "cyan"
            },
            "sel5LtdI9dX2aYPTo": {
                "id": "sel5LtdI9dX2aYPTo",
                "name": " Jesse Federman",
                "color": "purpleDark"
            },
            "selRMdTr5FODFoPWB": {
                "id": "selRMdTr5FODFoPWB",
                "name": "Roberto Machado",
                "color": "yellowDarker"
            },
            "selr9b5gdc2BB65tQ": {
                "id": "selr9b5gdc2BB65tQ",
                "name": "Antonio Machado",
                "color": "blueDarker"
            },
            "sel1HaQyc5yrJMu4k": {
                "id": "sel1HaQyc5yrJMu4k",
                "name": "Bhagaban Behera",
                "color": "cyanDark"
            },
            "selijs6QAVDTWKXD7": {
                "id": "selijs6QAVDTWKXD7",
                "name": "Sriharsha Setty",
                "color": "tealDark"
            },
            "seljyL2eyku8BV9TM": {
                "id": "seljyL2eyku8BV9TM",
                "name": "Nakul Kelkar",
                "color": "red"
            },
            "selCxgPcLfuni5mgY": {
                "id": "selCxgPcLfuni5mgY",
                "name": "Michel Triana",
                "color": "cyan"
            },
            "selP7pC0W6Dh53duo": {
                "id": "selP7pC0W6Dh53duo",
                "name": "Yamel Amador Fernandez",
                "color": "blueDark"
            },
            "selbT2wSrI6N3zWZC": {
                "id": "selbT2wSrI6N3zWZC",
                "name": "Eydel Rivero Ruiz",
                "color": "cyan"
            },
            "selQ4HBMtukl8xl4O": {
                "id": "selQ4HBMtukl8xl4O",
                "name": "Yansel Florian",
                "color": "grayMedium"
            },
            "selcHM8ZxAL06zdn6": {
                "id": "selcHM8ZxAL06zdn6",
                "name": "Maylin Ramirez",
                "color": "tealDarker"
            },
            "selZDtZnc1a1ZFX9x": {
                "id": "selZDtZnc1a1ZFX9x",
                "name": "Edward Ryall",
                "color": "orangeMedium"
            },
            "sel7O5DffbTcIZPVS": {
                "id": "sel7O5DffbTcIZPVS",
                "name": "Binod Nirvan",
                "color": "orangeDark"
            },
            "seleTck80APlfk61i": {
                "id": "seleTck80APlfk61i",
                "name": "Benjamin Rameau",
                "color": "blueDark"
            },
            "sel9TfLyKjDSC3eVv": {
                "id": "sel9TfLyKjDSC3eVv",
                "name": "Maria Rys",
                "color": "grayDarker"
            },
            "seliDkfw10CsbJm5v": {
                "id": "seliDkfw10CsbJm5v",
                "name": "Andrius Normantas",
                "color": "pink"
            },
            "selN4XT4jEZQ3FBaD": {
                "id": "selN4XT4jEZQ3FBaD",
                "name": "Mirko Basil",
                "color": "tealDark"
            },
            "selEwgcR91qYsVS9b": {
                "id": "selEwgcR91qYsVS9b",
                "name": "Erik Mayer",
                "color": "cyanDark"
            },
            "sel2R6NydX3uxDHKV": {
                "id": "sel2R6NydX3uxDHKV",
                "name": "Joe Moore",
                "color": "orangeDarker"
            },
            "selJUHqxwcpdwvxBe": {
                "id": "selJUHqxwcpdwvxBe",
                "name": "Harshad Wagh",
                "color": "purpleMedium"
            },
            "selCnoqFMBybTBRh4": {
                "id": "selCnoqFMBybTBRh4",
                "name": "Ankit Kalra",
                "color": "grayDarker"
            },
            "self0zrNW97ncb8To": {
                "id": "self0zrNW97ncb8To",
                "name": "Eden Dhaliwal",
                "color": "grayDarker"
            },
            "selyTeoBxrRtsIBaS": {
                "id": "selyTeoBxrRtsIBaS",
                "name": "Dryden Brown",
                "color": "blue"
            },
            "selIRrCvgLwseQdl5": {
                "id": "selIRrCvgLwseQdl5",
                "name": "Charlie Callinan",
                "color": "pinkDark"
            },
            "sels3NnVho5SibEHU": {
                "id": "sels3NnVho5SibEHU",
                "name": "Brian Kennish",
                "color": "greenDarker"
            },
            "selI6bSwuDBvPmUx0": {
                "id": "selI6bSwuDBvPmUx0",
                "name": "Jason Grad",
                "color": "redDark"
            },
            "selIF1tucJc14Z3bS": {
                "id": "selIF1tucJc14Z3bS",
                "name": "Grant Dexter",
                "color": "purple"
            },
            "selUZ2TXvz7Eqf3rp": {
                "id": "selUZ2TXvz7Eqf3rp",
                "name": "Mike Rosenthal",
                "color": "orangeMedium"
            },
            "seli1bmgDQehX1rwc": {
                "id": "seli1bmgDQehX1rwc",
                "name": "Edward Vetri",
                "color": "yellowDarker"
            },
            "selXgf73eb15cfx7m": {
                "id": "selXgf73eb15cfx7m",
                "name": "Ev Tchebotarev",
                "color": "blue"
            },
            "selyDOlUwqEPtbEJX": {
                "id": "selyDOlUwqEPtbEJX",
                "name": "Arseniy Ivanov",
                "color": "blue"
            },
            "selxvnn3zHZ4i6bKe": {
                "id": "selxvnn3zHZ4i6bKe",
                "name": "Rob Levy",
                "color": "blue"
            },
            "selJ5PQjJnFkzQQWl": {
                "id": "selJ5PQjJnFkzQQWl",
                "name": "Anatoly Yakovenko",
                "color": "blue"
            },
            "selPM3pgc2WA3ueAi": {
                "id": "selPM3pgc2WA3ueAi",
                "name": "Raj Gokal",
                "color": "blueDark"
            },
            "seldtnYr5iqtmkrlq": {
                "id": "seldtnYr5iqtmkrlq",
                "name": "Mark Studholme",
                "color": "greenDarker"
            },
            "selMeXPnUk5wBb500": {
                "id": "selMeXPnUk5wBb500",
                "name": "Finn Hansen",
                "color": "purple"
            },
            "selmer0OFRQn8HCh5": {
                "id": "selmer0OFRQn8HCh5",
                "name": "Will Wang",
                "color": "orangeDark"
            },
            "selGiPz1jIog69Q7S": {
                "id": "selGiPz1jIog69Q7S",
                "name": "Mike Meng",
                "color": "cyanMedium"
            },
            "selAI3T66qRKKed19": {
                "id": "selAI3T66qRKKed19",
                "name": "Jinwoo Park",
                "color": "tealDark"
            },
            "selslLLgt5zQWG4Pu": {
                "id": "selslLLgt5zQWG4Pu",
                "name": "Kyungjin Kim",
                "color": "tealMedium"
            },
            "selhD3rzP06qI9Wi5": {
                "id": "selhD3rzP06qI9Wi5",
                "name": "Hyun Youn Lee",
                "color": "greenMedium"
            },
            "selIFFwlLmXEebyDz": {
                "id": "selIFFwlLmXEebyDz",
                "name": "Jansen Teng",
                "color": "cyan"
            },
            "sel8LZgXCVXLC2HWI": {
                "id": "sel8LZgXCVXLC2HWI",
                "name": "Weekee Tiew",
                "color": "grayDark"
            },
            "selGPpJ8mQaGShmi9": {
                "id": "selGPpJ8mQaGShmi9",
                "name": "Weixiong Tay ",
                "color": "pinkDark"
            },
            "sel6mhnObueZskjwz": {
                "id": "sel6mhnObueZskjwz",
                "name": "Nelly Sutjiadi",
                "color": "greenMedium"
            },
            "sel2IRYuCaTU4aOkE": {
                "id": "sel2IRYuCaTU4aOkE",
                "name": "Jack Vinijtrongjit",
                "color": "grayDark"
            },
            "selZfQJAKlEgGhJYO": {
                "id": "selZfQJAKlEgGhJYO",
                "name": "Omar Moscoso",
                "color": "purpleMedium"
            },
            "selwCuGSjBHZDVBHs": {
                "id": "selwCuGSjBHZDVBHs",
                "name": "Jayson Casinillo",
                "color": "yellowMedium"
            },
            "selHTPtJnKkV8r3pT": {
                "id": "selHTPtJnKkV8r3pT",
                "name": "Bryan Hernandez",
                "color": "blue"
            },
            "selPQV13QYCRMqpXe": {
                "id": "selPQV13QYCRMqpXe",
                "name": "Link Johnny Yang",
                "color": "blue"
            },
            "sel2eZlRa03JBLvKK": {
                "id": "sel2eZlRa03JBLvKK",
                "name": "Bryce Johnson",
                "color": "pink"
            },
            "selcsWBE6gNUieC0s": {
                "id": "selcsWBE6gNUieC0s",
                "name": "Christian Zhang",
                "color": "greenDark"
            },
            "selrxWANAfOuATTKA": {
                "id": "selrxWANAfOuATTKA",
                "name": "0xFroyo",
                "color": "orangeDarker"
            },
            "selh5xlWSqtwVIVyE": {
                "id": "selh5xlWSqtwVIVyE",
                "name": "Garrett Hughes",
                "color": "cyanDark"
            },
            "selEtjentWgm7KD9X": {
                "id": "selEtjentWgm7KD9X",
                "name": "Dwight Torculas",
                "color": "red"
            },
            "selbw1BeVd66ogEUG": {
                "id": "selbw1BeVd66ogEUG",
                "name": "Giovanni Petrantoni",
                "color": "blue"
            },
            "sellvQFdSekxwNfFl": {
                "id": "sellvQFdSekxwNfFl",
                "name": "Ivo Georgiev",
                "color": "grayDarker"
            },
            "sel8IGjRltwrzsKBa": {
                "id": "sel8IGjRltwrzsKBa",
                "name": "Silver W.X",
                "color": "tealDark"
            },
            "selqEUzIYplRPmyFU": {
                "id": "selqEUzIYplRPmyFU",
                "name": "Krystal Yang",
                "color": "cyanMedium"
            },
            "selsIGRLBYUbYKoe5": {
                "id": "selsIGRLBYUbYKoe5",
                "name": "Tony Chen",
                "color": "yellow"
            },
            "selwkdI0a5ImKoAdE": {
                "id": "selwkdI0a5ImKoAdE",
                "name": " Zhong Shao",
                "color": "pink"
            },
            "selxNWGJgkGIKaDhS": {
                "id": "selxNWGJgkGIKaDhS",
                "name": "Ronghui Gu ",
                "color": "cyan"
            },
            "seleGCO11NJJmToGg": {
                "id": "seleGCO11NJJmToGg",
                "name": "Mark Smargon",
                "color": "greenDark"
            },
            "selhYtBc4kWHYRjDz": {
                "id": "selhYtBc4kWHYRjDz",
                "name": "John Lee",
                "color": "blueMedium"
            },
            "selk8WP4WSJvXzenc": {
                "id": "selk8WP4WSJvXzenc",
                "name": "Nam Tran",
                "color": "grayDarker"
            },
            "selZ20zjbzRWTHQe7": {
                "id": "selZ20zjbzRWTHQe7",
                "name": "Henry Bach",
                "color": "green"
            },
            "seljVzr073iAz32Ub": {
                "id": "seljVzr073iAz32Ub",
                "name": "Daniel Nilsson",
                "color": "blueDark"
            },
            "selr9YSsa7iDDugB7": {
                "id": "selr9YSsa7iDDugB7",
                "name": "Jiao David",
                "color": "yellow"
            },
            "selgxB73LOmlUq5tr": {
                "id": "selgxB73LOmlUq5tr",
                "name": "Noel Braganza",
                "color": "redMedium"
            },
            "selL6xBhSwkpgBLKF": {
                "id": "selL6xBhSwkpgBLKF",
                "name": "Anjo De Heus",
                "color": "gray"
            },
            "seleMqDIIHLNpovnc": {
                "id": "seleMqDIIHLNpovnc",
                "name": "Robbert Vroegindeweij",
                "color": "purpleDarker"
            },
            "selLJJYOImE0Fx2ZR": {
                "id": "selLJJYOImE0Fx2ZR",
                "name": " John Clarke",
                "color": "greenMedium"
            },
            "selFracuVzCFVWLEI": {
                "id": "selFracuVzCFVWLEI",
                "name": "Owen Colegrove",
                "color": "greenDarker"
            },
            "selC3u6WmViscS3xH": {
                "id": "selC3u6WmViscS3xH",
                "name": "Scotty Hendricks",
                "color": "grayDark"
            },
            "selElFlLrgkFiiVji": {
                "id": "selElFlLrgkFiiVji",
                "name": "Jason Citron",
                "color": "orangeDarker"
            },
            "selgcjitroPZKpdFR": {
                "id": "selgcjitroPZKpdFR",
                "name": "John Reynolds",
                "color": "tealDarker"
            },
            "selRHlwHE5XstbBYb": {
                "id": "selRHlwHE5XstbBYb",
                "name": "Sanj Bulsara",
                "color": "yellowDarker"
            },
            "selaXVmhE43E4pgtO": {
                "id": "selaXVmhE43E4pgtO",
                "name": "Mark Adams",
                "color": "purpleDarker"
            },
            "selBPm26eED1lzRjy": {
                "id": "selBPm26eED1lzRjy",
                "name": "John Anisere",
                "color": "redDark"
            },
            "sel8Adu1D1TtkZJ1W": {
                "id": "sel8Adu1D1TtkZJ1W",
                "name": "Bashir Aminu",
                "color": "purple"
            },
            "selw6vsiSEaGKK3Zu": {
                "id": "selw6vsiSEaGKK3Zu",
                "name": "Paul Prager",
                "color": "blue"
            },
            "selkAbEfhB4uYlFur": {
                "id": "selkAbEfhB4uYlFur",
                "name": "Jack Nolan",
                "color": "purple"
            },
            "selP4EhqxsWOrHzjX": {
                "id": "selP4EhqxsWOrHzjX",
                "name": "Domenic Carosa",
                "color": "redDarker"
            },
            "sel7fMPnBxRfSnlhb": {
                "id": "sel7fMPnBxRfSnlhb",
                "name": "Sebastian",
                "color": "pink"
            },
            "selDfurkIx0a9Dvlh": {
                "id": "selDfurkIx0a9Dvlh",
                "name": "Alexis Masseron",
                "color": "cyanDark"
            },
            "selkleuUQm8HauWgV": {
                "id": "selkleuUQm8HauWgV",
                "name": "Stephane Coquet",
                "color": "cyan"
            },
            "sel6MiZ66SQXB01Y8": {
                "id": "sel6MiZ66SQXB01Y8",
                "name": "Charlotte Eli",
                "color": "green"
            },
            "selMuFGiCmAVR5mpt": {
                "id": "selMuFGiCmAVR5mpt",
                "name": "Andrii Yasinetsky",
                "color": "grayDarker"
            },
            "selqhooVboxeN8baL": {
                "id": "selqhooVboxeN8baL",
                "name": "Ben Metcalfe",
                "color": "yellowDark"
            },
            "selTkIURx1gVeyq4J": {
                "id": "selTkIURx1gVeyq4J",
                "name": "Alex Kehaya",
                "color": "cyan"
            },
            "sel26tHMmPkWYP3aP": {
                "id": "sel26tHMmPkWYP3aP",
                "name": "Simon Jones",
                "color": "redDarker"
            },
            "sel82mxoeXaGOVv7l": {
                "id": "sel82mxoeXaGOVv7l",
                "name": "Artur Begyan",
                "color": "purpleMedium"
            },
            "selABVJrxKjq42A2c": {
                "id": "selABVJrxKjq42A2c",
                "name": "Bradian Muliadi",
                "color": "yellowMedium"
            },
            "sel1mat6eOwYTZegO": {
                "id": "sel1mat6eOwYTZegO",
                "name": "Lorenzo Ampil",
                "color": "blueDark"
            },
            "sel57E88KhULOZsCp": {
                "id": "sel57E88KhULOZsCp",
                "name": "Dave McGibbon",
                "color": "pinkDarker"
            },
            "selH7fUaoEl0l43TH": {
                "id": "selH7fUaoEl0l43TH",
                "name": "Mathias Klenk",
                "color": "pinkDark"
            },
            "selvh0jM3hgDlFFB7": {
                "id": "selvh0jM3hgDlFFB7",
                "name": "Felix Gerlach",
                "color": "teal"
            },
            "selRTCNotTcbfDRxt": {
                "id": "selRTCNotTcbfDRxt",
                "name": "Julien Bouteloup",
                "color": "redDarker"
            },
            "selwTwtMhUNNEGAhK": {
                "id": "selwTwtMhUNNEGAhK",
                "name": "Sharaf Nassar ",
                "color": "purpleMedium"
            },
            "sel8pJbvkMGffwUpB": {
                "id": "sel8pJbvkMGffwUpB",
                "name": " Anand Gomes",
                "color": "tealDarker"
            },
            "selnNVhZxN610RVkZ": {
                "id": "selnNVhZxN610RVkZ",
                "name": "Will Deane",
                "color": "purpleMedium"
            },
            "selT9f0Auc4E0f8e9": {
                "id": "selT9f0Auc4E0f8e9",
                "name": "Tri Pham",
                "color": "yellowMedium"
            },
            "seloTW7ZtM738G1D7": {
                "id": "seloTW7ZtM738G1D7",
                "name": "Clinton Bembry",
                "color": "blue"
            },
            "seleTcf3FHzI7cEib": {
                "id": "seleTcf3FHzI7cEib",
                "name": "Ian Place",
                "color": "blue"
            },
            "selw03h2HihuN4iEp": {
                "id": "selw03h2HihuN4iEp",
                "name": "Osama Khan",
                "color": "orangeDarker"
            },
            "selb93pN5wbjuKEh4": {
                "id": "selb93pN5wbjuKEh4",
                "name": "Matthew Harrison",
                "color": "cyanDark"
            },
            "seluEDtj2ls9CkyYG": {
                "id": "seluEDtj2ls9CkyYG",
                "name": "Daniel Heyman",
                "color": "tealDark"
            },
            "selFJ1mMwv4cyCB4C": {
                "id": "selFJ1mMwv4cyCB4C",
                "name": "Evan Spytma",
                "color": "blue"
            },
            "selBtZyXCWL5xyQqu": {
                "id": "selBtZyXCWL5xyQqu",
                "name": "Irene Umar",
                "color": "yellow"
            },
            "selZ5vdA2ltkL76eq": {
                "id": "selZ5vdA2ltkL76eq",
                "name": "Dan Wang",
                "color": "green"
            },
            "selGGNZrE8atnQxH7": {
                "id": "selGGNZrE8atnQxH7",
                "name": "Artem Lazarev",
                "color": "blue"
            },
            "selHz3Ww8PfGl47Rf": {
                "id": "selHz3Ww8PfGl47Rf",
                "name": "Andriy Bohutsky",
                "color": "blueMedium"
            },
            "seltm7CPbFOSuz2lt": {
                "id": "seltm7CPbFOSuz2lt",
                "name": "Joao Borges",
                "color": "cyanDark"
            },
            "selxNBD2N3moeeiB6": {
                "id": "selxNBD2N3moeeiB6",
                "name": "Matt Rutledge",
                "color": "cyanMedium"
            },
            "sel9QXXL4ybLsRS4H": {
                "id": "sel9QXXL4ybLsRS4H",
                "name": "Evelyn Mora",
                "color": "orangeDark"
            },
            "selLQ43qVm5wis1y4": {
                "id": "selLQ43qVm5wis1y4",
                "name": "Mathew Nguyen",
                "color": "blue"
            },
            "selaszRct82zk2eAn": {
                "id": "selaszRct82zk2eAn",
                "name": "Austin Roberts",
                "color": "blue"
            },
            "selI5y36XRZW1QKRw": {
                "id": "selI5y36XRZW1QKRw",
                "name": "Greg Lang",
                "color": "tealDarker"
            },
            "selxbPdI2QmRc2IBh": {
                "id": "selxbPdI2QmRc2IBh",
                "name": "Beth Van Horn",
                "color": "purpleMedium"
            },
            "seloptAjHiuiHio1F": {
                "id": "seloptAjHiuiHio1F",
                "name": "Audrey Raby",
                "color": "orange"
            },
            "selcnDSfCUzO3Q7SA": {
                "id": "selcnDSfCUzO3Q7SA",
                "name": "Patrick Poirier",
                "color": "green"
            },
            "selPCngm8jt9LCdg7": {
                "id": "selPCngm8jt9LCdg7",
                "name": "Ahmet Ozcan",
                "color": "grayDarker"
            },
            "selCHHg3o3s7Bst60": {
                "id": "selCHHg3o3s7Bst60",
                "name": "Sam Green",
                "color": "blueDarker"
            },
            "selDsg1X7U6VRwH6n": {
                "id": "selDsg1X7U6VRwH6n",
                "name": "Gokay Saldamli",
                "color": "orangeDarker"
            },
            "selwPWGyitGUimgZ2": {
                "id": "selwPWGyitGUimgZ2",
                "name": "Alexis Asseman",
                "color": "grayMedium"
            },
            "selWDsIIpjWyE9P5S": {
                "id": "selWDsIIpjWyE9P5S",
                "name": "Lucaz Lee",
                "color": "orangeDarker"
            },
            "selTrlCVE1BgGAFyM": {
                "id": "selTrlCVE1BgGAFyM",
                "name": "Justin Gorriceta-Banusing",
                "color": "purpleDarker"
            },
            "selvecXXC2YDZP39t": {
                "id": "selvecXXC2YDZP39t",
                "name": "Kevin Hoang",
                "color": "blueDark"
            },
            "seltHpvLbI0l7mdFC": {
                "id": "seltHpvLbI0l7mdFC",
                "name": "Ariane Lim",
                "color": "purpleDark"
            },
            "selLuROC2YkOxufCJ": {
                "id": "selLuROC2YkOxufCJ",
                "name": "Jeanne Anderson",
                "color": "cyan"
            },
            "selgI0nHu3RdPZ6lM": {
                "id": "selgI0nHu3RdPZ6lM",
                "name": "Hernan Lopez ",
                "color": "grayDarker"
            },
            "sel0xWxKKWzRNDI12": {
                "id": "sel0xWxKKWzRNDI12",
                "name": "Louis Nguyen",
                "color": "blue"
            },
            "selzlju7iC4vZPzec": {
                "id": "selzlju7iC4vZPzec",
                "name": "Rodrigo Etcheto",
                "color": "grayMedium"
            },
            "sel1Yf1JnP3hzIT7r": {
                "id": "sel1Yf1JnP3hzIT7r",
                "name": "Clement Wong",
                "color": "greenDark"
            },
            "selMBPrURAG6GN68z": {
                "id": "selMBPrURAG6GN68z",
                "name": "Mark Harris",
                "color": "redMedium"
            },
            "selJ4gGB6wbKYhwqJ": {
                "id": "selJ4gGB6wbKYhwqJ",
                "name": "Tobias Batton",
                "color": "green"
            },
            "selOb4iwavU7OGHYp": {
                "id": "selOb4iwavU7OGHYp",
                "name": "Anand Agarwala",
                "color": "redDark"
            },
            "sel4WeG41NN0795OW": {
                "id": "sel4WeG41NN0795OW",
                "name": "Jinha Lee",
                "color": "orangeDarker"
            },
            "selOmmOWP1o3tCPpg": {
                "id": "selOmmOWP1o3tCPpg",
                "name": "Przemek Kowalczyk",
                "color": "blue"
            },
            "selTvbRRkg4R7LBV0": {
                "id": "selTvbRRkg4R7LBV0",
                "name": "David Greenstein",
                "color": "greenDark"
            },
            "selZR972rFoNILvz2": {
                "id": "selZR972rFoNILvz2",
                "name": "Vignesh Hirudayakanth",
                "color": "tealMedium"
            },
            "selalKcoHewaqk2tj": {
                "id": "selalKcoHewaqk2tj",
                "name": " Matt Masurka",
                "color": "greenDarker"
            },
            "sel5zCoB7tPdnjg86": {
                "id": "sel5zCoB7tPdnjg86",
                "name": "Aaron Yee",
                "color": "blueMedium"
            },
            "selCQ1x1g3F5fK0k7": {
                "id": "selCQ1x1g3F5fK0k7",
                "name": "Tin Tran",
                "color": "orangeDarker"
            },
            "selTj8FPJleEBvW2y": {
                "id": "selTj8FPJleEBvW2y",
                "name": "Kevin Bui",
                "color": "blueDark"
            },
            "sel1J1Zf2tLDjxzLm": {
                "id": "sel1J1Zf2tLDjxzLm",
                "name": "Jeffrey Jordan",
                "color": "yellowDark"
            },
            "selShHUgz8AgLQIlB": {
                "id": "selShHUgz8AgLQIlB",
                "name": "Daniel George",
                "color": "orangeDarker"
            },
            "seljDMtp6isfaVg5h": {
                "id": "seljDMtp6isfaVg5h",
                "name": "Jeron Smith",
                "color": "redMedium"
            },
            "sel2hmnYCfKoOi3PE": {
                "id": "sel2hmnYCfKoOi3PE",
                "name": "Nicolas Burtey",
                "color": "gray"
            },
            "selXh4Te8Df53M90C": {
                "id": "selXh4Te8Df53M90C",
                "name": "Chris Hunter",
                "color": "yellowDark"
            },
            "sel9viSoF19yC3o4G": {
                "id": "sel9viSoF19yC3o4G",
                "name": "Asad J. Malik",
                "color": "cyan"
            },
            "selKKI9yc35LNLkjn": {
                "id": "selKKI9yc35LNLkjn",
                "name": "Jay Jaehyun Park",
                "color": "blue"
            },
            "selluPcd3WXmPHhpw": {
                "id": "selluPcd3WXmPHhpw",
                "name": "Mary Gooneratne ",
                "color": "green"
            },
            "selyOeIjkfLrzQrJO": {
                "id": "selyOeIjkfLrzQrJO",
                "name": "Luke Truitt",
                "color": "purpleDarker"
            },
            "selKWqK0kLzi8JnbY": {
                "id": "selKWqK0kLzi8JnbY",
                "name": "Lorne Lantz",
                "color": "purpleDark"
            },
            "selPlUEs3Mrnzj4wk": {
                "id": "selPlUEs3Mrnzj4wk",
                "name": "Marius Thomas",
                "color": "gray"
            },
            "selYMSfQ4I1c7ySYg": {
                "id": "selYMSfQ4I1c7ySYg",
                "name": "Soren Macbeth",
                "color": "grayDark"
            },
            "selNHPkNXpZrvXQLY": {
                "id": "selNHPkNXpZrvXQLY",
                "name": "Howard Lindzon",
                "color": "teal"
            },
            "selWCUKXwfcvYZsWT": {
                "id": "selWCUKXwfcvYZsWT",
                "name": "Marcus Bl\u00e4sche",
                "color": "redDarker"
            },
            "selW3pIqhfk9Il53Y": {
                "id": "selW3pIqhfk9Il53Y",
                "name": "Nick Vale",
                "color": "purpleDarker"
            },
            "selBiEzNNsWBFbWtQ": {
                "id": "selBiEzNNsWBFbWtQ",
                "name": "Chan Lee",
                "color": "cyanDarker"
            },
            "sel2YGsT1Cq5CzDqi": {
                "id": "sel2YGsT1Cq5CzDqi",
                "name": "Merijn Terheggen",
                "color": "orangeMedium"
            },
            "selGZ4n4UuWxrLhtQ": {
                "id": "selGZ4n4UuWxrLhtQ",
                "name": "Suruchi Gupta",
                "color": "gray"
            },
            "selv2693rpUkLITjo": {
                "id": "selv2693rpUkLITjo",
                "name": "Jinesh Doshi",
                "color": "greenDark"
            },
            "selWsHzlYJyDebHvG": {
                "id": "selWsHzlYJyDebHvG",
                "name": "Long Vuong ",
                "color": "redDarker"
            },
            "sel5p4ZlzhhoN4iLk": {
                "id": "sel5p4ZlzhhoN4iLk",
                "name": "Natthapol Assarasakorn",
                "color": "pinkDarker"
            },
            "selWbrcClUoY4BQFA": {
                "id": "selWbrcClUoY4BQFA",
                "name": "Sunil Hirani",
                "color": "grayMedium"
            },
            "seltGl8BJapOtxX3m": {
                "id": "seltGl8BJapOtxX3m",
                "name": "Steven Bartlett",
                "color": "grayMedium"
            },
            "selqxUmiwZe3vfOZW": {
                "id": "selqxUmiwZe3vfOZW",
                "name": "Furqan Rydhan",
                "color": "greenMedium"
            },
            "sel1Zht04PmIoEPBd": {
                "id": "sel1Zht04PmIoEPBd",
                "name": "Drew Orsinger",
                "color": "teal"
            },
            "selC4JkupKtARtxG6": {
                "id": "selC4JkupKtARtxG6",
                "name": "Trevor Orsinger",
                "color": "cyanDark"
            },
            "selaldCSPsXWqr9sW": {
                "id": "selaldCSPsXWqr9sW",
                "name": "Jorge Soriano",
                "color": "redDark"
            },
            "selmTqOF5sQoMeSDn": {
                "id": "selmTqOF5sQoMeSDn",
                "name": "Jaume Sola",
                "color": "cyanMedium"
            },
            "selVkq3kuFJlGh170": {
                "id": "selVkq3kuFJlGh170",
                "name": "Beka Kemertelidze",
                "color": "yellow"
            },
            "selDjKLn5xYZGyFVM": {
                "id": "selDjKLn5xYZGyFVM",
                "name": "Eralf Hatipoglu",
                "color": "pink"
            },
            "selqldf0MxRbZkZTX": {
                "id": "selqldf0MxRbZkZTX",
                "name": "Emin Budak",
                "color": "red"
            },
            "self2JewlJeK0WHYp": {
                "id": "self2JewlJeK0WHYp",
                "name": "Alex Migitko",
                "color": "grayMedium"
            },
            "selDpGpSwTIp4fQcQ": {
                "id": "selDpGpSwTIp4fQcQ",
                "name": "Uros Sosevic",
                "color": "orange"
            },
            "selQxuhdCIx469X5h": {
                "id": "selQxuhdCIx469X5h",
                "name": "Martin Kardzhilov",
                "color": "redDark"
            },
            "selerbF290BJHfocW": {
                "id": "selerbF290BJHfocW",
                "name": "Vincent Li",
                "color": "tealDark"
            },
            "selY5XxcaiwQUGc5m": {
                "id": "selY5XxcaiwQUGc5m",
                "name": "Jesse Redniss",
                "color": "yellowDark"
            },
            "selPb0M8Uuh4r3LxM": {
                "id": "selPb0M8Uuh4r3LxM",
                "name": "Yohji S",
                "color": "purpleMedium"
            },
            "selNNG3Z7IikNTYi5": {
                "id": "selNNG3Z7IikNTYi5",
                "name": "Erfan Isaac",
                "color": "grayMedium"
            },
            "selpynQNCnzRsWBBW": {
                "id": "selpynQNCnzRsWBBW",
                "name": "George Chuang",
                "color": "tealDarker"
            },
            "selhDeXfhJcIo9BLz": {
                "id": "selhDeXfhJcIo9BLz",
                "name": "Jakub Rehor",
                "color": "purpleMedium"
            },
            "selfoySXTo6rNJETw": {
                "id": "selfoySXTo6rNJETw",
                "name": "Robert Mah",
                "color": "gray"
            },
            "selAn8sbcrrgxg63c": {
                "id": "selAn8sbcrrgxg63c",
                "name": "Fleur Heyns",
                "color": "tealDarker"
            },
            "seluXzbOySoEfJyWb": {
                "id": "seluXzbOySoEfJyWb",
                "name": "Kevin Petit",
                "color": "purpleDark"
            },
            "selHdfX22o17vUVnP": {
                "id": "selHdfX22o17vUVnP",
                "name": "Brett Jones",
                "color": "gray"
            },
            "selETAwtJYobfg982": {
                "id": "selETAwtJYobfg982",
                "name": "Brent Lane",
                "color": "greenDarker"
            },
            "seluhTv4voQPe4iGA": {
                "id": "seluhTv4voQPe4iGA",
                "name": "Andrew Moss",
                "color": "orangeMedium"
            },
            "selByVaIu1CFEpfZM": {
                "id": "selByVaIu1CFEpfZM",
                "name": "Cedric Gautier",
                "color": "redDarker"
            },
            "sel8ymsCIMZTrN5FI": {
                "id": "sel8ymsCIMZTrN5FI",
                "name": "Nikolay Volf",
                "color": "cyanDarker"
            },
            "selJ7OFRlK9pXvr5U": {
                "id": "selJ7OFRlK9pXvr5U",
                "name": "Gabe Frank",
                "color": "blue"
            },
            "selbwxuYX8CKF0wOp": {
                "id": "selbwxuYX8CKF0wOp",
                "name": "Zhaojun",
                "color": "redMedium"
            },
            "seluk6ZhCIDYBOscH": {
                "id": "seluk6ZhCIDYBOscH",
                "name": "Thomas Bohner",
                "color": "cyan"
            },
            "selOdggGkVdeB3Mik": {
                "id": "selOdggGkVdeB3Mik",
                "name": "Maxim Piessen",
                "color": "yellowDark"
            },
            "seluaHF0oJVJZEuzg": {
                "id": "seluaHF0oJVJZEuzg",
                "name": "Chaim Finizola",
                "color": "green"
            },
            "selUm8a1WkcqcehQi": {
                "id": "selUm8a1WkcqcehQi",
                "name": "Alexei Zamyatin",
                "color": "blue"
            },
            "selgPNX0IcJ6fTTXW": {
                "id": "selgPNX0IcJ6fTTXW",
                "name": "Dominik Harz",
                "color": "cyan"
            },
            "selYcblhS4viaSAZS": {
                "id": "selYcblhS4viaSAZS",
                "name": "Kanav Singla",
                "color": "blue"
            },
            "sellBe17Ia1UJwpQG": {
                "id": "sellBe17Ia1UJwpQG",
                "name": "Prashant Sinha",
                "color": "cyan"
            },
            "selFJ7udBezcLDYhL": {
                "id": "selFJ7udBezcLDYhL",
                "name": "Shorya Mahajan",
                "color": "teal"
            },
            "selZGSVdSQWbY4fUa": {
                "id": "selZGSVdSQWbY4fUa",
                "name": "Herman Jacobs",
                "color": "blue"
            },
            "sel5jRNrjqY4xZeiF": {
                "id": "sel5jRNrjqY4xZeiF",
                "name": "David Nunn",
                "color": "blue"
            },
            "seloLBqfoNwfcNyM9": {
                "id": "seloLBqfoNwfcNyM9",
                "name": "Abhishek Singh Rajpurohit",
                "color": "blue"
            },
            "sels5CILMGRFSHFRW": {
                "id": "sels5CILMGRFSHFRW",
                "name": "Kuntal Ganguly",
                "color": "cyan"
            },
            "selmsRwT9NbjGq75W": {
                "id": "selmsRwT9NbjGq75W",
                "name": "Yash Dahenkar",
                "color": "teal"
            },
            "selUvRLYbg1dHteZm": {
                "id": "selUvRLYbg1dHteZm",
                "name": "Joshua Meteora",
                "color": "pink"
            },
            "sel6YYHi1U51Fbiy4": {
                "id": "sel6YYHi1U51Fbiy4",
                "name": "Serge Gianchandani",
                "color": "purple"
            },
            "selYni4zWaRvfenpy": {
                "id": "selYni4zWaRvfenpy",
                "name": "Sahan Ray",
                "color": "blue"
            },
            "selWsbNJC5ly6B8h4": {
                "id": "selWsbNJC5ly6B8h4",
                "name": "Vincent Geneste",
                "color": "orangeDarker"
            },
            "selgbEayHgGIJgd9g": {
                "id": "selgbEayHgGIJgd9g",
                "name": "Mathias Enzensberger",
                "color": "blueDark"
            },
            "selPaRt5gJzzGtetT": {
                "id": "selPaRt5gJzzGtetT",
                "name": "Aleksandr Paukonen",
                "color": "pinkDarker"
            },
            "selrvYmnR2Ftxkncd": {
                "id": "selrvYmnR2Ftxkncd",
                "name": "Pau Vivancos",
                "color": "gray"
            },
            "sellZAJGaxAoQwG4t": {
                "id": "sellZAJGaxAoQwG4t",
                "name": "Jules Urbach",
                "color": "blue"
            },
            "selRIWDIny7Yd2sZD": {
                "id": "selRIWDIny7Yd2sZD",
                "name": "Julian Rodriguez",
                "color": "greenDark"
            },
            "selnBVZEL6zd3xt2h": {
                "id": "selnBVZEL6zd3xt2h",
                "name": "Ahmed Salam",
                "color": "cyanDark"
            },
            "selVBUrX6zExKAWSu": {
                "id": "selVBUrX6zExKAWSu",
                "name": "Kenneth Lee",
                "color": "pinkMedium"
            },
            "selMo6z5DNMXZJoYA": {
                "id": "selMo6z5DNMXZJoYA",
                "name": "Batis Samadian",
                "color": "green"
            },
            "selU2xphgCGSDKEP0": {
                "id": "selU2xphgCGSDKEP0",
                "name": "Filipe Macedo",
                "color": "yellowDark"
            },
            "selbGWmWi3cR98X5T": {
                "id": "selbGWmWi3cR98X5T",
                "name": "Pedro Carmo Oliveira",
                "color": "purpleDarker"
            },
            "selBfbyu9hPK09DxI": {
                "id": "selBfbyu9hPK09DxI",
                "name": "Cliff Yung",
                "color": "greenDarker"
            },
            "selAyz1R9jIObE1FE": {
                "id": "selAyz1R9jIObE1FE",
                "name": "Leo Tan",
                "color": "red"
            },
            "sel2Q8VYNINgwKUPk": {
                "id": "sel2Q8VYNINgwKUPk",
                "name": "Lionel Yuan",
                "color": "redDarker"
            },
            "selFtgZwBdyj8IWzu": {
                "id": "selFtgZwBdyj8IWzu",
                "name": "WJ Veron",
                "color": "tealMedium"
            },
            "selgc0swM58j9eCPd": {
                "id": "selgc0swM58j9eCPd",
                "name": "Catherine Su",
                "color": "purpleMedium"
            },
            "selNWjUuXjANuQCj2": {
                "id": "selNWjUuXjANuQCj2",
                "name": "Maximilian Stoeckl",
                "color": "blue"
            },
            "selzKCduqHvjSYmfN": {
                "id": "selzKCduqHvjSYmfN",
                "name": "Kristofer Dayne Penseyres",
                "color": "cyanMedium"
            },
            "selT0g33y73wWNUrE": {
                "id": "selT0g33y73wWNUrE",
                "name": "Bilal El Alamy",
                "color": "yellow"
            },
            "selkdNPEezmTnPoKG": {
                "id": "selkdNPEezmTnPoKG",
                "name": "Juan Ibagon",
                "color": "yellowDarker"
            },
            "selhG5EP2aktUDdZs": {
                "id": "selhG5EP2aktUDdZs",
                "name": "Kevin",
                "color": "blueDarker"
            },
            "sel23PcAGnnR4ilSo": {
                "id": "sel23PcAGnnR4ilSo",
                "name": "Vanessa ",
                "color": "blueMedium"
            },
            "sel5brn6S0rTDKcQb": {
                "id": "sel5brn6S0rTDKcQb",
                "name": "Franky",
                "color": "yellowDark"
            },
            "selCYvvSkHdgVSc3U": {
                "id": "selCYvvSkHdgVSc3U",
                "name": "Cynthia Wandia",
                "color": "purpleDark"
            },
            "sellnLO126yham0D0": {
                "id": "sellnLO126yham0D0",
                "name": "David Hwan",
                "color": "blueDarker"
            },
            "sel3qyE5xx24ZM1C3": {
                "id": "sel3qyE5xx24ZM1C3",
                "name": "Jean Amiouny",
                "color": "pinkDarker"
            },
            "selaCzGZXk2QYtKBu": {
                "id": "selaCzGZXk2QYtKBu",
                "name": "Roy Breidi",
                "color": "yellow"
            },
            "selQupxMZazRrBQDc": {
                "id": "selQupxMZazRrBQDc",
                "name": "Timmu T\u00f5ke",
                "color": "purpleDarker"
            },
            "sel9viqm1lQvWgog2": {
                "id": "sel9viqm1lQvWgog2",
                "name": "Kaspar Tiri",
                "color": "blueDark"
            },
            "selrnERzeZcyiuT5R": {
                "id": "selrnERzeZcyiuT5R",
                "name": "Orlando Nandito",
                "color": "blue"
            },
            "selzZTSYblzpLEdBk": {
                "id": "selzZTSYblzpLEdBk",
                "name": "Anargya Simson",
                "color": "grayDark"
            },
            "selzCmoqQ2qinB5W7": {
                "id": "selzCmoqQ2qinB5W7",
                "name": "Alexander Lim",
                "color": "orange"
            },
            "selm6C0JtGdiZuJMM": {
                "id": "selm6C0JtGdiZuJMM",
                "name": "Matija Rosovic",
                "color": "tealMedium"
            },
            "seltJBr6frtMPtdN9": {
                "id": "seltJBr6frtMPtdN9",
                "name": "Noman Rasheed",
                "color": "cyanDark"
            },
            "selja6F46onTW7emt": {
                "id": "selja6F46onTW7emt",
                "name": "Alvin Lam  ",
                "color": "cyanDark"
            },
            "sel29JcNBMLj7apAF": {
                "id": "sel29JcNBMLj7apAF",
                "name": "Cholo Maputol",
                "color": "cyan"
            },
            "selszs1kIIR0oqTIB": {
                "id": "selszs1kIIR0oqTIB",
                "name": "Janze de Guzman",
                "color": "cyanDarker"
            },
            "selPTQiZguHABli5e": {
                "id": "selPTQiZguHABli5e",
                "name": "Rupert Sy Cabrera",
                "color": "pinkMedium"
            },
            "seloDBGno0QaAurPH": {
                "id": "seloDBGno0QaAurPH",
                "name": "Paolo Niccolo Santos",
                "color": "redDark"
            },
            "selJWXKlqP4tAXAJa": {
                "id": "selJWXKlqP4tAXAJa",
                "name": "Emiliano Grodzki",
                "color": "grayDark"
            },
            "selsqWp7ANckjdPQy": {
                "id": "selsqWp7ANckjdPQy",
                "name": "Amos Whitewolf ",
                "color": "orangeMedium"
            },
            "sel7T9dqp0O418zSx": {
                "id": "sel7T9dqp0O418zSx",
                "name": "Mitch Penman-Allen",
                "color": "orangeDark"
            },
            "selxUPyPgQUkxoFbv": {
                "id": "selxUPyPgQUkxoFbv",
                "name": "Jan Hartmann ",
                "color": "teal"
            },
            "selidhBNpN08atCWU": {
                "id": "selidhBNpN08atCWU",
                "name": " Aaron Kirshenberg",
                "color": "redDarker"
            },
            "sel6F6cvBYuUlDWM2": {
                "id": "sel6F6cvBYuUlDWM2",
                "name": " Nicholas Amos",
                "color": "tealDarker"
            },
            "selz3dUaR44RAzTCf": {
                "id": "selz3dUaR44RAzTCf",
                "name": "Michael Padilla",
                "color": "grayDark"
            },
            "sel7rsZ7qpuEjvJIO": {
                "id": "sel7rsZ7qpuEjvJIO",
                "name": "Shier ",
                "color": "tealDarker"
            },
            "seldE5clu5UziqJ2U": {
                "id": "seldE5clu5UziqJ2U",
                "name": "Zack",
                "color": "yellowDark"
            },
            "selYqmBaeeNS57Uf0": {
                "id": "selYqmBaeeNS57Uf0",
                "name": "Max Chamberlin",
                "color": "greenDark"
            },
            "selu8OVEoamMDDlke": {
                "id": "selu8OVEoamMDDlke",
                "name": "Alessandro Rietmann",
                "color": "green"
            },
            "selU4Ch5zcjNdMvoL": {
                "id": "selU4Ch5zcjNdMvoL",
                "name": "Tejas Thole",
                "color": "redDarker"
            },
            "selzuEjF4VSl4Zx5j": {
                "id": "selzuEjF4VSl4Zx5j",
                "name": "Jake Kim",
                "color": "grayMedium"
            },
            "sellHUQ9IhVs55zK6": {
                "id": "sellHUQ9IhVs55zK6",
                "name": "Dmitry Tolok",
                "color": "greenDark"
            },
            "selM6LI2xsUnbzidB": {
                "id": "selM6LI2xsUnbzidB",
                "name": "Vlad Kostanda",
                "color": "cyanDarker"
            },
            "selkULX5uE9L5M2lh": {
                "id": "selkULX5uE9L5M2lh",
                "name": " Chris Tramount",
                "color": "green"
            },
            "selC0eT8NNzjMUVTL": {
                "id": "selC0eT8NNzjMUVTL",
                "name": "Aryan Jabbari ",
                "color": "grayMedium"
            },
            "selWiUqilWGQfvV5L": {
                "id": "selWiUqilWGQfvV5L",
                "name": "Tang Hongbo",
                "color": "redDark"
            },
            "selQgxu8v64bnlx83": {
                "id": "selQgxu8v64bnlx83",
                "name": "Willy Lionel Pomathios",
                "color": "pinkDarker"
            },
            "selfLPs69v3Xg3CJR": {
                "id": "selfLPs69v3Xg3CJR",
                "name": "Alex Zhu",
                "color": "grayDark"
            },
            "sel6tK9jcFDCnJ11F": {
                "id": "sel6tK9jcFDCnJ11F",
                "name": "Ervin Zhuang",
                "color": "cyanMedium"
            },
            "selphXLXPwB7FPoBa": {
                "id": "selphXLXPwB7FPoBa",
                "name": "Daniel Schmerin",
                "color": "blue"
            },
            "selXdmF7VaJU9Dbbh": {
                "id": "selXdmF7VaJU9Dbbh",
                "name": "Yossi Hasson",
                "color": "tealMedium"
            },
            "seluvB3m6HPmIhsE6": {
                "id": "seluvB3m6HPmIhsE6",
                "name": " Snehal Fulzele",
                "color": "grayDarker"
            },
            "selG29SrLCkbAWBte": {
                "id": "selG29SrLCkbAWBte",
                "name": " Fred Brothers",
                "color": "greenDarker"
            },
            "sel3EAtDeAFy8WFlO": {
                "id": "sel3EAtDeAFy8WFlO",
                "name": "Arpit Agrawal",
                "color": "yellowMedium"
            },
            "selwN4KqhiA3uxUY2": {
                "id": "selwN4KqhiA3uxUY2",
                "name": "Kien Vuong",
                "color": "yellowDarker"
            },
            "sel5K9HMncvdTHYDs": {
                "id": "sel5K9HMncvdTHYDs",
                "name": "Joffrey Dalet ",
                "color": "cyan"
            },
            "selhzGMdFXcizzjip": {
                "id": "selhzGMdFXcizzjip",
                "name": "Alexander Trefonas",
                "color": "blue"
            },
            "selu8Xl8JhXCgiESC": {
                "id": "selu8Xl8JhXCgiESC",
                "name": "Mathias Imbach",
                "color": "blue"
            },
            "selgDI2G6UHp57JeY": {
                "id": "selgDI2G6UHp57JeY",
                "name": "Gerald Goh",
                "color": "gray"
            },
            "selUWGVBqWO4YdQyX": {
                "id": "selUWGVBqWO4YdQyX",
                "name": "Luka Muller",
                "color": "pinkDark"
            },
            "seljTeRZDLe0VUCMN": {
                "id": "seljTeRZDLe0VUCMN",
                "name": "Jacob Ballou",
                "color": "pinkMedium"
            },
            "seltDrnQkoACjdeKT": {
                "id": "seltDrnQkoACjdeKT",
                "name": "Sean Guthrie",
                "color": "purpleDarker"
            },
            "selZm6ozldKFyoFDb": {
                "id": "selZm6ozldKFyoFDb",
                "name": " Mar\u00eda Paula Fern\u00e1ndez",
                "color": "cyanDark"
            },
            "seluImwUhob8rWCss": {
                "id": "seluImwUhob8rWCss",
                "name": "Trent Elmore",
                "color": "yellowMedium"
            },
            "selnLNS02uUGLKLi7": {
                "id": "selnLNS02uUGLKLi7",
                "name": "Michael O'Rourke ",
                "color": "purpleDark"
            },
            "selUETmqpX0H6rE3T": {
                "id": "selUETmqpX0H6rE3T",
                "name": "Sam Hotchkiss",
                "color": "cyanDarker"
            },
            "sel6sYA7KNGk7A7bS": {
                "id": "sel6sYA7KNGk7A7bS",
                "name": "Brian Krogsgard",
                "color": "cyanDark"
            },
            "sel8TzZjQifS2mPbp": {
                "id": "sel8TzZjQifS2mPbp",
                "name": "Jennifer Jacobs",
                "color": "green"
            },
            "selvyCe7z4kfFm7i3": {
                "id": "selvyCe7z4kfFm7i3",
                "name": "Jaime Leverton",
                "color": "blue"
            },
            "selD922L0cKVHb557": {
                "id": "selD922L0cKVHb557",
                "name": "Marc van der Chijs",
                "color": "blue"
            },
            "selq0pBfa9Jn7E37Q": {
                "id": "selq0pBfa9Jn7E37Q",
                "name": "Ferdinando M. Ametrano",
                "color": "gray"
            },
            "selvwwWGEAqBqC3PS": {
                "id": "selvwwWGEAqBqC3PS",
                "name": "Paolo Mazzocchi",
                "color": "blue"
            },
            "selVnMtmvXXpROEg4": {
                "id": "selVnMtmvXXpROEg4",
                "name": "Danny Hayes",
                "color": "cyanDark"
            },
            "sel6elwwv1mK8xsGb": {
                "id": "sel6elwwv1mK8xsGb",
                "name": "Soheila Yalpani",
                "color": "greenDarker"
            },
            "seltydP1iusNHUUSL": {
                "id": "seltydP1iusNHUUSL",
                "name": "Philip Eggen",
                "color": "gray"
            },
            "sel8r6pi0rmXVs6U9": {
                "id": "sel8r6pi0rmXVs6U9",
                "name": "Theodore Rozencwajg",
                "color": "green"
            },
            "sel20v1nWpEjGnXBS": {
                "id": "sel20v1nWpEjGnXBS",
                "name": "Don van der Krogt",
                "color": "purpleDark"
            },
            "sely3QdCnAMx6CeXz": {
                "id": "sely3QdCnAMx6CeXz",
                "name": "Laetitia Grimaud",
                "color": "cyanDark"
            },
            "selR9a1Z1H0CoaVoq": {
                "id": "selR9a1Z1H0CoaVoq",
                "name": "Anuj Kumar Kodam",
                "color": "blue"
            },
            "selbGYL8W3i8wNhvh": {
                "id": "selbGYL8W3i8wNhvh",
                "name": "Amarnath JV",
                "color": "blue"
            },
            "selP95Y5BHg9GrQ1Y": {
                "id": "selP95Y5BHg9GrQ1Y",
                "name": "Rosa Shores",
                "color": "purpleDark"
            },
            "selyG7B3e2bKIpm57": {
                "id": "selyG7B3e2bKIpm57",
                "name": "Gabe Higgins",
                "color": "pinkMedium"
            },
            "selLBdzdkudIimJBq": {
                "id": "selLBdzdkudIimJBq",
                "name": "Devayani Latey",
                "color": "orange"
            },
            "selzaMXTD5ouWDZjg": {
                "id": "selzaMXTD5ouWDZjg",
                "name": "Soham Garud ",
                "color": "purpleDarker"
            },
            "selvf4rU3PC2YRxj6": {
                "id": "selvf4rU3PC2YRxj6",
                "name": "Jordan Fried",
                "color": "grayDark"
            },
            "selqUN2Y6RmPJbeq6": {
                "id": "selqUN2Y6RmPJbeq6",
                "name": "Peng Zhao",
                "color": "blue"
            },
            "selieDY0UniywscHA": {
                "id": "selieDY0UniywscHA",
                "name": "Mark Paul",
                "color": "greenDark"
            },
            "selLq64XPrF8jeJqj": {
                "id": "selLq64XPrF8jeJqj",
                "name": "Pete Ho",
                "color": "grayDark"
            },
            "selX2VtkljcZthVuB": {
                "id": "selX2VtkljcZthVuB",
                "name": "Paul Ngyen",
                "color": "tealDark"
            },
            "selZaIOrEs9WnbDB8": {
                "id": "selZaIOrEs9WnbDB8",
                "name": "Justine Lu",
                "color": "pinkDarker"
            },
            "selRp2VaY8jBQfhtW": {
                "id": "selRp2VaY8jBQfhtW",
                "name": "David Tseng ",
                "color": "grayDarker"
            }
        },
        "disableColors": False
    }
}
CATEGORY = {
    "id": "fldjd43zfXdpAWzaq",
    "name": "Category",
    "type": "select",
    "typeOptions": {
        "choices": {
        "sel21n4zLpVKL1gG9": {
            "id": "sel21n4zLpVKL1gG9",
            "name": "DeFi",
            "color": "redDarker"
        },
        "selDVhfexVqGp3ClM": {
            "id": "selDVhfexVqGp3ClM",
            "name": "NFTs",
            "color": "redDark"
        },
        "selNAACcraMbkWWZk": {
            "id": "selNAACcraMbkWWZk",
            "name": "Web3",
            "color": "redDarker"
        },
        "selx8ouft38637DCN": {
            "id": "selx8ouft38637DCN",
            "name": "Infrastructure",
            "color": "grayDark"
        },
        "selSTNpxlceJac4jF": {
            "id": "selSTNpxlceJac4jF",
            "name": "CeFi",
            "color": "gray"
        }
        },
        "disableColors": False
    }
}
SUB_CATEGORIES = {
    "id": "fldT0Fasv4hkjwbb3",
    "name": "Sub-categories",
    "type": "multiSelect",
    "typeOptions": {
        "choices": {
        "sell9IdF42xAB6PpD": {
            "id": "sell9IdF42xAB6PpD",
            "name": "Funding",
            "color": "cyanDark"
        },
        "selMOkXsDg9uF7yky": {
            "id": "selMOkXsDg9uF7yky",
            "name": "Exchange",
            "color": "cyanDarker"
        },
        "selq5X31pNknXhaoI": {
            "id": "selq5X31pNknXhaoI",
            "name": "Layer 2",
            "color": "pinkMedium"
        },
        "selZr6MadGxPpnDQ8": {
            "id": "selZr6MadGxPpnDQ8",
            "name": "Oracle",
            "color": "grayMedium"
        },
        "selq7eMdSoDWonG0i": {
            "id": "selq7eMdSoDWonG0i",
            "name": "Gaming",
            "color": "orangeDarker"
        },
        "seluDzmssCbFFmV9R": {
            "id": "seluDzmssCbFFmV9R",
            "name": "Trading",
            "color": "blueDarker"
        },
        "selef4S5WJC4IM5tm": {
            "id": "selef4S5WJC4IM5tm",
            "name": "Wallet",
            "color": "blueMedium"
        },
        "selupHDJSYm5mu4bk": {
            "id": "selupHDJSYm5mu4bk",
            "name": "Indexing",
            "color": "greenDark"
        },
        "selVahC7O6BnkBD8V": {
            "id": "selVahC7O6BnkBD8V",
            "name": "Data",
            "color": "blue"
        },
        "selWQzakewEMAHkLo": {
            "id": "selWQzakewEMAHkLo",
            "name": "Messaging",
            "color": "red"
        },
        "selLX5pjWR2lNiiik": {
            "id": "selLX5pjWR2lNiiik",
            "name": "Coding",
            "color": "purpleDark"
        },
        "selMj5UOUcRkN3Kut": {
            "id": "selMj5UOUcRkN3Kut",
            "name": "Derivatives",
            "color": "pinkMedium"
        },
        "sel0Zd4KBREL3c5UN": {
            "id": "sel0Zd4KBREL3c5UN",
            "name": "Lending/Borrowing",
            "color": "blueMedium"
        },
        "selvGzMjoDPG7XJ9Z": {
            "id": "selvGzMjoDPG7XJ9Z",
            "name": "Yield",
            "color": "blueDarker"
        },
        "sellYmzt8QKHT4Qe6": {
            "id": "sellYmzt8QKHT4Qe6",
            "name": "Layer 1",
            "color": "grayDarker"
        },
        "selSvURbjEVTCTfAB": {
            "id": "selSvURbjEVTCTfAB",
            "name": "Privacy",
            "color": "orangeDark"
        },
        "selW7RXZgA8uEyfmm": {
            "id": "selW7RXZgA8uEyfmm",
            "name": "Security",
            "color": "cyanDark"
        },
        "selwmA5MVXNI126l5": {
            "id": "selwmA5MVXNI126l5",
            "name": "Insurance",
            "color": "tealMedium"
        },
        "sel21fyyW5VT9cdHQ": {
            "id": "sel21fyyW5VT9cdHQ",
            "name": "Legal",
            "color": "redDark"
        },
        "selW6YgYqO8txIKGw": {
            "id": "selW6YgYqO8txIKGw",
            "name": "Analytics",
            "color": "red"
        },
        "selqmXdrjBHX28GkI": {
            "id": "selqmXdrjBHX28GkI",
            "name": "Interoperability",
            "color": "tealMedium"
        },
        "selTxHtBLNZMcKB8H": {
            "id": "selTxHtBLNZMcKB8H",
            "name": "Liquidity",
            "color": "tealDark"
        },
        "selxo5vPdu6ezikS2": {
            "id": "selxo5vPdu6ezikS2",
            "name": "Payment",
            "color": "pinkDarker"
        },
        "selKX9dtuHP1oX0nw": {
            "id": "selKX9dtuHP1oX0nw",
            "name": "Audio",
            "color": "green"
        },
        "selFxikoMbaTNXm0V": {
            "id": "selFxikoMbaTNXm0V",
            "name": "Stablecoins",
            "color": "grayDarker"
        },
        "selMJVxbaxSSb3Use": {
            "id": "selMJVxbaxSSb3Use",
            "name": "Intellectual property",
            "color": "greenDarker"
        },
        "selFHHilWjai3jdEz": {
            "id": "selFHHilWjai3jdEz",
            "name": "Options",
            "color": "pinkMedium"
        },
        "sel41xDsdMM03aYuS": {
            "id": "sel41xDsdMM03aYuS",
            "name": "APIs",
            "color": "blueDark"
        },
        "selJQ95pMWUQbFdlc": {
            "id": "selJQ95pMWUQbFdlc",
            "name": "Smart contracts",
            "color": "purpleDarker"
        },
        "selKrNODU0V0VYy6r": {
            "id": "selKrNODU0V0VYy6r",
            "name": "Staking",
            "color": "pinkDarker"
        },
        "selnE4pqcdVk3WHp4": {
            "id": "selnE4pqcdVk3WHp4",
            "name": "Aggregator",
            "color": "purpleMedium"
        },
        "selbrkkdkvgwXGyF3": {
            "id": "selbrkkdkvgwXGyF3",
            "name": "UX",
            "color": "cyan"
        },
        "selMwKVasBUiMvOBd": {
            "id": "selMwKVasBUiMvOBd",
            "name": "Tokenization",
            "color": "yellowDark"
        },
        "selN8M0gVgILvHQF4": {
            "id": "selN8M0gVgILvHQF4",
            "name": "Parachain",
            "color": "tealMedium"
        },
        "selSy67dYNIpqLn6W": {
            "id": "selSy67dYNIpqLn6W",
            "name": "Marketplace",
            "color": "pinkMedium"
        },
        "seltbhYafqFmDoS3h": {
            "id": "seltbhYafqFmDoS3h",
            "name": "Metaverse",
            "color": "purpleDark"
        },
        "selSWOJHKkliUMc5Z": {
            "id": "selSWOJHKkliUMc5Z",
            "name": "Risk management",
            "color": "yellowDark"
        },
        "seluckyqrs5V3C4K8": {
            "id": "seluckyqrs5V3C4K8",
            "name": "Bots",
            "color": "grayDarker"
        },
        "selxLf6P60MtogspR": {
            "id": "selxLf6P60MtogspR",
            "name": "Automation",
            "color": "greenDarker"
        },
        "selsYMdiU9wOSgPXo": {
            "id": "selsYMdiU9wOSgPXo",
            "name": "Cloud",
            "color": "purpleDarker"
        },
        "selJMcbVM2LjT0IKq": {
            "id": "selJMcbVM2LjT0IKq",
            "name": "Mobile",
            "color": "greenDark"
        },
        "selGunSDuOz7Ng31L": {
            "id": "selGunSDuOz7Ng31L",
            "name": "Auction",
            "color": "tealDark"
        },
        "seltZNeBAr0CzYjjW": {
            "id": "seltZNeBAr0CzYjjW",
            "name": "Tooling",
            "color": "purpleDark"
        },
        "selz8hIMFX4cQofgN": {
            "id": "selz8hIMFX4cQofgN",
            "name": "Environment",
            "color": "teal"
        },
        "selvyrdIDKPT3s4BI": {
            "id": "selvyrdIDKPT3s4BI",
            "name": "DeFi - NFTs",
            "color": "yellowDarker"
        },
        "selsP7S7EVCCDJU6D": {
            "id": "selsP7S7EVCCDJU6D",
            "name": "Prediction",
            "color": "grayDark"
        },
        "selGaumcVU2UfQjWY": {
            "id": "selGaumcVU2UfQjWY",
            "name": "Recruitment",
            "color": "purple"
        },
        "selBEHcUSSkc6TS1h": {
            "id": "selBEHcUSSkc6TS1h",
            "name": "Synthetics",
            "color": "yellow"
        },
        "selpIAUCvH6oVoO2p": {
            "id": "selpIAUCvH6oVoO2p",
            "name": "Real world assets",
            "color": "pinkDarker"
        },
        "selK2XjNEDflLwHTd": {
            "id": "selK2XjNEDflLwHTd",
            "name": "Real estate",
            "color": "purpleDark"
        },
        "selVIir3d1PFfWVUl": {
            "id": "selVIir3d1PFfWVUl",
            "name": "Governance",
            "color": "pinkMedium"
        },
        "selFjiEeDooS6MWOU": {
            "id": "selFjiEeDooS6MWOU",
            "name": "Social token",
            "color": "cyanDark"
        },
        "selcQCkyT4NuaVNBJ": {
            "id": "selcQCkyT4NuaVNBJ",
            "name": "AMM",
            "color": "grayDarker"
        },
        "selgrvtztlQP08W6i": {
            "id": "selgrvtztlQP08W6i",
            "name": "Fractionalization",
            "color": "teal"
        },
        "selV6QKx05y2iPgmM": {
            "id": "selV6QKx05y2iPgmM",
            "name": "Financial infrastructure",
            "color": "blue"
        },
        "selkJbQcxR87sSeG8": {
            "id": "selkJbQcxR87sSeG8",
            "name": "Banking",
            "color": "purpleDark"
        },
        "selglubre56J1LbkG": {
            "id": "selglubre56J1LbkG",
            "name": "Storage",
            "color": "pinkDarker"
        },
        "selEOISlQ7DxwAh4h": {
            "id": "selEOISlQ7DxwAh4h",
            "name": "Brokerage",
            "color": "tealDark"
        },
        "selbFtSo32gN8wTRy": {
            "id": "selbFtSo32gN8wTRy",
            "name": "Custody",
            "color": "orangeDark"
        },
        "selNMUCloFJd4Mpck": {
            "id": "selNMUCloFJd4Mpck",
            "name": "Travel",
            "color": "pinkMedium"
        },
        "selULaeUgTzGf8peq": {
            "id": "selULaeUgTzGf8peq",
            "name": "Art",
            "color": "cyanMedium"
        },
        "sel8zyl4RwaExCSAt": {
            "id": "sel8zyl4RwaExCSAt",
            "name": "Mining",
            "color": "yellowDark"
        },
        "sel9vuJrin1CB2q0j": {
            "id": "sel9vuJrin1CB2q0j",
            "name": "Social network",
            "color": "yellowDarker"
        },
        "selIcCPFGn04TDdxq": {
            "id": "selIcCPFGn04TDdxq",
            "name": "DAO",
            "color": "tealDark"
        },
        "selxnudvRNk699HbK": {
            "id": "selxnudvRNk699HbK",
            "name": "Tax",
            "color": "blueDark"
        },
        "selPAT4CNfi0Et3PO": {
            "id": "selPAT4CNfi0Et3PO",
            "name": "Mobility",
            "color": "pink"
        },
        "selqNfPpRrI0CsmLQ": {
            "id": "selqNfPpRrI0CsmLQ",
            "name": "Supply chain",
            "color": "gray"
        },
        "sel4l33Q5SYpXjdUA": {
            "id": "sel4l33Q5SYpXjdUA",
            "name": "Education",
            "color": "tealMedium"
        },
        "selnzzhr2nYdJPLGP": {
            "id": "selnzzhr2nYdJPLGP",
            "name": "Machine Learning",
            "color": "orangeDark"
        },
        "selU0nRTAJ63IYy8h": {
            "id": "selU0nRTAJ63IYy8h",
            "name": "Savings",
            "color": "tealDarker"
        },
        "selzt332RrGWmrkei": {
            "id": "selzt332RrGWmrkei",
            "name": "Cashback",
            "color": "yellowDark"
        },
        "selK4eNa5izAu7JkV": {
            "id": "selK4eNa5izAu7JkV",
            "name": "ETF",
            "color": "redDark"
        },
        "seltIoLsG7yWUAazh": {
            "id": "seltIoLsG7yWUAazh",
            "name": "Notification",
            "color": "pinkDarker"
        },
        "selb9adu6JO9VCsmr": {
            "id": "selb9adu6JO9VCsmr",
            "name": "Enterprise",
            "color": "cyanDark"
        },
        "sel4mYvGsAUxhOobl": {
            "id": "sel4mYvGsAUxhOobl",
            "name": "Flash loan",
            "color": "greenDarker"
        },
        "selqSfBbaFicqy3RD": {
            "id": "selqSfBbaFicqy3RD",
            "name": "Social trading",
            "color": "yellowDark"
        },
        "selbeW3GRzR3esurG": {
            "id": "selbeW3GRzR3esurG",
            "name": "Accounting",
            "color": "grayMedium"
        },
        "selPNEgXerQw9oqhO": {
            "id": "selPNEgXerQw9oqhO",
            "name": "Index",
            "color": "pink"
        },
        "sel2VbNGHiif3l7T0": {
            "id": "sel2VbNGHiif3l7T0",
            "name": "Advertising",
            "color": "pinkDarker"
        },
        "selD6op5vuQ4OLA4R": {
            "id": "selD6op5vuQ4OLA4R",
            "name": "Justice",
            "color": "purple"
        },
        "selozEDBj83Fyh63F": {
            "id": "selozEDBj83Fyh63F",
            "name": "Perpetual",
            "color": "blueMedium"
        },
        "sel0edOs4ZbuMg0It": {
            "id": "sel0edOs4ZbuMg0It",
            "name": "AI",
            "color": "purpleDarker"
        },
        "selfF8ELzPKg2j31C": {
            "id": "selfF8ELzPKg2j31C",
            "name": "Avatar",
            "color": "blueMedium"
        },
        "selwPCUblvWI823pB": {
            "id": "selwPCUblvWI823pB",
            "name": "Collectibles",
            "color": "greenDarker"
        },
        "selYlYYm4n0ps9fY0": {
            "id": "selYlYYm4n0ps9fY0",
            "name": "Scalability",
            "color": "orangeMedium"
        },
        "selTdjwAZhY5tVNyv": {
            "id": "selTdjwAZhY5tVNyv",
            "name": "Yield Aggregator",
            "color": "grayDark"
        },
        "selPFplb2f0VXrSVQ": {
            "id": "selPFplb2f0VXrSVQ",
            "name": "Information",
            "color": "blueDarker"
        },
        "sel94CflpA9O97gd3": {
            "id": "sel94CflpA9O97gd3",
            "name": "P2P",
            "color": "redMedium"
        },
        "selU1T74zKemdShV4": {
            "id": "selU1T74zKemdShV4",
            "name": "Multi-products",
            "color": "orangeMedium"
        },
        "seloKXPWHUzGceJS7": {
            "id": "seloKXPWHUzGceJS7",
            "name": "DeFi - BTC",
            "color": "pinkMedium"
        },
        "selxIiAERKsVUjwp2": {
            "id": "selxIiAERKsVUjwp2",
            "name": "Price discovery",
            "color": "cyan"
        },
        "selcOgRYJRRfmfJxr": {
            "id": "selcOgRYJRRfmfJxr",
            "name": "Asset management",
            "color": "green"
        },
        "selPhrYhfOiSWo3tM": {
            "id": "selPhrYhfOiSWo3tM",
            "name": "DApp",
            "color": "blueMedium"
        },
        "selTuPXuN3aRIFbGi": {
            "id": "selTuPXuN3aRIFbGi",
            "name": "Audit",
            "color": "purpleMedium"
        },
        "selYqT8dODnQ9ZgID": {
            "id": "selYqT8dODnQ9ZgID",
            "name": "Curation",
            "color": "yellowMedium"
        },
        "seleD0NuCZbxvcIUd": {
            "id": "seleD0NuCZbxvcIUd",
            "name": "Debt",
            "color": "orangeDarker"
        },
        "selqFS52lTg9VhNAw": {
            "id": "selqFS52lTg9VhNAw",
            "name": "Media",
            "color": "teal"
        },
        "selFgkQ7wek04wcxr": {
            "id": "selFgkQ7wek04wcxr",
            "name": "Identity",
            "color": "blue"
        },
        "sel7IEamb9CO4WvNi": {
            "id": "sel7IEamb9CO4WvNi",
            "name": "Sports",
            "color": "pinkDark"
        },
        "selGPx6DW1RC4nCBG": {
            "id": "selGPx6DW1RC4nCBG",
            "name": "Referral",
            "color": "green"
        },
        "selOwepOOAMvuscro": {
            "id": "selOwepOOAMvuscro",
            "name": "Launchpad",
            "color": "green"
        },
        "selsEKOotzoTdPFXK": {
            "id": "selsEKOotzoTdPFXK",
            "name": "Freelancing ",
            "color": "red"
        },
        "selIDbV9ZY4B0NYEr": {
            "id": "selIDbV9ZY4B0NYEr",
            "name": "Nodes",
            "color": "orangeDarker"
        },
        "selPJSvKgHRjYxorF": {
            "id": "selPJSvKgHRjYxorF",
            "name": "Lottery",
            "color": "orangeDark"
        },
        "selwhKk3N5BLcREQc": {
            "id": "selwhKk3N5BLcREQc",
            "name": "Pricing",
            "color": "orange"
        },
        "selsbM4kwfulnKUVj": {
            "id": "selsbM4kwfulnKUVj",
            "name": "Limit orders",
            "color": "pinkDark"
        },
        "selcUO0NeV6ykYHtw": {
            "id": "selcUO0NeV6ykYHtw",
            "name": "Rating",
            "color": "cyan"
        },
        "selmmAxbPoxlgRlkc": {
            "id": "selmmAxbPoxlgRlkc",
            "name": "Labor",
            "color": "orangeDark"
        },
        "selkHe33qDQKjYHhO": {
            "id": "selkHe33qDQKjYHhO",
            "name": "Middleware",
            "color": "purpleMedium"
        },
        "selUy4kucvCZEKlTc": {
            "id": "selUy4kucvCZEKlTc",
            "name": "Music",
            "color": "cyanDark"
        },
        "selBLx3ZMkst0N4cb": {
            "id": "selBLx3ZMkst0N4cb",
            "name": "Intelligence",
            "color": "redDarker"
        },
        "sel1x14NUSeOiU1qf": {
            "id": "sel1x14NUSeOiU1qf",
            "name": "Compliance",
            "color": "pinkMedium"
        },
        "selaqfajjEgmB5eqF": {
            "id": "selaqfajjEgmB5eqF",
            "name": "AR/VR",
            "color": "tealDarker"
        },
        "selxSFyjvd6XvDUJt": {
            "id": "selxSFyjvd6XvDUJt",
            "name": "R&D",
            "color": "tealDarker"
        },
        "sely5oLTdRo3tVtiq": {
            "id": "sely5oLTdRo3tVtiq",
            "name": "Leisure",
            "color": "greenMedium"
        },
        "seljpuPrPv437AOem": {
            "id": "seljpuPrPv437AOem",
            "name": "Investment",
            "color": "pinkMedium"
        },
        "selgBWZdR4BAlpXFo": {
            "id": "selgBWZdR4BAlpXFo",
            "name": "E-commerce",
            "color": "tealDark"
        },
        "selx0mDJwyNdjJlnm": {
            "id": "selx0mDJwyNdjJlnm",
            "name": "VPN",
            "color": "yellow"
        },
        "sel926GtvkJFGYI3f": {
            "id": "sel926GtvkJFGYI3f",
            "name": "Wrapping",
            "color": "pinkDark"
        },
        "sel9SoO7ueZ0AsepG": {
            "id": "sel9SoO7ueZ0AsepG",
            "name": "Farming",
            "color": "gray"
        },
        "seltDa4YlVVhrYgZm": {
            "id": "seltDa4YlVVhrYgZm",
            "name": "No-code",
            "color": "cyan"
        },
        "selQ6AxrI2rcWwfcA": {
            "id": "selQ6AxrI2rcWwfcA",
            "name": "Minting",
            "color": "green"
        },
        "selp3RieKysJqwizf": {
            "id": "selp3RieKysJqwizf",
            "name": "Connectivity",
            "color": "blueDark"
        },
        "selCt34zJvzY4sa3L": {
            "id": "selCt34zJvzY4sa3L",
            "name": "DEX",
            "color": "grayDarker"
        },
        "selbjVP4Jt3rLZ3vD": {
            "id": "selbjVP4Jt3rLZ3vD",
            "name": "Authority",
            "color": "pink"
        },
        "selknBYvNz1V2XSdO": {
            "id": "selknBYvNz1V2XSdO",
            "name": "Certification",
            "color": "blueDark"
        },
        "selQjDfa0jk8l1lVf": {
            "id": "selQjDfa0jk8l1lVf",
            "name": "Bridge",
            "color": "grayDarker"
        },
        "selFXrwk8z44SxlS7": {
            "id": "selFXrwk8z44SxlS7",
            "name": "Bandwidth",
            "color": "cyanMedium"
        },
        "selMPfokKTqRPn4Rp": {
            "id": "selMPfokKTqRPn4Rp",
            "name": "Mortgage",
            "color": "yellowDark"
        },
        "selWtYSr2B0U8PNKa": {
            "id": "selWtYSr2B0U8PNKa",
            "name": "Paratoken",
            "color": "pink"
        },
        "selpoU3DugqXtD0sY": {
            "id": "selpoU3DugqXtD0sY",
            "name": "Movie",
            "color": "gray"
        },
        "selBwGWYERmz0p08M": {
            "id": "selBwGWYERmz0p08M",
            "name": "Entertainment",
            "color": "orange"
        },
        "selr1cQUshVCi4JWZ": {
            "id": "selr1cQUshVCi4JWZ",
            "name": "Portfolio management",
            "color": "cyanDarker"
        },
        "selzesd4mgEXuSL7G": {
            "id": "selzesd4mgEXuSL7G",
            "name": "Incubator",
            "color": "grayMedium"
        },
        "selsXtOZgYTQBumQZ": {
            "id": "selsXtOZgYTQBumQZ",
            "name": "Microcredit",
            "color": "greenDark"
        },
        "selm3PH9im5a8eOvU": {
            "id": "selm3PH9im5a8eOvU",
            "name": "Sharding",
            "color": "orangeMedium"
        },
        "selAWynBllCvw2iCs": {
            "id": "selAWynBllCvw2iCs",
            "name": "Healthcare",
            "color": "yellowMedium"
        },
        "selaIAHs6szrvGXUq": {
            "id": "selaIAHs6szrvGXUq",
            "name": "Securities",
            "color": "yellow"
        },
        "selcVzyWmu6TIjOUI": {
            "id": "selcVzyWmu6TIjOUI",
            "name": "Collateralization",
            "color": "blueMedium"
        },
        "selLAkRiEMYq8jnGY": {
            "id": "selLAkRiEMYq8jnGY",
            "name": "Developers",
            "color": "pinkDarker"
        },
        "selNJox5rkKI6wmdq": {
            "id": "selNJox5rkKI6wmdq",
            "name": "Bitcoin",
            "color": "purpleDark"
        },
        "seluFT8Jqy85RHcJs": {
            "id": "seluFT8Jqy85RHcJs",
            "name": "Hardware",
            "color": "blueMedium"
        },
        "selfmqP9zhjXBHPD6": {
            "id": "selfmqP9zhjXBHPD6",
            "name": "Infrastructure",
            "color": "blueDark"
        },
        "selQApjkguDToNtdy": {
            "id": "selQApjkguDToNtdy",
            "name": "Telcos",
            "color": "blue"
        },
        "selBdGJJCj5FcUTon": {
            "id": "selBdGJJCj5FcUTon",
            "name": "Fraud",
            "color": "purpleMedium"
        },
        "sel8DNQ4ty27uq0Hv": {
            "id": "sel8DNQ4ty27uq0Hv",
            "name": "IoT",
            "color": "blueDark"
        },
        "selszY9LKeMPNqsiT": {
            "id": "selszY9LKeMPNqsiT",
            "name": "DeFi",
            "color": "blue"
        },
        "selLvRyQZtjLoPSrG": {
            "id": "selLvRyQZtjLoPSrG",
            "name": "Cryptography",
            "color": "tealDark"
        },
        "selHVc25kqgTgVTxf": {
            "id": "selHVc25kqgTgVTxf",
            "name": "Label",
            "color": "greenDarker"
        },
        "sel9kfwWatfLyNISw": {
            "id": "sel9kfwWatfLyNISw",
            "name": "Packaging",
            "color": "cyanDark"
        },
        "selTX6vfN5LZycNL7": {
            "id": "selTX6vfN5LZycNL7",
            "name": "Studio",
            "color": "blueMedium"
        },
        "selkO0lMGGEliOSiX": {
            "id": "selkO0lMGGEliOSiX",
            "name": "Authentification",
            "color": "blueDarker"
        },
        "selCLEuegJZ7d9Jk2": {
            "id": "selCLEuegJZ7d9Jk2",
            "name": "Signing",
            "color": "yellowMedium"
        },
        "selsJYNZYf0BalaA9": {
            "id": "selsJYNZYf0BalaA9",
            "name": "Charity",
            "color": "greenMedium"
        },
        "selX7Pcv7kMrfFek4": {
            "id": "selX7Pcv7kMrfFek4",
            "name": "Transport",
            "color": "pink"
        },
        "selQ62HIhSIDyW51D": {
            "id": "selQ62HIhSIDyW51D",
            "name": "Logistics",
            "color": "orange"
        },
        "selhbhzhQRroIXo5w": {
            "id": "selhbhzhQRroIXo5w",
            "name": "Consulting",
            "color": "greenMedium"
        },
        "selMrkLVW1u0xMxGe": {
            "id": "selMrkLVW1u0xMxGe",
            "name": "Video",
            "color": "blueDarker"
        },
        "selrxiGwKDbU9Wa0Q": {
            "id": "selrxiGwKDbU9Wa0Q",
            "name": "Key management",
            "color": "yellowMedium"
        },
        "selDIe0xtgbFE31VO": {
            "id": "selDIe0xtgbFE31VO",
            "name": "Telecom",
            "color": "purple"
        },
        "seld4RnsCU3KCpAaX": {
            "id": "seld4RnsCU3KCpAaX",
            "name": "Document Management System",
            "color": "yellowDarker"
        },
        "sel9wbkOklyQ4YraT": {
            "id": "sel9wbkOklyQ4YraT",
            "name": "Luxury",
            "color": "pinkDarker"
        },
        "sel6Jt6KoPGixeBc0": {
            "id": "sel6Jt6KoPGixeBc0",
            "name": "Communication",
            "color": "grayMedium"
        },
        "sel4Cr1rOnPidlmjb": {
            "id": "sel4Cr1rOnPidlmjb",
            "name": "Marketing",
            "color": "greenDarker"
        },
        "selYu23fXDDCrhKjW": {
            "id": "selYu23fXDDCrhKjW",
            "name": "Gallery",
            "color": "cyan"
        },
        "selwfez212JMBhmdB": {
            "id": "selwfez212JMBhmdB",
            "name": "MEV",
            "color": "purpleDarker"
        },
        "selMetUUnI9OKopGG": {
            "id": "selMetUUnI9OKopGG",
            "name": "Hackathon",
            "color": "red"
        },
        "selecZhtCoGsZA7cy": {
            "id": "selecZhtCoGsZA7cy",
            "name": "Employment",
            "color": "gray"
        },
        "selkY4awNjTydgtky": {
            "id": "selkY4awNjTydgtky",
            "name": "Space",
            "color": "pink"
        },
        "selP4mAGVijce9PIP": {
            "id": "selP4mAGVijce9PIP",
            "name": "Social club",
            "color": "redMedium"
        },
        "selfExURtl2PSFpLw": {
            "id": "selfExURtl2PSFpLw",
            "name": "Income",
            "color": "cyanDark"
        },
        "sel2qWAf6zpnqN9jQ": {
            "id": "sel2qWAf6zpnqN9jQ",
            "name": "Bounty",
            "color": "blueDarker"
        },
        "sel0CXxS19wzxW6JA": {
            "id": "sel0CXxS19wzxW6JA",
            "name": "Registry",
            "color": "teal"
        },
        "selQYmK4emh85JePY": {
            "id": "selQYmK4emh85JePY",
            "name": "Sales",
            "color": "purple"
        },
        "selXHt8awLVkf5VEx": {
            "id": "selXHt8awLVkf5VEx",
            "name": "Digital Media",
            "color": "redDarker"
        },
        "selbY9Zt6P1Es1Ja1": {
            "id": "selbY9Zt6P1Es1Ja1",
            "name": "Bug",
            "color": "green"
        },
        "sellNiQVpRujjRXga": {
            "id": "sellNiQVpRujjRXga",
            "name": "Software",
            "color": "cyanDarker"
        },
        "sel4j46OsdS5LBdou": {
            "id": "sel4j46OsdS5LBdou",
            "name": "Membership",
            "color": "greenDarker"
        },
        "selENjH30W8O2EU65": {
            "id": "selENjH30W8O2EU65",
            "name": "Backup",
            "color": "yellowMedium"
        },
        "sel7dfkEPI6qWtc1S": {
            "id": "sel7dfkEPI6qWtc1S",
            "name": "Cricket",
            "color": "greenDarker"
        },
        "selo87yNnxFLuYVmS": {
            "id": "selo87yNnxFLuYVmS",
            "name": "Payroll",
            "color": "blue"
        },
        "selcWI1n7hbHE7oAs": {
            "id": "selcWI1n7hbHE7oAs",
            "name": "Wifi",
            "color": "blue"
        },
        "selCBtouK7hOb9nQO": {
            "id": "selCBtouK7hOb9nQO",
            "name": "cAMM",
            "color": "redMedium"
        },
        "selX4Wjf1X9o9Tf9P": {
            "id": "selX4Wjf1X9o9Tf9P",
            "name": "ML",
            "color": "grayMedium"
        },
        "sel8PcejNU7YQJzL8": {
            "id": "sel8PcejNU7YQJzL8",
            "name": "Betting",
            "color": "pinkDarker"
        },
        "selAShV8nQllTz6Er": {
            "id": "selAShV8nQllTz6Er",
            "name": "Stocks",
            "color": "pinkDark"
        },
        "selcX5hhkWoS3FVh9": {
            "id": "selcX5hhkWoS3FVh9",
            "name": "Guild",
            "color": "pinkDarker"
        },
        "selpb9EL1qtsZVW3Y": {
            "id": "selpb9EL1qtsZVW3Y",
            "name": "City",
            "color": "orangeMedium"
        },
        "selRV20lKFrhVtubH": {
            "id": "selRV20lKFrhVtubH",
            "name": "Microverse",
            "color": "blueDarker"
        },
        "selMJhbtzLTL5pDJT": {
            "id": "selMJhbtzLTL5pDJT",
            "name": "Layer 3",
            "color": "orange"
        },
        "sel7Vd24YH3wrG0Xc": {
            "id": "sel7Vd24YH3wrG0Xc",
            "name": "Arbitrage",
            "color": "greenDarker"
        },
        "selEjPQKLuqZYM2HT": {
            "id": "selEjPQKLuqZYM2HT",
            "name": "Fashion",
            "color": "green"
        },
        "selLYOsUbzwvlUIkc": {
            "id": "selLYOsUbzwvlUIkc",
            "name": "Simulations",
            "color": "cyan"
        },
        "seltqBAsl8Dfw4Cj8": {
            "id": "seltqBAsl8Dfw4Cj8",
            "name": "Bond",
            "color": "pinkDark"
        },
        "selTiRn3eS6P6vrUG": {
            "id": "selTiRn3eS6P6vrUG",
            "name": "ESG",
            "color": "pinkDark"
        }
        },
        "disableColors": False
    }
}
COLUMN_MATCH = {
    "fld7v0ugjCe9N07W1" : "Fundraising Round",
    "fld0t86SH12Fx2aD6" : "Round",
    "fldSGmVP3olLGmAID" : "Date",
    "fldhntVnAppLIOUAl" : "Investors",
    "fldbHI1iWcw6U912R" : "Amount",
    "fld05vhEx0sIhbK4B" : "Valuation",
    "fldJHMHegLEl2A56n" : "Description",
    "fldZpYosKMqtY2nqQ" : "Founder",
    "fld8ZuXfzyuH1b9Dv" : "Website",
    "fldruqJ51OKbiswEI" : "Project",
    "fldjd43zfXdpAWzaq" : "Category",
    "fldT0Fasv4hkjwbb3" : "Sub-categories",
    "fldcDMf8A5D64Ecdf" : "Announcement",
    "flde2aIuRxurF0KNt" : "End date" # end date를 가지고 있는 project는 아직 없음
}
deepdata = {
    "Round": ROUND,
    "Founder": FOUNDER,
    "Category": CATEGORY,
    "Sub-categories": SUB_CATEGORIES
}
req = requests.get(DATA_URL, headers=headers)
data = json.loads( req.text )
f = open('airTableData.csv','a',encoding='utf-8-sig', newline='')
wr = csv.writer(f)

def makecol(id):
    return COLUMN_MATCH[id]

cols = list(map(makecol,COLUMN_MATCH.keys()))
# column들의 제목을 배열로 나타내줍니다.
# pprint(cols)
wr.writerow(cols)

# needData는 우리가 원하는 정보를 가지고 있는 곳을 가리킵니다.
needData = data["data"]["tableDatas"][0]["rows"]
for i in range(len(needData)):
    print(i)
    row = needData[i]["cellValuesByColumnId"]
    rowForCSV = []

    for id in COLUMN_MATCH.keys():
        value = COLUMN_MATCH[id]
        try:

            if value == "Investors" or value == "Project":
                multiSelect = ""
                for a in row[id]:
                    multiSelect += a["foreignRowDisplayName"]+"/"
                rowForCSV.append(multiSelect[:-1])

            elif value == "Round" or value == "Category":
                pureValue = deepdata[value]["typeOptions"]["choices"][row[id]]["name"]
                rowForCSV.append(pureValue)

            elif value == "Founder" or value == "Sub-categories":
                multiSelect = ""
                for a in row[id]:
                    pureValue = deepdata[value]["typeOptions"]["choices"][a]["name"]
                    multiSelect += pureValue +'/'
                rowForCSV.append(multiSelect[:-1])
            else: 
                rowForCSV.append(row[id])
        except KeyError:
            rowForCSV.append("none")

    # pprint(rowForCSV)
    wr.writerow(rowForCSV)
print("1963이 나왔다면 성공입니다.")
f.close()