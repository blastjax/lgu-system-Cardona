from datetime import date, datetime
from sqlalchemy.orm import Session
from app.models import *

def is_valid_datetime(date_str):
    try:
        if isinstance(date_str, datetime.datetime):
            return True
        # Check if the value is a string before trying to parse it
        if not isinstance(date_str, str):
            return False
        # Replace space with 'T' to comply with ISO 8601 if necessary
        date_str = date_str.replace(' ', 'T')
        # Attempt to convert the string to a datetime object
        datetime.fromisoformat(date_str)
        return True
    except ValueError:
        return False

def get_or_create(db: Session, model, **kwargs):
    """
    Get or create a database entry for a given model.

    :param db: Database session.
    :param model: The model to query.
    :param kwargs: Keyword arguments to filter the model.
    :return: The database entry.
    """
    print(f"Querying {model.__name__} with {kwargs}")
    db_entry = db.query(model).filter_by(**kwargs).first()
    if not db_entry:
        db_entry = model(**kwargs)
        db.add(db_entry)
        db.commit()
        db.refresh(db_entry)
    return db_entry

def insert_attack_relationship(db: Session, attack_id: int, cell_value: str, model, association_model, col_name: str):
    print(f"Inserting {model.__name__} relationship for {cell_value} into {association_model.__name__}.")
    # Check if the entry already exists
    db_entry = get_or_create(db, model, name=cell_value)

    # Create association if it doesn't exist
    exists = db.query(association_model).filter_by(attack_id=attack_id, **{f"{col_name}_id": db_entry.id}).first()

    if not exists:
        association_entry = association_model(
            attack_id=attack_id,
            **{f"{col_name}_id": db_entry.id}
        )
        db.add(association_entry)
        db.commit()
        db.refresh(association_entry)

def insert_attack_relationship_with_utc(db: Session, attack_id: int, cell_value: str, utc_col_name: str, utc_cell_value: str, model, association_model, col_name: str):
    print(f"Inserting {model.__name__} relationship for {cell_value} into {association_model.__name__}.")
    # Check if the entry already exists
    db_entry = get_or_create(db, model, name=cell_value)

    # Create association if it doesn't exist
    exists = db.query(association_model).filter_by(attack_id=attack_id, **{f"{col_name}_id": db_entry.id}).first()

    invalid_entries = []  # Collect invalid entries

    if not exists:
        if not is_valid_datetime(utc_cell_value) and utc_cell_value is not None:
            invalid_entries.append({utc_col_name: utc_cell_value})  # Log invalid datetime

        association_entry = association_model(
            attack_id=attack_id,
            **{f"{col_name}_id": db_entry.id},
            **{f"{utc_col_name}": utc_cell_value if is_valid_datetime(utc_cell_value) else None}
        )
        db.add(association_entry)
        db.commit()
        db.refresh(association_entry)
    
    return invalid_entries

def update_table(db: Session, table, table_id: int, data: dict):
    row = db.query(table).filter_by(id=table_id).first()

    if row:
        # Update the row with the new data
        for key, value in data.items():
            setattr(row, key, value)

        db.commit()
        db.refresh(row)
    else:
        print(f"{table.__name__} with ID {table_id} not found.")

def create(db: Session, model, data):
    """
    Create a database entry for a given model using Pydantic model data.

    :param db: Database session.
    :param model: The model to query.
    :param data: The Pydantic model data.
    :return: The database entry.
    """
    print(f"Creating {model.__name__} with {data}")
    # Unpack the data (Pydantic model) into keyword arguments
    if model.__name__ == "Attack":
        db_entry = model(**data)
    else:
        db_entry = model(**data.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def update(db: Session, model, model_id: int, data):
    """
    Update a database entry for a given model using Pydantic model data.

    :param db: Database session.
    :param model: The model to query.
    :param model_id: The ID of the model to update.
    :param data: The Pydantic model data.
    :return: The updated database entry.
    """
    print(f"Updating {model.__name__} with ID {model_id} using {data}")

    # Get the model entry to update
    db_entry = db.query(model).filter(model.id == model_id).first()

    if db_entry:
        if model.__name__ == "Attack":
            update_data = {k: v for k, v in data.items() if v is not None}  # Only include fields that are set (not None)
        else:
            # Update the model entry with the new data, ignoring None values
            update_data = data.dict(exclude_unset=True)  # Only include fields that are set (not None)
        # update_data = data.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_entry, key, value)  # Only update provided fields
        db.commit()
        db.refresh(db_entry)
    else:
        print(f"{model.__name__} with ID {model_id} not found.")

    return db_entry

def serialize_value(value):
    """Convert values to a JSON-serializable format."""
    if isinstance(value, (datetime, date)):
        return value.isoformat()  # Convert datetime/date to ISO 8601 string
    return value  # Return as is for other types

def serialize_params(params):
    """Serialize the parameters dictionary."""
    if params is None:
        return None
    return {k: serialize_value(v) for k, v in params.items()}