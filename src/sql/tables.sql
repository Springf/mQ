CREATE TABLE "question" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"body"	TEXT NOT NULL,
	"answer"	TEXT NOT NULL,
	"answer_type"	TEXT NOT NULL,
	"level"	INTEGER NOT NULL,
	"prompt"	TEXT NOT NULL,
	"created_datetime"	TEXT NOT NULL
);

CREATE TABLE "variable" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"question_id"	INTEGER,
	"variable"	TEXT,
	"created_datetime"	TEXT NOT NULL
);

CREATE TABLE "test" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"level"	INTEGER NOT NULL,
	"taker"	TEXT NOT NULL,
	"time_limit"	INTEGER NOT NULL,
	"created_datetime"	TEXT NOT NULL,
	"start_datetime"	TEXT,
	"end_datetime"	TEXT
);

CREATE TABLE "test_questions" (
	"test_id"	INTEGER NOT NULL,
	"question_id"	INTEGER NOT NULL,
	"variable_id"	INTEGER,
	"order"	INTEGER NOT NULL,
	"mark"	INTEGER NOT NULL,
	"answer"	TEXT,
	"correct"	INTEGER,
	"start_datetime"	TEXT,
	"last_updated"	INTEGER,
	"time_spent"	INTEGER,
	PRIMARY KEY("test_id","question_id")
);