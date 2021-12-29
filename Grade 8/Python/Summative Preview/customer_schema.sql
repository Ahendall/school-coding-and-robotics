CREATE TABLE sqlite_sequence(name,seq); -- Idk what this is used for but i found it when i ran .schema lol

CREATE TABLE customers (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT NOT NULL,
   cash DECIMAL DEFAULT 1000.00,
   prev_order TEXT,
   prev_price DECIMAL
);
