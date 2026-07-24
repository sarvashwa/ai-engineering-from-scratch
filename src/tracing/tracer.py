from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor

def configure_tracing():

    provider = TracerProvider()
    trace.set_tracer_provider(provider)

    exporter = ConsoleSpanExporter()
    
    processor = BatchSpanProcessor(exporter)

    provider.add_span_processor(processor)
    