# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import sys
import subprocess

root_dir = '/usr/lib64/az/lib/python3.6/site-packages/azure/cli/command_modules'
mod_list = [mod for mod in sorted(os.listdir(root_dir)) if os.path.isdir(os.path.join(root_dir, mod)) and mod != '__pycache__']

pytest_base_cmd = 'PYTHONPATH=/usr/lib64/az/lib/python3.6/site-packages python3 -m pytest -x -v --boxed -p no:warnings --log-level=WARN'
pytest_parallel_cmd = '{} -n auto'.format(pytest_base_cmd)

exit_code = subprocess.call(['{} --junit-xml /azure_cli_test_result/{}.xml --pyargs azure.cli.command_modules.{}'.format(pytest_parallel_cmd, 'vm', 'vm')], shell=True)
if exit_code == 5:
    print('No tests found for {}'.format(mod_name))
elif exit_code != 0:
    sys.exit(exit_code)
