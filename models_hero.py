from flask_app.config.mysqlconnection import connectToMySQL

db = 'Hero_schema'
class Hero:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.alias = data['alias']
        self.origin = data['origin']
        
    @classmethod
    def create(cls , data):
        query = """
        INSERT into heros(first_name , last_name , alias , origin)
        Values (%(first_name)s , %(last_name)s , %(alias)s , %(origin)s )
        """
        return connectToMySQL (db).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM heros'    
        results = connectToMySQL (db).query_db(query)
        heros = []
        for hero in results:
            heros.append(hero)
        return heros
    
    @classmethod
    def get_one(cls,data):
        query =  """
        SELECT * FROM heros 
        WHERE id = %(id)s
        """
        results = connectToMySQL (db).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def update(cls,form_data,hero_id):
        query = f"Update heros set first_name = %(first_name)s,last_name = %(last_name)s, alias = %(alias)s , origin = %(origin)s where id={hero_id};"
        return connectToMySQL(db).query_db(query,form_data)

    