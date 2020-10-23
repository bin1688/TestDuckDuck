import pytest
import datetime
# import datetemp
# from datetemp import DateTemp
import requests

url = 'https://api.duckduckgo.com/?q=presidents%20of%20the%20united%20states&format=json&pretty=1%22'
response = requests.get(url).json()

# create a list with all 45 president names
actual_list_of_president_names = [
    "George Washington",
    "John Adams",
    "Thomas Jefferson",
    "James Madison",
    "James Monroe",
    "John Quincy Adams",
    "Andrew Jackson",
    "Martin Van Buren",
    "William Henry Harrison",
    "John Tyler",
    "James K. Polk",
    "Zachary Taylor",
    "Millard Fillmore",
    "Franklin Pierce",
    "James Buchanan",
    "Abraham Lincoln",
    "Andrew Johnson",
    "Ulysses S. Grant",
    "Rutherford B. Hayes",
    "James Garfield",
    "Rutherford B. Hayes",
    "Rutherford B. Hayes",
    "Benjamin Harrison",
    "Grover Cleveland",
    "William McKinley",
    "Theodore Roosevelt",
    "William Howard Taft",
    "Woodrow Wilson",
    "Warren G. Harding",
    "Calvin Coolidge",
    "Herbert Hoover",
    "Franklin D. Roosevelt",
    "Harry S. Truman",
    "Dwight D. Eisenhower",
    "John F. Kennedy",
    "Lyndon B. Johnson",
    "Richard M. Nixon",
    "Gerald R. Ford",
    "James Carter",
    "Ronald Reagan",
    "George H. W. Bush",
    "William J. Clinton",
    "George W. Bush",
    "Barack Obama",
    "Donald J. Trump",
]

# create a list to put all the presidents' last name.
actualLastName = []
for i in actual_list_of_president_names:
    actualLastName.append(i.split(' ')[-1])

# create a list to put all the presidents' last name from api.duckduckgo.com
presidentLastNamesFromResponse = []
for i in range(len(response["RelatedTopics"])):
    if response["RelatedTopics"][i]['FirstURL'].split('/')[-1].split('_')[-1] in actualLastName:
        presidentLastNamesFromResponse.append(response["RelatedTopics"][i]['FirstURL'].split('/')[-1].replace('_', ' ').split(' ')[-1])

# use actual the actual presidents' last as input value to test with the last names collected from duckduckgo.com
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
