import warnings

warnings.filterwarnings("ignore")
import pandas as pd
import pickle


def pkl_output(filename):
    data = pd.read_csv(filename)
    # data.drop("satisfaction", axis=1, inplace=True)

    data = pd.get_dummies(data=data, columns=['Gender', 'Customer Type', 'Type of Travel', 'Class', 'Seat comfort',
                                              'Departure/Arrival time convenient', 'Food and drink', 'Gate location',
                                              'Inflight wifi service', 'Inflight entertainment', 'Online support',
                                              'Ease of Online booking', 'On-board service', 'Leg room service',
                                              'Baggage handling', 'Checkin service', 'Cleanliness', 'Online boarding'],
                          drop_first=True)

    columns = ['Age', 'Flight Distance', 'Departure Delay in Minutes', 'Arrival Delay in Minutes', 'Gender_Male',
               'Customer Type_disloyal Customer', 'Type of Travel_Personal Travel', 'Class_Eco', 'Class_Eco Plus',
               'Seat comfort_1',
               'Seat comfort_2', 'Seat comfort_3', 'Seat comfort_4', 'Seat comfort_5',
               'Departure/Arrival time convenient_1',
               'Departure/Arrival time convenient_2', 'Departure/Arrival time convenient_3',
               'Departure/Arrival time convenient_4',
               'Departure/Arrival time convenient_5', 'Food and drink_1', 'Food and drink_2', 'Food and drink_3',
               'Food and drink_4',
               'Food and drink_5', 'Gate location_1', 'Gate location_2', 'Gate location_3', 'Gate location_4',
               'Gate location_5',
               'Inflight wifi service_1', 'Inflight wifi service_2', 'Inflight wifi service_3',
               'Inflight wifi service_4',
               'Inflight wifi service_5', 'Inflight entertainment_1', 'Inflight entertainment_2',
               'Inflight entertainment_3',
               'Inflight entertainment_4', 'Inflight entertainment_5', 'Online support_1', 'Online support_2',
               'Online support_3',
               'Online support_4', 'Online support_5', 'Ease of Online booking_1', 'Ease of Online booking_2',
               'Ease of Online booking_3',
               'Ease of Online booking_4', 'Ease of Online booking_5', 'On-board service_1', 'On-board service_2',
               'On-board service_3',
               'On-board service_4', 'On-board service_5', 'Leg room service_1', 'Leg room service_2',
               'Leg room service_3',
               'Leg room service_4', 'Leg room service_5', 'Baggage handling_2', 'Baggage handling_3',
               'Baggage handling_4',
               'Baggage handling_5', 'Checkin service_1', 'Checkin service_2', 'Checkin service_3', 'Checkin service_4',
               'Checkin service_5', 'Cleanliness_1', 'Cleanliness_2', 'Cleanliness_3', 'Cleanliness_4', 'Cleanliness_5',
               'Online boarding_1', 'Online boarding_2', 'Online boarding_3', 'Online boarding_4', 'Online boarding_5']

    for i in columns:
        if i not in list(data):
            data[i] = 0

    with open('airlines/svc.pkl', 'rb') as f:
        model = pickle.load(f)

    return model.predict(data)

