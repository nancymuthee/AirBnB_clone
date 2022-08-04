import uuid
import datetime
import string



class BaseModel:
    models = []
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    
    def __str__(self):
        return f'BaseModel({self.id}, {self.__dict__})'
        
    def save_model(self):
        self.updated_at = datetime.datetime.now()
        self.created_at = self.created_at
        BaseModel.models.append(self)
        
    def to_dict(self):
        model_dict = {"id":self.id, "time created":self.created_at.isoformat(), "time updated":self.updated_at.isoformat()}
        
        return model_dict
