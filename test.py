import requests


def get_info():
    url_user = "http://127.0.0.1:5000/users"
    response = requests.get(url_user)
    return response.json()


def send_info():
    userId = str(input("Enter user id: "))
    name = str(input("Enter the name: "))
    city = str(input("Enter the city: "))
    try:
        locations = int(input("Enter the number of locations(0 if you want to leave empty): "))
        if locations == 0:
            locations = "None"
        else:
            aux = []
            for i in range(locations):
                aux.append(str(input("Enter de " + str(i) + " location: ")))
            locations = aux
    except:
        print("Yep you just try to test if can handle exceptions. It does but i'm lazy so now every file in your computer is goint to be deleted.")

    url_send = f"http://127.0.0.1:5000/users?userId={userId}&name={name}&city={city}&locations={locations}"
    response = requests.post(url_send)
    return response.json()


data = send_info()
print(data)