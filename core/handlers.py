from django.core.exceptions import ValidationError

class ConfigTypeHandler:
    """Base handler for configuration types."""
    @staticmethod
    def validate(data):
        return data

class StringHandler(ConfigTypeHandler):
    pass

class HashHandler(ConfigTypeHandler):
    @staticmethod
    def validate(data):
        try:
            if not isinstance(data, dict):
                raise ValidationError("Value must be a JSON object for Hash type.")
            return data
        except Exception:
            raise ValidationError("Value must be valid JSON.")

class ListHandler(ConfigTypeHandler):
    @staticmethod
    def validate(data):
        try:
            if not isinstance(data, list):
                raise ValidationError("Value must be a JSON array for List type.")
            return data
        except Exception:
            raise ValidationError("Value must be valid JSON.")

class SetHandler(ConfigTypeHandler):
    @staticmethod
    def validate(data):
        try:
            if not isinstance(data, list) or len(data) != len(set(data)):
                raise ValidationError("Value must be a JSON array with unique elements for Set type.")
            return data
        except Exception:
            raise ValidationError("Value must be valid JSON.")

class SortedSetHandler(ConfigTypeHandler):
    @staticmethod
    def validate(data):
        try:
            if not isinstance(data, list) or any(not isinstance(i, list) or len(i) != 2 for i in data):
                raise ValidationError("Value must be a JSON array of [value, score] pairs for Sorted Set type.")
            return data
        except Exception:
            raise ValidationError("Value must be valid JSON.")
