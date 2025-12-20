from sqlalchemy import  Column , Integer , String , Boolean, Text , ForeignKey  , Date , text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base
from datetime  import date , datetime 
from sqlalchemy import CheckConstraint

class TripRequest(Base):
    __tablename__ = "trip_requests"

    id = Column(Integer, primary_key=True, index=True)

    # Basic Traveler Info
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False , unique=True)
    phone = Column(String(20))

    adults = Column(Integer, default=1)
    children = Column(Integer, default=0)

    # Travel Details
    destination = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    trip_type = Column(String(30))

    # Budget & Stay Preferences
    per_person_budget = Column(Integer)
    total_budget = Column(Integer)
    stay_category = Column(String(20))
    stay_type = Column(String(20))
    room_type = Column(String(30))
    meal_plan = Column(String(50))
    transport_mode = Column(String(30))

    # Activities & Experience
    activities = Column(Text)
    custom_activities = Column(Text)

    # Special Requests
    special_requirements = Column(Text)
    custom_addons = Column(Text)
    other_info = Column(Text)

    # Pickup & Drop
    pickup_location = Column(Text)
    drop_location = Column(Text)

    # Agreement
    agreed_terms = Column(Boolean, default=False)

    # Timestamp
    submitted_at = Column(TIMESTAMP(timezone=True) , nullable= False ,server_default = text('now()') ) 

class ODT(Base):
    __tablename__ = "odt_bookings"

    id = Column(Integer , primary_key= True , index=  True )
    full_name = Column(String(100), nullable=False )
    email_address = Column(String(100), nullable=False )
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    contact_number = Column(String(20), nullable=False)
    whatsapp_number = Column(String(20), nullable=False)
    college_name = Column(String(200), nullable=False)
    pick_up_loc = Column(String(50), nullable=False)
    drop_loc = Column(String(50), nullable=False)
    meal_preference = Column(String(30), nullable=False)
    trip_exp_level = Column(String(40))
    medical_details = Column(String(100))
    payment_screenshot = Column(String(255), nullable=False)
    agree = Column(Boolean, default=False)
    submitted_at = Column(TIMESTAMP(timezone=True) , nullable= False ,server_default = text('now()') ) 

    __table_args__ = (
        CheckConstraint("full_name <> '' AND TRIM(full_name) <> ''", name="full_name_not_blank"),
        CheckConstraint("email_address <> '' AND TRIM(email_address) <> ''", name="email_not_blank"),
        CheckConstraint("gender <> '' AND TRIM(gender) <> ''", name="gender_not_blank"),
        CheckConstraint("college_name <> '' AND TRIM(college_name) <> ''", name="college_not_blank"),
    )

class Manali(Base):
    __tablename__ ="manali"

    id = Column(Integer , primary_key = True , index = True )
    full_name = Column(String(100) , nullable = False)
    gender = Column(String(20) , nullable = False)
    age = Column(Integer , nullable = False)
    email_address = Column(String(100) , nullable =  False)
    contact_number = Column(String(20), nullable=False)
    whatsapp_number = Column(String(20), nullable=False)
    emergency_contact_number = Column(String(20), nullable=False)
    college_name = Column(String(200), nullable=False)
    proof_id_type = Column(String(200) , nullable = False) 
    chosen_id_number = Column(String(50) , nullable = False) 
    id_image = Column(String(255) , nullable = False) 
    medical_details = Column(String(200))
    special_request = Column(String(300))
    agree = Column(Boolean, default=False)
    submitted_at = Column(TIMESTAMP(timezone=True) , nullable= False ,server_default = text('now()') ) 

class Tamia(Base):
    __tablename__="tamia"

    id = Column(Integer , primary_key = True , index = True )
    full_name = Column(String(100) , nullable = False)
    gender = Column(String(20) , nullable = False)
    age = Column(Integer , nullable = False)
    email_address = Column(String(100) , nullable =  False)
    contact_number = Column(String(20), nullable=False)
    whatsapp_number = Column(String(20), nullable=False)
    emergency_contact_number = Column(String(20), nullable=False)
    college_name = Column(String(200), nullable=False)
    proof_id_type = Column(String(200) , nullable = False) 
    mode_of_transport = Column(String(50) , nullable = False)
    chosen_id_number = Column(String(50) , nullable = False) 
    id_image = Column(String(255) , nullable = False) 
    medical_details = Column(String(200))
    special_request = Column(String(300))
    agree = Column(Boolean, default=False)
    submitted_at = Column(TIMESTAMP(timezone=True) , nullable= False ,server_default = text('now()') ) 


class Rishikesh_Haridwar(Base):
    __tablename__="rishikesh_haridwar"

    id = Column(Integer , primary_key = True , index = True )
    full_name = Column(String(100) , nullable = False)
    gender = Column(String(20) , nullable = False)
    age = Column(Integer , nullable = False)
    email_address = Column(String(100) , nullable =  False)
    contact_number = Column(String(20), nullable=False)
    whatsapp_number = Column(String(20), nullable=False)
    emergency_contact_number = Column(String(20), nullable=False)
    college_name = Column(String(200), nullable=False)
    proof_id_type = Column(String(200) , nullable = False) 
    mode_of_transport = Column(String(50) , nullable = False)
    chosen_id_number = Column(String(50) , nullable = False) 
    id_image = Column(String(255) , nullable = False) 
    medical_details = Column(String(200))
    special_request = Column(String(300))
    agree = Column(Boolean, default=False)
    submitted_at = Column(TIMESTAMP(timezone=True) , nullable= False ,server_default = text('now()') ) 

class Saarthi_Form(Base):
    __tablename__="saarthi_form"
    id = Column(Integer , primary_key = True , index = True )
    full_name = Column(String(50) , nullable = False)
    date_of_birthday = Column(Date , nullable = False)
    gender = Column(String(20) , nullable = False)
    aadhar_number = Column(String(50) , nullable = False)
    aadhar_card_image = Column(String(255) , nullable = False)
    profile_image = Column(String(255) , nullable = False)
    email_address = Column(String(100) , nullable =  False)
    contact_number = Column(String(20), nullable=False)
    whatsapp_number = Column(String(20), nullable=False)
    current_city = Column(String(30) , nullable = False) 
    state = Column(String(30) , nullable = False)
    address = Column(String(100) , nullable = False)
    occupation = Column(String(50) , nullable = False)
    organization_name = Column(String(70) , nullable = False)
    job_role = Column(String(50) , nullable = False)
    work_exp = Column(String(30) , nullable = False)
    company_id = Column(String(255))
    profile_url = Column(String(300) , nullable = False)
    role = Column(String(100) , nullable = False) 
    motive = Column(String(300) , nullable = False)
