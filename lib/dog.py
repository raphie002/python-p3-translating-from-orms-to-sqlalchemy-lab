# lib/dog.py
from models import Dog

def create_table(base, engine):
    '''
    Takes a declarative_base (Base) and an engine 
    and creates the database table(s).
    '''
    base.metadata.create_all(engine)

def save(session, dog):
    '''
    Takes a SQLAlchemy session and a Dog instance and saves the dog to the database.
    '''
    session.add(dog)
    session.commit()

def get_all(session):
    '''
    Takes a session and returns a list of all Dog instances from the database.
    '''
    return session.query(Dog).all()

def find_by_name(session, name):
    '''
    Takes a session and a name, and returns the first Dog instance 
    corresponding to that name.
    '''
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, dog_id):
    '''
    Takes a session and an id, and returns the Dog instance 
    corresponding to that id.
    '''
    # We use 'dog_id' here as 'id' is a reserved keyword in Python
    return session.query(Dog).get(dog_id)

def find_by_name_and_breed(session, name, breed):
    '''
    Takes a session, a name, and a breed, and returns the Dog instance 
    matching both.
    '''
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    '''
    Takes a session, a Dog instance, and a new breed, and updates 
    the instance's breed in the database.
    '''
    dog.breed = breed
    session.commit()