from django.db.models import DecimalField,Model,DateTimeField

class HeatData(Model):
    DECIMAL_DEFAULTS = {
        "decimal_places":6,
        "max_digits": 12,
        "default": 0
    } 
    
    firstSensor = DecimalField(**DECIMAL_DEFAULTS)
    secondSensor = DecimalField(**DECIMAL_DEFAULTS)
    thirdSensor = DecimalField(**DECIMAL_DEFAULTS)

    updatedAt = DateTimeField(auto_now=True)
    createdAt = DateTimeField(auto_now_add=True)
