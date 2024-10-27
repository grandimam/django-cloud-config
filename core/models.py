from django.db import models
from core.handlers import StringHandler
from core.handlers import HashHandler
from core.handlers import ListHandler
from core.handlers import SetHandler
from core.handlers import SortedSetHandler
from django.core.exceptions import ValidationError

class ConfigItem(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=[
        ('string', 'String'),
        ('hash', 'Hash'),
        ('list', 'List'),
        ('set', 'Set'),
        ('sorted_set', 'Sorted Set'),
    ])

    def __str__(self):
        return self.name

class GlobalConfig(models.Model):
    name = models.TextField(help_text="Stores JSON for complex types like Hash, List, Set, and Sorted Set")
    value = models.ForeignKey(ConfigItem, on_delete=models.CASCADE)

    TYPE_HANDLERS = {
        'string': StringHandler,
        'hash': HashHandler,
        'list': ListHandler,
        'set': SetHandler,
        'sorted_set': SortedSetHandler,
    }

    @property
    def type(self):
        return self.value.type

    def clean(self):
        handler_class = self.TYPE_HANDLERS.get(self.type)
        if not handler_class:
            raise ValidationError(f"Unsupported config type: {self.type}")
        self.value = handler_class.validate(self.value)
        return self.value
            

    def __str__(self):
        return f"{self.value.name}: {self.value}"
