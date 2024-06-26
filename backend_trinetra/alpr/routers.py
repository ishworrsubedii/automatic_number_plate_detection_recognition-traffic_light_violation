"""
Created By: ishwor subedi
Date: 2024-02-22
"""


class ImageCaptureRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'alpr' and model._meta.model_name == 'imagecapture':
            return 'image_capture_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'alpr' and model._meta.model_name == 'imagecapture':
            return 'image_capture_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'image_capture_db':
            return app_label == 'alpr'
        elif app_label == 'alpr' and model_name == 'imagecapture':
            return False
        return None


class ImageLoadRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'alpr' and model._meta.model_name == 'imageload':
            return 'image_load_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'alpr' and model._meta.model_name == 'imageload':
            return 'image_load_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'image_load_db':
            return app_label == 'alpr'
        elif app_label == 'alpr' and model_name == 'imageload':
            return False
        return None


class ALPRRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'alpr' and model._meta.model_name == 'alpr':
            return 'alpr_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'alpr' and model._meta.model_name == 'alpr':
            return 'alpr_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'alpr_db':
            return app_label == 'alpr'
        elif app_label == 'alpr' and model_name == 'alpr':
            return False
        return None


class ALPRRecognitionRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'alpr' and model._meta.model_name == 'alprrecognition':
            return 'alpr_recognition_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'alpr' and model._meta.model_name == 'alprrecognition':
            return 'alpr_recognition_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'alpr_recognition_db':
            return app_label == 'alpr'
        elif app_label == 'alpr' and model_name == 'alprrecognition':
            return False
        return None


class ALPRRecognizedImageRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'alpr' and model._meta.model_name == 'alprrecognizedimage':
            return 'alpr_recognized_image_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'alpr' and model._meta.model_name == 'alprrecognizedimage':
            return 'alpr_recognized_image_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'alpr_recognized_image_db':
            return app_label == 'alpr'
        elif app_label == 'alpr' and model_name == 'alprrecognizedimage':
            return False
        return None


class ALPRNonRecognizedImageRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'alpr' and model._meta.model_name == 'alprnonrecognizedimage':
            return 'alpr_non_recognized_image_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'alpr' and model._meta.model_name == 'alprnonrecognizedimage':
            return 'alpr_non_recognized_image_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'alpr_non_recognized_image_db':
            return app_label == 'alpr'
        elif app_label == 'alpr' and model_name == 'alprnonrecognizedimage':
            return False
        return None
