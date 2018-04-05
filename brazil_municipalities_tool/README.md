# Brazilian municipalities name matching

Write a list Brazilian municipality names to be checked in `input.csv`, one per line with the municipality name followed by the 2-letter state code, separated by a comma.

Run the script with `python script.py`.

Matches with known names are automatic. If a new name is encountered, close matches are presented, and the correct match can be selected.

The script will write a list of IBGE codes corresponding to the municipalities in `output.csv`

If no match has been found for a name, the output will have "UNKNOWN" instead of the IBGE code.

The new matches are stored in `new_names`. Please send a copy of this file to clement.suavet@sei.org when you are done using the tool, so that the new names can be added to the Trase database.

Brazilian 2-letter state codes:

| State name | Code |
|---|---|
|ACRE|AC|
|ALAGOAS|AL|
|AMAPA|AP|
|AMAZONAS|AM|
|BAHIA|BA|
|CEARA|CE|
|DISTRITO FEDERAL|DF|
|ESPIRITO SANTO|ES|
|GOIAS|GO|
|MARANHAO|MA|
|MATO GROSSO DO SUL|MS|
|MATO GROSSO|MT|
|MINAS GERAIS|MG|
|PARAIBA|PB|
|PARANA|PR|
|PARA|PA|
|PERNAMBUCO|PE|
|PIAUI|PI|
|RIO DE JANEIRO|RJ|
|RIO GRANDE DO NORTE|RN|
|RIO GRANDE DO SUL|RS|
|RONDONIA|RO|
|RORAIMA|RR|
|SANTA CATARINA|SC|
|SAO PAULO|SP|
|SERGIPE|SE|
|TOCANTINS|TO|
