from django.db import models


class Gender(models.Model):
    gender = models.CharField(max_length=10, default="Male")


class Adress(models.Model):
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)


class Client(models.Model):
    name = models.CharField(max_length=255)
    adress = models.ForeignKey("Adress", on_delete=models.PROTECT)
    company = models.BooleanField(default=True)


class IndividualClientDetails(models.Model):
    client_id = models.ForeignKey("Client", on_delete=models.PROTECT)
    pesel = models.CharField(max_length=11)
    last_name = models.CharField(max_length=255)
    Gender = models.ForeignKey("Gender", on_delete=models.PROTECT)


class CompanyClientDetails(models.Model):
    client_id = models.ForeignKey("Client", on_delete=models.PROTECT)
    nip = models.CharField(max_length=10)


class Position(models.Model):
    position = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=15, decimal_places=3)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.ForeignKey("Gender", on_delete=models.PROTECT)
    position = models.ForeignKey("Position", on_delete=models.PROTECT)


class GearboxType(models.Model):
    gearbox_type = models.CharField(max_length=50)


class FuelType(models.Model):
    fuel_type = models.CharField(max_length=50)


class CarCategory(models.Model):
    car_category = models.CharField(max_length=50)


class Car(models.Model):
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year_of_production = models.IntegerField()
    engine_displacement = models.IntegerField()
    gearbox_type = models.ForeignKey("GearboxType", on_delete=models.PROTECT)
    power = models.IntegerField()
    fuel_type = models.ForeignKey("FuelType", on_delete=models.PROTECT)
    vin = models.CharField(max_length=17)
    car_category = models.ForeignKey("CarCategory", on_delete=models.PROTECT)
    mileage_in_km = models.IntegerField()
    intackt = models.BooleanField(default=False)


class House(models.Model):
    address = models.ForeignKey("Adress", on_delete=models.PROTECT)
    area = models.DecimalField(max_digits=15, decimal_places=3)


class InsurancePolicy(models.Model):
    client_id = models.ForeignKey("Client", on_delete=models.PROTECT)
    employee_id = models.ForeignKey("Employee", on_delete=models.PROTECT)
    car_id = models.ForeignKey("Car", on_delete=models.PROTECT)
    house_id = models.ForeignKey("House", on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=15, decimal_places=3)
