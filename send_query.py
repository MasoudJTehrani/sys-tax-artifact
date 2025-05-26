# Use the following command in a terminal to search for papers and replicate our results

pip install findpapers

# Collelcting papers from 2017 to January 2024
findpapers search output.json --query '(([autonomous] OR [self driving] OR [driverless] OR [unmanned] OR [automated]) AND ([vehicle*] OR [car*] OR [drone*] OR [truck*] OR [tractor*] OR [submarine*] OR [boat*] OR [maritime]) AND ([attack*] OR [exploit*] OR [threat*] OR [adversarial]))' --since 2017-01-01  --until 2024-01-01 --token-scopus "47d55b6080a1477d8750ceee0856d4ee" --token-ieee "6bjgy2dp7544azdspnc8cpud" --publication-types "journal, conference proceedings" --databases "scopus,ieee,acm"

# You can remove the "until" argument to collect all the papers from 2017 to now. But it will not replicate our results