import pytest
import requests

url = 'https://api.duckduckgo.com/?q=presidents%20of%20the%20united%20states&format=json&pretty=1%22'
response = requests.get(url).json()

# create a list to put all the presidents' last name from api.duckduckgo.com
presidentLastNamesFromResponse = []
for president in response["RelatedTopics"]:
    presidentLastNamesFromResponse.append(president['FirstURL'].split('/')[-1].replace('_', ' ').split(' ')[-1])

# use actual presidents' last names as an input value to test with the last names collected from duckduckgo.com
@pytest.mark.parametrize("actualPresidentLastName", ['Adams', 'Adams', 'Buchanan',
                                       'Buren', 'Bush', 'Bush', 'Carter',
                                       'Cleveland', 'Clinton', 'Coolidge',
                                       'Eisenhower', 'Fillmore', 'Ford',
                                       'Garfield', 'Grant', 'Harding',
                                       'Harrison', 'Harrison', 'Hayes',
                                       'Hayes', 'Hayes', 'Hoover', 'Jackson',
                                       'Jefferson', 'Johnson', 'Johnson',
                                       'Kennedy', 'Lincoln', 'Madison',
                                       'McKinley', 'Monroe', 'Nixon',
                                       'Obama', 'Pierce', 'Polk', 'Reagan',
                                       'Roosevelt', 'Roosevelt', 'Taft',
                                       'Taylor', 'Truman', 'Trump', 'Tyler',
                                       'Washington', 'Wilson'])
def test_EachPresidentInList(actualPresidentLastName):
    assert actualPresidentLastName in presidentLastNamesFromResponse
