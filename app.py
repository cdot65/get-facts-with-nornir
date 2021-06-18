from nornir_pyez.plugins.tasks import pyez_facts
import os
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from rich import print


script_dir = os.path.dirname(os.path.realpath(__file__))
nr = InitNornir(config_file=f"{script_dir}/config.yaml")

response = nr.run(
    pyez_facts
)

devices = []
for dev in response:
    print(response[dev].result)
