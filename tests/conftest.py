import pytest
import sys
import os
#from pytest_reorder import default_reordering_hook as pytest_collection_modifyitems
from pytest_reorder import make_reordering_hook

import time

# https://opentelemetry-python.readthedocs.io/en/latest/
# from opentelemetry import metrics
# from opentelemetry.sdk.metrics import Counter, MeterProvider
# from opentelemetry.sdk.metrics.export import ConsoleMetricsExporter
# from opentelemetry.sdk.metrics.export.controller import PushController
#
# # https://github.com/open-telemetry/opentelemetry-python/blob/master/examples/metrics/collector.py
# from opentelemetry.ext.otcollector.metrics_exporter import (
#     CollectorMetricsExporter,
# )


tests_order = [
    "basic",
    "file",
    "query",
    "schema",
    "profile",
    "sla",
    "attach",
    "slow",
    None
]

sys.path.append(os.path.join(os.path.dirname(__file__), 'helpers'))

skipmarkers = [
    "slow",
    "slas",
    "profiles",
    "queries",
    "files",
    "schema",
    "basic",
    "diag",
]
#TODO: figure out how to present the last line of stdout from 'neoload' to test step (after step name)
#https://pythontesting.net/framework/pytest/pytest-logging-real-time/

def pytest_addoption(parser):
    parser.addoption(
        "--skipall", action="store_true", default=False, help="skips all tests...except those specified with --only[category]"
    )
    for m in skipmarkers:
        parser.addoption(
            "--skip"+m, action="store_true", default=False, help="skips "+m+" tests"
        )
        parser.addoption(
            "--only"+m, action="store_true", default=False, help="only run "+m+" tests"
        )

def pytest_configure(config):
    for m in skipmarkers:
        config.addinivalue_line("markers", m+": mark test as "+m+" to run")

def pytest_collection_modifyitems(session, config, items):

    reorderingFunction = make_reordering_hook(
        list(map(lambda s: None if s is None else r'(^|.*/)(test_)?'+s, tests_order))
    )

    skip = pytest.mark.skip(reason="need option to run")

    for item in items:
        if any(filter(lambda m: config.getoption("--only"+m), skipmarkers)):
            for m in skipmarkers:
                if m in item.keywords and not config.getoption("--only"+m):
                    item.add_marker(skip)
        else:
            for m in skipmarkers:
                if m in item.keywords and config.getoption("--skip"+m):
                    item.add_marker(skip)

    reorderingFunction(session,config,items)



#def pytest_configure(config):

# def pytest_sessionstart(session):
#     metrics.set_preferred_meter_implementation(lambda T: Meter())
#     meter = metrics.meter()
#     exporter = ConsoleMetricsExporter()
#
#     counter = meter.create_metric(
#         "totalTime",
#         int,
#         Counter,
#         ("test",),
#     )
#
#
# def pytest_sessionfinish(session, exitstatus):
#     exporter.export([(counter, label_values)])
#     exporter.shutdown()
#
# #def pytest_unconfigure(config):
#
# def current_time():
#     return int(round(time.time() * 1000))
#
# @pytest.fixture(scope="function", autouse=True)
# def run_around_tests(request):
#     start_time = current_time()
#
#     yield
#
#     total_time = current_time() - start_time
#
#     label_values = ("staging",)
#     counter_handle = counter.get_handle(label_values)
#     counter_handle.add(total_time)
