"""
Script to check a Brazilian municipality name and return IBGE code.

Clement Suavet
csuavet@sei-international.org
2018
"""

import json

from difflib import get_close_matches

with open('data.json', 'r') as fin:
    data = json.load(fin)

def check_municipality(mun_name, state_code):
    mun_name = mun_name.upper()
    state_code = state_code.upper()
    all_state_muns = [mun for mun in data['municipalities'] if mun['state'] == state_code]
    mun_codes = {name: mun['code'] for mun in all_state_muns for name in mun['names']}
    all_names = mun_codes.keys()

    # only one possibility
    if mun_name in all_names and len([name for name in all_names if name == mun_name]) == 1:
        return mun_codes[mun_name]
    else:
        # check for approximate match
        print()
        print(80 * "_")
        print("Looking for match for name:", mun_name + ' (' + state_code + ')')
        M = get_close_matches(mun_name, all_names, 10)

    # no close match found
    if len(M) == 0:
        choice = ''

    # at least one close match found
    else:
        # print name matches
        for i, n in enumerate(M):
            print(str(i+1) + ':' + M[i])

        # let user choose correct name
        choice = input(
            "Select number or press RETURN if no match...\n")

        result = mun_codes[M[int(choice)-1]]
        print(result)
        with open('new_names', 'a') as fout:
            fout.write(mun_name + ',' + result + '\n')

        [mun['names'] for mun in data['municipalities'] if mun['code'] == result][0].append(mun_name)
        
        with open('data.json', 'w') as fout:
            json.dump(data, fout, indent=2)
            
        return result

if __name__ == '__main__':
    results = ''
    with open('input.csv', 'r') as fin:
        for line in fin:
            mun_name, state_code = line.rstrip().split(',')
            try:
                results += check_municipality(mun_name, state_code) + '\n'
            except:
                results += 'UNKNOWN\n'
    with open('output.csv', 'w') as fout:
        fout.write(results)
