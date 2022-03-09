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
        self.dojo = []


    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        results = connectToMySQL(cls.db).query_db(query, data)
        # dojo = cls(results[0])
        # for row in results:
        #     n = {
        #         'name': row['dojo.name'],
        #         'location': row['dojo.location'],
        #         'language': row['dojo.language'],
        #         'comment': row['dojo.comment']
        #     }
        #     dojo.append(Dojo(n))
        # return dojo

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True 
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False
        return is_valid