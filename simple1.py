#!./CICD/bin/python3

from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F
from prettyprinter import pprint
from nornir.core.exceptions import NornirExecutionError

nr = InitNornir(config_file="config.yaml")

nr.inventory.defaults.username = "jlapaca"
nr.inventory.defaults.password = "A#!B59E+ZnPS"
#nr.inventory.defaults.port = 22

def nugget_test(task):
    task.run(napalm_get, getters=["get_facts"])

#results = nr.run(task=nugget_test)
devices = nr.filter(asset_tag = "01-SW02-R1P2")
result = devices.run(task=nugget_test)
print_result(result)
failure = nr.data.failed_hosts
if failure:
    raise NornirExecutionError("Nornir Failure Detected")
#import ipdb;
#ipdb.set_trace()