class GRPPERSONASRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'personas_personas','personas_historialLaboral'}


    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to grp_personas_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'grp_personas_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to grp_personas_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'grp_personas_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'grp_personas_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'grp_personas_db'
        return None

class GRPCORERouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'core_monedas'}


    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to grp_core_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'grp_core_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to grp_core_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'grp_core_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'grp_core_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'grp_core_db'
        return None

class GRPCORPRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'corp_cobrarSupermonedas','corp_autorizaciones','corp_empresas'}


    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to grp_corp_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'grp_corp_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to grp_corp_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'grp_corp_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'grp_corp_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'grp_corp_db'
        return None




