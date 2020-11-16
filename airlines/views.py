from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MyForm
from django.shortcuts import redirect
import pandas as pd
from .pkl_reader import pkl_output
from django.contrib import messages


def index(request):
    form = MyForm()

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            customer = form

            data = {
                "Gender": customer['gender'].value(),
                'Customer Type': customer['Customer_Type'].value(),
                'Type of Travel': customer['Type_of_Travel'].value(),
                'Class': customer['class_type'].value(),
                'Seat comfort': customer['Seat_Comfort'].value(),
                'Departure/Arrival time convenient': customer['Departure_Arrival_time_convenient'].value(),
                'Food and drink': customer['Food_and_drink'].value(),
                'Gate location': customer['Gate_location'].value(),
                'Inflight wifi service': customer['Inflight_wifi_service'].value(),
                'Inflight entertainment': customer['Inflight_entertainment'].value(),
                'Online support': customer['Online_support'].value(),
                'Ease of Online booking': customer['Ease_of_Online_booking'].value(),
                'On-board service': customer['Onboard_service'].value(),
                'Leg room service': customer['Leg_room_service'].value(),
                'Baggage handling': customer['Baggage_handling'].value(),
                'Checkin service': customer['Checkin_service'].value(),
                'Cleanliness': customer['Cleanliness'].value(),
                'Online boarding': customer['Online_boarding'].value()
            }

            df = pd.DataFrame([data])
            df.to_csv("airlines/data.csv", index=False)

            res = str(pkl_output("airlines/data.csv")[0])
            messages.add_message(request, messages.INFO, res)
            return HttpResponse(res)


    context = {'form': form, "messages": messages}
    return render(request, 'airlines/main.html', context)

# def model_results(request):
#     form = MyForm(request.POST)
#     print(form['gender'].value())
#     return redirect("index")
