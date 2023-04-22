#include <iostream>
#include <memory>
#include <string>
#include <grpcpp/grpcpp.h>
#include "temperature_conversion.grpc.pb.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;
using temperature::TemperatureConversion;
using temperature::CelsiusToFahrenheitRequest;
using temperature::CelsiusToFahrenheitResponse;
using temperature::FahrenheitToCelsiusRequest;
using temperature::FahrenheitToCelsiusResponse;

class TemperatureConversionServiceImpl final : public TemperatureConversion::Service {
 public:
  Status ConvertCelsiusToFahrenheit(ServerContext* context, const CelsiusToFahrenheitRequest* request, CelsiusToFahrenheitResponse* response) override {
    double temperature_celsius = request->temperature_celsius();
    double temperature_fahrenheit = temperature_celsius * 1.8 + 32.0;

    response->set_temperature_fahrenheit(temperature_fahrenheit);

    return Status::OK;
  }

  Status ConvertFahrenheitToCelsius(ServerContext* context, const FahrenheitToCelsiusRequest* request, FahrenheitToCelsiusResponse* response) override {
    double temperature_fahrenheit = request->temperature_fahrenheit();
    double temperature_celsius = (temperature_fahrenheit - 32.0) / 1.8;

    response->set_temperature_celsius(temperature_celsius);

    return Status::OK;
  }
};

void RunServer() {
  std::string server_address("0.0.0.0:50051");
  TemperatureConversionServiceImpl service;

  ServerBuilder builder;
  builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
  builder.RegisterService(&service);
  std::unique_ptr<Server> server(builder.BuildAndStart());
  std::cout << "Server listening on " << server_address << std::endl;
  server->Wait();
}

int main(int argc, char** argv) {
  RunServer();
  return 0;
}
