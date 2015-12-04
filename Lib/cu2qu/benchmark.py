# Copyright 2015 Google Inc. All Rights Reserved.
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


from __future__ import print_function, division, absolute_import

import random
import timeit

MAX_ERR = 5
MAX_N = 10

SETUP_CODE = '''
from cu2qu import %s
from __main__ import setup_%s
args = setup_%s()
'''


def generate_curve():
    return [
        tuple(float(random.randint(0, 2048)) for coord in range(2))
        for point in range(4)]


def setup_curve_to_quadratic():
    return generate_curve(), MAX_ERR, MAX_N


def setup_curves_to_quadratic():
    num_curves = 3
    return (
        [generate_curve() for curve in range(num_curves)],
        [MAX_ERR] * num_curves, MAX_N)


def run_test(name):
    print('%s:' % name)
    results = timeit.repeat(
        '%s(*args)' % name,
        setup=(SETUP_CODE % (name, name, name)),
        repeat=1000, number=1)
    print('min: %s s' % min(results))
    print('avg: %s s' % (sum(results) / len(results)))
    print()


def main():
    random.seed(1)
    run_test('curve_to_quadratic')
    run_test('curves_to_quadratic')


if __name__ == '__main__':
    main()