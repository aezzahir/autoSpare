#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.spear import Spear


# Create a new spear instance
my_spear = Spear()
my_spear.designation = "Spearhead Model A"
my_spear.nsn = "1234-5678-9012"
my_spear.description = "A durable and versatile spearhead designed for combat and hunting purposes."
my_spear.save()
print(my_spear)

print("Creating Another Spear")
# Create another spear instance
another_spear = Spear()
another_spear.designation = "Barbed Lance 3000"
another_spear.nsn = "9876-5432-1098"
another_spear.description = "The Barbed Lance 3000 features an innovative design for enhanced piercing capabilities."
another_spear.save()
print(another_spear)