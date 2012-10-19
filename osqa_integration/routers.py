class OSQARouter(object):
    def db_for_read(self, model, **hints):
        "Point all operations on osqa models to 'other'"
        if model._meta.app_label == 'osqa':
            return 'osqa'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on osqa models to 'other'"
        if model._meta.app_label == 'osqa':
            return 'osqa'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in osqa is involved"
        if obj1._meta.app_label == 'osqa' or obj2._meta.app_label == 'osqa':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the osqa app only appears on the 'osqa' db"
        if db == 'osqa':
            return model._meta.app_label == 'osqa'
        elif model._meta.app_label == 'osqa':
            return False
        return None
