import sqlite3

class MemoryDB:
    def __init__(self):
        self.conn = sqlite3.connect("memory_store.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS user_trips (destination TEXT, budget INTEGER, days INTEGER, activities TEXT)")
        self.conn.commit()
    
    def store_trip(self, destination, budget, days, activities):
        self.cursor.execute("SELECT COUNT(*) FROM user_trips WHERE destination=? AND budget=? AND days=? AND activities=?", 
                            (destination, budget, days, activities))
        count = self.cursor.fetchone()[0]
    
        if count == 0:  # Store the trip only if it doesn't exist
            self.cursor.execute("INSERT INTO user_trips VALUES (?, ?, ?, ?)", (destination, budget, days, activities))
            self.conn.commit()
    
    def get_past_trips_by_destination(self, destination):
        self.cursor.execute("SELECT * FROM user_trips WHERE destination=? ORDER BY ROWID DESC LIMIT 5", (destination,))
        return self.cursor.fetchall()
