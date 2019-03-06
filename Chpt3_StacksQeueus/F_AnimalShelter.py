from ./../Chpt2_LinkedLists/LinkedList import LinkedList
import unittest


class Animal():
  def __init__(self, name, order):
    self.name = name
    self.order = order

  def __str__(self):
    return self.name

class Cat(Animal): pass
class Dog(Animal): pass


class AnimalShelter:
	def __init__(self):
		self.dogs = new LinkedList()
		self.cats = new LinkedList()
		self.order = 1

	def enqueue(self, animal):
		animal.order = order
		order += 1
		if animal.__class__ == Dog:
			self.dogs.add(animal)
		else:
			self.cats.add(animal)
		return self

	def dequeueAny(self):
		if self.dogs.head is None:
			return self.dequeueCat()
		if self.cats.head is None:
			return self.dequeueDog()

		if self.dogs.head.value.order < self.cats.head.value.order:
			return self.dequeueDog()
		else:
			return self.dequeueCat()

	def dequeueDog(self):
		return self.__dequeueList(self.dogs)
		
	def dequeueCat(self):
		return self.__dequeueList(self.cats)
		
	def __dequeueList(ll):
		if ll.head is None:
			return None
		else:
			value = ll.head.value
			ll.head = ll.head.next
			return value


class Test(unittest.TestCase):
  def test_animal_shelter(self):
    shelter = AnimalShelter()
    shelter.enqueue(Cat("Hanzack"))
    shelter.enqueue(Dog("Pluto"))
    shelter.enqueue(Cat("Garfield"))
    shelter.enqueue(Cat("Tony"))
    shelter.enqueue(Dog("Clifford"))
    shelter.enqueue(Dog("Blue"))
    self.assertEqual(str(shelter.dequeueAny()), "Hanzack")
    self.assertEqual(str(shelter.dequeueAny()), "Garfield")
    self.assertEqual(str(shelter.dequeueDog()), "Pluto")
    self.assertEqual(str(shelter.dequeueDog()), "Clifford")
    self.assertEqual(str(shelter.dequeueCat()), "Tony")
    self.assertEqual(str(shelter.dequeueCat()), "None")
    self.assertEqual(str(shelter.dequeueAny()), "Blue")
    self.assertEqual(str(shelter.dequeueAny()), "None")

if __name__ == "__main__":
  unittest.main()



