CREATE TABLE IF NOT EXISTS customers (
	name TEXT NOT NULL,
	cash DECIMAL DEFAULT 1000.00,
	prev_order TEXT DEFAULT "1",
	prev_price DECIMAL DEFAULT 1.0
);