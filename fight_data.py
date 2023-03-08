class FlightData:

    # def __init__(
    #     self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date, stop_overs=0, via_city=""):
    #     self.price = price
    #     self.origin_city = origin_city
    #     self.origin_airport = origin_airport
    #     self.destination_city = destination_city
    #     self.destination_airport = destination_airport
    #     self.out_date = out_date
    #     self.return_date = return_date
    #     self.stop_overs = stop_overs
    #     self.via_city = via_city
try:
    data = response.json()["data"][0]
except IndexError:
    #print("Exception activated!")
    query["max_stopovers"] = 1

    response = request.get(
        url=f"{os.getenv('Tequila Endpoint')}/v2/search",
        headers=headers,
        params=query,
    )

    try: data = response.json()["data"][0]
        #pprint(data)
    except IndexError:
        return None
    else: flight_data = FlightData(
        price=data["price"],
        origin_city=data["route"][0]["cityFrom"],
        origin_airport=data["route"][0]["flyFrom"],
        destination_city=data["route"][1]["cityTo"],
        destination_airport=data["route"][1]["flyTo"],
        out_date=data["route"][0]["local_departure"].split("T")[0],
        return_date=data["route"][2]["local_departure"].split("T")[0],
        stop_overs=1,
        via_city=data["route"][0]["cityTo"]
    )

    print(f"{flight_data.destination_city}: ＄{flight_data.price}")
    return flight_data
else:
    flight_data = FlightData(
        price = data["price"],
        origin_city=data["route"][0]["cityFrom"],
        origin_airport=data["route"][0]["flyFrom"],
        destination_city=data["route"][0]["cityTo"],
        destination_airport=data["route"][0]["flyTo"],
        out_date=data["route"][0]["local_departure"].split("T")[0],
        return_date=data["route"][1]["local_departure"].split("T")[0]
    )

    print(f"{flight_data.destination_city}: ＄{flight_data.price}")
    return flight_data