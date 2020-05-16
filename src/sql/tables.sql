CREATE TABLE "question" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"body"	TEXT NOT NULL,
	"answer"	TEXT NOT NULL,
	"answer_type"	TEXT NOT NULL,
	"level"	INTEGER NOT NULL,
	"prompt"	TEXT NOT NULL,
	"created_datetime"	TEXT NOT NULL
)

CREATE TABLE "variable" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"question_id"	INTEGER,
	"variable"	TEXT,
	"created_datetime"	TEXT NOT NULL
)