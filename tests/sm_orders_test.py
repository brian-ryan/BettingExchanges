import sys
import configparser
import os
import pandas as pd
import time

sys.path.append("../smarketswrapper")
# Importing modules
import sessions
import orders

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', None)

def parse_config():
    conf_path = os.path.dirname(__file__).replace("tests", "conf") + "/conf.conf"

    config = configparser.ConfigParser()
    config.read(conf_path)

    configs_dict = {}

    for field in config["details"]:
        configs_dict[field] = config["details"][field]

    return configs_dict


configs = parse_config()
uname = configs["sm_uname"]
pw = configs["sm_pw"]

def main():
    success, sesstoken = sessions.connect_session(uname, pw)

    if success:

        # Test 1 - should be success
        success, details = orders.place_order(sesstoken, 43440296, 12553850, 0.05, 2, "buy", 'good_til_halted')

        if success and type(details)==dict:
            print('Test 1 for placing an order successful.')
        else:
            print('Test 1 for placing order failed, success: {0}, details: {1}'.format(success, details))

        # Test 2 - should be success
        success, details = orders.place_order(sesstoken, 43440296, 12553850, 0.5, 2, "sell",
                                              'good_til_halted')

        if success and type(details) == dict:
            print('Test 2 for placing an order successful.')
        else:
            print('Test 2 for placing order failed, success: {0}, details: {1}'.format(success, details))

        # Test 3 - should be a failure

        success, details = orders.place_order(sesstoken, 434402960, 12553850, 0.5, 2, "sell",
                                              'good_til_halted')

        if success==False and type(details) == str:
            print('Test 3 for placing an order successful.')
        else:
            print('Test 3 for placing order failed, success: {0}, details: {1}'.format(success, details))

        # Test 4 - should be a success

        success, details = orders.get_order_log(sesstoken)
        print(details)
        if success and type(details)==dict:
            print("Test 4 for getting order log successful")
        else:
            print("Test 4 for placing order failed, success: {0}, details: {1}".format(success, details))

        # Test 5 - should fail

        success, details = orders.get_order_log(sesstoken+"a")

        if success==False and type(details) == str:
            print("Test 5 for getting order log successful")
        else:
            print("Test 5 for placing order failed, success: {0}, details: {1}".format(success, details))


    else:
        print("Failed to generate a session token, cannot perform tests.")




main()

#success, sesstoken = sessions.connect_session(uname, pw)
#success, details = orders.place_order(sesstoken, 43440296, 12553850, 0.05, 1, "buy", 'good_til_halted')
#time.sleep(1)
#success, details = orders.get_order_log(sesstoken)

#print('Live data frame')
#print(details['live'])

#print('Fills data frame')
#print(details['fills'])

#print('Pending data frame')
#print(details['pending'])






