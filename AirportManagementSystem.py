from datetime import date


def check_baggage(baggage_weight):
    if baggage_weight in range(1, 27):
        return True
    else:
        return False


# 2.
def check_immigration(expiry_year):
    dt = date.today()
    if expiry_year >= dt.year:
        return True
    else:
        return False


# 3.
def check_security(noc_status):
    if noc_status == "VALID" or noc_status == "valid":
        return True
    else:
        return False


# 4.
def traveler():
    traveler.traveler_id = int(input("Enter your ID"))
    traveler.traveler_name = str(input("Enter your Name"))
    traveler.baggage_weight = int(input("Enter your Baggage Weight"))
    traveler.expiry_year = int(input("Enter your Expiry Year"))
    traveler.noc_status = str(input("Enter your NOC_Status"))
    return


traveler()

if check_baggage(traveler.baggage_weight) and check_immigration(traveler.expiry_year) and check_security(
        traveler.noc_status):
    print(str(traveler.traveler_id) + " " + traveler.traveler_name)
    print("Allow Traveler to Fly!")
else:
    print(str(traveler.traveler_id) + " " + traveler.traveler_name)
    print("Detain Traveller for Re-Checking!")



