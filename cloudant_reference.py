# CLOUDANT REFERENCE - BLUE BAGUETTE #
# HANS STOETZER #

from cloudant.client import Cloudant
from cloudant.result import Result, ResultByKey
import random

# CREDENTIALS #
# THESE ARE ADMIN CREDENTIALS WITH ALL PERMISSIONS ENABLED.....NO PRESSURE #

USERNAME = "ef15632f-93ee-4c1d-adbc-57c18369feae-bluemix"
PASSWORD = "1124dcfb3c559ffd80306c960ea3fc7cf74814902493828c5bf47f3c3de88b02"
ACCOUNT_NAME = "ef15632f-93ee-4c1d-adbc-57c18369feae-bluemix"

# Use Cloudant to create a Cloudant client using account #

client = Cloudant(USERNAME, PASSWORD, account=ACCOUNT_NAME, connect=True, auto_renew=True)

# Perform client tasks by establishing a session #

session = client.session()

# List all available DB instances #

print('Databases: {0}'.format(client.all_dbs()))

# Open an existing DB #

database = client['master_dataset_v1']

# Retrieve Result wrapped document content - i.e. all instances available to query      #
# I know what you're thinking...I thought this would be slow too... but it's hella fast #

result_collection = Result(database.all_docs, include_docs=True)

# Example of querying an instance, treated just like an Array #

result_collection[0]

# Given the info above, here's a function we'd actually use to retrieve data for the bot #
# Function will return n random instances #

def get_db_entries(n):
    rand = random.randint(0,5804)
    return result_collection[rand:rand + n]

# Example - Retrieve 3 Random Entries #

get_db_entries(3)

# How to logout and end client session #

client.disconnect()

