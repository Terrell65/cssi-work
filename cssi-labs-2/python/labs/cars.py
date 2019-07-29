from google.appengine.ext import ndb

class Car(ndb.Model):
    carMake = ndb.StringProperty(required=True)
    carModel = ndb.StringProperty()

car1 = Car(carMake="ford",carModel='taurus')
car2 = Car(carMake="benz",carModel= 'sclass')
car1.put()
print(car1.carMake)
