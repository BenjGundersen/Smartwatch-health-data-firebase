# deleting a document within a collection
db.collection("Mar 03 - Mar 09").document("Mar 07").delete()

# getting data from a document within a collection
doc_ref = db.collection("Mar 03 - Mar 09").document("Mar 06")

doc = doc_ref.get()
if doc.exists:
    print(f"Document data: {doc.to_dict()}")
else:
    print("That document does not exist!")

# modifying data from a document withtin a collection
doc_ref = db.collection("Mar 03 - Mar 09").document("Mar 07")
doc_ref.set({"Steps": 2000000, "Calories": 700, "Lower Heart Rate":49, "Upper Heart rate": 137})