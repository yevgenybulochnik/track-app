from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

# Alias common SQLAlchemy names

Column = db.Column
relationship = relationship
Model = db.Model
