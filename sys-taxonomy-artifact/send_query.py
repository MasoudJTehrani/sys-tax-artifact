

import findpapers
import datetime

# Use the following command to search for papers

# pip install findpapers

# findpapers search /output.json --query '(([autonomous] OR [self driving] OR [driverless] OR [unmanned] OR [automated]) AND ([vehicle*] OR [car*] OR [drone*] OR [robot*]) AND ([attack*] OR [exploit*] OR [threat*] OR [adversarial]))' --since 2017-01-01 --token-scopus "47d55b6080a1477d8750ceee0856d4ee" --token-ieee "6bjgy2dp7544azdspnc8cpud" --publication-types "journal, conference proceedings" --databases "scopus,ieee,acm"

# this is for text
# findpapers search /content/TestQueryResults2017.json --limit-db 1 --query '(([autonomous] OR [self driving] OR [driverless] OR [unmanned] OR [automated]) AND ([vehicle*] OR [car*] OR [drone*] OR [robot*]) AND ([attack*] OR [exploit*] OR [threat*] OR [adversarial]))' --since 2017-01-01 --token-scopus "47d55b6080a1477d8750ceee0856d4ee" --token-ieee "6bjgy2dp7544azdspnc8cpud" --publication-types "journal, conference proceedings" --databases "scopus,ieee,acm"