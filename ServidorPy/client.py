import grpc
import temperature_pb2
import temperature_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = temperature_pb2_grpc.TemperatureConverterStub(channel)

while True:
    print("Select an option:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Kelvin to Fahrenheit")
    print("6. Fahrenheit to Kelvin")
    print("7. Quit")

    option = input()
    if option == "7":
        break

    print("Enter a temperature value:")
    value = float(input())

    if option == "1":
        temperature = temperature_pb2.TemperatureRequest(temperature=value, unit="C")
        response = stub.CelsiusToFahrenheit(temperature)
        print(f"{value}C = {response.temperature}F")
    elif option == "2":
        temperature = temperature_pb2.TemperatureRequest(temperature=value, unit="F")
        response = stub.FahrenheitToCelsius(temperature)
        print(f"{value}F = {response.temperature}C")
    elif option == "3":
        temperature = temperature_pb2.TemperatureRequest(temperature=value, unit="C")
        response = stub.CelsiusToKelvin(temperature)
        print(f"{value}C = {response.temperature}K")
    elif option == "4":
        temperature = temperature_pb2.TemperatureRequest(temperature=value, unit="K")
        response = stub.KelvinToCelsius(temperature)
        print(f"{value}K = {response.temperature}C")
    elif option == "5":
        temperature = temperature_pb2.TemperatureRequest(temperature=value, unit="K")
        response = stub.KelvinToFahrenheit(temperature)
        print(f"{value}K = {response.temperature}F")
    elif option == "6":
        temperature = temperature_pb2.TemperatureRequest(temperature=value, unit="F")
        response = stub.FahrenheitToKelvin(temperature)
        print(f"{value}F = {response.temperature}K")
    else:
        print("Invalid option. Please select a valid option.")
