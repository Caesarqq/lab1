# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remov` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aircrafts(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50,
                            db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    makemodel = models.CharField(db_column='MakeModel', max_length=10, db_collation='utf8mb4_0900_ai_ci', blank=True,
                                 null=True)  # Field name made lowercase.
    totalseats = models.IntegerField(db_column='TotalSeats')  # Field name made lowercase.
    economyseats = models.IntegerField(db_column='EconomySeats')  # Field name made lowercase.
    businessseats = models.IntegerField(db_column='BusinessSeats')  # Field name made lowercase.

    class Meta:
        db_table = 'aircrafts'


class Airports(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    countryid = models.ForeignKey('Countries', models.DO_NOTHING, db_column='CountryID')  # Field name made lowercase.
    iatacode = models.CharField(db_column='IATACode', max_length=3)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='utf8mb4_0900_ai_ci', blank=True,
                            null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'airports'


class Amenities(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    service = models.CharField(db_column='Service', max_length=50,
                               db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        db_table = 'amenities'


class Amenitiescabintype(models.Model):
    cabintypeid = models.OneToOneField('Cabintypes', models.DO_NOTHING, db_column='CabinTypeID',
                                       primary_key=True)  # Field name made lowercase. The composite primary key (CabinTypeID, AmenityID) found, that is not supported. The first column is selected.
    amenityid = models.ForeignKey(Amenities, models.DO_NOTHING, db_column='AmenityID')  # Field name made lowercase.

    class Meta:
        db_table = 'amenitiescabintype'
        unique_together = (('cabintypeid', 'amenityid'),)


class Amenitiestickets(models.Model):
    amenityid = models.OneToOneField(Amenities, models.DO_NOTHING, db_column='AmenityID',
                                     primary_key=True)  # Field name made lowercase. The composite primary key (AmenityID, TicketID) found, that is not supported. The first column is selected.
    ticketid = models.ForeignKey('Tickets', models.DO_NOTHING, db_column='TicketID')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        db_table = 'amenitiestickets'
        unique_together = (('amenityid', 'ticketid'),)


class Cabintypes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50,
                            db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.

    class Meta:
        db_table = 'cabintypes'


class Countries(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50,
                            db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.

    class Meta:
        db_table = 'countries'


class Offices(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    countryid = models.ForeignKey(Countries, models.DO_NOTHING, db_column='CountryID')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50,
                             db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50,
                             db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=250,
                               db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.

    class Meta:
        db_table = 'offices'


class Reviews(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    from_field = models.CharField(db_column='From',
                                  max_length=255)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    to = models.CharField(db_column='To', max_length=255)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender')  # Field name made lowercase.
    cabintypeid = models.IntegerField(db_column='CabinTypeId')  # Field name made lowercase.
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        db_table = 'reviews'


class Roles(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50,
                             db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.

    class Meta:
        db_table = 'roles'


class Routes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    departureairportid = models.ForeignKey(Airports, models.DO_NOTHING,
                                           db_column='DepartureAirportID')  # Field name made lowercase.
    arrivalairportid = models.ForeignKey(Airports, models.DO_NOTHING, db_column='ArrivalAirportID',
                                         related_name='routes_arrivalairportid_set')  # Field name made lowercase.
    distance = models.IntegerField(db_column='Distance')  # Field name made lowercase.
    flighttime = models.IntegerField(db_column='FlightTime')  # Field name made lowercase.

    class Meta:
        db_table = 'routes'


class Schedules(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.TimeField(db_column='Time')  # Field name made lowercase.
    aircraftid = models.ForeignKey(Aircrafts, models.DO_NOTHING, db_column='AircraftID')  # Field name made lowercase.
    routeid = models.ForeignKey(Routes, models.DO_NOTHING, db_column='RouteID')  # Field name made lowercase.
    economyprice = models.DecimalField(db_column='EconomyPrice', max_digits=19,
                                       decimal_places=4)  # Field name made lowercase.
    confirmed = models.IntegerField(db_column='Confirmed')  # Field name made lowercase.
    flightnumber = models.CharField(db_column='FlightNumber', max_length=10, db_collation='utf8mb4_0900_ai_ci',
                                    blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'schedules'


class Tickets(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    scheduleid = models.ForeignKey(Schedules, models.DO_NOTHING, db_column='ScheduleID')  # Field name made lowercase.
    cabintypeid = models.ForeignKey(Cabintypes, models.DO_NOTHING,
                                    db_column='CabinTypeID')  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=50,
                                 db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=50,
                                db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=14,
                             db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    passportnumber = models.CharField(db_column='PassportNumber', max_length=9,
                                      db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    passportcountryid = models.IntegerField(db_column='PassportCountryID')  # Field name made lowercase.
    bookingreference = models.CharField(db_column='BookingReference', max_length=6,
                                        db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    confirmed = models.IntegerField(db_column='Confirmed')  # Field name made lowercase.

    class Meta:
        db_table = 'tickets'


class Users(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    roleid = models.ForeignKey(Roles, models.DO_NOTHING, db_column='RoleID')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=150,
                             db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50,
                                db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, db_collation='utf8mb4_0900_ai_ci', blank=True,
                                 null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50,
                                db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    officeid = models.ForeignKey(Offices, models.DO_NOTHING, db_column='OfficeID', blank=True,
                                 null=True)  # Field name made lowercase.
    birthdate = models.DateField(db_column='Birthdate', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    incorrectlogintries = models.IntegerField(db_column='IncorrectLoginTries', blank=True,
                                              null=True)  # Field name made lowercase.
    nextlogintime = models.DateTimeField(db_column='NextLoginTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'users'

# class UserLogins(models.Model):
#     id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
#     userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
#     logintime = models.DateTimeField(db_column='LoginTime')  # Field name made lowercase.
#     logouttime = models.DateTimeField(db_column='LogoutTime', blank=True, null=True)  # Field name made lowercase.
#     errorreason = models.CharField(db_column='ErrorReason', max_length=255, blank=True, null=True)  # Field name made lowercase.
# 
#     class Meta:
#      
#         db_table = 'user_logins'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
# 
#     class Meta:
#      
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
# 
#     class Meta:
#      
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
# 
# 
# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
# 
#     class Meta:
#      
#         db_table = 'django_migrations'
# 
# 
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
# 
#     class Meta:
#      
#         db_table = 'django_session'


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)
# 
#     class Meta:
#      
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
# 
#     class Meta:
#      
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
# 
#     class Meta:
#      
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
# 
#     class Meta:
#      
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
# 
#     class Meta:
#      
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
# 
#     class Meta:
#      
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
