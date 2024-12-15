document.addEventListener('DOMContentLoaded', () => {
    flight_duration();
});

function flight_duration() {
    document.querySelectorAll(".duration").forEach(element => {
        let time = element.dataset.value.split(":");
        element.innerText = time[0]+"h "+time[1]+"m";
    });
}


function add_traveller() {
    let div = document.querySelector('.add-traveller-div');
    let fname = div.querySelector('#fname');
    let lname = div.querySelector('#lname');
    let gender = div.querySelectorAll('.gender');
    let gender_val = null
    if(fname.value.trim().length === 0) {
        alert("Please enter First Name.");
        return false;
    }

    if(lname.value.trim().length === 0) {
        alert("Please enter Last Name.");
        return false;
    }

    if (!gender[0].checked) {
        if (!gender[1].checked) {
            alert("Please select gender.");
            return false;
        }
        else {
            gender_val = gender[1].value;
        }
    }
    else {
        gender_val = gender[0].value;
    }

    let passengerCount = div.parentElement.querySelectorAll(".each-traveller-div .each-traveller").length;

    let traveller = `<div class="row each-traveller">
                        <div>
                            <span class="traveller-name">${fname.value} ${lname.value}</span><span>,</span>
                            <span class="traveller-gender">${gender_val.toUpperCase()}</span>
                        </div>
                        <input type="hidden" name="passenger${passengerCount+1}FName" value="${fname.value}">
                        <input type="hidden" name="passenger${passengerCount+1}LName" value="${lname.value}">
                        <input type="hidden" name="passenger${passengerCount+1}Gender" value="${gender_val}">
                        <div class="delete-traveller">
                            <button class="btn" type="button" onclick="del_traveller(this)">
                                <svg width="1.1em" height="1.1em" viewBox="0 0 16 16" class="bi bi-x-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                                    <path fill-rule="evenodd" d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>
                                </svg>
                            </button>
                        </div>
                    </div>`;
    div.parentElement.querySelector(".each-traveller-div").innerHTML += traveller;
    div.parentElement.querySelector("#p-count").value = passengerCount+1;
    div.parentElement.querySelector(".traveller-head h6 span").innerText = passengerCount+1;
    div.parentElement.querySelector(".no-traveller").style.display = 'none';
    fname.value = "";
    lname.value = "";
    gender.forEach(radio => {
        radio.checked = false;
    });

    let pcount = document.querySelector("#p-count").value;
    let fare = document.querySelector("#basefare").value;
    let fee = document.querySelector("#fee").value;
    if (parseInt(pcount)!==0) {
        document.querySelector(".base-fare-value span").innerText = parseInt(fare)*parseInt(pcount);
        document.querySelector(".total-fare-value span").innerText = (parseInt(fare)*parseInt(pcount))+parseInt(fee);
    }

}

function del_traveller(btn) {
    let traveller = btn.parentElement.parentElement;
    let tvl = btn.parentElement.parentElement.parentElement.parentElement;
    let cnt = tvl.querySelector("#p-count");
    cnt.value = parseInt(cnt.value)-1;
    tvl.querySelector(".traveller-head h6 span").innerText = cnt.value;
    if(parseInt(cnt.value) <= 0) {
        tvl.querySelector('.no-traveller').style.display = 'block';
    }
    traveller.remove();
    
    let pcount = document.querySelector("#p-count").value;
    let fare = document.querySelector("#basefare").value;
    let fee = document.querySelector("#fee").value;
    if (parseInt(pcount) !== 0) {
        document.querySelector(".base-fare-value span").innerText = parseInt(fare)*parseInt(pcount);
        document.querySelector(".total-fare-value span").innerText = (parseInt(fare)*parseInt(pcount))+parseInt(fee);   
    }
}

{% extends 'layout.html' %}

{% load static %}

{% block head %}
    <title>Book | Flight</title>
    <link rel="stylesheet" href="{% static 'css/book_style.css' %}">
    <script type="text/javascript" src="{% static 'js/book.js' %}"></script>
{% endblock %}

{% block body %}
    <section class="section section1">
        <form action="{% url 'book' %}" onsubmit="return book_submit()" method="POST">
            {% csrf_token %}
            <input type="hidden" name="flight1" value="{{flight1.id}}">
            <input type="hidden" name="flight1Date" value='{{flight1ddate | date:"d-m-Y"}}'>
            <input type="hidden" name="flight1Class" value="{{seat}}">
            {% if flight2 %}
                <input type="hidden" name="flight2" value="{{flight2.id}}">
                <input type="hidden" name="flight2Class" value="{{seat}}">
                <input type="hidden" name="flight2Date" value='{{flight2ddate | date:"d-m-Y"}}'>
            {% endif %}
            <div class="row main-row">
                <div class="col-8">
                <div class="ticket-details">
                    <h5>Ticket Details</h5>
                    <hr>
                    <div class="media-airline">
                        <div>
                            <div class="brand">{{flight1.airline}}</div>
                            <div>&nbsp;&middot;&nbsp;</div>
                            <div class="plane-name">{{flight1.plane}}</div>
                            <div>&nbsp;&middot;&nbsp;</div>
                            <div class="plane-name">{{seat}}</div>
                        </div>
                    </div>
                    <div class="row ticket-details-div">
                        <div class="col-3 airline-name">
                            <div class="brand">{{flight1.airline}}</div>
                            <div class="plane-name">{{flight1.plane}}</div>
                        </div>
                        <div class="col-3 depart-time">
                            <div class="time">{{flight1.depart_time | time:'H:i'}}</div>
                            <div class="date ddate" data-value='{{flight1ddate | date:"d-m-Y"}}'>{{flight1ddate | date:"D, d M y"}}</div>
                            <div class="place">{{flight1.origin.city}}</div>
                            <div class="airport">{{flight1.origin.airport}}</div>
                        </div>
                        <div class="col-3 time-details">
                            <div class="duration" data-value="{{flight1.duration}}"></div>
                        </div>
                        <div class="col-3 arrival-time">
                            <div class="time">{{flight1.arrival_time | time:'H:i'}}</div>
                            <div class="date adate" data-value='{{flight1adate | date:"d-m-Y"}}'>{{flight1adate | date:"D, d M y"}}</div>
                            <div class="place">{{flight1.destination.city}}</div>
                            <div class="airport">{{flight1.destination.airport}}</div>
                        </div>
                    </div>
                    {% if flight2 %}
                        <!--Round Trip-->
                        <div style="padding: 0 15px;" class="round-seperator"><hr style="border-top: 0.5px dashed rgba(0,0,0,.1);"></div>
                        <!--/Round Trip-->
                        <div class="media-airline">
                            <div>
                                <div class="brand">{{flight2.airline}}</div>
                                <div>&nbsp;&middot;&nbsp;</div>
                                <div class="plane-name">{{flight2.plane}}</div>
                                <div>&nbsp;&middot;&nbsp;</div>
                                <div class="plane-name">{{seat}}</div>
                            </div>
                        </div>
                        <div class="row ticket-details-div">
                            <div class="col-3 airline-name">
                                <div class="brand">{{flight2.airline}}</div>
                                <div class="plane-name">{{flight2.plane}}</div>
                            </div>
                            <div class="col-3 depart-time">
                                <div class="time">{{flight2.depart_time | time:'H:i'}}</div>
                                <div class="date ddate">{{flight2ddate | date:"D, d M y"}}</div>
                                <div class="place">{{flight2.origin.city}}</div>
                                <div class="airport">{{flight2.origin.airport}}</div>
                            </div>
                            <div class="col-3 time-details">
                                <div class="duration" data-value="{{flight2.duration}}"></div>
                            </div>
                            <div class="col-3 arrival-time">
                                <div class="time">{{flight2.arrival_time | time:'H:i'}}</div>
                                <div class="date adate">{{flight2adate | date:"D, d M y"}}</div>
                                <div class="place">{{flight2.destination.city}}</div>
                                <div class="airport">{{flight2.destination.airport}}</div>
                            </div>
                        </div>
                    {% endif %}
                    <hr>
                    <div class="baggage-details">

                        <svg width="1em" height="1.5em" viewBox="0 3 16 16" class="bi bi-bag" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" d="M8 1a2.5 2.5 0 0 0-2.5 2.5V4h5v-.5A2.5 2.5 0 0 0 8 1zm3.5 3v-.5a3.5 3.5 0 1 0-7 0V4H1v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V4h-3.5zM2 5v9a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V5H2z"/>
                        </svg> 

                        30 Kgs Check-in, 7 Kgs Cabin
                    </div>
                </div>
                <div class="traveller-details">
                    <div class="traveller-head">
                        <h5>Contact Information</h5>
                    </div>
                    <hr>
                    
                    <div class="row contact-details-div">
                        <div class="row form-group">
                            <!--<div class="input-group col">
                                <div class="input-group-prepend">
                                    
                                </div>
                            </div>-->
                            <div class="col-3 ci">
                                Country Code