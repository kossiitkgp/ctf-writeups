import json
from os import name
import sys
import requests
import pycurl

# COLORS
ERROR = "\033[91m"
PROGRESS = "\033[93m"
SUCCESS = "\033[92m"
NORMAL = "\033[37m"

if len(sys.argv) < 3:
    print(ERROR,"\bUSAGE: python ctf_readme.py [CTF NAME] [EVENT ID]")
    exit(1)

CTF_NAME = sys.argv[1]
# CTF_URL = sys.argv[2]
EVENT_ID = sys.argv[2]
# TEAM_ID = sys.argv[4]

# access challenges.json from ctf.ctfname.tld/api/v1/challenges
# I was unable to handle ctfd auth
# def get_challenges(url):
#     try:
#         req_url = f"{url}api/v1/challenges"
#         print(PROGRESS, "[*]", end="")
#         print("Sending request to", req_url)
#         SESSION_TOKEN = input("Enter your CTFd Session Token\n> ")
#         res = requests.get(req_url, headers={"Cookie":f"{SESSION_TOKEN}"})
#         
#         if res.status_code == 200:
#             # challenge_list = res.json()
#             print(res.content)
#             print(SUCCESS, "[+] Response received from ", req_url, " with status", res.status_code)
#             # return challenge_list["data"]
#         else:
#             print("ERROR: ", res.status_code)
#             print(res)
#             return None
#     except: 
#         print(ERROR, "Failed to send request")

def get_challenges(json_file):
    print(PROGRESS, "[*] Opening ", json_file)
    with open(json_file, "r") as challenge_file:
        challenges = json.loads(challenge_file.read())
        if challenges["success"] == True:
            print(SUCCESS, "[+] Successfully got challenges")
            return challenges["data"]
        else:
            print(ERROR, "[-] Error in ", json_file)

def get_ctf_data(event_id):
     try:
         req_url = f"https://ctftime.org/api/v1/events/{event_id}/"
         print(PROGRESS, "[*]", end=" ")
         print("Sending request to", req_url)
         # res = requests.get(req_url, allow_redirects=False)
         cookies = {
             'sessionid': '24ee8e4e5aea0195217555d661566bc9',
             'csrftoken': 'FViObKer0wZUrQpSYDPfidtNSi0iPB4H',
             'twtr_pixel_opt_in': 'N',
             'ss': '"eyJ1c2VybmFtZSI6ICJzdWJ6Y3ViZXIiLCAiaWQiOiAxOTMzNDksICJ0cyI6IDE3MzkyNjg4NDJ9:2ba7bc9ab4135fb401a11107f07783818f09e9c4af89b155deaa124b53b4bbd2"',
             'pt': '"gAAAAABnqyLqszIR9U9jZ2Lj2ReMjAPHViBJSa422WROWxGWGVQ5saRJ5jPEPUK8TfOsj6HMGloxS_Nvr23XIluSTZ8yFYoxI96hUPi9C0dLPeyTLdUH0Qmk9hzdYRwg7o751Ajxyg95a2qmXzNlbj2keK09x3ZrIXu99XdAii-xiIYS_dr5BIeK9qaqjvxEarpORynusp0bmBm_bWt2q0c9m6zS5E9DN4vf8lCw6-Yt7JkIt97w5p8aLNim8m6ZHtnsIm0M1Wsit3LjJeb2fznjtAhDpUiUeg=="',
         }

         headers = {
             'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0',
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Language': 'en-US,en;q=0.5',
             # 'Accept-Encoding': 'gzip, deflate, br, zstd',
             'DNT': '1',
             'Sec-GPC': '1',
             'Connection': 'keep-alive',
             # 'Cookie': 'sessionid=24ee8e4e5aea0195217555d661566bc9; csrftoken=FViObKer0wZUrQpSYDPfidtNSi0iPB4H; twtr_pixel_opt_in=N; ss="eyJ1c2VybmFtZSI6ICJzdWJ6Y3ViZXIiLCAiaWQiOiAxOTMzNDksICJ0cyI6IDE3MzkyNjg4NDJ9:2ba7bc9ab4135fb401a11107f07783818f09e9c4af89b155deaa124b53b4bbd2"; pt="gAAAAABnqyLqszIR9U9jZ2Lj2ReMjAPHViBJSa422WROWxGWGVQ5saRJ5jPEPUK8TfOsj6HMGloxS_Nvr23XIluSTZ8yFYoxI96hUPi9C0dLPeyTLdUH0Qmk9hzdYRwg7o751Ajxyg95a2qmXzNlbj2keK09x3ZrIXu99XdAii-xiIYS_dr5BIeK9qaqjvxEarpORynusp0bmBm_bWt2q0c9m6zS5E9DN4vf8lCw6-Yt7JkIt97w5p8aLNim8m6ZHtnsIm0M1Wsit3LjJeb2fznjtAhDpUiUeg=="',
             'Upgrade-Insecure-Requests': '1',
             'Sec-Fetch-Dest': 'document',
             'Sec-Fetch-Mode': 'navigate',
             'Sec-Fetch-Site': 'none',
             'Sec-Fetch-User': '?1',
             'Priority': 'u=0, i',
         }

         res = requests.get('https://ctftime.org/api/v1/events/2607/', cookies, headers=headers)
         
         
         if res.status_code == 200:
             print(SUCCESS, "[+] Response received from ", req_url, "with status", res.status_code)
             return json.loads(res.text)
         else:
             print("ERROR: ", res.status_code)
             print(json.loads(res.text))
             return None
     except: 
         print(ERROR, "Failed to send request")

def generate_readme_description(ctf_data):
    readme_description = f"""
<div align="center">
  <a href="{ctf_data['ctftime_url']}">
      <img src="{ctf_data['logo']}" alt="Logo" width="150" height="150">
  </a>
  
  <h3 align="center">{ctf_data['title']}</h3>
  
  <p align="center">
      {ctf_data['start'].split('T')[0]} to {ctf_data['finish'].split('T')[0]}
      <br />
      <a href="{ctf_data['ctftime_url']}">CTFtime URL</a>
      |
      <a href=''>{ctf_data['weight']} weight</a>
  </p>
</div>
"""
    return readme_description


def generate_challenges_table(challenge_list):
    challenge_table = "<div align='center'>\n\nName | Category | Points | Solves | Solved By Us |\n-----|----------|--------|--------|--------------|\n"
    if(challenge_list != None):
        for challenge in challenge_list:
            challenge_table += f"{writeup_link_formatting(challenge)} | {challenge["category"]} | {challenge["value"]} | {challenge["solves"]} | {challenge["solved_by_me"]}\n"
        challenge_table += "\n\n</div>"
        print(SUCCESS, "[+] generated challenges table in markdown")
        return challenge_table
    else:
        print(ERROR, "[-] ERROR: Failed to get challenges")


def writeup_link_formatting(challenge):
    if challenge["solved_by_me"] == True:
        return f"[{challenge["name"]}]"
    else:
        return f"{challenge["name"]}"

README_HEADER = f"# {sys.argv[1]}"
CHALLENGE_LIST = get_challenges("challenges.json")
CHALLENGE_TABLE = generate_challenges_table(CHALLENGE_LIST)
CTF_DATA = get_ctf_data(EVENT_ID)
README_DESCRIPTION = generate_readme_description(CTF_DATA)
README_FOOTER = f"""
## Comments/Learnings

> Category-wise comments

## Writeups/Resources Dump

**category**:
- \\[team/solver\\]\\(link\\)
"""

if CHALLENGE_TABLE != None:
    README = f"{README_HEADER}\n{README_DESCRIPTION}\n{CHALLENGE_TABLE}\n\n{README_FOOTER}"
    print(PROGRESS, "[*] Generating README_NEW.md")
    with open("README_NEW.md", "w") as final_readme:
        final_readme.write(README)
        print(SUCCESS, "[+] Successfully wrote to README_NEW.md")
        print(NORMAL, "    You can run 'mv README_NEW.md README.md' if everything looks good")
