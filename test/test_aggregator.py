# coding: utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


from apm.aggregator import Aggregator


def test_merge_metrics():
    aggregator = Aggregator('test', 100000)
    aggregator.put({
        'responseTime': 10,
        'count': 1,
        'statusCode': 1,
        'url': 'foo',
    })
    aggregator.put({
        'responseTime': 20,
        'count': 2,
        'statusCode': 1,
        'url': 'foo',
    })
    metrics = aggregator.buffer[('foo', 1)]
    assert metrics['count'] == 3
    assert metrics['responseTime'] == (10 + 20 * 2) / 3
