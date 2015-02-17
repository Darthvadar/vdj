# Copyright 2014 Uri Laserson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""params.py

Define directory and file names that must be manually modified
to point to certain resources.
"""

import os
import warnings

warnings.simplefilter('always')

if os.path.isfile(os.path.expanduser('~/.vdjconfig.json')):
    with open(os.path.expanduser('~/.vdjconfig.json'), 'r') as ip:
        config_data = json.load(ip)
else:
    config_data = {}

# locate some directories
vdj_dir = os.path.dirname(os.path.abspath(__file__))

if 'IMGT_DIR' in os.environ:
    imgt_dir = os.environ['IMGT_DIR']
elif 'imgt_dir' in config_data:
    imgt_dir = config_data['imgt_dir']
else:
    warning.warn("Could not load value for imgt_dir. May cause problems loading refseq.")

# define organism of refseq data
organism = 'human'

# define some other directories and variables
data_dir = os.path.join(vdj_dir, 'data')

if 'VDJ_PROCESSED_DIR' in os.environ:
    processed_dir = os.environ['VDJ_PROCESSED_DIR']
elif 'processed_dir' in config_data:
    processed_dir = config_data['processed_dir']
else:
    processed_dir = os.path.join(vdj_dir, 'processed')
