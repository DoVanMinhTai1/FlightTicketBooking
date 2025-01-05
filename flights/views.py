from django.shortcuts import render
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
import math
from . import handler
from payment.models import Seat
from .models import *
from .constant import FEE
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create your views here.
"""
Hàm flight lấy dữ liệu từ request và kiểm tra loại chuyến bay là 1 hay 2 ( khứ hồi hay 1 chiều) sau đó sẽ truy vấn dựa vào loại chuyến bay cùng với hạng ghế 
kết quả sẽ được truyền đến trang search.html
"""
def flight(request):
    o_place = request.GET.get('Origin')
    d_place = request.GET.get('Destination')
    trip_type = request.GET.get('TripType')
    departdate = request.GET.get('DepartDate')
    depart_date = datetime.strptime(departdate, "%Y-%m-%d")
    people = request.GET.get('people')
    return_date = None
    if trip_type == '2':
        returndate = request.GET.get('ReturnDate')
        return_date = datetime.strptime(returndate, "%Y-%m-%d")
        flightday2 = Week.objects.get(number=return_date.weekday())  ##
        origin2 = Place.objects.get(code=d_place.upper())  ##
        destination2 = Place.objects.get(code=o_place.upper())  ##
    # seat = request.GET.get('SeatClass')
    seat = 'economy'
    flightday = Week.objects.get(number=depart_date.weekday())
    destination = Place.objects.get(code=d_place.upper())
    origin = Place.objects.get(code=o_place.upper())
    intermediate_flights = []
    intermediate_flights2 = []
    flights = None
    if seat == 'economy':
        # lấy chuyến bay thẳng
        flights = Flight.objects.filter(
            depart_day=flightday,
            origin=origin.pk,
            destination=destination.pk
        ).exclude(
            economy_fare=0
        )
        flights_with_seats = []
        for fl in flights:
            # Đếm số ghế trống cho mỗi chuyến bay
            available_seats = Seat.objects.filter(status='AVAILABLE', flight=fl).count()

            # Kiểm tra xem chuyến bay có đủ ghế cho số người cần
            if available_seats >= int(people):
                flights_with_seats.append(fl)
        try:
            max_price = flights.last().economy_fare
            min_price = flights.first().economy_fare
        except:
            max_price = 0
            min_price = 0

        if trip_type == '2':  ##
            flights2 = Flight.objects.filter(depart_day=flightday2, origin=origin2.pk, destination=destination2.pk).exclude(
                economy_fare=0).order_by('economy_fare')  ##
            flights_with_seats2 = []
            for fl in flights2:
                # Đếm số ghế trống cho mỗi chuyến bay
                available_seats = Seat.objects.filter(status='AVAILABLE', flight=fl).count()

                # Kiểm tra xem chuyến bay có đủ ghế cho số người cần
                if available_seats >= int(people):
                    flights_with_seats2.append(fl)
            try:
                max_price2 = flights2.last().economy_fare  ##
                min_price2 = flights2.first().economy_fare  ##
            except:
                max_price2 = 0  ##
                min_price2 = 0  ##
            intermediate_flights2 = handler.find_intermediate_flights(flights2,flightday2, origin2, destination2,people).get('intermediate_flights')
    elif seat == 'business':
        flights = Flight.objects.filter(depart_day=flightday, origin=origin, destination=destination).exclude(
            business_fare=0).order_by('business_fare')
        flights_with_seats = []
        for fl in flights:
            # Đếm số ghế trống cho mỗi chuyến bay
            available_seats = Seat.objects.filter(status='AVAILABLE', flight=fl).count()

            # Kiểm tra xem chuyến bay có đủ ghế cho số người cần
            if available_seats >= int(people):
                flights_with_seats.append(fl)
        try:
            max_price = flights.last().business_fare
            min_price = flights.first().business_fare
        except:
            max_price = 0
            min_price = 0

        if trip_type == '2':  ##
            flights2 = Flight.objects.filter(depart_day=flightday2, origin=origin2, destination=destination2).exclude(
                business_fare=0).order_by('business_fare')  ##
            flights_with_seats2 = []
            for fl in flights2:
                # Đếm số ghế trống cho mỗi chuyến bay
                available_seats = Seat.objects.filter(status='AVAILABLE', flight=fl).count()

                # Kiểm tra xem chuyến bay có đủ ghế cho số người cần
                if available_seats >= int(people):
                    flights_with_seats2.append(fl)
            try:
                max_price2 = flights2.last().business_fare  ##
                min_price2 = flights2.first().business_fare  ##
            except:
                max_price2 = 0  ##
                min_price2 = 0  ##
            intermediate_flights2 = handler.find_intermediate_flights(flights2, flightday2, origin2,
                                                                               destination2,people).get('intermediate_flights')

    elif seat == 'first':
        flights = Flight.objects.filter(depart_day=flightday, origin=origin, destination=destination).exclude(
            first_fare=0).order_by('first_fare')
        flights_with_seats = []
        for fl in flights:
            # Đếm số ghế trống cho mỗi chuyến bay
            available_seats = Seat.objects.filter(status='AVAILABLE', flight=fl).count()

            # Kiểm tra xem chuyến bay có đủ ghế cho số người cần
            if available_seats >= int(people):
                flights_with_seats.append(fl)
        try:
            max_price = flights.last().first_fare
            min_price = flights.first().first_fare
        except:
            max_price = 0
            min_price = 0

        if trip_type == '2':  ##
            flights2 = Flight.objects.filter(depart_day=flightday2, origin=origin2, destination=destination2).exclude(
                first_fare=0).order_by('first_fare')
            flights_with_seats2 = []
            for fl in flights2:
                # Đếm số ghế trống cho mỗi chuyến bay
                available_seats = Seat.objects.filter(status='AVAILABLE', flight=fl).count()

                # Kiểm tra xem chuyến bay có đủ ghế cho số người cần
                if available_seats >= int(people):
                    flights_with_seats2.append(fl)
            try:
                max_price2 = flights2.last().first_fare  ##
                min_price2 = flights2.first().first_fare  ##
            except:
                max_price2 = 0  ##
                min_price2 = 0  ##    ##
            intermediate_flights2 = handler.find_intermediate_flights(flights2, flightday2, origin2,
                                                                               destination2,people).get('intermediate_flights')
    intermediate_flights = handler.find_intermediate_flights(flights,flightday, origin, destination,people).get('intermediate_flights')
    # print(calendar.day_name[depart_date.weekday()])
    if trip_type == '2':
        return render(request, "search.html", {
            'flights': flights_with_seats,
            'origin': origin,
            'destination': destination,
            'flights2': flights_with_seats2,  ##
            'origin2': origin2,  ##
            'destination2': destination2,  ##
            'seat': seat.capitalize(),
            'trip_type': trip_type,
            'depart_date': depart_date,
            'return_date': return_date,
            'max_price': math.ceil(max_price / 100) * 100,
            'min_price': math.floor(min_price / 100) * 100,
            'max_price2': math.ceil(max_price2 / 100) * 100,  ##
            'min_price2': math.floor(min_price2 / 100) * 100,
            'intermediate_flights': intermediate_flights,
            'intermediate_flights2': intermediate_flights2,
            'people': people,
        })
    else:
        return render(request, "search.html", {
            'flights': flights_with_seats,
            'origin': origin,
            'destination': destination,
            'seat': seat.capitalize(),
            'trip_type': trip_type,
            'depart_date': depart_date,
            'return_date': return_date,
            'max_price': math.ceil(max_price / 100) * 100,
            'min_price': math.floor(min_price / 100) * 100,
            'intermediate_flights': intermediate_flights,
            'people': people,
        })

def review(request):
    if request.user.is_authenticated:
        people = request.GET.get('people')
        if request.GET.get('tripType') == '1':
            if request.GET.get('stop') == 'yes':
                # Xử lý cho chuyến bay cho nối chuyến
                flight0Id = request.GET.get('flight.0.id')
                flight1Id = request.GET.get('flight.1.id')
                flight0Date = request.GET.get('flight.0.date')
                flight1Date = request.GET.get('flight.1.date')
                seat = request.GET.get('seatClass')
                connecting = handler.connecting_flights(flight0Id, flight1Id, flight0Date, flight1Date)
                return render(request, "book.html", {
                        'flight0': connecting.get('flight0'),
                        'flight1': connecting.get('flight1'),
                        'flight0adate': connecting.get('flight0adate'),
                        'flight0ddate': connecting.get('flight0ddate'),
                        "flight1ddate": connecting.get('flight1ddate'),
                        "flight1adate": connecting.get('flight1adate'),
                        "seat": seat,
                        "fee": FEE,
                        'seats1': Seat.objects.filter(flight=connecting.get('flight0').pk),
                        'stop': 'yes',
                        'tripType': '1',
                        'people': people,
                    })
            if request.GET.get('stop') == 'no':
                #Xử lý cho chuyến bay không nối chuyến vẫn giữ nguyên
                flight_1 = request.GET.get('flight1Id')
                date1 = request.GET.get('flight1Date')
                seat = request.GET.get('seatClass')
                flight1 = Flight.objects.get(id=flight_1)
                flight1ddate = datetime(int(date1.split('-')[2]), int(date1.split('-')[1]), int(date1.split('-')[0]),
                                        flight1.depart_time.hour, flight1.depart_time.minute)
                flight1adate = (flight1ddate + flight1.duration)
                return render(request, "book.html", {
                    'flight1': flight1,
                    "flight1ddate": flight1ddate,
                    "flight1adate": flight1adate,
                    "seat": seat,
                    "fee": FEE,
                    'tripType': '1',
                    'stop': 'no',
                    'seats1': Seat.objects.filter(flight=flight1.pk),
                    'people': people,
                })
        else:
            stop1 = request.GET.get('stop1')
            stop2 = request.GET.get('stop2')
            re = {'tripType': '2', 'people': people,}
            # Xử lý cho chuyến bay cho nối chuyến
            if stop1 =='yes':
                flightId = request.GET.get('flight1Id')
                flight0Id = flightId.split(',')[0]
                flight1Id = flightId.split(',')[1]
                flight0Date = request.GET.get('flight.0.date')
                flight1Date = request.GET.get('flight.1.date')
                seat = request.GET.get('seatClass')
                connecting = handler.connecting_flights(flight0Id, flight1Id, flight0Date, flight1Date)
                re.update({
                        'flight0': connecting.get('flight0'),
                        'flight1': connecting.get('flight1'),
                        'flight0adate': connecting.get('flight0adate'),
                        'flight0ddate': connecting.get('flight0ddate'),
                        "flight1ddate": connecting.get('flight1ddate'),
                        "flight1adate": connecting.get('flight1adate'),
                        "seat": seat,
                        "fee": FEE,
                        'seats1': Seat.objects.filter(flight=connecting.get('flight0').pk),
                        'stop1': 'yes',
                    })
            if stop2 =='yes':
                flightId = request.GET.get('flight2Id')
                flight0Id = flightId.split(',')[0]
                flight1Id = flightId.split(',')[1]
                flight0Date = request.GET.get('flight.2.date')
                flight1Date = request.GET.get('flight.3.date')
                seat = request.GET.get('seatClass')
                connecting = handler.connecting_flights(flight0Id, flight1Id, flight0Date, flight1Date)
                re.update({
                    'flight2': connecting.get('flight0'),
                    'flight3': connecting.get('flight1'),
                    'flight2adate': connecting.get('flight0adate'),
                    'flight2ddate': connecting.get('flight0ddate'),
                    "flight3ddate": connecting.get('flight1ddate'),
                    "flight3adate": connecting.get('flight1adate'),
                    "seat": seat,
                    "fee": FEE,
                    'seats2': Seat.objects.filter(flight=connecting.get('flight0').pk),
                    'stop2': 'yes',
                })
            if stop1 =='yes' and stop2 =='yes':
                return render(request, "book.html", re)
            if stop1 =='no' and stop2 =='no':
                # Xử lý cho chuyến bay không nối chuyến vẫn giữ nguyên
                flight_1 = request.GET.get('flight1Id')
                date1 = request.GET.get('flight1Date')
                seat = request.GET.get('seatClass')
                round_trip = False
                if request.GET.get('flight2Id'):
                    round_trip = True

                if round_trip:
                    flight_2 = request.GET.get('flight2Id')
                    date2 = request.GET.get('flight2Date')

                flight1 = Flight.objects.get(id=flight_1)
                flight1ddate = datetime(int(date1.split('-')[2]), int(date1.split('-')[1]),
                                        int(date1.split('-')[0]),
                                        flight1.depart_time.hour, flight1.depart_time.minute)
                flight1adate = (flight1ddate + flight1.duration)
                flight2 = None
                flight2ddate = None
                flight2adate = None
                if round_trip:
                    flight2 = Flight.objects.get(id=flight_2)
                    flight2ddate = datetime(int(date2.split('-')[2]), int(date2.split('-')[1]),
                                            int(date2.split('-')[0]),
                                            flight2.depart_time.hour, flight2.depart_time.minute)
                    flight2adate = (flight2ddate + flight2.duration)
                if round_trip:
                    return render(request, "book.html",{
                        'flight1': flight1,
                        'flight2': flight2,
                        "flight1ddate": flight1ddate,
                        "flight1adate": flight1adate,
                        "flight2ddate": flight2ddate,
                        "flight2adate": flight2adate,
                        "seat": seat,
                        'seats1': Seat.objects.filter(flight=flight1.pk),
                        'seats2': Seat.objects.filter(flight=flight2.pk),
                        "fee": FEE,
                        'tripType': '2',
                        'stop1': 'no',
                        'stop2': 'no',
                    })
                return render(request, "book.html", {
                    'flight1': flight1,
                    "flight1ddate": flight1ddate,
                    "flight1adate": flight1adate,
                    "seat": seat,
                    "fee": FEE,
                    'seats1': Seat.objects.filter(flight=flight1.pk),
                    'tripType': '2',
                    'stop1': 'no',
                })
            if stop2 =='no':
                seat = request.GET.get('seatClass')
                round_trip = False
                if request.GET.get('flight2Id'):
                    round_trip = True
                if round_trip:
                    flight_2 = request.GET.get('flight2Id')
                    date2 = request.GET.get('flight2Date')
                flight2 = None
                flight2ddate = None
                flight2adate = None
                if round_trip:
                    flight2 = Flight.objects.get(id=flight_2)
                    flight2ddate = datetime(int(date2.split('-')[2]), int(date2.split('-')[1]),
                                            int(date2.split('-')[0]),
                                            flight2.depart_time.hour, flight2.depart_time.minute)
                    flight2adate = (flight2ddate + flight2.duration)
                if round_trip:
                    re.update({
                        'flight2': flight2,
                        "flight2ddate": flight2ddate,
                        "flight2adate": flight2adate,
                        "seat": seat,
                        'seats2': Seat.objects.filter(flight=flight2.pk),
                        "fee": FEE,
                        'stop1': 'no',
                        'stop2': 'no',
                    })
            if stop1 == 'no':
                flight_1 = request.GET.get('flight1Id')
                date1 = request.GET.get('flight1Date')
                seat = request.GET.get('seatClass')
                flight1 = Flight.objects.get(id=flight_1)
                flight1ddate = datetime(int(date1.split('-')[2]), int(date1.split('-')[1]), int(date1.split('-')[0]),
                                        flight1.depart_time.hour, flight1.depart_time.minute)
                flight1adate = (flight1ddate + flight1.duration)
                re.update({
                    'flight1': flight1,
                    "flight1ddate": flight1ddate,
                    "flight1adate": flight1adate,
                    "seat": seat,
                    "fee": FEE,
                    'seats1': Seat.objects.filter(flight=flight1.pk),
                    'stop1': 'no',
                })
            return render(request, "book.html", re)
    else:
        return HttpResponseRedirect(reverse("login"))