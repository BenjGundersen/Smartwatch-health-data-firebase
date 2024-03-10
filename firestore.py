import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('health-data-from-watch-af6ca002382c.json')

app = firebase_admin.initialize_app(cred)
db = firestore.client()

password = "123SuperSecure"
password_check = input("Enter your password: ")
if(password_check == password):

    doc_ref = db.collection("Feb 25 - Mar 02").document("Feb 26")
    doc_ref.set({"Steps": 9804, "Calories": 443.4, "Lower Heart Rate": 52, "Upper Heart rate": 114})

    doc_ref = db.collection("Feb 25 - Mar 02").document("Feb 27")
    doc_ref.set({"Steps": 12041, "Calories": 544.6, "Lower Heart Rate": 51, "Upper Heart rate": 119})

    doc_ref = db.collection("Feb 25 - Mar 02").document("Feb 28")
    doc_ref.set({"Steps": 12581, "Calories": 569.1, "Lower Heart Rate": 50, "Upper Heart rate": 112})

    doc_ref = db.collection("Feb 25 - Mar 02").document("Feb 29")
    doc_ref.set({"Steps": 11571, "Calories": 523.4, "Lower Heart Rate": 52, "Upper Heart rate": 121})

    doc_ref = db.collection("Feb 25 - Mar 02").document("Mar 01")
    doc_ref.set({"Steps": 11487, "Calories": 519.6, "Lower Heart Rate": 53, "Upper Heart rate": 125})

    doc_ref = db.collection("Feb 25 - Mar 02").document("Mar 02")
    doc_ref.set({"Steps": 1055, "Calories": 47.7, "Lower Heart Rate": 47, "Upper Heart rate": 114})

    doc_ref = db.collection("Mar 03 - Mar 09").document("Mar 03")
    doc_ref.set({"Steps": 1562, "Calories": 70.6, "Lower Heart Rate": 57, "Upper Heart rate": 110})

    doc_ref = db.collection("Mar 03 - Mar 09").document("Mar 04")
    doc_ref.set({"Steps": 18212, "Calories": 823.8, "Lower Heart Rate": 42, "Upper Heart rate": 143})

    doc_ref = db.collection("Mar 03 - Mar 09").document("Mar 05")
    doc_ref.set({"Steps": 12531, "Calories": 566.8, "Lower Heart Rate": 51, "Upper Heart rate": 128})

    doc_ref = db.collection("Mar 03 - Mar 09").document("Mar 06")
    doc_ref.set({"Steps": 15086, "Calories": 682.4, "Lower Heart Rate": 49, "Upper Heart rate": 121})

    doc_ref = db.collection("Mar 03 - Mar 09").document("Mar 07")
    doc_ref.set({"Steps": 20000000, "Calories": 659.2, "Lower Heart Rate": 49, "Upper Heart rate": 137})


    print("That password is correct. Changes have been made to the database.")
else:
    print("That is the incorrect password. No changes have been made to the databse.")





