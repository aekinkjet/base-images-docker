# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""A binary for constructing images from a source context."""

import sys
import argparse

from containerregistry.tools import patched

from ftl.common import args
from ftl.common import logger
from ftl.common import builder_runner

from ftl.python import builder as python_builder

parser = argparse.ArgumentParser(
    description='Construct python images from source.')

args.init_args(parser)
# TODO(aaron-prindle) remove this once arg passing solution discovered
parser.add_argument(
    '--destination',
    dest='destination_path',
    action='store',
    default=None,
    help='The base path that the node_modules will be installed in the \
    final image')

# Version string used to bust caches.
_PYTHON_CACHE_VERSION = 'v1'


def main(args):
    args = parser.parse_args(args)
    logger.setup_logging(args)
    python_ftl = builder_runner.BuilderRunner(args, python_builder,
                                              _PYTHON_CACHE_VERSION)
    python_ftl.GenerateFTLImage()


if __name__ == '__main__':
    with patched.Httplib2():
        main(sys.argv[1:])
