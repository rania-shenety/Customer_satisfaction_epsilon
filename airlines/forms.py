from django import forms

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

Customer_Type = (
    ("Loyal Customer", "Loyal Customer"),
    ("disloyal Customer", "disloyal Customer")
)

class_type = (
    ("Business", "Business"),
    ("Eco", "Eco"),
    ("Eco Plus", "Eco Plus"),
)

Type_of_Travel = (
    ("Business travel", "Business travel"),
    ("Personal Travel", "Personal Travel")
)

rating = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)


class MyForm(forms.Form):
    gender = forms.ChoiceField(label="Gender", choices=GENDER_CHOICES)
    Customer_Type = forms.ChoiceField(label="Customer Type", choices=Customer_Type)
    age = forms.IntegerField(label="Age")
    Type_of_Travel = forms.ChoiceField(label="Type of Travel", choices=Type_of_Travel)
    class_type = forms.ChoiceField(label="Class", choices=class_type)
    Flight_Distance = forms.IntegerField(label="Flight Distance")
    Seat_Comfort = forms.ChoiceField(choices=rating)
    Departure_Arrival_time_convenient = forms.ChoiceField(choices=rating)
    Food_and_drink = forms.ChoiceField(choices=rating)
    Gate_location = forms.ChoiceField(choices=rating)
    Inflight_wifi_service = forms.ChoiceField(choices=rating)
    Inflight_entertainment = forms.ChoiceField(choices=rating)
    Online_support = forms.ChoiceField(choices=rating)
    Ease_of_Online_booking = forms.ChoiceField(choices=rating)
    Onboard_service = forms.ChoiceField(choices=rating)
    Leg_room_service = forms.ChoiceField(choices=rating)
    Baggage_handling = forms.ChoiceField(choices=rating)
    Checkin_service = forms.ChoiceField(choices=rating)
    Cleanliness = forms.ChoiceField(choices=rating)
    Online_boarding = forms.ChoiceField(choices=rating)
    Departure_Delay_in_Minutes = forms.IntegerField()
    Arrival_Delay_in_Minutes = forms.IntegerField()
