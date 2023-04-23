import grpc
import temperature_pb2
import temperature_pb2_grpc
from concurrent import futures

class TemperatureConverterServicer(temperature_pb2_grpc.TemperatureConverterServicer):
    def CelsiusToFahrenheit(self, request, context):
        temperature = request.temperature * 9/5 + 32
        return temperature_pb2.TemperatureResponse(temperature=temperature)

    def FahrenheitToCelsius(self, request, context):
        temperature = (request.temperature - 32) * 5/9
        return temperature_pb2.TemperatureResponse(temperature=temperature)

    def CelsiusToKelvin(self, request, context):
        temperature = request.temperature + 273.15
        return temperature_pb2.TemperatureResponse(temperature=temperature)

    def KelvinToCelsius(self, request, context):
        temperature = request.temperature - 273.15
        return temperature_pb2.TemperatureResponse(temperature=temperature)

    def KelvinToFahrenheit(self, request, context):
        temperature = (request.temperature - 273.15) * 9/5 + 32
        return temperature_pb2.TemperatureResponse(temperature=temperature)

    def FahrenheitToKelvin(self, request, context):
        temperature = (request.temperature - 32) * 5/9 + 273.15
        return temperature_pb2.TemperatureResponse(temperature=temperature)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
temperature_pb2_grpc.add_TemperatureConverterServicer_to_server(TemperatureConverterServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
print("Server started. Listening on port 50051.")
server.wait_for_termination()
