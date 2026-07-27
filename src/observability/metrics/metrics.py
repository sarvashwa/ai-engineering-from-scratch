from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider

class Metrics:

    def __init__(self, request_counter):
        self.request_counter = request_counter

def create_metrics() -> Metrics:

    meter_provider = MeterProvider()
    metrics.set_meter_provider(meter_provider)

    meter = metrics.get_meter("ai-engineering-from-scratch")

    request_counter = meter.create_counter(
        name = "rag.requests",
        description = "Total RAG requests",
        unit = "1",
    )

    return Metrics(
        request_counter = request_counter
    )