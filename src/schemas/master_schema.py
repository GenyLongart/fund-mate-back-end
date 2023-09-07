from marshmallow import ValidationError
from werkzeug.datastructures import FileStorage

class MasterSchema():
    # validation for uploaded files
    def validate_uploaded_file(self, in_data, attributeName):
        errors = {}
        file: FileStorage = in_data.get(attributeName, None)

        if type(file) != FileStorage:
            errors[attributeName] = [
                f"Invalid content. Only PDF, PNG, JPG/JPEG files accepted"]
            raise ValidationError(errors)

        elif file.content_type not in {"image/jpeg", "image/png", "application/pdf"}:
            errors[attributeName] = [
                f"Invalid file_type: {file.content_type}. Only PDF, PNG, JPG/JPEG images accepted."]
            raise ValidationError(errors)
        
        # Define the maximum allowed file size in bytes (e.g., 10 MB)
        max_file_size = 10 * 1024 * 1024  # 10 MB in bytes

        # Check if the file size exceeds the maximum allowed size
        if file.content_length is not None and file.content_length > max_file_size:
            errors["identityFile"] = [f"File size exceeds the maximum allowed size of {max_file_size} bytes."]
            raise ValidationError(errors)

        return in_data

