# app/utils/response_helper.py
from fastapi import HTTPException
from sqlalchemy import CheckConstraint, ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint
from starlette.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError

from app.utils.helpers import serialize_params

def success_response(data=None, message="Success", status_code=200):
    return JSONResponse(status_code=status_code, content={
        "success": True,
        "message": message,
        "data": data
    })

def error_response(message="Error", error=None, status_code=500):
    if status_code == 500:
        message = "An unexpected error occurred"
        error = str(error)
    elif status_code == 404:
        message = "Resource not found"
        error = str(error)
        
    return JSONResponse(status_code=status_code, content={
        "success": False,
        "message": message,
        "error": error
    })

def handle_error(e, model=None):
    if isinstance(e, IntegrityError):
        error_message = e.orig.diag.message_primary
        constraint_name = None
        
        sqltext = None

        if 'check constraint' in error_message:
            # Extract the name of the check constraint
            constraint_name = error_message.split('check constraint "')[1].split('"')[0]  # Extract the constraint name from the error message
            for constraint in model.__table__.constraints:
                if constraint.name == constraint_name:
                    if isinstance(constraint, CheckConstraint):
                        sqltext = str(constraint.sqltext)
                        break

        error = {
            "detail": error_message
        }

        if sqltext:
            error["constraint"] = sqltext
        return error_response(
            message="Database Integrity Error",
            error=error,
            status_code=400
        )
    elif isinstance(e, ValidationError):
        return error_response(
            message="Validation Error",
            error=e.errors(),  # Pydantic validation errors
            status_code=422
        )
    elif isinstance(e, HTTPException):
        return error_response(
            message="HTTP Exception",
            error=e.detail,
            status_code=e.status_code
        )
    else:
        return error_response(
            message="An unexpected error occurred",
            error=str(e),
            status_code=500
        )
