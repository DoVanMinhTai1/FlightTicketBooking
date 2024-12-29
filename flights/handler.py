from datetime import datetime

from flights.models import Flight


def find_intermediate_flights(flights,flightday,origin,destination):
    flights = Flight.objects.filter(
        depart_day=flightday,
        origin=origin.pk,
        destination=destination.pk
    ).exclude(
        economy_fare=0
    )
    # chuyến bay có thể tới điểm đích
    flights_sts = Flight.objects.filter(
        depart_day=flightday,
        destination=destination.pk
    ).exclude(
        economy_fare=0
    )

    # Collect intermediate stop points
    l = [fl.origin for fl in flights_sts if fl.origin != origin]

    # Chuyến bay có thể đi từ điểm đầu đến điểm trung gian
    flights_stt = Flight.objects.filter(
        depart_day=flightday,
        origin=origin,
        destination__in=l
    ).exclude(
        economy_fare=0
    )
    # lấy những chuyến bay hợp lệ chỉ lấy 5 cái bay thẳng và 3 cái có nối chuyến (gồm 2 chuyến nhỏ)
    valid_flight = []
    intermediate_flights = []
    for fl in flights:
        valid_flight.append(fl)
        if len(valid_flight) == 5:
            break
    check = {origin.code}
    for fl in flights_stt:
        if len(valid_flight) >= 10:
            break
        for fl1 in flights_sts:
            if fl.destination == fl1.origin and fl.arrival_time < fl1.depart_time:
                if not check.__contains__(fl.destination):
                    today = datetime.today().date()
                    arrival_datetime = datetime.combine(today, fl.arrival_time)
                    departure_datetime = datetime.combine(today, fl1.depart_time)
                    waiting_time = departure_datetime - arrival_datetime
                    valid_flight.append(fl)
                    valid_flight.append(fl1)
                    intermediate_flights.append((fl, fl1, waiting_time))
                    print(f"Added intermediate flights: {fl} -> {fl1}")
                    check.add(fl.destination)

    # Combine all QuerySets (order_by is applied only after union)
    # flights = flights.union(flights_sts).union(flights_stt).order_by('economy_fare')
    return {'valid_flight': valid_flight, 'intermediate_flights': intermediate_flights}

def connecting_flights(flight0Id,flight1Id,flight0Date,flight1Date):
    flight0 = Flight.objects.get(id=flight0Id)
    flight1 = Flight.objects.get(id=flight1Id)
    flight0ddate = datetime(int(flight0Date.split('-')[2]), int(flight0Date.split('-')[1]),
                            int(flight0Date.split('-')[0]),
                            flight0.depart_time.hour, flight0.depart_time.minute)
    flight0adate = (flight0ddate + flight0.duration)

    flight1ddate = datetime(int(flight1Date.split('-')[2]), int(flight1Date.split('-')[1]),
                            int(flight1Date.split('-')[0]),
                            flight1.depart_time.hour, flight1.depart_time.minute)
    flight1adate = (flight1ddate + flight1.duration)
    return {'flight0': flight0,
            'flight1': flight1,
            'flight0adate': flight0adate,
            'flight0ddate': flight0ddate,
            "flight1ddate": flight1ddate,
            "flight1adate": flight1adate}