import pickle
import shelve
variety1 = ["sweet", "hot", "dill"]
variety2 = ["whole", "spear","chip"]
variety3 = ["Claussen","Heinz","Ulassic"]
pickle_file = open("pickles1.dat", "wb")
pickle.dump(variety1, pickle_file)
pickle.dump(variety2, pickle_file)
pickle.dump(variety3, pickle_file)
pickle_file = open("pickles1.dat", "rb")
variety1 = pickle.load(pickle_file)
variety2 = pickle.load(pickle_file)
variety3 = pickle.load(pickle_file)
print("Pickling lists.\n")

print("Unpickling lists.")

print(variety1)
print(variety2)
print(variety3)

print("\nShelving lists.\n")

print("Retrieving the lists from a shelved file:")
pickles = shelve.open("pickles2.dat")
pickles["variety"] = ["sweet", "hot", "dill"]
pickles["shape"] = ["whole", "spear","chip"]
pickles["brand"] = ["Claussen","Heinz","Ulassic"]
pickles.sync()

keys = ["variety", "shape", "brand"]

for key in keys:
    print(key, "-", pickles[key])

print("\nPress the enter key to exit.")
