from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    db = "dojo_survey"
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        # self.dojo = []


    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL(cls.db).query_db( query, data )

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        return Dojo(results[0])

    @staticmethod
    def is_valid(dojo):
        is_valid = True
        if len(dojo['name']) < 2:
            is_valid = False
            flash("Name must be at least 2 characters.")
        if len(dojo['location']) < 1:
            is_valid = False
            flash("A location must be selected.")
        if len(dojo['language']) < 1:
            is_valid = False
            flash("A language must be selected.")
        if len(dojo['comment']) < 3:
            is_valid = False
            flash("Comments must be at least 3 characters.")
        return is_valid