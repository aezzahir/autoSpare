#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.supplier import Supplier

print("Creating New Supplier")
# Create a new supplier instance
my_supplier = Supplier()
my_supplier.name = "Excalibur Armaments"
my_supplier.cage_code = "12345"
my_supplier.address = "123 Spear Street, Armoryville"
my_supplier.save()
print(my_supplier)

print("Creating Another Supplier")
# Create another supplier instance
another_supplier = Supplier()
another_supplier.name = "Aegis Weaponry"
another_supplier.cage_code = "54321"
another_supplier.address = "456 Pike Plaza, Arsenal City"
another_supplier.save()
print(another_supplier)