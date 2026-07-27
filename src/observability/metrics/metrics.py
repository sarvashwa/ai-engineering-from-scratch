from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import InMemoryMetricReader
from opentelemetry.sdk.metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
)

class Metrics:

    def __init__(self, request_counter):
        self.request_counter = request_counter

def create_metrics() -> Metrics:

    # metric_reader = InMemoryMetricReader()
    
    # meter_provider = MeterProvider(
    #     metric_readers=[metric_reader]
    # )

    exporter = ConsoleMetricExporter()

    metric_reader = PeriodicExportingMetricReader(
        exporter=exporter
    )

    meter_provider = MeterProvider(
        metric_readers=[metric_reader]
    )
    metrics.set_meter_provider(meter_provider)

    meter = metrics.get_meter("ai-engineering-from-scratch")

    metrics.set_meter_provider(meter_provider)

    request_counter = meter.create_counter(
        name = "rag.requests",
        description = "Total RAG requests",
        unit = "1",
    )

    return Metrics(
        request_counter = request_counter
    )