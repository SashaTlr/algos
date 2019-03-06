from LinkedList import *
import unittest


class Animal():
	
  def __init__(self, name):
    self.name = name
    self.order = None

  def setOrder(self, order):
  	self.order = order

  def __str__(self):
    return self.name

class Cat(Animal): pass
class Dog(Animal): pass


class AnimalShelter:
	def __init__(self):
		self.dogs = LinkedList()
		self.cats = LinkedList()
		self.order = 1

	def enqueue(self, animal):
		animal.setOrder(self.order)
		self.order += 1
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
		
	def __dequeueList(self, ll):
		if ll.head is None:
			return None
		else:
			value = ll.head.value
			ll.head = ll.head.next
			return value


class Test(unittest.TestCase):
  def test_animalShelter(self):
    shelter = AnimalShelter()

    cat1 = Cat("One")
    cat2 = Cat("Two")
    cat3 = Cat("Three")

    dog1 = Dog("One")
    dog2 = Dog("Two")
    dog3 = Dog("Three")

    shelter.enqueue(cat1)
    shelter.enqueue(dog1)
    shelter.enqueue(cat2)
    shelter.enqueue(cat3)
    shelter.enqueue(dog2)
    shelter.enqueue(dog3)

    self.assertEqual(shelter.dequeueAny(), cat1)
    self.assertEqual(shelter.dequeueAny(), dog1)
    self.assertEqual(shelter.dequeueDog(), dog2)
    self.assertEqual(shelter.dequeueDog(), dog3)
    self.assertEqual(shelter.dequeueCat(), cat2)
    self.assertEqual(shelter.dequeueCat(), cat3)
    self.assertEqual(shelter.dequeueAny(), None)
    self.assertEqual(shelter.dequeueAny(), None)

if __name__ == "__main__":
  unittest.main()



