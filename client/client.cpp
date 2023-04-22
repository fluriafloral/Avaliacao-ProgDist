#include <iostream>
#include <memory>
#include <grpcpp/grpcpp.h>
#include "temperature_conversion.grpc.pb.h"

using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;
using temperature::TemperatureConversion;
using temperature::CelsiusToFahrenheitRequest;
using temperature::CelsiusToFahrenheitResponse;

class TemperatureConversionClient {
 public:
  TemperatureConversionClient(std::shared_ptr<Channel> channel)
      : stub_(TemperatureConversion::NewStub(channel)) {}

  double ConvertCelsiusToFahrenheit(double temperature_celsius) {
    CelsiusToFahrenheitRequest request;
    request.set_temperature_celsius(temperature_celsius);

    CelsiusToFahrenheitResponse response;
    ClientContext context;

    Status status = stub_->ConvertCelsiusToFahrenheit(&context, request, &response);

    if (status.ok()) {
      return response.temperature_fahrenheit();
    } else {
      std::cout << "Error converting temperature: " << status.error_code() << ": " << status.error_message() << std::endl;
      return 0.0;
    }
  }

 private:
  std::unique_ptr<TemperatureConversion::Stub> stub_;
};

int main(int argc, char** argv) {
  std::string server_address("localhost:50051");

  TemperatureConversionClient client(grpc::CreateChannel(server_address, grpc::InsecureChannelCredentials()));

  double temperature_celsius = 20.0;
  double temperature_fahrenheit = client.ConvertCelsiusToFahrenheit(temperature_celsius);

  std::cout << temperature_celsius << " degrees Celsius is equal to " << temperature_fahrenheit << " degrees Fahrenheit." << std::endl;

  return 0;
}