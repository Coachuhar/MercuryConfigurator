from import_export import resources
from .models import Formula

class FormulaResource(resources.ModelResource):
    class Meta:
        model = Formula