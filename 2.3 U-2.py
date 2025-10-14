Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Animal: 
... def make_sound(self): 
... raise NotImplementedError("Subclass must implement abstract method 'make_sound'") 
... class Dog(Animal): 
... def make_sound(self): 
... return "Woof! Woof!" 
... class Cat(Animal):def make_sound(self): 
... return "Meow!" 
... class Bird(Animal): 
... def make_sound(self): 
... return "Chirp! Chirp!" 
... # Demonstrating polymorphism 
... print("\n--- Polymorphism Demonstration ---") 
... animals = [Dog(), Cat(), Bird()] 
... for animal in animals: 
