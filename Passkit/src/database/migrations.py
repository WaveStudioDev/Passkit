# database/migrations.py

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import IntegrityError

# Define the base class for declarative models
Base = declarative_base()

# Define your models here or import them
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

class PasswordEntry(Base):
    __tablename__ = 'password_entries'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    website = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

def create_database(engine):
    """Create all tables in the database."""
    Base.metadata.create_all(engine)
    print("Database created and tables created.")

def drop_database(engine):
    """Drop all tables in the database."""
    Base.metadata.drop_all(engine)
    print("All tables dropped.")

def migrate(engine):
    """Run migrations to ensure the database is up to date."""
    # Here you can check for existing tables and apply changes as needed
    # This is a simplified example; in real applications, you might want to check for specific changes
    try:
        Base.metadata.create_all(engine)
        print("Migration completed successfully.")
    except IntegrityError as e:
        print(f"Migration error: {e}")

def main():
    """Main function to run migrations."""
    database_url = 'sqlite:///your_database.db'  # Change this to your database URL
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Uncomment the function you want to run
    # create_database(engine)
    # drop_database(engine)
    migrate(engine)

    session.close()

if __name__ == "__main__":
    main()